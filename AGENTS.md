# Redd XF

YouTube-first content venture. Videos on design, technology, and the AI-maker ethos.
Website at redd.in. YouTube channel @reddxf.

## Tech Stack

- **Framework:** Astro (static site generation)
- **Hosting:** GitHub Pages
- **Analytics:** PostHog (website), YouTube Data API v3, custom stats dashboard
- **Stats tool:** `~/Documents/Code/reddxf-statistics/` (Node.js + SQLite)
- **Social posting:** SocialsPoster (`~/Documents/Code/SocialsPoster/`), Paragraph API
- **Deploy:** Push to `main` branch → GitHub Pages auto-deploys to redd.in
- **Sitemap:** `@astrojs/sitemap` integration — auto-generated on build, no manual maintenance needed

## Project Structure

```
src/
├── content/
│   └── articles/          # Markdown articles (one .md per article)
├── pages/
│   ├── index.astro        # Homepage with tabs (Articles, Videos, Audio, Art)
│   └── articles/
│       └── [slug].astro   # Article template
├── layouts/
│   └── BaseLayout.astro   # Shared layout (nav, PostHog, footer)
public/
└── art/                   # Generated art images
```

## Commands

```bash
npm run dev      # Local dev server (http://localhost:4321)
npm run build    # Production build → dist/
npm run preview  # Preview production build
```

## Sitemap & SEO

The site uses the `@astrojs/sitemap` integration (configured in `astro.config.mjs`) to automatically generate sitemap files during build.

### Generated Files

- `sitemap-index.xml` — Main sitemap index (lists all sub-sitemaps)
- `sitemap-0.xml` — Contains all page URLs (homepage + all articles)

Both are generated into `dist/` on `npm run build` and deployed to:
- `https://redd.in/sitemap-index.xml` (submit this to Google Search Console)
- `https://redd.in/sitemap-0.xml`

### Google Search Console

- **Sitemap URL to submit:** `sitemap-index.xml`
- **Property:** `redd.in` (URL prefix method)
- The sitemap is regenerated automatically whenever new articles are added and the site is built — no manual sitemap updates needed.

### Adding SEO to New Articles

The sitemap picks up all pages automatically. No action needed beyond the normal build & deploy flow when adding articles.

## Deploy (CRITICAL — do not skip)

The site is deployed via **GitHub Pages** connected to the `main` branch.
Pushing to `main` triggers an automatic build and deploy to redd.in.

**After any code change (new article, content update, design change), you MUST:**

1. Verify the build passes: `npm run build`
2. Stage all changes: `git add -A`
3. Commit with a descriptive message: `git commit -m "feat: description"`
4. Pull rebase: `git pull --rebase origin main`
5. Push to deploy: `git push origin main`

**Code is NOT "done" until it is pushed.** Only mark a kanban task complete AFTER push succeeds.

## Adding a New Article

1. Write article as `.md` file in `src/content/articles/`
2. Generate featured image (if needed) using Image37 skill
3. Build site: `npm run build`
4. Commit & push to GitHub
5. Verify RSS: `curl https://redd.in/rss.xml`
6. Generate audio (optional)
7. Announce on social channels via SocialsPoster
8. Update Content Planner with status = ✅ Published

## Browser Automation (Chrome CDP)

Some tasks require driving a real Chrome browser (e.g., LinkedIn posting, Firefly/Twitter scheduling, Medium). Use the dedicated Chrome profile for Redd XF:

### Launch Chrome Instance

```bash
~/Documents/Code/reddxf/scripts/launch-chrome.sh
```

Or directly:
```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --user-data-dir="/Users/sharan/Library/Application Support/Google/Chrome-reddxf" \
  --remote-debugging-port=9224 \
  --no-first-run \
  --no-default-browser-check \
  --remote-allow-origins="*"
```

### Drive the Browser via `browser_exec`

Once Chrome is running, use the `browser_exec` tool to drive it. The Browser Use CLI connects to the CDP endpoint automatically.

**NEVER type URLs into the address bar.** Use the pre-imported helpers:

| Helper | Purpose |
|--------|---------|
| `new_tab(url)` | Navigate to a URL (opens new tab) |
| `goto_url(url)` | Navigate current tab to URL |
| `wait_for_load()` | Wait for page load |
| `page_info()` | Get page state (URL, title, text summary) |
| `js(expr)` | Evaluate JavaScript in page |
| `fill_input(selector, text)` | Type into an input field |
| `click_at_xy(x, y)` | Click at viewport coordinates |

### Accounts Logged In

- **LinkedIn:** Redd XF company page (ID: 13380986)
- **Firefly:** Twitter/X scheduling for @reddexperience
- **Medium:** @reddxf
- **Substack:** reddxf.substack.com
- **YouTube:** youtube.com/@reddxf

## Social Posting

### SocialsPoster (Twitter/Bluesky/Mastodon/LinkedIn)

```bash
cd ~/Documents/Code/SocialsPoster
source venv/bin/activate

# Post to all company accounts (Bluesky + Mastodon + LinkedIn)
python social_media_poster.py --type company -t "Post content here"

# Post to specific platform
python social_media_poster.py -p bluesky -a reddxf -t "Post content"
python social_media_poster.py -p mastodon -a reddxf -t "Post content"
```

Twitter/X posting goes through Firefly (Chrome browser automation), not the Twitter API.

### Paragraph (API)

Use the `mcp__paragraph__create_post` tool to publish articles directly to Paragraph.
API key is in `~/Documents/Code/reddxf-statistics/.env` as `PARAGRAPH_API_KEY`.

## Stats / Analytics

### Daily Stats Fetch

```bash
cd ~/Documents/Code/reddxf-statistics
node fetch-stats.js    # Fetches YouTube, PostHog, Bluesky, Mastodon, Paragraph, Substack, comments
```

### Query Stats

```bash
cd ~/Documents/Code/reddxf-statistics
python3 query-db.py     # Quick summary of latest stats
python3 query_stats.py  # Detailed stats query
```

### Dashboard

```bash
cd ~/Documents/Code/reddxf-statistics
npm run dashboard       # Starts Express server with dashboard
```

### Database Schema

Stats DB at `~/Documents/Code/reddxf-statistics/data/reddxf-stats.db`:
- `channel_stats` — daily YouTube subscriber/view/video counts
- `videos` — video metadata (title, duration, published_at)
- `video_stats` — per-video daily stats (views, likes, comments)
- `website_stats` — daily PostHog website stats
- `youtube_comments` — comment tracking
- `bluesky_account_stats`, `mastodon_account_stats` — social followers
- `paragraph_stats` — Paragraph post stats
- `substack_stats` — Substack subscriber stats

**Note:** Watch time/estimated minutes watched is NOT available via YouTube Data API v3. The 162 qualified watch hours figure comes from YouTube Studio (manual check). The stats DB can estimate a rough proxy but cannot give exact watch hours.

## Key Files

| File | Purpose |
|------|---------|
| `scripts/launch-chrome.sh` | Launch dedicated Chrome profile for Redd XF |
| `~/Documents/Code/reddxf-statistics/` | Stats fetcher + dashboard |
| `~/Documents/ReddXF/scripts/` | Video scripts (production notes) |
| `~/Documents/ReddXF/brand/` | Brand assets |
| `~/Documents/ReddXF/thumbnails/` | Video thumbnails |
| `~/Documents/ReddGroup/ventures/reddxf/plan.md` | Venture strategy plan |
| `~/Documents/ReddGroup/ventures/reddxf/Redd XF Content Planner.md` | Content pipeline (symlinked to Obsidian) |