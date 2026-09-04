import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const articles = defineCollection({
  loader: glob({
    pattern: '**/*.{md,mdx}',
    base: './src/content/articles',
  }),
  schema: z.object({
    title: z.string(),
    subtitle: z.string(),
    date: z.string(),
    author: z.string().default('sharanx'),
    tags: z.array(z.string()).default([]),
    audio: z.string().optional(),
    podcast: z.string().optional(),
    image: z.string().optional(),
  }),
});

const projects = defineCollection({
  loader: glob({
    pattern: '**/*.{md,mdx}',
    base: './src/content/projects',
  }),
  schema: z.object({
    title: z.string(),
    subtitle: z.string(),
    date: z.string(),
    author: z.string().default('sharanx'),
    tags: z.array(z.string()).default([]),
    image: z.string().optional(),
    client: z.string().optional(),
    website: z.string().optional(),
  }),
});

export const collections = { articles, projects };
