import { defineCollection, z } from 'astro:content';

const articles = defineCollection({
  type: 'content',
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

const posts = defineCollection({
  type: 'content',
  schema: z.object({
    date: z.string(),
    tags: z.array(z.string()).default([]),
    image: z.string().optional(),
  }),
});

export const collections = { articles, posts };
