---
title: "The New Age of the Design Generalist"
subtitle: "AI tools have made coding simpler. Skills are no longer relevant. Imagination and envisioning a particular future is more necessary than ever."
date: "30 Dec 2024"
author: "sharanx"
tags: ["design","ux","ai"]
---

# The 'Boring' Part

Recently I've been having a lot of difficulty in staying on top of my social media game. Not being a native to social media, I approached it with a certain disdain in the beginning and completely missed the wave. But given the new course I have set upon, I intend to learn as much as I can and get better at this now.️

But the tedious aspect of social media has got to be the manual process of posting content on each and every channel that I have become a part of. That's the biggest hurdle and the most boring aspect of the entire process. There are some tools, and I subscribed to Typefully to be able to do this. But, alas, Typefully doesn't support the social platforms on Web3 that I am a part of. So I looked for various solutions and none of them satisfied my needs. It occurred to me to try building an application that would do this for myself with the help of AI and I am so glad I did because, a whole new world has opened up to me now!

I began down this path in the usual way that one builds software these days. I got access to ChatGPT, but I found the idea of copy-pasting between the chat interface and VS Code tedious and quite problematic as I am not a very good developer and often made mistakes with where I copied and pasted from. Github Copilot Chat was like having the same ChatGPT capability but repurposed for use within VS Code, though I still had to copy and paste between panels. But GitHub Copilot has a new feature called "Edits" which would directly make the edits to your code. This made things a whole lot more convenient. I could even describe what I wanted to do in plain english and it would make the right edits directly in my code. This was a game-changer! 

So, with my new setup in place, I began by describing what I intended to achieve at a high level and asked it to recommend the right technology stack. It recommended that I built with Vue.js for my intended purpose, I said "Fine" and it began whirring away setting up the environment with all the required files and started to build out my views. 

I didn't know what the limitations were going to be, so I wanted to do a trial project first. I gave it some instructions for a "Hello World" program and it performed it beautifully and I got it to work as expected without much difficulty. The trouble came afterwards where I asked it to scrap the trial project and begin working on the real one. It completely couldn't figure out how to take steps backwards. It was easier for me to delete the entire project folder and start again, so that's what I did. But it also highlighted to me that this would be a limitation I would have to deal with using this tool. So I had to chart a course of building features one by one while I get to the final version without having to remove or modify the previously built feature.

In my plan, I was going to build a social media posting utility that would allow me to post across multiple channels by supplying it with a single post. So the simplest form of that application was going to be a feature that would post a message on a single channel first, then I would add a drop-down with additional channels and then create a broadcaster that would post across every channel, then a scheduler, etc. 

This approach worked out rather well. I had to learn to be very specific at times and very broad at other times and that was straightforward enough. But I hit a road block when, after building out the functionality, I wanted to improve the UI and started making fixes. Now these fixes needed to be made across all the interfaces, but for some reason it had a lot of difficulty doing this across the various modules that I had built. It got to bad that I decided to use an entirely different front-end framework that would keep things standardised out of the box so that I would have to do very minimal work in order to make the UI look good. I chose to build the application with Streamlit. 

At the same time, I heard about Windsurf as an AI infused IDE and saw the demo video and it looked great, even better than Copilot Edits. So I downloaded it and built a simple demo application with the trial credits. It was simply an entirely different experience. I simply describe the application I wanted to build and broke it down into the steps that were going to be required to achieve that and since I had it in the "Write" mode, where it could make file edits and changes, it simply went about doing everything. If I was impressed with Copilot Edits, this blew my socks off. I had the entire application setup and ready to go with Windsurf taking some incredibly good decisions regarding the things I hadn't mentioned. It even named all the modules and variables in the code as I would have done myself! It was simply outstanding. I was able to achieve what I could with GitHub Copilot over the 5 or 6 days in a matter of 1 day. It did help that I was doing this a second time around, so I knew what the right approach was and didn't make as many mistakes.

But Windsurf hasn't been without it's flaws. There were two times where I asked it to write a module "like the edits that you made to the Twitter module..." and it not only wrote the new module in the way it had done the Twitter module, but went too far and made edits to other modules. I had to learn to limit its scope by adding "Do only this and don't make any other edits" to my instructions and that stopped the problematic edits from being performed. So, the very thing that it was great at and extremely useful at the beginning stages of an application became it's Achilles heel later on. It was quite literally the opposite of GitHub Edits in this regard. So, the workflow that I would use for future application development is to use Windsurf in the beginning stages of the application and then switch to GitHub Copilot for specific edits and module-level enhancements. But of course, I am talking about their qualities as of today. I completely expect that the teams behind these two tools will find ways to integrate the best features of each other's AI code companions. 

But this isn't meant to be a discussion on the usage of these tools at all. Creating a video about the right ways to work with these AI tools is a fool's errand because these tools have obviously been built by very smart people that really do understand what they're bringing to this world and they will keep making improvements until these tools work just the right way it is meant to be by it's users. No, it's a discussion about the fact that I now stand in front of a very designed and well built application that does exactly what I want it to do! The implications of this has in equal parts shaken me and blown my mind, and I had to talk about that!

