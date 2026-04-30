---
title: "The Design Tool Stack for Q2 2026: A DIY Guide"
subtitle: "How I replaced Figma with AI agents, Ollama and Hermes to build working prototypes"
date: 30 Apr 2026
author: sharanx
tags:
  - design
  - DIY
  - tools
  - ai
audio: design-tool-stack-q2-2026-diy-guide.mp3
image: design-tool-stack-q2-2026-diy-guide.png
---

I began my AI tooling adoption when Midjourney started to produce images of great quality. That was great for images, but I was always of the mentality that finding new tools was not where I wanted to spend my time. I just wanted to get things done.

Windsurf, Cursor, Krea.ai, Replicate, OpenCode and OpenWork were trialled, and I saw various levels of success. But it was with the release of Claude Sonnet 4.5 and Claude Code and other agentic coding platforms that I started to see real impact. Today, I rarely touch a specialised design tool. Figma has become a super-specialised tool that I only reach for when I need to lay out a social media banner. Even then, it feels like a trip to a foreign country where I have forgotten the language.

The future looked promising, but I had to figure out a lot of details to make this happen. This article is a record of the design stack I have built up to replace the old toolchain.

---

## What I Need From a Design Workflow

So when building all these tools as well as producing my regular outputs, I identified four main goals I needed to achieve:

### 1. Exploration
When initially working on a project, I need to try out multiple variations of design with different emphasis on different parts of the workflow, suitability to different audiences, and even design themes. Using AI to do this was unbelievably productive. These things would take a long time before, but now could be done with no more effort than typing a well-structured prompt.

### 2. Bridging the Gap
In the next stage, once I choose a specific direction, I need control over the changes I make on the outputs. Here, like Cursor or Claude Code does, pointing to different elements and asking for changes is the gold standard. Tools that allow this specific interaction win over the tools that do not.

### 3. Hand-off
Hand-off to the next stage in the life-cycle needs to become easier. With Figma, the hand-off was on a design surface and while the developer got some code, there was really a lot of discussion-led development that was still required. My requirement was to deliver working code that displays full functionality including micro-interactions, transitions, animations, and responsive layout.

### 4. Extending
Once a project is delivered, it usually requires feature additions or modifications. That task may be performed by another team member or even a different team. In these circumstances, I need to have the right things to build upon when that happens.

I evaluated the various tools against this backdrop of needs and the results are described below.

---

## Installing the Basic Requirements

There are two tools you need to install: Ollama (for models) and Hermes Agent (for agentic tooling). I will show you the fastest way to do this, and then break the steps down below in case the shortcut does not work for you.

### Option A: Single Command Installation

The simplest way to get started is with this command. It installs both Ollama and Hermes Agent, hooks them together, and sets the agent to use the latest available model:

`ollama launch hermes --model deepseek-v4-pro:cloud`

