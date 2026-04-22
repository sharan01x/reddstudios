---

title: "Co-existence of Voice Interfaces in Apps"
audio: "3affedad_audio.mp3"
subtitle: "While every sci-fi show depicts Voice Interfaces as the future as it seemingly makes for very simple interactions with devices. I examine this idea."
date: "23 Aug 2019"
author: "sharanx"
tags: ["design","ux","voice"]
image: "co-existence-voice-interfaces.png"

---

# Introduction

While every sci-fi show depicts Voice Interfaces as the future as it seemingly makes for very simple interactions with devices, the promise seems to always have been right over the horizon.

But recent developments have shown promise. And no, I’m not talking about the clunky UX offered by the Siri’s or Alexas which attempt to offer a single interface  experience, but other technologies that integrate within apps to offer a multi-modal interface and there lies something that has the potential to be useful.

## BACKGROUND

Let us begin by understanding the role of voice interfaces. Voice interfaces are great:

- They are simple to use.
- Almost everyone can use them.
- They have the potential to combine multiple steps that a typical GUI interface needs to have.
- And with localisation, they have the power to reach many more millions of users who find the existing touch-based GUI interfaces difficult to understand and use.

But many kinds of interfaces have been built for machines in the past. You have everything right from switches and buttons to mice, pens and screen-based touch interfaces like those on your smartphones. Every time some new interface was created by someone, there has been a tendency to portray it as the killer interface that will replace all interfaces. But the fact is that switches, handles, knobs and pens all exist today.

The reason for this is simple — each interface offers some specific advantage over another. For example, a light switch is cheap, it is always physically available to users, it is very simple to operate and is perfect for the electrical wiring system that it is a part of. Whereas it’s a far more efficient use of space to include a touch-based screen than to include a screen and a physical keyboard.

Until brain-machine interfaces like the one that Neuralink is working on become mainstream, all other interfaces including voice-based ones can be only a part of a collection of interfaces that will be used by humans. They will therefore need to be integrated into existing user interfaces and not thought of as replacements for anything. So the principle of design needs to be that of coexistence, not of replacement.

DESIGN FOR CO-EXISTENCE, NOT REPLACEMENT 

Secondly, we are talking about integrating voice-based interfaces into existing applications here using technologies like DialogFlow or Slang and this is not the same as creating a skill for Google or Alexa that could potentially be linked to a website or an app.

## INTERFACE DESIGN CONSIDERATIONS

While designing interfaces for Voice UI, the following need to be considered:

- Indicate that the interface is voice-enabled — Since it’s best to use examples when discussing complex topics like this, we will use the interface of one of our clients, Lenskart. Lenskart, is an e-commerce store that sells prescription and non-prescription glasses through their website and their apps. For this video, we’ll focus on the mobile app. So as you’ll see from the interface, we’ve included an activation button that’s been styled to indicate that you can tap this to say something.
- Indicate to the user what is voice-enabled and the kinds of commands that can be issued — There are also similar-looking icons placed on other elements in the interface that indicate that these other elements too are voice-enabled.
- Let the user know that their privacy is protected — When one taps the activation button, it gets “enabled” and starts listening for instructions from the user. We chose not to go with activation keywords here because there’s a learning curve involved with that. You’ll also notice that there’s a line around the button that keeps reducing and when it goes down completely, the button gets disabled. This mechanism does two things — one, it allows the user to give continuous commands without activating the voice interface each time. Two, it tells the user that this interface isn’t always going to be listening and respects the user’s privacy. Finally, tapping the activation button again immediately stops the system from listening further.
- Provide confirmation and feedback for actions performed — Now when the user issues a command, something like “Show me sunglasses”, the application has been designed so it goes straight to the screen that shows the sunglasses.
- Provide ways to recover from a mistaken action — If the voice-processing engine isn’t very sure about the guess it’s made about having heard “Sunglasses”, we can indicate the same to the user and get clarity on the next screen if the user really meant to do that or not. This allows a user to recover from the error by simply clicking the “Undo” button or saying, “No, I meant sunglasses”.
- Provide a way for power users to understand how to harness the power of voice — Users may intuitively begin using the voice features in the app but in the initial period when people may not really know how this works, providing them with the ability to understand what’s possible may be required. What we did to enable this is to have an information icon placed to the right of the activation button. Tapping this will bring up a sheet with all the available types of commands that can be issued on the application. This sheet could also be presented when the user says things like “What can I say?” or “What can you do?” which are equivalent commands on Google Assistant or Siri.
- Design for voice-only workflows — Voice-only workflows are powerful new user journeys that come up when working with voice. You don’t need to work through screens sequentially anymore and in most cases, multiple steps can be combined. In this example, the user can ask to check out and the cart page will show up after which the user can choose the method of payment and the delivery address. However, with voice, these two steps can be combined using a simple command like, “Checkout using card number ending with 0399 and deliver it to my home”. Upon this command being issued, a user is brought to a confirmation page that shows the card chosen and the address chosen and all the user needs to do is hit “Proceed”.

THIS IS AN EXTREMELY POWERFUL NEW CAPABILITY THAT IS OFFERED THROUGH VOICE INTERFACES AND REQUIRES UX DESIGNERS TO THINK DIFFERENTLY WHEN DESIGNING. 

Eliel Saarinen, Architect

## ADDITIONAL THOUGHTS

So that’s a quick look at how to design for voice-based interfaces. One just needs to keep in mind to not take an all-or-nothing approach, but rather design for a mixed interface. Getting started is surprisingly simple, but employing voice interfaces and exploiting their full power are going to require quite a bit of thought.