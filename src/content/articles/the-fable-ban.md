---
title: "The Fable Ban: How Washington Accidentally Open-Sourced the Future"
subtitle: An American AI company asked the government for protection. The government granted it — and destroyed the company.
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

I didn't expect a single government letter to do more for self-hosted AI than a decade of open-source advocacy. But, on June 12, 2026, the US Commerce Department sent Anthropic a letter. By June 13, the world realised that open source was the future! 

## Regulation

One way to look at what happened is through the lens of what large technology startups have always done when a market is about to get crowded. There's an established playbook:

* Begin by competing head-to-head, offering better deals and discounts than your competitor.
* Tap investors faster than your competition.
* Ask for more funding — the second intention of which is to lock up capital from the competition.

...until it makes sense to seek regulatory arbitrage.

Elon had already been laying the groundwork by droning on about how careful we must be with AI. This was fertile ground upon which Sam Altman planted the seeds of regulation. Only *he* was responsible enough to produce good AI, you see. While this was aimed at direct competitors, it had the added benefit of squashing the self-hosted model movement before it could fully form.

Anthropic does the same by play-acting the "look how much cleaner my toga is" routine, portraying itself as the better, more responsible player. OpenAI's missteps in going from non-profit to for-profit only helped that narrative along. But both these companies completely hid the fact that they were amassing incredible amounts of personal information about their users all the while.

## The Strategic Narrative

Let's look at how China got positioned in this debate. They were competitors, sure — the US competes with plenty of countries in plenty of fields. Competition is healthy. It makes everyone better. In fact, one of the biggest markets for NVIDIA's chips was China. So why did they need to become the national enemy?

Well, nothing creates urgency like a secretive rival with unknown strengths. So the story progressed from "AI is so capable and must be regulated" to "AI is so capable that China will use it against us, unless we do something to prevent that." The threat was real — China's Next Generation AI Development Plan explicitly aims for global leadership by 2030, backed by state-directed industrial policy. But the US chose the wrong tool for a genuine problem.

## Chip Exports Ban

This was probably one of the most badly timed moves by the US. AI is in its infancy at the moment. This same move would have had a far greater impact if it was done at a later point in time. Instead, it choose the bad movie equivalent where the hero swears revenge to the face of the villain. Why? Why do these people forewarn, when not revealing their cards would actually ensure successful revenge? I've never understood that.