**Note:** At the time of writing (April 2026), the best model I have found is DeepSeek V4 Pro. You can replace the model name with anything newer you find on the [Ollama Models](https://ollama.com/search) page.

### Option B: Manual Setup

If the shortcut command does not work for any reason, follow these three steps.

#### Step 1: Install Ollama

While some people prefer to use the frontier models from Anthropic or OpenAI, I have never been a big fan for two reasons:

1. They are not always most efficient in terms of costs or time taken.
2. They are not private, so this limits the kinds of projects I can work with them on.

I wanted to work with all the options available to me and for this reason, I wanted to work with other models that are available. There are many tasks that just do not need frontier-level intelligence and I wanted to be able to use the right tool for the right job. I went through many options, but found the Ollama subscription (also $20/mo) gave me the most flexible set of options.

The added benefit over using OpenRouter or another service is that I can switch between the more powerful cloud-hosted models and the more private locally running models without switching anything but the models. This is critical for headache-free operations.

Ollama has its own minimal and beautiful chat interface and will do for most common question-answering sessions if you need it.

**Installation:** Download Ollama from [their website](https://ollama.com/download).

#### Step 2: Install Hermes Agent

This is an agent harness that is comparable to OpenCode. It has agents, memory and the ability to develop and run skills, but I find that Hermes has been built with more security in mind and comes with many built-in tools and skills that make it great to use out of the box.

One important feature that Hermes Agent has is that it can build its own skills. So if it notices that I am doing something that it expects will be a task I am likely to repeat, it will just turn it into a skill. I find this incredibly helpful.

**Installation:** [Simple steps to follow](https://hermes-agent.nousresearch.com/docs)

#### Step 3: Connect the two

##### 1. Make Ollama available to other apps

Go to Ollama Settings and click on "Expose Ollama to the network". This will make your Ollama server available at the default location of `http://localhost:11434/v1` which is the OpenAI-compatible endpoint.

##### 2. Connect Hermes to Ollama

If you used the shortcut command and it worked, you can skip this. If not, run the following command in the terminal:

`hermes setup`

That will take you through a wizard where you can configure the Model & Provider. Choose 'custom' as the provider (unless Ollama is an option) and provide the local Ollama URI:

`http://localhost:11434/v1`

or

`http://127.0.0.1:11434/v1`

I recommend using the latest and greatest model name that is available. At the time of writing it is DeepSeek V4 Pro:

`deepseek-v4-pro:cloud`

You can find the models available in Ollama by going to the [Ollama Models](https://ollama.com/search) page.

Use "dummy-key" or anything else as the API key and ask it to auto-detect context length. And that is it. You have got everything you need.

---

## Using Hermes Agent

All you have to do to use Hermes Agent is open a terminal window and type in:

`hermes`

This will launch a chat interface and you can ask it to start building websites, applications, and so on. That is the Claude Code equivalent experience. But if you want to get the most out of your setup, look at performing some of the quality-of-life steps detailed below.

---

## Quality of Life Upgrades

### 1. Add a messaging interface

Since I do not expect to be using the agent only when I am in front of the computer, I want to make it available to me remotely. This is easily achieved by using one of the many supported gateways in Hermes. I chose Slack because I can have multiple threads easily and the interface is familiar. Others have liked Discord. I would caution against Telegram because of the threading limitations.

### 2. Add better memory

Hermes Agent comes with a robust memory system already built in, but I find that it only gets better if I ask it to use the Honcho memory system as well. It is a lot more involved and technical, so skip this if you are not comfortable with the terminal or Docker. I do not recommend using the hosted Honcho setup as that is a privacy hazard in my opinion.

### 3. Add multiple profiles

One more thing that helps with memory and context management is to create multiple Hermes Agent profiles. Basically, run multiple agents with the same infrastructure. You can assign different Slack App credentials to each and keep having separate conversations with each of them.

While the documentation may lead you to think of each profile as a separate function, like coding, marketing, and so on, I find it easier to think of them as people.

For example, I created five different agent profiles:

1. One main agent that I frequently talk with about performing all sorts of personal tasks. Sometimes it needs to write a small program to get the task done, sometimes it does research on the web, and at other times it manages medical reports and sets up reminders.

2. One agent assigned to teaching me languages.

3. One dedicated coding agent. This is because I have a lot of code that needs to be written and I do not need this agent to also have context about what my dog's medications need to be.

4. One running parts of my business.

5. One dedicated to doing things privately on my computer. I use a locally running model for this so that not even anonymised data leaves my system.

The only limitation of these profiles is that they cannot communicate with each other. This is probably a good thing. But I had imagined being able to hand off a task between each agent, and that is not possible in the way Hermes Agent is architected at this point in time.

### 4. Add soul

There is a SOUL.md file for each profile that you create. Take the time to add details about the agent and what they each need to know about you, your computer setup and organisation, what their default communication styles should be, and so on. I reduced a lot of repetition by specifying a "home" folder for each agent where I want it to look in case it does not know something I reference. It saved me a lot of time that I would otherwise spend telling it simple things like where it can find the company operations manual, or what the schedule is for upcoming writing exercises.

Another thing to specify in the Soul is the conditions under which you want it to delegate a task. More on this next.

### 5. Add delegation

Hermes Agent provides the ability to assign a different model to use as a delegate within the same profile. For example, you may want to use DeepSeek V4 Flash as the primary model and DeepSeek V4 Pro as the delegate model. By doing this, you get the fast and inexpensive responses when you ask a question, but when you need something more complicated done, your agent delegates the task and it will then use the more powerful model to do those things.

As mentioned above, in the coding profile's SOUL.md, I specified that "You should delegate any long-running or complicated coding tasks." This automatically makes my life easier and employs the more powerful model when it needs to.

### 6. Add MCPs (Chrome, Paper and Framer)

Google Chrome, Framer and Paper all offer connections to agents over MCP servers. Getting these configured makes it extremely simple to make edits, view them and share them as necessary. Just get your credentials and server URLs and ask your assistant to configure itself for these MCP servers and it will set it up.

### 7. Add GitHub

Since I am going further with design and developing working prototypes, GitHub is a great platform for version control and for collaboration on projects. Hermes Agent knows how to use GitHub even if you do not, so just ask it to start using it.

### 8. Use voice

It is just a lot faster to provide directions and inputs to your agents through voice. Working with code is difficult to do this way, but you will save yourself a lot of time by not having to type, which you will do a lot.

---

## What My Design Workflow Looks Like Now

With the tool stack that I have described, my new design workflow looks like this:

### Step 1: Plan with the agent
I describe what I want to achieve and ask the agent to specifically work on an implementation plan and not begin implementing it just yet. I specifically ask it to ask me any questions that it may have after it develops an implementation plan. 

### Step 2: Debate and influence
Usually, agents are meant to make assumptions about defaults and proceed to get the job done. But forcing it to respond with questions after developing an implementation plan forces it to list out the assumptions it is making. This is where you can influence the design of your application. 

### Step 3: Watch every step and intervene
Once you ask the agent to begin developing the application, you can see the thinking stream where it is making more of the detailed assumptions. This is where you watch and understand how it is thinking through stuff. Often, if you find that it is making the wrong assumptions, you can redirect it and tell it to go a different direction by interrupting the agent.

### Step 4: Test and refine
I always ask the application to be launched and test it often. When there are errors, I copy and paste the entire error and ask it to fix it. If I need to fix something and if that object can only be best identified by pointing to it, I will switch tools and go to Cursor or Windsurf and open up the same page there and use the tools to pick the element and ask for the changes there. I can then return to Slack and continue working on the application with Hermes Agent.

### Step 5: Create design systems
As we go along, I tell Hermes Agent to develop and iterate over the design system that governs the application. It is usually developed as a markdown file that I include as part of the project.

---

## Limitations

### 1. Figma is a no-go

I tried integrating my AI workflow within existing design tools like Figma, but this was not always successful and felt like a force-fit in a lot of situations.

### 2. Inter-agent communication

As mentioned, the various Hermes Agent profiles cannot communicate between each other. I have not found a workaround to this as yet. So for the time being, I have to repeat some of the things I may have already told one agent, but need to convey it over again to another agent.

In an ideal world, I would be talking to just one agent and it would hand off the task to the right agent with the right context and make sure the job gets done. I think we will get there.

### 3. Privacy

While this setup is definitely a lot better than working with the closed frontier model providers, the only guarantee that your private data will not be used by the model providers for training their models is their contracts specifying this with Ollama. There is no real assurance that your data is perfectly safe unless you are using the locally running models. If you still need to use the power of larger hosted models, you could benefit from having only fragments of your information available to each of these providers by rotating models often.

### 4. Low fidelity wireframes

The thinking we did when working through low-fidelity wireframes is just not possible with this new workflow. We need different ways to force that thinking even when the tools are far too efficient to need it.

That is the stack I am running in Q2 2026. It is not a perfect replacement for every design task, but it has already changed how I think about the gap between design and working software. If you try this, or a variant of it, let me know what you find.