import rss from '@astrojs/rss';
import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';

export const GET: APIRoute = async (context) => {
  const articles = await getCollection('articles');
  const sortedArticles = articles.sort(
    (a, b) => new Date(b.data.date).getTime() - new Date(a.data.date).getTime()
  );

  return rss({
    title: 'Redd XF',
    description: 'For the Post-Skill Designer',
    site: context.site ?? 'https://redd.in',
    items: sortedArticles.map((article) => ({
      title: article.data.title,
      description: article.data.subtitle,
      link: `/articles/${article.id}/`,
      pubDate: new Date(article.data.date),
      categories: article.data.tags,
    })),
    customData: `<language>en-us</language>`,
  });
};
