---

title: "Seven Structural Elements to Keep in Mind for Web3 UX Design"
audio: "c763e555_audio.mp3"
subtitle: "The structure of web3 influences the design of the applications"
date: "12 Feb 2023"
author: "sharanx"
tags: ["ux","web3","decentralisation","design"]
image: "seven-structural-web3.png"

---

# Introduction

Web3 is a decentralised internet powered by cryptography and blockchain technology that allows for transacting with any entity in the world without the need for trusted middle men. It has specific uses in fields where having a trusted third-party middleman may prove to be corruptible, inefficient or expensive. But far too often UX designers are starting from equivalents in Web2 creating poor user experiences.

# Unique Elements

There are several effects that the difference between these two structures affect the UX of applications built on top and the following are some main differences that UX designers must account for while designing Web3 applications:

## 1.  DECENTRALISATION IS SLOW AND EXPENSIVE

Since nodes in Web3 are distributed and are of different technical capabilities, data transmission across the network takes a lot of time compared to centralised systems. These processes can cause delays on the application layer, making them slow and expensive. In order to combat this, transactions are bunched up together before being written to the blockchain as a single write operation if far less expensive than several transactions writing the same amount of data.

It’s therefore essential for a UX designer designing applications to decide which data needs to be written to the blockchain and also when in a user’s sessions that needs to happen. For instance, in building a decentralised version of Instagram, would you record every “like” of the user as they occur, or collect all of them and commit them only at the end of the user’s session?

Many applications also adopt a Web2.5 design approach, where less critical interactions such as “likes” are stored on a centralised server for faster processing, while more critical data, such as who posted which picture, is written to the blockchain.

But there may other approaches that suit your applications and the right solution would entirely depend on the specifics.

## 2. THE BLOCKCHAIN HAS THE DATA

One of the most surprising ideas to me was that in the Web2 world, an application typically includes both a front-end and a back-end/storage layer delivered as an app. However, with data and storage openly available on a blockchain, the user interface and user experience is the application. This means that someone else could write a new UX layer for the same data, and the user could choose which application interface they prefer, losing nothing when switching between apps.

So, what’s the knock-on effect of this? It makes the UX layer super competitive, and the quality of experiences will only improve going forward. The app no longer stands for how well it manages to hoard and guard user data, but rather how good the experience is.

## 3. IT’S COMMUNITY OWNED

Unlike products and services in Web2 that are owned by corporations driven by the interests of investors and shareholders, Web3 has “projects” and “protocols” that are owned by communities, not individuals, due to the philosophy of decentralisation.

While there are participants attempting to amass wealth rather than distribute it to the community, more and more projects are evaluated on their decentralisation and ownership distribution. This impacts how things are designed because in traditional Web2 UX design, a good designer tries to balance the user’s needs against the needs of the company. However, in Web3, the success of the project is aligned with its users, as they hold the tokens and assign them their value.

With data no longer locked into an app residing in a database, it brings honesty to the equation. Apps that prioritise user interests will win in the future. App that use dark UX patterns to deceive users will not be successful in Web3.

## 4. NO COMMUNICATION CHANNELS EXIST, YET

In Web3, there is a lack of email or chat communication tools for peer-to-peer communication, and there is no de-facto protocol that can be assumed to be universally subscribed to such as email in Web2. Although tools like Push protocol and EthMail exist, they are not yet widely used and cannot be relied on for communication. This means that if someone buys something from your Web3 marketplace, there is currently no way to follow up with them to update them on the status of their purchase or to fix any issues, and they must come back and check with you.

Asking for their email address is not always an option, as it could compromise their pseudonymity, allowing you to connect their email address to their wallet and potentially uncover all their blockchain activities. Therefore, it is important to design around this depending on the context.

What I did on one project where a certain process would take upwards of a few days to complete was to allow the user to download a calendar appointment that stated when they needed to come back and check on the status of this process. You just need to be innovative about how to solve these kinds of problems.

