---
title: "The Fable Ban: When Export Controls Became Self-Sabotage"
subtitle: "An analysis of the US government's decision to bar Anthropic from providing its Fable model to non-US users"
date: 27 Jun 2026
author: sharanx
tags:
  - xf
  - article
  - AI
  - entertainment
  - industry-analysis
image: "the-fable-ban.png"
audio: "the-fable-ban.mp3"
---

Last week's Fable Fiasco was worthy of note because it was an important point in time for the AI industry. Let's plot the quick facts on the timeline and then anticipate what comes next:
## Data
After using the data freely available online, the frontier AI models need user-specific data in order to retain an advantage. You have to build a compelling feature that will allow user data to flow into your systems. You can't do that without building a compelling product that acts as your sidekick and which you rely on more and more.
## Regulation
One way to look at what happened is to look at things from the lens of what large technology startups have always done when competing in a market that's about to become crowded. There's an established playbook:

* Begin by competing head-to-head offering better deals and discounts than your competitor.
* Tap investors faster than your competition.
* Ask for more funding — the second intention of which is to lock up capital from the competition.

...until it makes sense to seek regulatory arbitrage.

Elon had already been laying the ground for this by stating how important it was to be careful about AI and its potential downsides. This was fertile ground upon which Sam Altman just planted the seeds of regulation in the US for this. Only he was responsible enough to produce good AI, you see. While this was pointed at the other direct competitors, it undoubtedly had the added benefit of squashing the open source movement that would form in this space once and for all.

Anthropic does the same by play-acting the "look how much cleaner my toga is" routine, portraying itself as the better, more responsible player. OpenAI's missteps in going from non-profit to for-profit only helped that narrative along. But both these companies completely hid the fact that they were amassing incredible amounts of personal information about their users all the while. 
## China as the villain
It was strange to see China being propped up as the enemy of the US in the field. They were competitors, sure — the US competes with many in various fields. Competition is healthy. It makes everyone better. In fact, one of the biggest markets for NVIDIA's chips was China. So why did they need to become the national enemy? Well, nothing creates urgency like the inclusion of a secretive villain who has unknown strengths. 

So, now, the story had progressed from "AI is so capable and must be regulated" to "AI is so capable that China will use it against us, unless we do something to prevent that"

## Chip Exports Ban
This was probably one of the most badly timed moves by the US. AI is in its infancy at the moment. This same move would have had a far greater impact if it was done at a later point in time. This is the bad movie equivalent where the hero swears revenge to the face of the villain. Why? Why do these people forewarn, when not revealing their cards would actually ensure successful revenge? I've never understood that.

The geopolitical tensions this created were absolutely not required. Now, since the ban, China clearly understands that they cannot rely on the US for their chips, so they have invested in local technology development. That's a move they would have been far less likely to prioritise so aggressively if the US had simply considered alternatives between full supply and outright ban. China's pursuit of semiconductor independence predates these bans by decades — what the restrictions did was intensify and focus investment that was already underway. Huawei's Ascend chips and the MindSpore ecosystem were marginal before; now they're strategically prioritised. This is a textbook case of infant-industry protection: the restriction created the market for the domestic alternative.

## GLM, Kimi, DeepSeek and the open weights releases
China is not new to the idea of producing things cheaply and getting users by that route. What do you get when the entire Chinese governmental apparatus focuses on beating the US? Open source, open weights, self host-able alternatives to frontier models that cost a fraction of the price that frontier labs in the US are producing. Are they a lot worse than frontier models? Not really, not in any meaningful way for everyday tasks. Definitely not for most enterprise use-cases.

