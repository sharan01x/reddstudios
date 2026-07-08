---
title: "Get Your Agent to Build You a Custom Audio Generation Tool"
subtitle: "A step-by-step guide to building your own audio generation pipeline with text-to-speech, voice cloning, and background music"
date: 7 Jul 2026
author: sharanx
tags:
  - ai
  - design
image: audio-generation-tool-header.png
audio: audio-generation-tool_audio.mp3
---

This is the second in a series about building custom tools to help you as a designer. We already covered custom image production in the previous video; in this one, we will be covering a custom audio generation tool. Most of these tasks can be performed locally on computers with modest amounts of memory and processing power. So, if you have ever needed to produce spoken words from text, produce background music, or clone an existing voice, read on.

## Why build these tools?

Just one quick question to answer before getting started — some of you asked why you should build these tools when you can simply ask your agent to do the same things. Well, there are two simple reasons.

First, if there is a process that you find yourself asking your agent to perform repeatedly with only minor changes each time, turning it into an executable app or script may improve the speed of execution and will definitely save you a lot of tokens.

Second, you will gain the ability to have these tools used by other agents that you may have.

A simple example is the social media posting tool that I have built for myself. Each time, the post is different, obviously, but apart from that, the process is absolutely the same: post messages via API calls and browser automation. I have two agents using the same tool. One posts exclusively to my company accounts and one only to my personal accounts.

With that out of the way, let's get into it.

## Text to Speech Tools

If you are anything like me, you find yourself listening to podcasts and the audio versions of Substack subscriptions when you are out walking your dog or running errands. I find it much more convenient than reading in these situations. Since I have a blog, I wanted my articles to be available in audio form so that readers have the choice of reading the article or listening to it, whichever they prefer.

Since I was producing audio versions for every new article I published, I decided to build a tool for the purpose and integrate it into the article publishing process.

Now, when I write a new article in Obsidian, I just ask my agent to go through all the steps of publishing the article and it will automatically produce the necessary header images (using the image37 tool I described in the previous video), create the audio version of the article, add it to Astro, build the new site, and finally push it to GitHub — all automatically.

This class of audio tools is called text-to-speech, or TTS for short. The leader in the field used to be ElevenLabs, a subscription SaaS, and they were genuinely better than a lot of other tools for quite a while. But within the past six months, many open-source projects have become extremely good. They include:

1. Kokoro
2. Fish Audio S2 Pro
3. Chatterbox — Turbo and Base variants
4. Qwen TTS — Turbo and Base variants
5. LuxTTS

When working with TTS, you need to consider what voice you want the text read in and how expressive that voice can be. Some models also allow you to clone voices, so that is also something to consider if you need that feature. Here is a table of these models and their capabilities across these two dimensions:

| Model Name        | Preset Voices | Custom Voices | Expression     | Languages      |
| ----------------- | ------------- | ------------- | -------------- | -------------- |
| Kokoro            | 54            | No            | No             | 9              |
| Fish Audio S2 Pro | 1 (generic)   | Yes           | Yes (~30 tags) | Multi          |
| Chatterbox Turbo  | No            | Yes           | Yes (tags)     | 1 (en)         |
| Chatterbox MTL    | No            | Yes           | Partial        | 23             |
| Qwen3-TTS Base    | No            | Yes           | No             | 10             |
| Qwen3-TTS Custom  | 9             | No            | Yes (instruct) | 10             |
| LuxTTS            | No            | Yes           | No             | Multi          |

So, depending on what you anticipate you will need in the future, you can choose one or more models from this list and find the GitHub repositories in the table below. There is absolutely nothing to stop you from using more than one of these models at the same time, so keep that in mind too.

| Model Name        | GitHub, NPM or Web Link                   |
| ----------------- | ----------------------------------------- |
| Kokoro            | npm package 'kokoro'                      |
| Fish Audio S2 Pro | https://github.com/fishaudio/fish-speech  |
| Chatterbox        | https://github.com/resemble-ai/chatterbox |
| Qwen3-TTS         | https://github.com/QwenLM/Qwen3-TTS       |
| LuxTTS            | https://github.com/ysharma3501/LuxTTS     |

**Note:** I have not included any online service providers here, as I do not think they are necessary any more. The LuxTTS package, for example, is an extremely small model that can produce very accurate results locally.

## Installation of the first model

I am going to start with Fish Audio S2 Pro. The installation process is simple — just ask your agent to:

```
Install and configure Fish-Audio S2 by following the instructions here: https://speech.fish.audio/install/
```

Substitute the text above with your model of choice and the link to the correct repository. You may also want to add the following to make installations and dependency management much simpler:

```
Use UV as the Python package manager and create virtual environments as necessary.
```

Adding this instruction about UV will save you a lot of effort in the future. Your agent should have all the information it needs to install this on your system. If you run into any issues, ask your own agent to debug the steps and it will.

Once the installation is done, ask your agent to run a test:

```
Generate an audio track using the Fish-Audio S2 model for the text "Hello! How are you?" and place that file on my desktop.
```

Your agent should go through the Fish Audio S2 code, figure out how to use it, and then generate the audio file from the text. If everything went well, this audio file should be on your desktop.

This demo step is also required before building the wrapper application, which will simplify using multiple models together.

## Creating the wrapper

If we leave things as they are, your AI agent will be able to use the model to generate the audio you want, but it will spend a lot of tokens and time going through the source code of the model every time. It becomes even harder when you start to use more models and features, as it will need to understand each of their codebases every time as well.

To avoid all this, we will build a "wrapper" that will act as an abstraction layer, essentially separating the complexity and the variations between models to create a unified way of working with all of them.