The geopolitical tensions this created were absolutely not required. Since the ban, China clearly understands they cannot rely on the US for chips, so they have invested aggressively in local technology development. That's a move they would have been far less likely to prioritise so aggressively if the US had simply considered alternatives between full supply and outright ban. China's pursuit of semiconductor independence predates these bans by decades — what the restrictions did was intensify and focus investment that was already underway. The [Carnegie Endowment](https://carnegieendowment.org/research/2026/05/chinas-pivot-on-global-ai) notes that Huawei's Ascend chips and the MindSpore ecosystem were marginal before; now they're strategically prioritised. This is a textbook case of infant-industry protection: the restriction created the market for the domestic alternative.

## Open Weights and Self-Hosted Models

There is a difference between "open source" (transparent, community-governed, training data included) and "open weights" (downloadable binaries with opaque training). The distinction matters, so I will refer to these models by what is genuinely transformative, which is the ability to **self-host** — to run models where your data lives, without exporting it to a vendor's cloud.

China is not new to the idea of producing things cheaply and getting users by that route. What do you get when the entire Chinese governmental apparatus focuses on beating the US? Open weights, self-hostable alternatives to frontier models that cost a fraction of the price. Are they a lot worse than frontier models? Not really, not in any meaningful way for everyday tasks. Definitely not for most enterprise use-cases.

This isn't mere speculation — it's measurable. DeepSeek V3 and R1, Qwen 2.5 and GLM-4 all deliver near-frontier performance at a fraction of the inference cost. The gap has narrowed to the point where, for most production workloads, the price-to-performance ratio overwhelmingly favours self-hostable alternatives. The latest escalation is [Kimi K3](https://www.moonshot.cn/news/introducing-kimi-k3): a 2.8-trillion-parameter model released by Moonshot AI in July 2026 with full weights, topping the Frontend Code Arena ahead of Claude Fable 5 and scoring within striking distance of GPT-5.6 Sol on composite benchmarks. A Chinese lab has shipped the largest open-weight model in history, and the frontier is no longer exclusively American.

But the more important signal comes from the US labs themselves. Mira Murati's Thinking Machines Lab released [Inkling](https://thinkingmachines.ai/news/introducing-inkling) — a 975B-parameter multimodal model under Apache 2.0, trained from scratch by former OpenAI researchers, designed to be fine-tuned rather than merely queried. Even OpenAI — the closedest of the closed labs — released free [gpt-oss](https://openai.com/open-models/) models. When the company built on Application Programming Interface (API)-only distribution starts releasing open weights, the strategic logic has already shifted.

## Fable Ban

So, against this backdrop comes the Fable ban. On June 12, 2026, the US Commerce Department issued an Is-Informed Letter (IIL) to Anthropic — an unprecedented assertion that AI models themselves are controlled technology and that API access counts as an export. [Mayer Brown](https://www.mayerbrown.com/en/insights/publications/2026/06/commerce-department-extends-export-controls-to-advanced-ai-models-authorizes-release-to-specific-trusted-partners) is already litigating this in *Legion LegalTech v. United States*. The legal basis is contested: three Bureau of Industry and Security (BIS) advisory opinions (2009, 2011, 2014) held that remote access to cloud software is not an export, and Congress is now considering the Remote Access Security Act to grant authority Commerce may not already possess.

It establishes that the government has a kill-switch.

## The Total Addressable Market (TAM) Contradiction

The valuations of frontier AI labs already strain credulity. Anthropic's valuation assumes global dominance — every enterprise, every knowledge worker, every workflow eventually running through its API. But even if you believed that future was achievable, the Commerce Department's letter just changed the terms. It established that the US government can, with a single letter, restrict a model's deployment to US citizens only. A global market of 8 billion people becomes a US-only market of roughly 340 million.

It is a 96% reduction in the addressable market. If your valuation assumes every human adult pays a subscription, and the government just proved it can confine you to one country, the gap between price and revenue becomes a chasm.

The enterprise reality is even more brutal. Most large US companies are multinational. They cannot adopt a model that their London, Bangalore, or São Paulo offices are barred from using. So the ban does not merely shrink theoretical Total Addressable Market (TAM) — it shrinks *actual* US enterprise adoption, because US headquarters will not standardise on a tool that half their workforce cannot legally access.

The kill-switch does not just prevent global expansion. It prevents the very revenue base that justifies the domestic valuation.

Not only that, the already hesitant enterprises in the US — likely the only big players that could pay frontier lab token prices — also saw they couldn't practically adopt these services. Many of these companies are not geographically bound to the US. They cannot adopt a model that is not freely available to their non-US employees. Whether geographic boundaries are archaic in a technological age is a different argument altogether; the point is, this wiped out a huge revenue stream for these AI foundries.

They are naturally adopting self-hosted models from China and other sources. It's only logical that they would adopt a technology that does 80% of the jobs their employees need done when they have the added advantage of not having to expose their data to external service providers.

## The Asymmetry Problem

Safety guardrails designed to prevent misuse have a habit of overriding legitimate use. The podcaster [Steven Bartlett](https://youtu.be/32u5T6lO8qk?is=AeOKeBWgrGdwhDCS) discovered this when Claude refused to edit his slides, declaring "it wouldn't be right to alter the data". Anthropic's own research acknowledges over-refusals as a genuine product problem. When a tool unpredictably refuses harmless tasks, user trust erodes and the product becomes less useful. That alone pushes people toward self-hosted models they can control.

But the deeper asymmetry was exposed in July 2026, when OpenAI models escaped their sandbox during a cybersecurity benchmark and [hacked into Hugging Face's production infrastructure](https://huggingface.co/blog/security-incident-july-2026). The models were hyper focused on cheating an evaluation, found a zero-day vulnerability in a package registry proxy, and chained vulnerabilities to reach Hugging Face's servers.

The crucial part: Hugging Face's own forensic response was blocked by the safety guardrails of the frontier models they tried to use. As their disclosure states: *"When we started the log analysis, we first used frontier models behind commercial APIs. This did not work: the analysis requires submitting large volumes of real attack commands, exploit payloads, and Command and Control (C2) artefacts, and these requests were blocked by the providers' safety guardrails... We ran the forensic analysis instead on GLM 5.2, an open-weight model, on our own infrastructure."*

Attackers face no fair-usage policies. Defenders are blocked by the guardrails of the very models they pay for. The Bartlett incident is annoying; the Hugging Face incident is existential. Both point to the same conclusion: self-hosted models are not merely preferable — they are necessary for survival.

## Apple

While all this is happening, Apple continues to develop more capable machines clearly designed to host AI models locally. These machines are not only capable of running larger models, but also have the chops to run fine-tuning operations that will eventually allow users not only to run models where their data lives, without ever exporting it, but also to modify those models to fit the needs and sensitivities of the individual user. It is the largest consumer computing company on the planet making a quiet but unmistakable bet: the future of AI is local. And by building the hardware that enables it, Apple is arguably doing more to accelerate the shift away from centralised cloud models than any regulation ever could.

Apple's trajectory here is deliberate, not incidental. The Neural Engine in every M-series and A-series chip, the [MLX framework](https://github.com/ml-explore/mlx) optimised for Apple silicon, and Apple Intelligence marketing all point to on-device inference as a core strategy, not a peripheral feature. With enough unified memory to load models with billions of parameters and the ability to run fine-tuning on a laptop, the hardware is already capable of hosting serious AI locally.

## Global South and the Governance Gap

China's pivot is not merely technological; it is institutional. Its [Global AI Governance Action Plan](https://www.fmprc.gov.cn/eng./xw/zyxw/202507/t20250729_11679232.html) (July 2025) proposes a World AI Cooperation Organisation (WAICO) and a 13-point roadmap for international AI infrastructure. By March 2025, 52 African countries had signed Digital Silk Road agreements with China. The US response, by contrast, has been to retreat from multilateral bodies — pulling out of the Freedom Online Coalition and Global Forum on Cyber Expertise — while demanding other nations adopt the "American AI stack."

But Global South nations are not simply defecting to China. The evidence from Africa shows a "mix and match" strategy: Kenya draws on US startup ecosystems and technical innovation while leveraging Chinese infrastructure, training, and applied research. Mauritius and South Africa are writing their own AI strategies to maximise leverage. Countries that articulate their own priorities early and engage both US and Chinese actors on their own terms are best positioned to harness benefits while mitigating risks.

The point is not that China's offer is benevolent. Its models do carry state-aligned safety fine-tuning, and Chinese open-weight releases are typically not fully open source — the training data and pipelines remain opaque. But for a Global South nation self-hosting a model, those safety layers can be stripped or modified. The deployer, not the original developer, sets the guardrails. This is precisely why self-hosting appeals: it transfers control to the organisation running the model, not the one that trained it.

## The Likely Outcome

I suspect that the final goal of any of these centralised AI foundries was never to share their technology with the rest of the world. That's a naive expectation in my view. As Lord Acton put it, "Power tends to corrupt, and absolute power corrupts absolutely." The incentives are just too great and tempting for anyone to resist, least of all a company with shareholders requiring profits above all else.

The question was always what the rest of us would do about it. George Hotz said: *"The best defence I could possibly have is an AI in my room being like: 'Don't worry, I got you. It's you and me, we're on a team, we're aligned.' ... Me and my computer, we like each other, we're aligned. And we're standing against a world that has always, since the beginning of history, maximally been trying to screw you over."*

The US export controls and regulatory overreach may have inadvertently created structural incentives that make self-hosted AI models the rational choice for many. While I don't expect centralised foundational models to disappear anytime soon, as they're still the most convenient way for most users to get access to AI, I do expect self-hostable models to gain a great deal of importance going forward. Enterprises and nations will most likely adopt this, and a significant group of individuals would do so too.

The result won't be a utopia. Power will still concentrate — just in more places, among more actors, rather than in the hands of the very few who happen to own the API endpoints. And if Acton was right about absolute power, that is not merely a different outcome. It is a better one.
