---
title: What Breaks When You Build Without a Developer
subtitle: "I started auditing apps built entirely with AI tools. Here's what I found — and what the founders who built them didn't know."
date: 10 Aug 2026
author: sharanx
tags:
  - ai
  - engineering
  - startups
image: "what-breaks-when-you-build-without-a-developer.png"
---

# The Problem Nobody Talks About

We all know the story by now. A founder has an idea, opens Bolt or Lovable or Cursor, and by Sunday night they have a working app. Users are signing up. Revenue is trickling in. The demo works. The pitch deck looks great.

What nobody talks about is what's underneath.

I've been running code audits on AI-built applications for the last few weeks. Not the kind of audits that engineers run — with linters and security scanners that output a wall of warnings meaningful only to someone who already knows what a CWE is. I mean audits translated into English. Plain English. The kind a founder reads and immediately knows what to do next.

## What I Found

The patterns are remarkably consistent across the apps I've audited. Here's what keeps showing up:

### 1. Secrets committed to the repo

This is the single most common finding. API keys, Stripe secret keys, database connection strings — all hardcoded directly in source files. Not in `.env` files (those are usually in `.gitignore`). In the actual code. `api_key = "sk_live_..."` sitting in `config.py` like it belongs there.

If your repo is public, anyone can read it. If your repo is private but you've ever shared access with a contractor, a VA, or a "technical co-founder" you met on a Discord server, they have your keys. And they outlive their welcome.

### 2. Authentication that works until it doesn't

The login flow works in the demo. You tested it. Your mum tested it. What you didn't test is what happens when 500 people try to log in at the same time, or when someone sends 10,000 requests to your `/login` endpoint in 30 seconds.

CSRF protection is frequently disabled on specific routes because the AI tool generated it without the decorator (or the founder removed it because "it was blocking my API calls"). Rate limiting is almost never configured. Session management often stores everything in memory, which means every server restart logs everyone out — and at scale, means the server crashes when memory fills up.

### 3. The database query that costs €340/month

This is the finding that makes founders sit up. An N+1 query pattern where the code fetches a list of items, then loops through each one and makes a separate database call for related data. With 100 records and 10 users, it's fine. With 10,000 records and 1,000 users, your Supabase bill goes from €25/month to €400/month and your page load goes from 200ms to 8 seconds.

The founder doesn't know because they've never had 1,000 users. The code was written by an AI that optimised for "make it work" not "make it scale." That's the right trade-off for an MVP. It's the wrong trade-off when you're paying for it.

### 4. Dependencies that are deprecated, heavy, or both

`moment.js` in 2026. `request` (deprecated since 2020). Three different HTTP libraries doing the same job. An entire `lodash` import when you're using two functions. None of these break your app today. All of them make it harder to maintain, slower to load, and more expensive to host.

### 5. No error handling beyond "it crashed"

AI tools are good at writing the happy path. They're less good at handling the unhappy path. When the database is down, when the API rate limit hits, when the payment fails — the app often returns a 500 error with a stack trace that includes your database connection string. Not ideal.

## Why This Matters Now

The tools are getting better. Bolt, Lovable, Cursor, v0 — they're all improving at a pace that makes last month's output look amateur. But the gap between "working app" and "production-ready app" is not closing. If anything, it's widening, because the tools are making it easier to build complex apps faster, which means more surface area for these issues to hide in.

The founders I've talked to aren't careless. They're focused on the product, the customers, the revenue — exactly what they should be focused on. But they're running businesses on code they can't read, and they have no way to know if there's a time bomb sitting in their repo.

## What I'm Building

I'm calling it SecondRead. The idea is simple: you send us your GitHub repo URL, and within 24 hours you get a report in plain English. Three sections:

- **What to fix today** — security issues, exposed secrets, critical bugs
- **What's costing you money** — inefficient patterns, heavy dependencies, infrastructure waste
- **What breaks at scale** — the things that work now and will fail with more users

Plus a contractor briefing: a numbered list of specific instructions you can copy-paste to any developer. "In `backend/accounts/views.py` line 57, remove the `@csrf_exempt` decorator." "In `settings.py`, add `DEFAULT_THROTTLE_CLASSES` with a rate of 100/minute per user." That kind of thing.

The analysis is real — Semgrep, Bandit, secret scanners, dependency analysis. The same tools professional engineering teams use. The translation layer is where the product lives: turning a wall of JSON output into something a founder can read in five minutes and act on in an afternoon.

## The Honest Part

I'm not going to pretend this replaces a good engineer. It doesn't. What it does is close the gap between "I built something with AI" and "I know what's in the thing I built." For a founder who can't hire a senior engineer yet, or who wants a sanity check before they do, it's the cheapest second opinion they'll ever get.

The first 20 audits are free. No signup, no dashboard, no trial. Just send your repo URL to hello@secondread.me and you'll get a report within 24 hours.

If the report is useful, the next one is €49. If you want ongoing monitoring — re-audits on every push — that's €199/month.

If it's not useful, you've lost nothing but an email.

---

*SecondRead is live at [secondread.me](https://secondread.me). Beta audits are free through August. Send your repo URL to reviewer@secondread.me.*