## 5. THE WALLET IS EVERYTHING

In Web3, everything is based on cryptography using the concept of a pair of public and private keys. This provides users with pseudonymity, but not anonymity, in an otherwise transparent and open world. These keys are essential not only for authorising payments but also for verifying wallet ownership, interacting with smart contracts and linking all purchases to the wallet. Essentially, everything is connected to the wallet.

However, this user-facing aspect of Web3 is largely unfamiliar to most people. Although it is vitally important to understand, most people do not know what these keys are. Losing or exposing the private key can result in the loss of all assets tied to it. Therefore, this area requires considerable design intervention to help people understand the significance of the keys, the right way to generate key pairs and the proper ways to store and protect them.

Then comes the usage of the wallet itself. It is used to sign messages from applications to authenticate yourself and also authorise transactions being made on your behalf. But these messages keep popping up with messages asking you permission for something reminding me of the early days of Windows 10 where the user kept getting asked to authorise even the most banal tasks. A lot more polish is required to only seek the user’s attention when you absolutely need it.

The technology is still so new that sometimes the messages from the underlying stack are exposed to the user, and they are presented with only hexadecimal code, asking them to sign the transactions. Wallet developers have a lot of work to do to make this a lot more user-friendly.

## 6. SMART CONTRACTS RULE

This is another concept in Web3 that has no equivalent in Web2. Smart Contracts are computer essentially programs that run on a network that was created to enforce an agreement between two parties. This means that two parties can rely on a transaction completing as agreed without the need for third-party guarantors and any associated expenses or delays, making transactions more efficient.

However, since Smart Contracts are written in code and they can be difficult for people to understand. Although the code behind these contracts can be viewed on blockchain explorers, more work needs to be done to make them accessible to the mainstream. When this happens, it will revolutionise everything!

## 7. CENSORSHIP IS DONE DIFFERENTLY

In Web2, platforms that are owned by individuals or a small group have another problem in that they are also held responsible for implementing the censorship on them. In theory this sounds okay and the obvious thing to do, but if you explore this question more closely, there are many problems with this supposition:

- They may very well be ill-suited to doing the job and may end up censoring things that shouldn’t have been censored excluding ideas that shouldn’t be excluded.
- They have no option but to impose their world views on their systems and if they have a very large world-wide user-base, they will essentially be imposing their views on all of them superseding what’s culturally right.
- Because they’re a central authority that can make these changes, they may be pressured by external individuals or groups to impose censorship that they themselves may not agree with.
- There is always the question of “But what about the children?” that sneaks into every conversation about censorship and since there’s no argument against that, the lowest common denominator is set as the bar.

The political leanings of a platform have been the reason for new ones to be setup creating silos and echo chambers that only confirm your already held beliefs without public discourse or the meeting of minds in the middle. This technology has the potential to fracture societies instead of bringing them together.

Web3 has a different architecture that does not have central authorities that can censor others, making it a haven for free speech absolutists. Adults who believe they should be exposed to all kinds of ideas to progress in life can do so without censorship. For individuals who want a certain level of censorship, they can choose to use a filter and block certain types of content. This step allows individuals to make their own choices without resorting to drastic measures of stifling someone’s voice or de-platforming them. Although it is not a whole solution, it is a step in the right direction. A lot of work has to be done in this field in terms of making this UX better.

# Conclusion

A decentralised internet can solve a lot of the issues that plague the world right now and give rise to new ways of interacting with others around the world. For this to become a reality, it needs mass adoption and the only thing stopping it is the complexity. User Experience designers can make a huge difference to adoption by making things much simpler for the everyday user. So if you’re a designer on this journey, kudos to you, you’re making a huge difference to the world.

However, things need to be evaluated from the ground up based on the underlying decentralised architecture in order to deliver superlative experiences that are either at par or even better than the Web2 versions as this is indeed possible.