Here is what you need to ask your agent to do next:

```
Build me a local audio generation tool called `audio37` in my Code folder. It should generate text-to-speech (TTS) and spoken article audio — all running locally. Make sure that all outputs are stored in a 'storage' folder within this tool's folder. Pass along the path to the file once the audio file is produced.

The tool is an **orchestration layer** that delegates to existing TTS providers, each installed in their own isolated virtualenv. Audio37's venv only handles CLI/API logic; it calls each provider via subprocess to the correct Python interpreter in that provider's `.venv/`.

Audio37 will also only be used via the CLI. So please make sure to allow all the required inputs to be provided through parameters. Use intelligent defaults when any required parameters are not provided, including setting the output format to MP3 if supported by the provider.

The first provider that it needs to work with is called Fish Audio S2 Pro, which you recently installed.

Once you're done, create the AGENTS.md file so that agents know how to use the tool.
```

This should get your agent to build out the wrapper tool. I have named this tool "audio37", but feel free to use another name if you prefer. It will also create the AGENTS file that any agent usually reads in order to figure out how to use a tool with which it is unfamiliar.

This process really should not take too long, and once it is done, it is time to test whether the tool is working well. This is one of the patterns that I recommend when working with agents: get them to build the stuff, but you remain the person who is testing things and making sure that they are working well.

To test the wrapper, ask it to do something like the following:

```
Use the audio37 tool to create an audio version of the text "Hey! It's me again! I hope this works as it should!"
```

The output this time should be the path to the file in the storage folder within the audio37 folder.

## Cloning voices

I used to use the Kokoro model with the British Male voice preset for the articles. I did this because the voice cloning technology from Fish Audio S2 Pro made my voice sound like a generic Indian voice rather than the voice I actually have. It seems that the older voice models had these prototypical voices, and if your voice was close to any of them, the models would just default to those. But these newer models seem to do a much better job of trying to copy the actual voice. They are not perfect, but definitely usable now.

If you would like to add the ability to clone voices, you can do so by using LuxTTS. The quality of the outputs provided by Qwen is better, but the model requires a huge file to be downloaded, which makes Lux a better recommendation for most people. The speed is also incredible. So, to do this, ask your agent to:

```
Install the LuxTTS model available at https://github.com/ysharma3501/LuxTTS and set it up with its own virtual environment using UV.

Once you're done with that, wire it up as a second provider to the audio37 tool we built earlier and extend it to allow for any new features supported by LuxTTS while choosing intelligent defaults, including using LuxTTS for all requests requiring a custom voice.

Add a "custom_voices" folder within the audio37 folder. If no custom voice file is provided, choose default.wav from that folder to use as the voice to clone.

Update the AGENTS.md file once you're done with the above installation.
```

This simple command will download and install the right files. Then it will rework the audio37 tool to make sure that you can continue to use a single tool to work with various audio models.

Now, before you run a test, you need to provide it with a voice to clone. You can do this easily by recording your voice using any number of tools built into your computer. Make sure it is about 20 seconds long. LuxTTS needs only a few seconds, but some models need between 10 and 25 seconds of recording. Name that file "default.wav" and drop it into the "custom_voices" folder within the audio37 folder. Then you can run the following test:

```
Use the audio37 tool to produce a custom voice version of today's top headline on BBC.com.
```

This should look up the website, find the heading, and get it spoken out sounding like the voice you supplied. It is as easy as that! If you find that the speech is too fast for any reason, ask your agent to set the default speed of speech to 0.8 if no speed is specified, and audio37 will automatically slow down the speech.

If you find better tools tomorrow, just bring them in and start using them as shown above. But your usage will not change. Your agent just keeps getting new capabilities without changing the way you use this audio37 tool.

## Extending audio37

The above should have given your agent some really amazing capabilities to help you with. But there are some ways in which you could extend the capabilities of audio37. Here are some ideas.

### Going the other way

Needless to say, you could easily go the other way and have the tool transcribe audio files to provide you with the text version of them. This is useful in many situations as well. You want to look for models that are capable of "speech to text" (STT). If you do this, just have your agent choose the right model and produce the text version of a voice file if one is provided as an input instead of text.

### Multiple voices

Suppose you want to have audio where a number of different "people" are speaking in it, like a podcast or a news programme with multiple newsreaders reading out each news story. You can do so by creating scripts with specific speaker names assigned to each part of the text that is meant to be spoken, and then asking audio37 to use a specific voice for each name. There may be a little more work that you need to do here, so if you do go down this path, leave me a message and I will create detailed instructions for doing this.

### Infusing emotion

Many audio models can infuse a little emotion into various parts of the audio while speaking. You may want them to say something in a whisper, laugh after saying something, or express surprise when saying something, and so on. Most of them require you to add tags within the supplied text, which will produce the audio with the right emotions. This can be an involved process, but there are ways to automate all of this.

### Cleaning up old files

Some of you will notice that we asked audio37 to keep the outputs in a "storage" folder. If you use this often, you will end up with a lot of audio files over time. Keeping track of cleaning up the folder becomes a difficult task over time. But you can automate this by asking your agent to make the audio37 tool automatically delete files in the storage folder that are more than 30 days old every time you use the tool.

## Conclusion

Building these kinds of tools can be a rewarding process. It is a lot of power in your hands. But if you do get stuck or are unable to figure out how to get this kind of tool to suit a specific need of yours, just drop me a message and I may be able to help you. If you got everything working, then congrats and have fun!

Next week, I am going to be talking about building a similar tool for video production. You should tune back in for that!