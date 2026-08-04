---
title: When Mascots Go Live: Converting the GEICO Gecko to Real-Time | Unreal Fest Chicago 2026
source: YouTube
url: https://www.youtube.com/watch?v=HljRmGJfSyk
author: Unreal Engine
ingested: 2026-08-04
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/when-mascots-go-live-converting-the-geico-gecko-to-real-time-unreal-fest-chicago/
frame_count: 0
frame_status: pending-selection
---

# When Mascots Go Live: Converting the GEICO Gecko to Real-Time | Unreal Fest Chicago 2026

**Source:** [YouTube](https://www.youtube.com/watch?v=HljRmGJfSyk)
**Author:** Unreal Engine
**Duration:** 23m25s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py when-mascots-go-live-converting-the-geico-gecko-to-real-time-unreal-fest-chicago <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Hello everyone, welcome to When Masked Go Live,
[0:05] Converting the Geico Geco into Real Time.
[0:08] So today I'm going to quickly introduce myself and Frame Store.
[0:12] Then we're going to talk about the Geico Geco,
[0:15] some of the initial challenges we had in this project.
[0:18] I'll go into detail of our Real Time system, some final thoughts, and what's coming next.
[0:25] So first of all, hello, I'm Camilla, I'm a Senior Technic Animator.
[0:29] I'm also Cora and Pipaka's mom.
[0:32] And I'm based in London, but as you can tell, I'm not British.
[0:36] I'm actually Brazilian and I started my career in Marketing.
[0:40] I worked over 10 years in Marketing until I decided to follow my passion and go shift to 3D animation.
[0:48] So that's when I packed my bags and moved to the UK to do a master in 3D animation.
[0:54] Some of you might recognize this character, the Seagull Rig,
[0:57] he's been going on for 80 years now as a free rig and lots of people have used him.
[1:04] So after I graduated, I got my first job at Ninja Theory,
[1:07] and I had the pleasure to work at Hellblade II and we also shipped Bleeding Edge at the time.
[1:13] And it was a Ninja that I found out about Unreal and I learned everything about it.
[1:17] And I fell in love with it, I really enjoy Unreal too now.
[1:21] And I like it so much that I started posting some content on my YouTube channel
[1:27] and then I also released a Contrary course.
[1:32] And that basically I decided it was time to step out of the game industry
[1:38] and that led me to Framestore because I didn't want to leave Unreal behind.
[1:43] And at Framestore we have an immersive department, which I'm going to talk a bit further,
[1:48] but Framestore for those who don't know is a VFX studio, is 40 years old, is Oscar winning,
[1:55] and we work with film, episodic, advertising and immersive, which is the area I'm in now.
[2:01] So immersive we say that our mission is to make screens invisible
[2:05] and to bring the digital magic into the physical world.
[2:08] We do that through park rides, VR experiences, live experiences,
[2:14] and that brings me to the Geico Geico.
[2:18] Oh hello there Camilo and hello Chicago.
[2:20] Thank you for having me in your city.
[2:22] Really chuffs my scales to be here at Unreal Fist.
[2:25] I feel very grateful.
[2:27] I usually spend those to my time talking about how people can save money on their car insurance by switching to Geico.
[2:32] But now I get to be here together with all of you and hear our Camilo and Framestore save me a lot of personal time.
[2:37] Yeah, so basically the Geico Geico.
[2:40] He's 20 years old relationship between Framestore, Geico and the marketing agency.
[2:47] Basically Geico is as recognized as Mickey Mouse according to proper research.
[2:52] Here in the US he is very famous.
[2:55] And as you can see by these social media comments, he is very, people are like in love with him
[3:00] and they love him as a mascot and as a character.
[3:05] So how do we go about bringing this TV advertising icon into the real world?
[3:11] Basically we need to make sure that we keep what makes him him.
[3:15] And that means that he has a lot of personalities, not just a generic character that we bring into Unreal.
[3:21] Basically we need to keep key features of him.
[3:25] Things like for example the eyes and all his facial expressions that is very important for this character.
[3:31] The eyes take over most of his face so we need to make sure we hit those key poses on it.
[3:37] Another thing is his voice is very unique and the British accent is very unique.
[3:42] So we need to make sure we keep that.
[3:45] And also when we bring him into the real world, I mean in real, we need to make sure the background and the world around him looks photo realistic.
[3:55] So we started this project in early 2023.
[3:59] And at that time we were already noticing a trend into the clients that was to create faster content, especially for social media.
[4:07] So just as a comparison here for a CG broadcast in our normal TV commercial, it's 30 seconds and we take 4 to 5 weeks to produce it.
[4:17] Of course you get a really high fidelity animation and you know have more creative control.
[4:23] But with the real-time versions we can create 10 to 15 seconds content in just 3 to 5 days.
[4:29] And that's actually counting for client feedback and back and forth like modifications.
[4:35] The real-time version also allows us to create live performances.
[4:40] It also gives us a quick turnaround and if an idea pops up we can just quickly create something.
[4:48] And we also have the, we created a tool that I'm going to explain a bit further, but you basically have the ability to puppeteer the gecko, even though you're not a technical person.
[4:59] So we gave that tool to the clients and they could execute that.
[5:04] So before I start, just a big shout out to the team.
[5:07] I was just one person amongst many great artists on it.
[5:11] We have lots of developers in this project as well and it was just a small team compared to a normal CG.
[5:20] And yeah, let's go into the details now.
[5:23] So I grouped these into the 7 initial challenges.
[5:27] So working from VFX studio, changing a VFX pipeline are very slow, like very slow.
[5:35] There is a reason for it because there is a legacy of years of experience and everything is very stable, reliable, but rigid.
[5:43] And that means that, you know, the beginning of this project we couldn't even publish a clean FBX from my scene.
[5:51] So we had to go through pipeline meetings and conversations and development to just have that base working at Framestore.
[5:59] So the second point is more the rigging side.
[6:03] So basically we had a root bone, but it was based on the middle of the character.
[6:10] And then of course we need a root bone that is in the center of the world.
[6:14] So we then created that.
[6:15] But again, as I said, the pipeline is very rigid.
[6:18] So just creating a new bone that is basically a new parent for everything else.
[6:24] It was a big discussion and a big change in the pipeline.
[6:27] We also had meetings about how do we call this bone because we can't rename the root bone because it will break the whole legacy of animations.
[6:35] So then we had the discussion of like how do we call it?
[6:38] And then we end up calling global joint.
[6:42] Another thing about the rigging is that we had a very complex hierarchy in the Maya original Maya rig.
[6:48] So he had different roots.
[6:50] He had a lot of joints for the rib cage.
[6:52] He had like a double knee deformation, double elbows deformation.
[6:57] And we had to convert that into just one single clear hierarchy.
[7:01] The way we do now is that we keep the complex rig in the Maya and then we also have what we call the engine rig in the same scene.
[7:11] And then the engine rig is just like parented constraint from the complex rig.
[7:16] And then when we publish the FBX, the FBX only considered the engine rig.
[7:23] So another thing was the facial rig.
[7:26] Originally he had hundreds of blend shapes.
[7:28] Again, that's how VFX normally works.
[7:30] And we had to go through it and just recreate a joint based facial rig.
[7:36] We do have some corrective blend shapes on top to make sure you will hit like those specific poses, especially for this character.
[7:43] But this was a really good exercise internally.
[7:47] This joint based rig actually we then started using even for commercials for other projects.
[7:53] So it was a good exercise that it started with GECO but actually then carried out to other projects.
[8:00] So number five, it was scale.
[8:03] So VFX works in decimeters.
[8:06] That means that we had to bring GECO to Unreal and scale him up 10 times.
[8:13] Again, because we didn't want to change the original rig and then mess up with the animations, we decided to do the scale in import time in Unreal.
[8:22] But I will talk a bit further on that that brought some issues to us.
[8:28] Sixth was about eye lighting.
[8:31] We got very specific comments on how the eyeball specifically should be lit.
[8:37] And because it was hard and it was tricky to work around with the rest of the character, we just decided to split the mesh and just have the eyeball separated as a static mesh.
[8:48] And then we just combined in the blueprint.
[8:54] So last point was about material color and intensity.
[8:59] Again, we got very specific comments about how the colors should work in this character.
[9:04] And it was based on different parts of the body.
[9:07] So for example, the hearts that he has in the back that had to be a very specific orange tone.
[9:13] We also got comments about his lips, comments about the spacing between the scales.
[9:19] So what our tech art Veronica did is that she just exposed all those parameters in the master materials based on the masks.
[9:27] So we could just fine tweak each individual part and then make sure that we will look as good as the CG version.
[9:38] So then coming to our real time system is basically a bunch of layers and things added into an animation blueprint.
[9:46] And I'm going to go over each of them.
[9:48] Essentially, we have inputs which are an audio for the voice that would then generate a lip sync animation.
[9:56] And the other input for the body can be mock up or can be the web app, which is the app that we developed for the clients to use.
[10:04] On top of that, we have layered animations, which I'm going to go through details later.
[10:11] And then when we combine all of these, we get an output, which is the final render.
[10:17] So for the lip sync, initially, we just did a quick prototype using Live Link Face.
[10:23] It's very easy to set that up.
[10:25] You just need the 52 poses.
[10:27] You connect with the camera and then you have a character animated.
[10:32] But as I said, this character has very specific pose and features.
[10:36] And you can see from the zeros that this wasn't holding really well.
[10:41] But if you need to do a quick prototype, that's a good solution.
[10:45] But for us, also, we needed to have an option to input the audio.
[10:50] And that means that if we went with this solution, you would have to have someone kind of mimicking the audio so we would match with the sound.
[10:58] So then we just decided to go with the Nvidia Audio2Face solution.
[11:02] Recently, we are testing FaceWare for that.
[11:06] But essentially, you just import an MP3 file and then it will output the 52 curves into Unreal.
[11:14] And then what we've done is that we could fine-tune the curves in Unreal.
[11:19] So for example, this character never really moves the jaw forward.
[11:23] So then we kill that curve in Unreal.
[11:25] And other ones, we intensify it.
[11:28] So for example, jaw open, I think is one that we put like 1.5 intensity.
[11:33] And then we could just play with the audio and see how that was working.
[11:37] So hopefully the audio will play in this one.
[11:41] Nah, you're thinking of the caveman, mate.
[11:43] Nah, I bundled my boat car and home with Gogo.
[11:46] Well, unless you mean my bundled theme barbecue this weekend.
[11:49] There'll be plenty of beef and bundling there.
[11:52] Yeah, so this was like one of the early tests and it was already holding really well.
[11:58] So the other thing I mentioned was about the layered animation.
[12:01] So it's very important in this type of projects that we don't think only when the character is talking.
[12:06] It's important that he looks alive when he's not talking, when he's just standing there,
[12:11] especially if you're doing a live activation and things like that.
[12:15] So in the video, I just cropped apart that he's not talking, for example.
[12:19] And you can see that he's just looking around, but he looks alive.
[12:23] And the way to do this is just, again, layering a lot of animations of eye, points of interest, emotions and breathing.
[12:31] And then the hands we actually use based on the audio.
[12:37] So for the procedural eye movement, our lead developer Claude,
[12:41] he really went into deep research about it and a proper scientific understanding of how do the eyes work?
[12:49] How does it work? Like when you move your head around, how long does it take for the eye to stabilize the saccades movement and everything?
[12:58] And then he applied all the knowledge into a humanoid character so we could get a better sense of if it was working for us feeling real or not.
[13:08] And then we applied into Gekko. As I said, his eyes are very important.
[13:12] So this was the first thing that we'd done and we knew that we had to nail that part really well.
[13:17] And yeah, it just looks great. As soon as we applied to him, it looks like he's alive already.
[13:25] So the topic was points of interest. Of course, you can't have the character just looking that straight on.
[13:32] He needs to be looking at something. So we came up with two solutions for that.
[13:37] The left one is basically we scattered different points of interest in the scene and then he would just lurk between them randomly.
[13:46] So it's never like staying too long in one pose. It's just looking around, kind of very natural.
[13:52] And then the other solution, the right. So that video is from our web app.
[13:56] And basically you could just mark a point and fix how many cray frames you wanted for Gekko to just fixate his targets into that specific point.
[14:08] So about the hands and pleated movements, I think with the eyes, the hands are the both things that sell Gekko's emotions and his movement.
[14:18] So that was the second most important thing for us.
[14:22] And the way we've done this is was using, we have three blend spaces, one for left hand, one for right hand and one for both hands.
[14:31] And each of them have four poses.
[14:33] And then to move those curves around, basically Zak, our senior developer, trained some animations that we had from our animators.
[14:42] And the way it works now is that if we input an audio and he's talking louder, the movement will be faster and more broader.
[14:51] And then if he's talking, be quiet and then with more poses, then the movements will be a bit slower and more contained.
[14:58] And also in the web app, you have the ability to specify which hand you want to play or you could just say it to be random.
[15:07] So hopefully this way we achieved something that doesn't look too repetitive and too robotic just with a couple of poses and just using an additive.
[15:19] For the emotions, we took inspiration to this motion chart, which is just basically a 2D vector.
[15:26] So here, all the human emotions are spreading this graph.
[15:30] Basically on the top, you have more active emotions.
[15:34] And then on the bottom, you have more passive, left to negative and right positive.
[15:39] And then what we've done is that we had 10 additive poses, just a single pose for each emotion.
[15:46] And then we would drive those emotions using the same idea of the emotion chart.
[15:50] And this way, we would never get like a 0 to 100% for each pose.
[15:55] And again, it would avoid it looking a bit robotic because you have always an average between three emotions as you're moving around.
[16:05] And also makes it a bit more natural to go, for example, from happy to angry, you go a little bit into excited.
[16:12] So the whole transition looks more natural.
[16:17] And then the final point was breathing.
[16:20] So don't underestimate the power of breathing animation.
[16:24] It's just easy to just forget about it, but it's so obvious, but it really makes the change.
[16:30] And it's all these small details that if you put on top of each other, that's what makes it different.
[16:36] And in this case, we just had a little bit of a shoulder and a little bit of a chest movement
[16:41] and just added as an additive layer in the animation blueprint.
[16:50] And here's our real-time web app.
[16:52] So basically, this was the tool that we developed and delivered to the client.
[16:57] And basically, they just could access the tool and create their own videos for social media.
[17:03] So they can move, change the cameras, they can add props, they can change the background.
[17:10] They can add some animations that we created for them already, like a wave
[17:15] or something a bit more specific that we just have for them.
[17:19] They could also bring it in the mp3 file and then just output and render an animation.
[17:29] Here's just a comparison just to show one side is CG, one side is real-time basically for this character.
[17:37] And you can't really tell which one is H if you want to have a guess.
[17:43] But basically, on the left side is the real-time, on the right side is the CG character.
[17:48] And even we were very impressed when we managed to achieve this high level of quality and fidelity with this character.
[17:58] So then this is a final example that was posted in their social media just to show how the quality of the output of this tool.
[18:07] In the beginning, it's just using the web app.
[18:10] And in the end, when he's like moving and eating, it's a bit of a mock-up.
[18:16] When it comes to finding the perfect home insurance, GEICO works for you.
[18:20] And since I'm the GEICO GECO, I work for you too.
[18:22] Like testing hot sauces on your behalf.
[18:25] That's way too hot. Who can eat this?
[18:29] This even hot up. Who chose these?
[18:37] So what didn't work so well?
[18:39] As in any project, things go a bit wrong and we just need to, you know, we have a deadline and you need to fix it somehow.
[18:48] So as I mentioned, the scaling for us was the biggest during the end for the tail.
[18:53] This was in real 5.3.
[18:55] So when we apply the physics asset into it, the tail just shrink.
[19:00] And we tried some other techniques, but as you can see, nothing was really working.
[19:04] So the solution to just to get something working was to add an IK node directly into the animation blueprint.
[19:12] And it would just follow the body movement if he was walking.
[19:15] If he was standing, we had an option to just have a pose that had the tail a little bit curled.
[19:21] And as he wasn't moving, you could just get away with that.
[19:29] Another issue that we had was eyelid clipping with the eyeball.
[19:33] So basically in some of the poses, when we were like mixing the poses, the emotions, there were some combinations that would cause that clipping.
[19:43] And the solution that we found for that was just to scale down the eyeball when it would blink.
[19:49] So just getting the bullying of the blink.
[19:52] And then when that was on basically the eyeball with switch, the light switch to 0.98.
[19:58] And then when the blink was off, he'll go back to one.
[20:05] So some final thoughts is, so first of all, our creative director will, he is been working with this character for a long time.
[20:14] He's a creative director, but he's also animated him for a long time.
[20:18] So having someone that is very familiar with the character is invaluable.
[20:22] He was the person that we would go to and just ask, like, does this look like Gekko or not?
[20:28] Like, when you are working with something like that, you just got to be too focused on the small details.
[20:35] And we're also always reviewing things with him, just simply asking the question, does it look like Gekko or not?
[20:42] And he would come with comments like, oh, Gekko wouldn't do this.
[20:46] Or for example, we shouldn't be seeing so much of the white part of his eyeballs.
[20:51] And just small comments that you wouldn't think about, but having someone that actually knows the character was really good.
[20:58] Another point is that camera angles and cuts can go a long way on making something exciting and different to watch.
[21:05] The same with props.
[21:07] So if you play with those items and you add the prop or, you know, change the camera,
[21:11] you don't need to have that much volume of animation to just come up with something exciting.
[21:18] And then the last thing was that Unreal 5 really allowed us to break the sigma of a gamey look.
[21:24] Again, coming from a VFX, we have that thing internally that is like, oh, this looks like game.
[21:30] This is a real look.
[21:32] And we just shown that basically you can't tell the difference.
[21:36] There is nothing like a real look.
[21:38] It's more about what style do you want to go for and Unreal can achieve that.
[21:42] So Unreal 5, it was a huge step in that sense.
[21:47] And then what's next is basically last week Gekko took part into a podcast.
[21:53] The easy for the podcast, for the round and find out.
[21:56] And it's really cool.
[21:57] Actually, it's really funny.
[21:59] I recommend watching it's like six minutes.
[22:01] And this was the longest continuous animation ever produced for Gekko.
[22:06] And it was all using our tool.
[22:08] And it just proves how you can go into like culture and more...
[22:13] Yeah, just bringing him into a real world and have this type of interactions was really fascinating.
[22:20] Wow. All right.
[22:22] So what you're telling us, Camilla, is I no longer have to exist only inside of a television screen.
[22:27] So that means I can do whatever I want.
[22:29] I read some of my own social media comments just because I feel like it.
[22:33] Here's one from Instagram.
[22:35] I could stare into your eyes all day, Mr. Gekko.
[22:37] And another one from Reddit.
[22:39] Gekko's out here aging like fine wine while the rest of us are just trying not to crumble under the weight of adulting.
[22:45] And from X, the Gekko Gekko is so cute, actually I want to kiss his little head.
[22:50] Feels rather nice to see all of the love.
[22:53] Thanks again for having me, Camilla.
[22:55] I hope everyone enjoys the remaining time here at Unreal Fest.
[23:00] And that's it.
[23:04] Yeah, feel free to reach out in my social media and everything.
[23:08] And if you have any questions, there's a microphone here.
[23:11] Thank you.



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
