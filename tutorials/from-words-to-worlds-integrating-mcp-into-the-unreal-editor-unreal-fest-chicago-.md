---
title: From Words to Worlds: Integrating MCP into the Unreal Editor | Unreal Fest Chicago 2026
source: YouTube
url: https://www.youtube.com/watch?v=lDf_y-YPELo
author: Unreal Engine
ingested: 2026-08-03
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/from-words-to-worlds-integrating-mcp-into-the-unreal-editor-unreal-fest-chicago-/
frame_count: 0
frame_status: pending-selection
---

# From Words to Worlds: Integrating MCP into the Unreal Editor | Unreal Fest Chicago 2026

**Source:** [YouTube](https://www.youtube.com/watch?v=lDf_y-YPELo)
**Author:** Unreal Engine
**Duration:** 36m40s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py from-words-to-worlds-integrating-mcp-into-the-unreal-editor-unreal-fest-chicago- <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Alright, hello everyone and welcome to From Words to Worlds. We really appreciate you being here today.
[0:09] I'm Nathan. I'm Jess. And I'm Quentin. And today we're going to talk to you about the work that our teams did to enable an MCP server in the Unreal Engine.
[0:21] And hopefully all of you are here because, you know, we announced yesterday that we've launched official MCP support in Unreal with the 5.8 release.
[0:29] It's open. It's free. And we're releasing not just a server, but support out of the box for two dozen different engine and editor systems.
[0:40] It's something just shy of a thousand different APIs that are all ready to go.
[0:45] And like we showed in the state of Unreal, you can do a lot with those tool sets out of the box, things like materials, blueprints, PCG, the works.
[0:55] And our goal today is going to be to dig down, go under the hood, talk about what we did to enable that, and then how you can extend the MCP for your own games and experiences.
[1:06] So before I do that, though, I want to talk a bit about the philosophy that we have. And we've tried to embody in building this technology, which is what we want out of an LLM, is that we believe it should be an assistant and not a magic bullet.
[1:19] This isn't just a statement of principle. It's a statement of like what we believe the technology is good at today.
[1:25] And so in order to make sure that we were following this vision, we had three principles that we thought about a lot during development.
[1:31] And the first was that we wanted to make sure that we were working with LLMs in a way that was directable, where the AI or the model is there to amplify your creative intent, not to replace it.
[1:42] The second principle is that everything should be editable, that AI, the LLM, it shouldn't get special access, special permissions, special formats, that everything that an LLM does should be inspectable by you while it's doing it.
[1:57] And the results of that work should be indistinguishable from anything any human did with the assets, so that when the model is done, you can edit it, change it, review it, etc.
[2:08] And then finally, we wanted to make sure that we weren't building like a closed system or a black box. Unreal has always been a tool that you can take and customize and extend.
[2:17] And we wanted to make sure that our MCP and LLM work embodied that. And there's a very, very clear path for customization by all of you.
[2:26] And then finally, we wanted to do all of this not in the context of like a cheap demo or a toy example, but a scenario that would be really challenging for a large language model, something like world building.
[2:38] And to tell you more about that, a welcome, J.S.
[2:42] Thank you.
[2:47] Thank you, Ninta.
[2:48] So I'd say roughly about a year ago, we wanted to explore all well-building with benefit from LLM's reasoning.
[2:56] And while staying true to our vision, I would end all something really complex like building a city procedurally.
[3:04] But we had a core challenge to deal with, spatial operations. As you may know, LLM's typically struggle with those. They're really, really good with words, but they're not naturally built for treat environment creation or low-level spatial operations.
[3:19] So how do we go from the text on the left to the city on the right?
[3:25] We felt like we had a solution, or at least a part of it. Unreal Engine excels at this, especially with its built-in procedural content generation framework or PCG.
[3:36] So the idea became really, really simple. We have a great tool for spatial world building, Unreal, and a powerful new tool for reasoning and automation, the LLM's. What if they became friends?
[3:49] To achieve this, we combined four key elements together. First, tool sets, followed by primitives, examples, and skills, or in short, documentation.
[3:59] Let's dig into each of those to better understand the foundation of our approach.
[4:06] You could think of an LLM as a brain in a jar. So the first prerequisite for any of this to work is to give the LLM the ability to interact with Unreal.
[4:17] And it happens to be that tool sets do exactly that. They are APIs for LLM's.
[4:23] In our case, we use and combine multiple. But the most important one for this particular challenge is the PCG tool set and its set of dedicated functions.
[4:33] Mainly, everything to do with creating, editing, reading, and executing graphs.
[4:41] Nathan will cover later in the talk how you two can extend the collection of tool sets that we provide.
[4:48] Now that the LLM is able to interact with Unreal, we need to give it the best context possible for it to succeed.
[4:56] It started with providing its vocabulary, which we call PCG primitives.
[5:01] It allows the LLM to build environments faster and more reliably without having to reason about every single step.
[5:09] PCG can be seen as a chain of functions to build worlds. But unlike Python, which LLM's are way more familiar with, PCG is much less represented in their training data.
[5:22] So they mainly rely on the documentation and what they can extrapolate from it, which is not great.
[5:30] So we went on and created a library of over 80 plug and play primitive spatial operations.
[5:36] It's a mini framework using PCG subgraphs on top of all the native operations available.
[5:42] Simply put, there's streamlined bite size functions that the LLM can string together as words to build environments in Unreal.
[5:51] And as you can see in this video, these functions are being added to the graph by asking it to create shapes, compose them, applying transforms, or simply sampling, filtering and spawning.
[6:04] These subgraphs are fully parameterized and documented. They don't need LLMs to work at all. But on the other hand, LLMs are much more capable with them.
[6:15] Keep those in mind because everything we'll show next is using these small operations combined together.
[6:24] Our next step was to build a lot of examples. These are complete PCG graph built out of the primitives,
[6:30] ranging from use case agnostic basics to concrete environments of different types.
[6:36] If the primitive functions were its vocabulary, then the example would be the simple sentences, paragraphs, chapters, and sometimes even entire books, as you can see here.
[6:48] The LLM can consult them at any point in time to build something similar or reproduce it.
[6:55] But it can also learn from useful patterns that you can apply in different situations.
[7:01] Since this is all data driven, you can extend the system quite easily by providing project specific primitives and examples.
[7:10] But you can also use the LLM to build them if you want, which we actually did once we had everything set up.
[7:17] The final essential component is skills. They contain the information that the LLM needs but doesn't have to succeed at a given task.
[7:26] But they also help generalizing beyond the examples. To stick with the language metaphor, skills are the principles of good storytelling.
[7:35] And these guidelines extend way beyond the PCG framework.
[7:39] We can create and combine skills for anything in the engine, including actor and asset manipulation, materials, lighting, Niagara, name it.
[7:51] With these four key elements, tool sets, primitives, examples, and skills, we're now ready to do world building.
[7:58] And that's what we're going to showcase.
[8:01] Let's look at a small scale example first for illustrative purpose.
[8:10] On the left here we have Unreal Engine, and on the right is a terminal. The key problems are summarized in the lower left corner.
[8:17] In this single session, we load the required tool sets and skills, then define the context. We want to furnish this modern apartment living room.
[8:26] The next step is to provide a description, such as its dimension and whereabouts in the level.
[8:33] Then we want to place props. First a sofa with a rug, then a wrong coffee table, which are all retrieved by the LM using semantic search.
[8:43] We keep adding more and more to the scene and adjusting as we go.
[8:47] At any point in time, you can add an asset manually to the level and refer to it in your session context.
[8:54] Spatial relationships are important even in such a small space.
[9:00] Now you'll have to expect to adjust things because it will definitely fail, especially with pivots, overlaps, and orientations.
[9:08] A standardized library with good information and instructions about transforms for your project will go a very long way.
[9:16] Once we have our basic layout, we can start using prompts that have a much larger impact.
[9:21] We use it here to give a story to the scene or try a complete rearrangement.
[9:25] At this scale, the gain is obviously not in the individual asset placement, but in those broader, more impactful changes for faster iteration.
[9:35] So now let's move to city scale where things truly start to shrink. Quentin.
[9:38] So from the very beginning, we wanted to change the new PCG system plus the LM reasoning we've connected to it with something ambitious and larger, something like an entire city.
[10:02] And if you remember, we had made a city in the past for the Matrix Awakened, and this city was a really hard one.
[10:10] It was a very complex system and it was generated outside of Unreal and overall was fairly rigid to set up and to interact with.
[10:20] And we figured that using this would be a perfect playground for the PCG primitive plus the example workflow that we've established.
[10:30] Now what we are going to show is how we managed to create this entire procedural generation of the city sample through PCG and prompting.
[10:41] This is its procedural story, prompt by prompt and through manual interaction in the viewport, we reshape the city layout.
[10:48] Starting with splines that define the city boundaries, the main roads that create districts, lots, roads and buildings through a chain of complex relationships and operations.
[11:00] And as you can see in the lower right on the PCG graph, the primitive we talked about earlier becomes the spatial vocabularies which the LM do the CRT building process.
[11:10] It will write, brick by brick, the logic of how we build a city.
[11:15] We are establishing the rules like the highway supersedes building footprints, all the terrain hills conforms to the road and highways, which building style should be used for this or that category of districts.
[11:31] And the same applies to the forest that will build itself around the city with its own PCG graph.
[11:39] A little later we asked to sparse, to scatter sparsely building districts to make the city skyline.
[11:49] And finally, the city rulebook is written.
[11:53] And the result is a fully parametric city entirely generated with PCG and prompts in Unreal Engine.
[12:01] This didn't take weeks like it used to, it took a day.
[12:05] This is not a black box, this is real data that you can open, inspect, edit, extend and that could be shipped in a game today.
[12:15] Built from a complex network of interdependent PCG graph, every part of the city can be adjusted, regenerated procedurally in a few minutes.
[12:26] You can ask to squabble an entire district to be a park, reserve block to be a parking.
[12:29] The LLM understands how the graph are organized and what needs to be updated.
[12:37] And looking a bit closer, we can demonstrate the procedural nature of the system.
[12:42] Here you can see the buildings rebuilding around the highway.
[12:47] Or you can ask for a specific building to be more prominent in the scene and the LLM will scan through the city and assess what this means.
[12:54] While the system makes the building still editable, it's not a locked-in actor.
[13:04] And this worked for an entire team.
[13:09] Here another artist, Jess, recreated Central Park in a separate session and we dropped it directly in the city.
[13:17] And because it's procedural, you can see that it reburns itself around it.
[13:21] And one convenient feature of using the LLM is that we can refer to real-world data.
[13:28] So for this park, we simply ask for the actual size and layout of Central Park and how to reproduce its key feature at the correct scale.
[13:39] And so as we progressed, we realized that we don't always need to create PCG graph for small operation.
[13:45] And we came up with what we call instance. It's a Fire and Forget function call.
[13:51] It's executing a premade PCG graph without leaving a trace in the layout.
[13:56] And that means that we can benefit from the entire framework without forcing the user into a graph.
[14:02] Again, this is all that had written. You can extend those as you want.
[14:07] And all the examples you see in the video are currently using the PCG primitives.
[14:13] So we create a spline using selected actors. In between the spline, we scatter assets.
[14:20] We shuffle everything. Then after a few manual operations, we can save everything as an assembly and spawn it back in the level as an optimized actor.
[14:29] And keep in mind that this is not using any PCG graph that will stay in the level. This is just called on the fly.
[14:37] So while the LNM can actually make a forest with the primitive and the example we've provided, we wanted to tackle something a bit more complex, which is Biomecore.
[14:49] And for those who have never heard of it, Biomecore is a powerful PCG data driven biome creation tool.
[14:56] It's highly complex and kind of requires pretty advanced knowledge.
[15:00] And here we created a skill to guide the LNM on how to use Biomecore.
[15:06] And so now it's aware of all the data structure and how to create it from the ground up.
[15:11] So it's a lot more convenient to use. It's like prompting to ask for it.
[15:17] That's a great example where the LNM can help you use a system that already exists and that has been proven to work.
[15:26] It's a valuable approach alongside what we've shown before.
[15:31] Another great example of a skill used was for the lighting.
[15:36] When we started to experiment with lighting and we asked the LNM to adjust the default lighting setup,
[15:44] we quickly realized that just based on the list of parameters and the documentation that he knows about, the LNM wasn't able to do too much of a good job.
[15:54] And also something else to think about is that he can modify parameters on the fly, but it doesn't actually have visual feedback, so he doesn't know if what he has done actually worked.
[16:04] So as we iterated on this, not only we provided feedback to what he's doing and we tried to capture all that feedback into a skill,
[16:13] but we also gave it the ability to take screenshots and iterate on it.
[16:18] So now with the skill, it knows the subtle detail of the default lighting setup of Unreal, which assets are composing it, how they work between each other.
[16:28] And we gave it some fundamental lighting skills, like starting from the ground up with the light position and the intensity, so he has the overall color and mood,
[16:38] the correlation between the direct and field lights, or something like not overcompensating everything in the post-process to try to desperately achieve a look.
[16:48] And I think most importantly, as I mentioned, is like now, he can take screenshots, so he will go on a cycle of changing parameters, taking a screenshot,
[16:59] and try to converge toward the look.
[17:03] And that's what we're going to see here.
[17:05] So let's say for example we ask for a purple dusk.
[17:07] Not only will we adjust the send position, which is kind of expected, but he will modify all the parameters at once and make it more compelling.
[17:13] He will touch the cloud, the sky tint, the post-process domain in values, everything together while taking screenshots.
[17:20] Now for the overcast, actually an interesting attempt where he actually got it wrong.
[17:25] He modified the cloud material in the wrong way, and then he was taking a screenshot and assessing that he was good, but he was actually, because he was fully blown white.
[17:33] But then, you know, you can chat your way back to correctness like you would do with any chatbot, because at the end, it's conversation.
[17:40] As I mentioned before, like for Central Park, you can refer to real-world place.
[17:46] So he finds the information that matches that, kind of like color temperature, climate, and coordinates.
[17:54] And because we can provide images, now we can also ask it to hit a precise visual target, and it will cycle through the screenshot and parameters to try to, you know, converge and achieve that look.
[18:06] So from all of those experimentation, exploration, we have a few insights that we would like to share.
[18:15] We are quite happy how PCG fit naturally to be the spatial language for the LLM, and that works out pretty well.
[18:24] But something that we realize is that the technical artist is the key, and that's something that should not be underestimated.
[18:32] This takes a lot of time and experience to use it to its full potential, and that's not going to be a one prompt that's going to give you a result.
[18:42] You need to know what you're doing, and you need to use it to assist you.
[18:47] Looking at what we've done, and the exploration we've done, is a good place to start, because we've already ironed out the initial kinks of this system.
[18:57] You should know that all the primitives and examples can be used with or without the LLM. It's not a closed system.
[19:06] And what the LLM helps you create with PCG doesn't have to be used with LLM.
[19:12] It will always produce deterministic results, because this is PCG.
[19:16] And I think most importantly, you can extend it to your proper use cases, and that's exactly what we are going to cover next with Nathan.
[19:26] Nathan, please show them how it's done.
[19:33] Cool. So our final section is on how you can extend the Unreal MCP in a way that's particular for your gamer experience.
[19:43] As a little bit of context, the big picture is that we've talked about the MCP server, which is the bridge or the gateway between you and your agent and the world of Unreal.
[19:54] JS and Quinten just talked about many of the things that we've done inside the existing engine systems and what we've learned along the way.
[20:02] And now I'm going to talk about how you can take some of these principles and technologies and extend them yourself.
[20:07] We're going to talk about three types of extension, tool sets, skills and examples, and we'll start with tool sets.
[20:16] So in case you've forgotten 15 minutes ago, tool sets, what are they?
[20:21] They are really APIs for LLMs.
[20:24] And why APIs? It's really about efficiency.
[20:27] If you want to have an LLM interact with an application, doing it programmatically is much more token efficient and lower latency,
[20:35] then trying to move the mouse and click around.
[20:38] And there's just one problem, which is that one of the LLMs stands for language, and so LLMs and the MCP standard speak JSON.
[20:48] But as game developers, we work with Blueprints, C++, Python, and we don't really want to worry about JSON conversion and the standards behind it.
[20:58] And this is particularly important because we're going to expose entire domains, not just one or two functions, but the PCG tool set.
[21:07] You can see there are many functions, there are many domains in Unreal, so we're going to add a lot of tools.
[21:13] And our team, one of our goals was to make it as easy as possible to add new domains and add new tools without worrying about tons of boilerplate logic.
[21:22] So the way we've tackled that is leveraging Unreal's reflection system.
[21:27] And Unreal, going back a long time, has had a great reflection system with UStruct and FProperty and all of that.
[21:34] And we're going to leverage that to automatically create the JSON that we need.
[21:38] And for MCP, we actually need two flavors of JSON. One is called JSON schema and the other is called JSON data.
[21:45] And if you're not familiar with this, JSON schema is basically the type definition.
[21:50] So if you say, I have a function and that function has an argument and that argument is an integer, well, the schema is what tells you things like,
[21:57] the name and type of that argument. But then, of course, whenever you invoke a function or set a property, you need its value and that's JSON data.
[22:07] And these two things go together and you need both of them working to have an MCP integration.
[22:13] The thing is like, integer looks pretty simple, but of course, in Unreal, we need to think about supporting enums and then there's also structs, maybe more than a few structs.
[22:22] And ultimately, we have to support like all of the things, all the types, including, you know, pointer-like types like UObject and UClass.
[22:31] And then they can be nested, so you have containers of arrays of structs, so it goes on and on.
[22:37] But we've done that work for you. The 5.8 has very, very robust JSON schema and JSON data conversion.
[22:45] So hopefully this is a detail that you'll think about now and never again, maybe. I hope.
[22:50] So with that, it makes it really, really easy for you to build APIs where that conversion is handled automatically.
[22:59] And so in 5.8, if you want to make a new tool set, it's very simple, you just derive from UToolSet definition.
[23:06] And then when you want to add tools to that, they're just static U functions, just like anything else you would write in Unreal.
[23:14] Same types, same signatures, same metadata, same tool tips.
[23:17] Excuse me, because of that, everything is fully type safe.
[23:22] And you don't really need to learn anything new, you just write your tools exactly the way you would write an API for anyone else in your game.
[23:29] Also, because we're leveraging Unreal's reflection, all of this stuff works in Python as well.
[23:35] I actually started my career as a technical artist. I love Python, it's a great language.
[23:39] And we wanted to make sure that exposing editor features wasn't something that only engine programmers could do,
[23:47] but technical artists, technical designers, software test engineers could all do that in C++ or in Python.
[23:55] And because of that, basically your signature is the schema, and we can automatically take that C++ or that Python,
[24:03] we'll create the JSON schema for you, handle the JSON data bindings.
[24:08] We'll also pick up things like metadata, so tool tips become documentation, MINS and maxes, all of that stuff is automatically bundled up for you.
[24:17] And so basically what happens is that when the LLM now wants to invoke one of your tools,
[24:22] it will send some JSON data over the wire and something like, oh, this is the name of the function I want to invoke,
[24:27] and this is the JSON data of the arguments into that function.
[24:32] We convert that transparently, and then we call your function.
[24:36] And to you, it just looks like your code ran, the parameters are called in, the you function is invoked,
[24:43] and then when you're done, you return whatever you want, just like you normally would in Unreal.
[24:48] And we convert that from the Unreal types to JSON data and send that back over the wire.
[24:54] Super simple, really, really fun to work with.
[24:57] There's a couple other things that we've considered that are worth thinking about.
[25:01] Very often LLMs, you'll ask it to do something and then it invokes a long running operation.
[25:06] And ideally, you don't want to block the editor for seconds, minutes, anything like that.
[25:11] You want to be able to happen in the background.
[25:13] So we've actually built the tool set internals are all inherently asynchronous,
[25:19] but you functions are not right, you functions are just fire and forget.
[25:22] So we've built a little bridge, which is a class that's designed for returning asynchronous results.
[25:29] The base class is called you tool call async result.
[25:33] There's a bunch of the subclasses for different types, like if you want to return a string,
[25:38] asynchronously or an image, those are all built in, you can extend it with your own types, super easy.
[25:44] And then you can make your own asynchronous functions that kind of do whatever they want,
[25:47] use whatever async framework is best for your game and then return that result over the wire through the tool call async result.
[25:57] So in doing all of these, you know, couple of dozen tool sets, we've learned a few things, sometimes painfully,
[26:04] and we want to share some high level learnings and best practices with you.
[26:08] So one of the first things when you're building a tool set is you want to like make the API clean,
[26:12] take the time to give functions and arguments, you know, good names, right, tool tips, think a bit about the types, right,
[26:21] you want to design your API kind of like you're designing it for like a junior programmer, you know, somebody who's really smart,
[26:27] but maybe isn't an expert in your domain.
[26:30] And so kind of clarity of API design really helps that junior programmer, which is roughly what LLMs are in this domain today.
[26:37] You want your APIs to be complete. And so you want to do kind of a crud type approach where, you know, if there's a setter, there should be a getter,
[26:46] but often there might also be a list function.
[26:49] If you look at a lot of cases, we say, oh, well, I as a human, I know what the properties are, but the LM doesn't.
[26:55] And so you want, you know, not just get property and set property, but list properties so that the LM even knows what it could get or what it could set.
[27:03] Composability is really, really important.
[27:06] LLMs have a lot of knowledge. They're really, really good at kind of putting building blocks together.
[27:11] So you want to build your APIs, not to be kind of like monolithic or on rails, but to be modular and flexible.
[27:17] So the LLM can say, okay, you gave me this job, I'll put the APIs together in this way, oh, a different job, different APIs.
[27:24] And so using kind of like types that are combinable, clear, makes for composable and usable APIs.
[27:31] And finally, you really want to be in a sense communicative.
[27:34] Modern LLMs are really trained to be good problem solvers, but that's predicated on feedback.
[27:41] And obviously your APIs can include positive feedback like, oh, it's succeeded or it failed or here's the actors that were selected.
[27:48] But very often LLMs will make mistakes.
[27:51] They'll invoke tools with invalid arguments, a system won't be available.
[27:56] And you want to not silently fail, but actually return a useful error that tells the LLM like what went wrong and why and maybe even how it might fix something.
[28:04] And it makes itself.
[28:06] And we actually have a standard error path in tool sets where in Python and in C++ you can return informative errors and they'll automatically get sent over.
[28:15] And because that way you don't have to say, well, let's make sure the LLM never makes a mistake.
[28:19] Like it's going to make a mistake, but you can make sure that it's able to fix the mistakes when they happen.
[28:24] So the second thing we want to talk about our skills.
[28:27] As JS mentioned, skills are really distilled information that the LLM needs, but doesn't have.
[28:35] You know, the LLM has kind of like a fuzzy recollection, right, of all of the text on the internet.
[28:39] It's got whatever is in the context window.
[28:42] But I really liked Quintin's example of the lighting skill, where like in Unreal when you're doing lighting, you really want to set the sun before the sky, right?
[28:51] And that's a kind of important gotcha that the LLM may not get right much of the time may not know.
[28:59] That's kind of like technical artist knowledge, but when you write it down in a skill, it allows the LLM to perform that task more reliably.
[29:06] So we've added a native kind of skill to Unreal.
[29:10] It's this new class called you agent skill, and it's based on an open standard called agent skills.
[29:16] If you've ever worked with like Claude code, the skill definition is the same one.
[29:22] And we've basically just taken the same semantics and spirit and tried to make it Unreal native.
[29:27] So because this is a new class, making a new skill is just a matter of deriving from you agent skill.
[29:34] You can do that in C++, Python or in blueprints.
[29:38] And the blueprints part is kind of neat because it becomes a you asset.
[29:41] And so if you want to say like have a skill and check it in and share it with other people on your project, you just add it to your project like anything else and check it in like anything else.
[29:51] And now it's shareable.
[29:53] One of the other cool things though is you can see the base of a skill is just like a big bucket of text.
[29:59] And that's great.
[30:01] But because we're in the world of you know, you objects, we actually allow for programmatic skill text construction.
[30:06] So if you want, there's a function that you can override that whenever we read the skill text out, we invoke the function.
[30:14] And that way you can modify, edit, append to your skill basically programmatically getting some extra context, you know, out of your project before the LMC is the final skill text.
[30:25] So again, best practices, things that we found work best.
[30:29] The first is that you really want to focus on skills that are novel that are adding information that the LM can't get anywhere else.
[30:36] So if a tool already returns that info, don't put it in the skill.
[30:42] If it's a million times over on the internet, don't put it in a skill.
[30:46] Focus on the things that are proprietary novel surprising, right?
[30:50] Secondly, you want your information, your skill to be written in a kind of collegial form.
[30:56] Often when people encounter skills for the first time, they think of it as like, I'm going to script the LLM and be very didactic and pedagogical and write a lot of text and this do this and not that.
[31:06] But LLMs again, they're pretty smart and tokens are precious.
[31:10] So you want to actually write them like, it doesn't need to be that elaborate, like the same way you would talk to a colleague, hey, when you're lighting the sun, or when you're doing outdoor lighting, set the sun before the sky, and then maybe look at the clouds, right?
[31:23] Literally, that's the kind of text that works well in skills.
[31:27] You want skills to be durable.
[31:30] And so another gotcha is that you want to be careful about embedding things like names of properties or names of functions that could easily change out from underneath the skill.
[31:40] And because skills are at the end of the day, pure text, it's hard to programmatically verify things like, oh, I renamed this property, but I didn't update the skill.
[31:48] And now the skill is kind of a lie.
[31:50] So again, and being novel and collegial actually helps you avoid writing things that are that specific.
[31:58] And then finally, you want to be parsimonious, right?
[32:02] Context is precious.
[32:04] Every token counts.
[32:06] So take the time to like write a shorter letter and really focus on those previous best practices, which will result in like just the information you need and no more.
[32:15] Finally, I want to talk briefly about examples.
[32:17] We had lots of good demonstration of that earlier.
[32:20] So the thing I'll touch on here is how do you find examples or how do you help the LLM find them?
[32:25] And there's two models we've seen work well.
[32:27] One of what we call static examples.
[32:29] And these are like templates where you decide up front, hey, for effects, you know, maybe it's like an explosion, maybe it's like a spell, maybe it's like a tracer.
[32:38] And you decide, great, there's, you know, these are my effects.
[32:41] These are my templates.
[32:42] Go for it.
[32:43] That works well in some domains.
[32:44] But there are other domains that like say gameplay programming where the best example for a weapon might be different than a power up and might be different than an NPC, even though they're kind of all blueprints.
[32:56] And so you, in those cases, dynamic examples work really well, where essentially you want to make sure that your tool set is able to, you know, inspect and read your assets.
[33:06] And then the skill will tell the LLM, hey, actually, you know, if you're doing this, go find an example and read it.
[33:11] And maybe here's the rules for what good examples look like or where you might find them.
[33:16] Again, it's the way you would talk to a new colleague.
[33:18] And the dynamic example discovery helps the LLM work in more complex and kind of fungible domains.
[33:25] So hopefully that gave you an understanding of how we extend tool sets, skills and examples.
[33:31] And to bring us home, we're going to head back to JS.
[33:33] All right. In conclusion, let's wrap this up.
[33:44] Here are some of our key takeaways.
[33:47] The LLM and tech inside Unreal, such as PCG, can be used in ways that are really complementary.
[33:54] They can truly be friends after all.
[33:57] We're already seeing benefits in our own internal productions.
[34:01] But this is still experimental.
[34:04] Interaction, reliability, speed, cost, there's a lot of work still to go.
[34:10] And you can follow the work on GitHub.
[34:14] It's quite self-contained, so you can expect to be able to integrate in your projects or cherry pick, whatever you want.
[34:21] We also generally like to think that if it's useful for users, it will be for LLMs and vice versa.
[34:30] With or without using LLMs in the end, features get developed and improved for all use cases.
[34:39] As an example, for 5.8 in this well-building exploration context, we worked on the primitive library, manual exits, performance and stability across the board.
[34:52] So these are all crucial for all Unreal Engine users and PCG users.
[34:56] If your recall or vision was to build an extensible system that was directable and that would produce editable output, just like everything else in Unreal.
[35:09] And we're exactly here today.
[35:11] The LLM assists you, but true art skills are required to make the most out of it.
[35:17] But once you do, you can start iterating faster.
[35:22] This is what is actually available for you.
[35:24] The MCP server tool sets and skills that we've talked about, including example implementation of the Semantic search, the PCG Primitives plugin with all of its spatial operations, examples and the Instant Fire and Fragget function calls.
[35:40] On Unreal Engine skills for Cloud Code plugin, and we're planning on releasing the CD-SAMPLE PCG plugin as a later this year.
[35:49] We're targeting end of summer.
[35:52] So you can load and explore everything.
[35:54] It might contain a few more primitives in that exact CD that we've showed today.
[36:00] To get going, you can use and scan this QR code.
[36:04] It should get you to the official documentation where there's more detailed guidelines.
[36:08] But you can also search for MCP in Unreal Editor on our official box page.
[36:14] But before we open the discussion in this Q&A session, I would like to say a very big thank you to everyone who's working on this with us.
[36:22] And thank you for coming to this talk.



---

## Structured Notes

### Core Technique
[PENDING EXTRACTION]

### Summary
[PENDING EXTRACTION]

### Key Steps
[PENDING EXTRACTION]

### UE Systems / Blueprints / Settings
[PENDING EXTRACTION]

### Difficulty
[PENDING EXTRACTION]

### UE Version
[PENDING EXTRACTION]

### Tags
[PENDING EXTRACTION]

---

## Related Entries
[PENDING EXTRACTION]
