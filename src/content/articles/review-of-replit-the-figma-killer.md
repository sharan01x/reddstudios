---
title: "Review of Replit, the Figma Killer"
subtitle: "Replit has been thought of as a tool that will replace Figma. I tested it out to see if that is true."
date: "31 Jul 2025"
author: "sharanx"
tags: ["design","ux","ai","tools","technology"]
audio: "99458576_audio.mp3"
---

# Introduction

In my previous video, I wondered why design and coding tools had to be different and require constant translation when moving between them. Just two days later, Paul Graham tweeted that one of his well-known companies had ditched Figma in favour of Replit — validation that my curiosity was onto something big. As someone always eager to explore innovative tools, I couldn’t resist diving in myself. In this review, I’ll walk you through my experience with Replit and share whether it truly lives up to the hype.

# Disclaimer

Firstly, I must say that this article is in no way sponsored by Replit. I paid for the account myself and used the software and these opinions are mine alone. I got myself the $25/month plan. I paid extra per month firstly because I was just testing this out, but also because I feel that committing to a single platform for a whole year makes no sense when new tools are being developed and released all the time.

# Using Replit

## Objective

So, my objective was simple:  I wanted to prompt my way into bringing a working product to life and it needed to have the UX and UI that I wanted for it. The application that I was trying to build was one that could be used to take notes during meetings, summarise it and then share it with the user. I chose this as it’s not too complex but also not as easy as the demo apps that have been shown to work in a lot of cases.

## Third Attempt

After signing up, I was presented this box that asked what I wanted to build today. In my first two attempts, I said that I wanted to build an audio recording application that does such and such. For some reason this just didn’t work. It failed miserably, but we’ll talk more about it later on. So what I describe here is my third attempt where I changed tactics and tried to approach this in a very non-technical way. 

I began by stating that I wanted to build an app that would take notes during meetings. I further specified that there should be a toggle button to start and stop recordings, that it should clearly indicated that it is active and also send the recordings to a server for processing where it would be transcribed and the meeting notes generated. 

I didn’t specifically mention any platforms or specifications of the UI. I was hesitant to provide too much detail as I have seen AI agents breakdown because of this. Providing too little detail also doesn’t usually provide me the output that I want, so I’m never quite sure exactly how much detail I needed to provide. But there’s a helpful, “Improve Prompt” button and I’ve seen that clicking these usually provides the level of detail that is expected by the system. So I clicked it and it added details about the UI itself and chose “dark mode” for some reason. I’m not a fan, but I don’t hate it enough to want to change it for a trial app, so I just went ahead and asked it to start building.

Some interesting things happened at this point. It started “Thinking…” and after a few seconds came back and reiterated what it thought I wanted it to build. Mind you, I had just asked it to improve my prompt, so from my perspective it was already aware of what it was supposed to build, so when it said something like, “So you want to build…” with added surprise like it had become aware of this message for the very first time, it felt like I was talking to a moron, not something that was going to make things any easier. 

It feels like I’m splitting hairs here. I know the system needs to confirm what’s been understood, but I have seen more and more AI based interfaces use these conversational style interfaces and end up making this mistake of not keeping the user’s context in mind. 

Anyway, the good thing was that it suggested additional features that I could add on to my initial request. The suggestions were great and extremely relevant, but, not something I really needed to consider at this moment. This was really mis-timed and should have been something that was suggested after the main request was completed (which it actually does). It would have made more sense to ask questions that it needed clarifications on at this point.

Moreover, my experience with using AI based tools to create applications has taught me that it is better to start small and then build up the set of features that you want. So you need to do some planning yourself actually. 

Anyway, I asked it to just go ahead and build out the basic application first and then it began whirring away. The chat flow moved to the left and the right side showed a section called “Progress” and lots of things started to fly by. Pieces of code, snapshots of interfaces and more pieces of code, more snapshots, a database getting created, dependencies being installed, etc. and then finally, after about 3 to 5 minutes, it stopped, a panel slid up with the application in view (this is a nice feature by the way), and then in the chat, it asked me to confirm if the interface was visible to me. It had been taking snapshots until now, so I wasn’t sure what the question was. I clicked around on the interface and saw all the required components were indeed there. I clicked the microphone button and saw that nothing really happened. So I assumed that this is what was supposed to happen and so I responded in the chat stating that exactly, that the interface looked fine but nothing functioned as yet. But it didn’t quite respond to me and instead just went ahead and started building out the functionality. 

Again, I saw a whole lot of code flash by and then it finally stopped and asked me to test out the functionality. To my utter amazement the application worked and even had a nice visualisation and everything. I started recording, said a few things and when I stopped it, it saved the recording and then moved it to the server.

The layout was a little messed up and I also needed to improve the algorithm behind the uploading to the server bit, because it was possible that the mobile phone that is recording the meeting isn't always going to be able to stay connected to the server. So in such circumstances, it should save the recordings locally and then try to attempt to push the recording to the server whenever it connects again.

## Making Changes

After having made some edits in the previous attempts, I realised what was possible to edit and what wasn't. So I just cut to the chase and got rid of troublesome elements and made it make some changes that I needed. 

I was able to add additional features quite easily, but when I tried to ask it to work on a feature to mitigate upload issues and instead, to chunk the uploads in 10 second blocks and then try to upload it to the server, it failed to do this level of a complex task. But at this time, when I tried to go back to a previous checkpoint where things were working, it completely failed that and it seemed like it's roll-back wasn't well done. It seems that when it comes to using AI tools for development and prototyping work, there's no going back, only forward.

## Failures

There was one early attempt that I made where Replit hit an obstacle that it couldn't surmount. It gave me 3 options to continue trying,  try a different approach or to rewrite the whole thing in a completely different way. 