This isn't mere speculation — it's measurable. DeepSeek V3 and R1 achieve near-frontier performance on coding, reasoning, and mathematics benchmarks at a fraction of the inference cost. Qwen 2.5 and GLM-4 deliver comparable results on many enterprise tasks. On the overall [Arena leaderboard](https://huggingface.co/spaces/lmarena-ai/chatbot-arena), GLM 5.2 (Max) currently sits at #9 — ahead of GPT 5.4 (High) — demonstrating that the gap between "frontier" and "open weights" has narrowed to the point where, for most production workloads, the price-to-performance ratio overwhelmingly favours the open alternatives. 

## SpaceX IPO
I understand that there are many models for evaluating a company's value, and that it's more art than science. But if you believe that revenues must justify the value of a company, basically the price to sales ratio, then the SpaceX IPO valuation assumes that every human on Earth will be a paying customer of its services. This is not just one company making this assumption. Anthropic's valuation also assumes a similar metric. Whether this is achievable — whether every human adult is able to pay the subscription amount — is yet to be seen. But the point to note is the total addressable market (TAM) assumed is global, not just the ~340 million people in the US.

## Fable Ban
So, against this backdrop comes the Fable ban, based on US export restriction laws. It establishes that the government has a kill-switch that can prevent an AI foundry from achieving the TAM necessary for their stock valuations.

Not only that, the already hesitant enterprises in the US, likely the only big players that could pay the price of the tokens coming from the frontier labs, also saw that they couldn't practically adopt their services because many of these companies are not geographically bound to the US. They cannot adopt a model that is not freely available to their non-US employees. Whether geographic boundaries are archaic in a technological age is a different argument altogether; the point is, this wiped out a huge revenue stream for these AI foundries.

They are naturally adopting the open-source self-hosted models from China and other sources. It's only logical that they would adopt a technology that does 80% of the jobs their employees need done when they have the added advantage of not having to expose their data to external service providers.

## Overcorrections 
In trying to cater to safety requirements, one foundational model company has gone overboard, curtailing users from performing even tasks that are not safety-related. The famous podcaster of DOAC, [Steven Bartlett](https://youtu.be/32u5T6lO8qk?is=AeOKeBWgrGdwhDCS), quips that he was trying to use Claude to make some edits to slides that he was creating when Claude completely refused to execute the task stating that "It wouldn't be right to alter the data", imposing a worldview born in a San Francisco lab on users across the world, whether or not it made sense in their culture.

This isn't an isolated anecdote — it's part of a documented pattern. Anthropic's own research acknowledges that over-refusals are a genuine product problem, not a theoretical concern. When models impose value judgements on non-harmful tasks, they undermine user trust and make the tool less useful in practice. The Bartlett incident exemplifies a broader tension: safety guardrails designed to prevent misuse can themselves become a liability when they override legitimate, context-appropriate requests. 

## Apple
While all this is happening, Apple continues to develop more capable machines clearly designed to host AI models locally. These machines are not only capable of running larger models, but also have the chops to run fine-tuning operations that will eventually allow users not only to run models where their data lives, without ever exporting it, but also to modify those models to fit the needs and sensitivities of the individual user. It is the largest consumer computing company on the planet making a quiet but unmistakable bet: the future of AI is local. And by building the hardware that enables it, Apple is arguably doing more to accelerate the shift away from centralised cloud models than any regulation ever could.

Apple's trajectory here is deliberate, not incidental. The Neural Engine in every M-series and A-series chip, the MLX framework optimised for Apple silicon, and Apple Intelligence marketing all point to on-device inference as a core strategy, not a peripheral feature. With enough unified memory to load models with billions of parameters and the ability to run fine-tuning on a laptop, the hardware is already capable of hosting serious AI locally.

## Lord Acton and George Hotz
The least of my expectations is that Anthropic will soon follow OpenAI and delay their IPO.

While I don't expect centralised foundational models to disappear anytime soon, I do expect locally hosted models to gain importance. 

The final goal of any of these foundries was never to share their technology with the rest of the world. That's a naive expectation. As Lord Acton put it, "Power tends to corrupt, and absolute power corrupts absolutely." They were always going to hoard control of that vital technology among the very few.

The question was always what the rest of us would do about it. George Hotz said: *"The best defence I could possibly have is an AI in my room being like: 'Don't worry, I got you. It's you and me, we're on a team, we're aligned.' ... Me and my computer, we like each other, we're aligned. And we're standing against a world that has always, since the beginning of history, maximally been trying to screw you over."*

The ban didn't change the game. It just made the next move obvious.
