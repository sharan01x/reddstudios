import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Read index.html and extract posts
function extractPosts() {
    const indexHtml = fs.readFileSync(path.join(__dirname, '../../index.html'), 'utf-8');
    
    // Extract posts section
    const postsMatch = indexHtml.match(/id='posts-tab' class='tab-content active'>(.*?)<\/div><\/div>\s*<!-- Articles Tab Content -->/s);
    if (!postsMatch) {
        console.log('Could not find posts section');
        return [];
    }
    
    const postsSection = postsMatch[1];
    
    // Extract individual posts
    const postRegex = /<div class="post-card" data-tags="([^"]*)">[\s\S]*?<div class="post-content[^"]*">([\s\S]*?)<\/div>[\s\S]*?<span class="post-date">([^<]*)<\/span>[\s\S]*?<\/div>[\s\S]*?<\/div>[\s\S]*?<\/div>/g;
    
    const posts = [];
    let match;
    
    while ((match = postRegex.exec(postsSection)) !== null) {
        const tags = match[1].split(' ').filter(t => t);
        let content = match[2].trim();
        const date = match[3].trim();
        
        // Clean up content
        content = content
            .replace(/&#x27;/g, "'")
            .replace(/&#34;/g, '"')
            .replace(/&quot;/g, '"')
            .replace(/&amp;/g, '&')
            .replace(/<br\s*\/?>/g, '\n');
        
        posts.push({
            tags,
            content,
            date,
            image: null
        });
    }
    
    // Also extract images
    const imageRegex = /<div class="post-card" data-tags="([^"]*)">[\s\S]*?<div class="post-image"><img src="([^"]*)"/g;
    let imageMatch;
    let postIndex = 0;
    
    while ((imageMatch = imageRegex.exec(postsSection)) !== null) {
        // Find the corresponding post
        const postWithImage = posts.find((p, i) => {
            const postCardMatch = postsSection.substring(0, imageMatch.index).match(/<div class="post-card"/g);
            const cardIndex = postCardMatch ? postCardMatch.length : 0;
            return i === cardIndex;
        });
        
        if (postWithImage) {
            postWithImage.image = imageMatch[2];
        }
    }
    
    return posts;
}

// Extract articles list from index.html
function extractArticlesList() {
    const indexHtml = fs.readFileSync(path.join(__dirname, '../../index.html'), 'utf-8');
    
    const articlesMatch = indexHtml.match(/<div class="articles-list">([\s\S]*?)<\/div>\s*<\/div>\s*<!-- Audio Tab Content -->/);
    if (!articlesMatch) {
        console.log('Could not find articles section');
        return [];
    }
    
    const articlesSection = articlesMatch[1];
    
    const articleRegex = /<div class="article-item" data-tags="([^"]*)">[\s\S]*?<a href="([^"]*)">([^<]*)<\/a>[\s\S]*?<div class="article-subtitle">([^<]*)<\/div>[\s\S]*?<span class="article-date">([^<]*)<\/span>[\s\S]*?<span class="article-author">by ([^<]*)<\/span>/g;
    
    const articles = [];
    let match;
    
    while ((match = articleRegex.exec(articlesSection)) !== null) {
        articles.push({
            tags: match[1].split(' ').filter(t => t),
            htmlFile: match[2],
            title: match[3].trim(),
            subtitle: match[4].trim(),
            date: match[5].trim(),
            author: match[6].trim()
        });
    }
    
    return articles;
}

// Extract article content from HTML file
function extractArticleContent(htmlFile) {
    const filePath = path.join(__dirname, '../../', htmlFile);
    if (!fs.existsSync(filePath)) {
        console.log(`File not found: ${htmlFile}`);
        return null;
    }
    
    const html = fs.readFileSync(filePath, 'utf-8');
    
    // Extract title
    const titleMatch = html.match(/<h1>([^<]*)<\/h1>/);
    const title = titleMatch ? titleMatch[1] : '';
    
    // Extract subtitle
    const subtitleMatch = html.match(/<div class="subtitle">([^<]*)<\/div>/);
    const subtitle = subtitleMatch ? subtitleMatch[1] : '';
    
    // Extract tags
    const tagsMatch = html.match(/<div class="tags-display-view">([\s\S]*?)<\/div>/);
    let tags = [];
    if (tagsMatch) {
        const tagRegex = /<span class="tag-chip-view">([^<]*)<\/span>/g;
        let tagMatch;
        while ((tagMatch = tagRegex.exec(tagsMatch[1])) !== null) {
            tags.push(tagMatch[1].trim());
        }
    }
    
    // Extract date
    const dateMatch = html.match(/<span class="date">([^<]*)<\/span>/);
    const date = dateMatch ? dateMatch[1] : '';
    
    // Extract audio
    const audioMatch = html.match(/<source src="([^"]*audio\.mp3)"/);
    const audio = audioMatch ? audioMatch[1] : null;
    
    // Extract podcast
    const podcastMatch = html.match(/<source src="([^"]*podcast\.mp3)"/);
    const podcast = podcastMatch ? podcastMatch[1] : null;
    
    // Extract content
    const contentMatch = html.match(/<div class="content">([\s\S]*?)<\/div>\s*<\/div>\s*<\/div>/);
    let content = '';
    if (contentMatch) {
        content = contentMatch[1]
            .replace(/<p>/g, '\n\n')
            .replace(/<\/p>/g, '')
            .replace(/<h1>/g, '\n# ')
            .replace(/<\/h1>/g, '')
            .replace(/<h2>/g, '\n## ')
            .replace(/<\/h2>/g, '')
            .replace(/<h3>/g, '\n### ')
            .replace(/<\/h3>/g, '')
            .replace(/<ol>/g, '\n')
            .replace(/<\/ol>/g, '')
            .replace(/<ul>/g, '\n')
            .replace(/<\/ul>/g, '')
            .replace(/<li>/g, '- ')
            .replace(/<\/li>/g, '')
            .replace(/<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"[^>]*>/g, '\n![$2]($1)\n')
            .replace(/<[^>]*>/g, '')
            .replace(/&#x27;/g, "'")
            .replace(/&#34;/g, '"')
            .replace(/&quot;/g, '"')
            .replace(/&amp;/g, '&')
            .replace(/&nbsp;/g, ' ')
            .replace(/\n\s*\n\s*\n/g, '\n\n')
            .trim();
    }
    
    return { title, subtitle, tags, date, audio, podcast, content };
}

// Generate slug from title
function generateSlug(title) {
    return title
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/^-|-$/g, '');
}

// Main migration
function migrate() {
    console.log('Starting migration...\n');
    
    // Migrate posts
    console.log('Migrating posts...');
    const posts = extractPosts();
    console.log(`Found ${posts.length} posts`);
    
    posts.forEach((post, index) => {
        const slug = `post-${index + 1}-${post.date.toLowerCase().replace(/ /g, '-')}`;
        const frontmatter = `---
date: "${post.date}"
tags: ${JSON.stringify(post.tags)}${post.image ? `\nimage: "${post.image}"` : ''}
---

${post.content}`;
        
        fs.writeFileSync(
            path.join(__dirname, '../content/posts', `${slug}.md`),
            frontmatter
        );
    });
    console.log(`Migrated ${posts.length} posts\n`);
    
    // Migrate articles
    console.log('Migrating articles...');
    const articlesList = extractArticlesList();
    console.log(`Found ${articlesList.length} articles`);
    
    articlesList.forEach((article) => {
        const content = extractArticleContent(article.htmlFile);
        if (!content) return;
        
        const slug = generateSlug(article.title);
        const frontmatter = `---
title: "${content.title}"
subtitle: "${content.subtitle}"
date: "${content.date}"
author: "${article.author}"
tags: ${JSON.stringify(content.tags)}${content.audio ? `\naudio: "${content.audio}"` : ''}${content.podcast ? `\npodcast: "${content.podcast}"` : ''}
---

${content.content}`;
        
        fs.writeFileSync(
            path.join(__dirname, '../content/articles', `${slug}.md`),
            frontmatter
        );
        console.log(`Migrated: ${article.title}`);
    });
    
    console.log('\nMigration complete!');
}

migrate();