I responded in the chat stating that exactly, that the interface looked fine but nothing functioned as yet. But it didn't quite respond to me and instead just went ahead and started building out the functionality. There was a stop button and I clicked that but by that time, I think some code was written and that was that. It was a bad build and I just couldn't recover from that point onwards. I had to scrap the project and begin again.

## Using Templates

I even thought that I am making my life difficult by trying to build an app from scratch. There are a lot of templates available on Replit and I thought I'd try that out. But when I use a template, the AI Agent is no longer available to me and I can only talk to the AI Assistant that cannot write the code like the agent. I thought this was really strange and I didn't proceed with using the templates even though they seemed really appealing to me as starting points. 

# Lessons Learnt

This was a very informative experience for me. When I used the trial version, it ran out of available credits. If you've watched an older video of mine, you know that I have tried using GitHub Copilot and Windsurf and I ran into some problems there that made the left the development experience wanting. So I was actually really looking forward to trying out Replit because I had heard so much about it. But here's where I think things are at with Replit:

## Making multiple attempts is required

I've seen this with other coding agents and it's kind of interesting that I am seeing the same pattern occur here, but your chances of creating the application that you want in one shot is next to impossible. You need to go through the process multiple times like a video game and running into different bosses and striking out and then starting making sure to avoid those pitfalls when you try to build it all over again. 

## Start small and then add on

While Replit provides you the options to add a whole number of features all at the beginning, it's not a good idea. I think it's best to start with the barebones version of the application first and then once you have that bit working, add on new features.

## Editing the UI is hard

When I referenced elements on the screen by a certain logical name, it wasn't always understood by the agent. But since there's no way to point at a thing and identify them, it just wasn't possible to edit some elements. 

I also didn't see where the files were until much later, so going through the code and referring to a specific element just wasn't easy either.

So I used UI strategies where I worked around the need for these difficult elements. 

## Checkpoints don't work well

When I realised that the checkpoints weren't working as expected and weren't as reliable, I began downloading the files at the points where I felt I had things functioning just like I wanted. 

Additionally, there was a point where I chose the wrong checkpoint that was a much earlier version of the code where things had been working. Once it tried to restore to that point, there was no way to go forward to the next checkpoint instead. This was severely frustrating for me.

## Couldn't bring it to life

Despite the three attempts, I couldn't bring the project to life. I downloaded the code and while I tried to get it to function locally, I haven't been able to install the database and build the structure as yet. There's no file backup for the database elements, so I've got to figure this out on my own. I'm really not looking forward to this. 

# Bottom Line

## Not there yet

I don't know what Paul Graham's acquaintance was thinking when they've committed to working with Replit and remove Figma. I don't think Replit is there yet. Can they get there in the future? I sure hope so. But will I be replacing Figma, Framer and Windsurf right now? No, not at all. 

## UX is not great

If you watch some videos of Replit from before, you'll notice that the agent chat window has gone from being the ancillary element on the right to the primary element on the left. This signals that they thing of code and files as secondary elements to writing the code right now. But they haven't evolved fully as yet. In order to appeal to designers or non-developers, the interface needs to be able to refer to elements and operate them in different ways. As an example, if I had a way to point at elements on the right-side preview pane, it would have made my life so very easy.

Additionally, they need to provide a way to build and utilise design systems at the same time. 

## Really not meant to create stuff you have in mind

It occurred to me that if I begin with a very specific idea in my mind and try to recreate that using Replit, it's going to be super hard if not impossible. So this tool really isn't about doing that, but instead to explore new ideas and interactions. 

Even if I gave Replit exactly the same set of commands in the same order, I don't think it would arrive at the same output at the end. That's a challenge for anyone that wants to have any kind of control over the outcomes. But for exploration, it's a fine approach. 

## I wouldn't build anything large or serious

As mentioned before, I have to assume that I need to attempt to build the project multiple times. This limits the kinds of things I can do with Replit. I cannot imagine building a large application. 

Since the project that was output in the end felt like a precarious Jenga tower, I am not exactly certain that this application would perform well in production. I'm just not that confident. If it's a blog or a static website, that's an entirely different matter and I probably wouldn't feel the same way about that. 

## Deployment is a nice touch

I think Claude and OpenAI demonstrated the artefacts panel in their interfaces. I found that to be extremely important because we could avoid the environment setup and things like that. With Replit, they've taken that to the next level by including deployment. So not only can you test and see stuff while building it, you don't have to deal with deployment issues that are all too common when you're ready to push the app and make it live. 

## Local software incompatibility

One of the biggest issues that you will face with Replit and it's ilk is that you cannot have it interface with locally running software. In this example itself, I had the option of having this app work with Ollama installed locally because I would actually be running many tests and didn't want to hook it up to OpenAI. But there was no way to do this that I could figure out. 

## They're straddling two boats and need to commit

While it's perfectly natural for every startup to pivot when they find new product-market-fits, I think Replit is currently mid-pivot as they haven't really committed to building tools for non-developers as yet. They began as a developer focussed tool to begin with, and they haven't completely changed their focus and redesigned the older tools to suit the needs of designers and other non-developers. Once they commit, I think I would expect a lot more from them.

# Conclusion

I have never hit "Cancel Subscription" on any tool faster than I did with Replit. The task they've undertaken is hard, but they're not yet where they need to be to get me as a user. My experience developing an application was much better with Windsurf (in conjunction with Perplexity) and I'll be going back to it. 

But if this blog has somehow made its way to the Replit team, I would happily invite them to a chat with me as I can recommend many more things that they could do to get users like me on board. Otherwise, I wish them well and hope to use their software after a few months to see if it will suit me then. Until then, I wish them luck!

# Accompanying video

Supplement video contrasting features with Lovable.dev