# The Interesting Part

The following are the changes that I expect to see on the horizon. There are numerous impacts of the stuff that I've been doing that I can see and I've done my best to list them in a logical order.

## OS

Firstly, these tools, in their current form have made a huge leap forward in the span of a year. The capabilities of frontier and open-source AI models are only going to become better over time. This will allow them to factor more parameters into their operations. In other words, you will be able to communicate with the AI engines in as many ways as you need, speaking some actions, writing out some others and even supplying your Figma designs straight into the LLM's for them to understand and execute. 

But then, if you extend that idea, one may ask, why couldn't the AI write the program at the time of need? Or even better, couldn't the AI become the application necessary to do the tasks and instead of providing a chat interface, provide the interface that an application would provide a user. A majority of applications are simply interfaces over some data source, so while there are many qualifiers to this sentence, the short answer is yes, it truly can become that super app and replace the user-facing part of the operating system. The OS will be relegated to managing security, permissions and managing the hardware interfaces. ^5b3b30

## Skills

In this world, where would UX design fit in? If an AI can understand the best ways humans interact with interfaces, they can not only produce those interfaces with scarily effective interfaces, but also tune it to the needs of a single individual, no longer serving only the needs of the majority. In such a world, what role would a human UX designer play? I fear, it will no longer be relevant. 

## Roles

In the short-term however, the role of the UX designer will change. They will no longer be beholden to a developer and their capabilities anymore and can circumvent them and develop a great application on their own -- just as a developer will no longer need a designer for the applications they will create. As AI takes over more tasks, traditional design roles are likely to shift from execution-oriented to focus on strategic direction. 

The job will be to instruct AI agents to perform the required tasks in the manner in which it needs to be done in order to achieve the goal. So practical imagination and planning will be the skills that will set us apart going forward. People like lead designers or lead design organisations are going to be much better equipped to jump into this role more naturally than anyone else. But this is only for the short-term and they too will need to go up the chain and up-skill themselves to think like entrepreneurs in the long term, because AI will take over the planning aspect as well soon.

## Tools

Our current design tools are built for specialists and therefore are designed for precision. You can edit just this pixel, move exactly this screen and change exactly this effect. However AI can handle the details and the tools of the future are going to be designed around doing things with broad strokes. So it can take inputs like, "a background of a desert dune" or "a login flow with 2FA", instead. The broad strokes are just going to get broader over time with humans being able to specify things in a increasingly abstracted manner. If you look at Krea.ai as an example and see what they're doing with the Edit feature and compare that with the Photoshop workflow, this aspect will become even more evident. 

Logically, this also means that the target audience is going to change. It's no longer going to be appealing only to a graphic designer anymore but an entrepreneur running a company could use Krea, today, with little to no knowledge of graphic design and create some stunning artwork for themselves. 

## Economies of Scale

The dynamics of the economy will also change within the digital space. One of the biggest challenges in the software industry has been to design features that appeal to every individual. But because it costs a lot to design, code, test and release a certain feature, the decision has always been skewed towards appealing to the majority of users and ignoring the fringe needs. But with AI in the mix, this very dynamic can change. As I was discussing before, every feature and interface can be built to appeal to the individual user. Maybe the workflow will be that the human orchestrated output will be the feature that appeals to the majority of users, but AI can use that as a starting point and fill in the gaps to make that feature work for the fringe users? This changes the entire industry.

## Unexpected Benefactors

One of the biggest benefactors of the economies of scale change are going to be the group of people that are currently disadvantaged by the digital world today. For example, these could be people with eyesight challenges or even the elderly that have so far been left behind by the digital world and are left more and more unsafe because of it. My own father keeps sending me fake videos of various things completely believing whatever thee video says. And since he's at high risk in a digital world, I have had to ask him to not do any digital banking and completely prevented him from using UPI and such. My mother is unable to use these technologies as she's a non-native-English-speaker and most interfaces are designed for English. Imagine user interfaces that will adapt to them without additional costs to the software developer. They would finally be able to cross the chasm and join the rest of the digital world.

## The Generalist

In this AI assisted world, there is a power-shift taking place. The users of AI are going to be able to build anything they can imagine. You no longer are constrained by needing a large team to execute on your vision. A lot of the roles of the team that one needed to build in the past can be executed by an AI agent today. It's only going to be able to handle more roles in the future. This means that the required capital to build the companies of the future is only going to reduce. It therefore means that more and more people with the imagination and desire to do something will simply be able to. 

A typical entrepreneur today is a generalist that understands a little bit of all the pieces that are required to execute something and can bring all those pieces together. Broadly speaking, they identify the need in the market, develop a vision for the solution to the problem, then they bring in specialists to fill in the gaps and capitalists to provide the capital required, and create the culture required to execute on the vision. It's this very person's role that will be made infinitely better in the future. In the digital world, we're ushering in the dawn of the age of the generalist. 

# Accompanying Video