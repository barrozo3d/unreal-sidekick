---
title: Unreal Engine UMG Tutorial 🎮 Build HUD & UI Systems (Beginner to Pro Guide)
source: YouTube
url: https://www.youtube.com/watch?v=cMPQ_W32VzI
author: GameDev
ingested: 2026-07-20
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/unreal-engine-umg-tutorial-build-hud-ui-systems-beginner-to-pro-guide/
frame_count: 0
frame_status: pending-selection
---

# Unreal Engine UMG Tutorial 🎮 Build HUD & UI Systems (Beginner to Pro Guide)

**Source:** [YouTube](https://www.youtube.com/watch?v=cMPQ_W32VzI)
**Author:** GameDev
**Duration:** 64m26s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames are not captured yet. Read the timestamped transcript below, pick moments
that actually show a technique/result worth a still (not blind percentages —
even within a named chapter, verify the real moment against its timestamps), then run:
  python select_frames.py unreal-engine-umg-tutorial-build-hud-ui-systems-beginner-to-pro-guide <ts1> <ts2> ...
(seconds or mm:ss). This appends a "Captured Frames" section and updates the
frontmatter before you write the Structured Notes below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] with those brand new course where you learn about different sections of Unreal Engine 4 in bite-sized videos.
[0:06] So this is UMG. We'll be looking at pretty much every single element inside UMG and how to do trivial things, how to do some things, how to carry out certain workflows in UMG.
[0:19] And you might start with some basics like how to position things inside UMG and so on.
[0:25] And then we'll gradually go on to other things which can be watched and complete isolation.
[0:32] So if you are already aware of what UMG is, then you might skip some of the first few videos and we'll be giving you practical solutions for practical problems.
[0:43] Problems that game developers might really encounter while they are working on a game project.
[0:49] And we have divided this into different sections.
[0:53] This section is UMG, Unreal Motion Graphics, which is used for creating user interface in Unreal.
[0:59] So I'll be going ahead and creating a blank project.
[1:02] So go over to the new project, Blueprint, Not C++, and blank, and desktop console, maximum quality, and we don't need to start a content for now because if you want to start a content, then we can add it later on.
[1:16] And then choose a path to save your project, a location for your project to be stored, and then give it a name for it.
[1:23] I'm going to name mine UMG and UE4 and then I'll simply say create a project for me.
[1:28] And depending on the speed of your computer, the project will be completed.
[1:33] The project will be loaded that faster and this is almost done.
[1:37] And because this has no starter content, so this should take much faster to load it up.
[1:41] And it's almost there. There you go.
[1:44] Okay, so there we have all of this.
[1:47] We have folders and it's a completely blank project.
[1:51] As you can see, nothing inside the content and these are the folders that come by default.
[1:55] And we also have a blank level for us to see.
[1:59] So this first video is going to teach you how to position things inside Unreal Motion Graphics or UMG.
[2:05] So for the inside the content folder, I'm going to create a new folder and I'm going to call this widgets.
[2:10] So it's good to keep them organized and double click that.
[2:14] I'm going to write clicks and to create a new user interface, your new UI widget,
[2:19] go to user interface and click on the widget blueprint.
[2:22] Not any of these things because these are quite advanced stuff.
[2:25] So we're just going to be covering widget blueprint for now and how to do a lot of things inside widget blueprint.
[2:29] And the first thing we'll be covering is how to position things.
[2:33] So I will just name this as positioning.
[2:38] And we'll create quite a lot of widget blueprints as we go for learning new topics.
[2:43] And this will be positioning learn.
[2:46] I'll just say how to position positioning, how to position.
[2:54] Okay, I'll just say how to positioning in UMG.
[3:01] Okay, and then just open that up.
[3:05] If you're absolutely new to UMG, then I recommend that you watch some of the interactive videos on what a UMG editor is like.
[3:13] But if you have some idea about it, but this could be more of a refresher for you.
[3:17] So this is what happens when you open a brand new UMG.
[3:21] You are presented with a designer and right next to that you have a graph view where you can write your blueprint code to drive the behavior of the elements inside the designer.
[3:31] And immediately in the hierarchy, you'll see the name of your UMG.
[3:36] That is the root and then you have Canvas panel, which is provided to you by default.
[3:41] And out here you have all of these, I'd say enables or disables the localization preview and all that.
[3:46] And then it also if you have a specific language, then you can use that.
[3:50] And then you have these transformation tools.
[3:52] You have a just in a widget layout transform.
[3:55] This is for the move tool and it also lets you snap it.
[3:58] And this is for zoom to fit.
[4:00] And this is for you to test out what your UI will look like in different screen sizes, be it monitors that is PC and all that, or be televisions or be laptops or be tablets or phones.
[4:13] So it has all of these categories that you can test what your UI will look like.
[4:18] So all it does is when I click on something like, let's say, I click on something like Microsoft Surface Pro landscape.
[4:26] And this is what a Microsoft Surface Pro looks like.
[4:30] I mean, that's what the aspect ratio and everything gets simulated.
[4:33] So these are more like presets.
[4:35] Okay. So for now, I think I'll just stick with 720p 720p.
[4:39] That's the television.
[4:41] And or you can also say 20 inch monitor.
[4:44] That's also okay.
[4:45] Whatever you choose.
[4:46] So I'll stick to 720p.
[4:48] And then of course, these are different things that when you say custom, then it lets you give within a height.
[4:54] And accordingly, it's going to scale the canvas panel for you.
[4:59] Or you can also say desired.
[5:01] And and anything that you add inside the canvas panel, it will take the shape of that.
[5:06] So for instance, if I just use text and I drop it here, it's going to take the shape of the, it's going to take the size of the text block.
[5:13] If I say, if I click on text block and I say size to content and the canvas panel and the text block are going to be the same size.
[5:19] Okay. And of course, I'll go back to first screen and I'll get rid of text block and let's get down to how we can position things in UMG.
[5:29] It's more of a quick refresher.
[5:31] And anything that you throw inside here is that canvas panel is also going to be used for positioning it.
[5:37] So for instance, if I use a button and I drop it inside here.
[5:42] And when you click on the button, you can see that automatically adds that as a child of canvas panel.
[5:48] Now, it's true that I drag and drop it as a child, but I can also drag and drop it inside the designer right away and will still be added as a child of the canvas panel.
[5:57] So I'll get rid of that button.
[5:59] And this button, if you can see that it gets the slot as canvas panel slot.
[6:04] And it gets a slot as canvas panel slot because it's a child of canvas panel and it will be by default anchored to the top left.
[6:12] Okay. And of course, you can move this around wherever you like, but this is by default anchor to the top left.
[6:18] Now, absolute basics to understand about positioning is if you could see that because this particular button is a child of the canvas panel.
[6:27] So that's why you could see that the slot is canvas panel slot.
[6:31] And the top slot here is always dedicated for the transformation or the positioning controls for that particular element.
[6:40] And canvas panel does not really have anything because that is the main parent.
[6:44] What it has is it does have a transform.
[6:47] So if you want, you can transform it and scale it.
[6:49] But normally people don't do that.
[6:51] People just have a canvas panel and then they start parenting things, you know, making elements, children of the canvas panel.
[6:57] So this is the button that you made a child of it.
[7:00] Now, if I have to drag and also the positioning properties of any child is always inherited from the positioning of its parent.
[7:11] So for instance, if I have to bring in, let's say, and look for panel, if I have to bring in a horizontal box and drop it here,
[7:20] if I look at the horizontal box, we'll get all of those same transformation or same positioning setup as you had it for the button.
[7:28] That's because the button is also direct child of canvas panel.
[7:33] And so is the horizontal box.
[7:35] So if I, let's say, I just drag this canvas panel out here, sorry, the horizontal box, and I do something like this.
[7:46] Horizontal box, there you go.
[7:50] Now, if I get this button and I drag it inside the horizontal box, you can see that the button automatically snaps it, snaps itself to the left.
[7:57] And why is that so?
[7:59] Because so far it was right in the center, but I, I dragged it and dropped inside the horizontal box.
[8:04] Now horizontal box has its own property of grouping things inside itself.
[8:08] And at the same time, now also the parent child relationship between button zero and canvas panel has changed.
[8:14] So button zero is now the direct child of horizontal box and horizontal box is now the direct child of canvas panel.
[8:20] So button zero is not no longer the direct child of canvas panel.
[8:24] So you, if you click on button zero now, you will not see the same positioning properties or slot for positioning properties.
[8:32] And also the slot has changed out here.
[8:34] It, it, it, you know, it takes the name of its immediate parent, which is horizontal box slot and not the canvas panel.
[8:41] Horizontal box though can still be positioned because it has these positioning.
[8:45] So if I say I want to bring this down to the center.
[8:49] And I first say I'll align this as point five and point five, which is also good practice because that brings it dead to the center.
[8:57] And then when I make this, if I zero the position X and position Y, you can see that it's in dead center.
[9:04] Okay.
[9:05] It's in dead center and the pivot is right in the center, which is good practice unless you want something else.
[9:10] And of course you can size this up so I can say I'll just make this 350 by 350.
[9:18] Okay.
[9:19] So that's like square horizontal panel with just one button in the top left.
[9:24] Of course I can select this.
[9:25] I can do a bunch of things, but I cannot really change the position.
[9:29] I can using the padding.
[9:31] So if I say I have, you know, I want to give it a list padding of 10, it's going to move 10 minutes.
[9:36] I say 50, I'm going to move 50 units.
[9:38] And if I say I want this to be a top panel, no top padding or 50 and a bottom padding of 50.
[9:47] So this is how I can resize it.
[9:49] Otherwise I can not really track things here.
[9:51] I don't have this kind of widget where, you know, I don't have this kind of gizmo for a child element inside a horizontal box.
[9:59] That's the way it works.
[10:00] So if I want to resize something, I can either use these horizontal and vertical alignment center that out.
[10:06] This is what the line center.
[10:08] And of course I can say this and this and this that.
[10:14] And then again, this is vertically aligned fill.
[10:17] And if I say that, now I can give it some padding.
[10:21] And if I say this, what if you are like top, so this, these are all the presets that you can have by default, this fills it up and by default, this also fills it up horizontally.
[10:31] So if I have to say fill, then it's going to fill up the whole panel with just one button.
[10:36] Okay.
[10:37] And says secretly attempts to fill all available to based on the percentage value that is zero to one.
[10:43] So if I say point three, five to this, and then I do that, let's say this is zero, this is point two.
[10:55] No, this actually fills up everything.
[10:57] It doesn't matter.
[10:58] That's because it has nothing else.
[11:00] It just really fills up everything.
[11:02] So if I had another, let's say I had another button, I tracked and dropped in another button inside the horizontal box here like that.
[11:10] Now this is, this is one, and this is not fill it.
[11:15] So now if I do that, then now this takes up point five and point five.
[11:19] So I have to say this will only take up point five.
[11:23] Now I can see that this, as soon as it says, as soon as I said this only takes point five and I say this also takes point five.
[11:31] You can see that it's a now both of them are sharing half of each.
[11:36] And even if I say one out here and one out here, so even that is going to give it exactly half depends on which is higher.
[11:45] Now if I say this, so we can take point one, then everything else will be taken by this guy by the second button.
[11:52] Okay.
[11:53] So now that was about the horizontal panel.
[11:55] So I moved the horizontal panel.
[12:00] I click on that horizontal panel and the horizontal panel.
[12:05] I just moved that somewhere to the left like this.
[12:08] And if I say if I change the anchor point, so just take a look at anchor points for a second.
[12:13] I take this choose this anchor point, which is the left center.
[12:17] Okay.
[12:18] And then again, if I really want this guy, but really want this guy to stick exactly at the center of this dot.
[12:25] So that's like the exact center of the top exactly as it says.
[12:30] If I want to do that, then the only thing I can do is I can first.
[12:34] This is normally zero, zero, and we had changed it to 0.5, 0.5.
[12:38] And this has some position based on how we are moving things.
[12:41] So if I really want this to be the center, so what I can do is I first know zero this out like I did earlier.
[12:50] And the size is fine.
[12:53] The size is actually relative to the size to content.
[12:56] If this is checked, then whatever content is pushed inside, then that would be the size of the entity itself or the object itself.
[13:03] So now the moment you say alignment at zero zero and position into zero zero, it automatically aligns itself to zero zero position and this is zero zero position is zero zero zero 0.
[13:16] This is 0.50 and this is 1 and 0 and this is no one and 0.5 and this is one and one. Okay. And this would be 0.5. No, this would be zero and no, I believe this would be 0.5 and zero and this would also be, you know, this would be, I believe one and zero, zero and one. Yeah.
[13:40] And so on. So now in the center, this is 0.5. This is 0.5. And this is how it moves. So zero to one and zero to one in the Y. But this has to be 0.5 and 0.5. So what's what happens when I say 0.5 out here, 0.5 out here. So it now it sits right in the middle.
[13:58] That's because the positioning of the horizontal box are relative to where the canvas panel is and canvas panel actually gives its children the ability to focus its direct children the ability to, you know, change the positions you will based on anchors and anchors.
[14:14] What anchors are what dictate the absolute position or absolute fixed positions of your elements when the screen size changes. So what do I mean by that is, let's say I instead of out here, I'll just say I'll put this somewhere.
[14:32] I'll first delete the horizontal box. No, I'll just keep it. Okay. I'll just say I'll do this out here and then I'll just move that. And let's say I don't want that to start from center.
[14:43] In fact, I don't want to start that from here. So I'll just reset this to 00 so that it sits there. Okay. Now, if I say if I'm not anchored there, or if I'm anchored elsewhere, then let's say if I change my screen size to something like portrait.
[15:03] Okay. And if I look at portrait, it's still sitting at the top of the corner. If I had not anchored it, let's say I had anchored it here, but I had moved this whole thing somewhere out here like that.
[15:16] And then if I change the screen size to something like landscape and you can see that it actually goes out of the screen itself. It's because it's not anchored properly. So, and now I say, now the calculation is not incorrect.
[15:30] Okay. The calculation is absolutely dead on because if I go back to my portrait scene, okay. And if you can see that this thing is not really moving, it's only the screens that's moving and it's also the distance between the anchor point and this thing also stays constant.
[15:46] So if this has to grow longer, if the portrait has to grow longer, it will still stay there. It's not going to grow according to the size of the growth of the screen itself. So that's why anchoring is really difficult.
[15:58] Now, if you always want your, you know, if you always want the elements to be anchored wherever it is right now, so you can just move this and you can just drop it here like this. So now this is sort of like 0.5 and 0.5.
[16:10] There's a very weird position to anchor it. If you really want it that way, then you can also custom anchor it and that's going to be the anchor for you. Okay. Now, of course, this is the absolute position. Now, if I do that, then it's going to go away.
[16:23] So if you really want it to be the center, then I can say 0.5 and 0.5. So now that goes to the center and also the positions have been zeroed out. Now, if I change the screen size to something like landscape, now you can see that it hasn't really moved out of the canvas panel because it knows how much units to position it by from the anchor.
[16:43] And it knows that it's exactly how much position from the bottom from the left from the left right and top and everywhere. So it's not going to move your button or your element away, or it's not going to make your element disappear because the screen size is just either shrunk or increase.
[16:58] So if I go back to a bigger screen size, let's say I, I'll just say 720p, just go back to Microsoft Surface Pro Portrait and this is the portrait and you can see that it hasn't, it does not go away from the screen no matter what.
[17:19] Somehow it ranges itself to the screen and it's always consistent with the distance that it has, distance it's going to be having from all the directions. So that's why positioning is important and this is how we position stuff.
[17:37] So I'll go back to my 720p. Okay. Okay. So and one more thing is if you really want to see how this thing works, this is a horizontal box and this has different properties from a canvas panel.
[17:50] So inside a horizontal box, everything is going to be aligned horizontally. So if I look at the button zero, it has 0.1 it only takes 0.1. So if I also say auto, it's just going to take still, it's still going to say take the same amount.
[18:03] If I say again fill and I use one out there. Now it's taken as much space as it can within the available horizontal box limits.
[18:15] Now if I have to change this, if I say color and opacity, if I say no, not this, out here normal, if I say this is red. Okay. And this is blue or green.
[18:33] Okay. So now we have two buttons, one is red and one is blue. And if I change this, I'll just rename this to PTN1 and the second one to then two. Okay. Or PTN red and PTN green.
[18:53] So for the PTN red, if I again bring this down to 0.5, you can see that it only takes half of it and it takes and other one that we can green because it says that I want this to fill up completely 100% of it.
[19:08] And so it takes up as much space as it can. So this is given up 0.5 of its space. So this guy has just taken that up. Okay. So I don't want that this guy to fill it up. So I can also say 0.1. Now this guy will fill it up for whatever that is worth.
[19:25] So I say 0.1. It does not mean that there's going to be empty space between them. So they're still going to go for whatever's available. That's because that's what it says. It says fill.
[19:36] Now if it's 0.1 now because these both are equal, so they both work on a person dial basis. Now if this is 0.1 and this is 0.1, it's almost regarded as a they're still going to take the equal share will give them equal space.
[19:50] The horizontal box decides that okay, they both point one with the buttons are point one. So I'll just give them point one share and then let them select based on how much they want to take on whatever's remaining whatever space is remaining.
[20:06] So what they do is they first take the point one space and then they go for this and because they both have equal at point one and point one. So they both end up taking equal spaces. This is the same as saying one and one.
[20:22] So they both are taking equal space. So the biggest takeaway from here is all of these panels they have their own stay with positioning in different ways. This is how horizontal box is positioning itself or these positioning of its children.
[20:40] But that's not how a canvas panel does a canvas panel. The moment you add a child to the canvas panel. Let like horizontal box is an immediate child to the canvas panel. This has gotten all these anchor properties and it's got the position properties a size and alignment size to content said or and everything else.
[20:58] But this is not the case with the button is that our children or horizontal box. In fact, the only way these guys can be positioned is when you are adding them across all the four directions or and if you want to size them then you size them based on a person and a percentage base.
[21:15] And then you can align them in different ways and everything else remains the same. But when it comes to positions, every single panel in the room to teal positioning for its or have different rules for positioning its children.
[21:29] So it depends on what exactly you need for your case. So and you can use your you can use the appropriate panel for that. So if you want something where you don't really need to worry about spaces on anything and you want them all to be stacked in a horizontal way or in a way.
[21:45] You can use the vertical way then you can use the horizontal box and there are other things that other panels like these are all the panels that they have and all have something that's different from each other in the way that they know in the way that they deal with positioning for the children.
[22:00] So so we'll be covering most of them.
[22:02] I think we'll be covering with the switcher and scale box and store box and actually we'll cover what what they are what they mean and where they're used. But this is basics of positioning and it's the model of the story is it's always parent child relationship and the children element or child element in the
[22:22] UMG always inherits the positioning attributes from its parent. So and also depends on what kind of panel you're working with. So if the parent that you're working with is a canvas panel then its children is always going to have its immediate children always going to have this positioning properties.
[22:39] If you're working at the horizontal box then its children is always going to have this kind of positioning properties where it's all relative to the space available within the horizontal box and same will apply all of these panels out here.
[22:53] It manual or not the canvas panel canvas panelist this same will apply to the vertical box or the uniform grid panel or even probably the rap box but that's how the positioning works inside and below it.
[23:06] So that's welcome back to the second video on UMG and in this video you will learn about how to size things up. We saw a little bit of it in the first one. So just going to take that a little forward.
[23:16] So I'm going to create a new user interface widget. You have widget and widget blueprint and I'll just say how to how to size how to size how to size then UMG.
[23:29] That's okay. All right. So now of course the same thing screen size stays the same that does not change unless you want to fill or custom. So I'm not going to do anything there.
[23:41] But as you noticed in the last video we had canvas panel. So this canvas panel allows its children to do a bunch of things that other panels do not allow them to do.
[23:51] So I drop in an image and this image has the freedom to choose its position to this anchor to this alignment and all of that stuff.
[24:01] Okay. So if I choose this, let's say I just drag and drop this in the center. Now I have the liberty to choose size for this image and I'll just say 100 by 100.
[24:13] There you go. And if I say center it and zero this out and then bring it out to the centers that's that center. Okay. And maybe I'll just say that's a 200 by 200.
[24:27] So now if this is an image of something, let's say if I go down to brush and image size itself is 32 by 32, you can see that, you know, this thing or the slot out here of which it's a child of canvas panel.
[24:43] It overrides the size of the image here. Okay. So if I really want this to let's say I want this to size up to, I don't know, if I say 300 by 300, you can see that's not doing anything out there because that's been overdidden by the size of the slot canvas panel slot this particular slot out here.
[25:03] You will not be able to do anything to the image size out here. Unless if you really want to change that, you know, you can just say size to content and now it's actually going to be a 32 by 32.
[25:13] If I don't, then it's going to go back to 100 by 200. Let's say I do this as 500 by 500. And of course, it's not going to show anything because the values of the size for this particular image being a child of the canvas panel has been overridden by the properties of the slot out here.
[25:31] That's why you can notice it says canvas panel slot in brackets, but out here it is not. So these properties are not going to affect the, you know, the size x and the size y of this particular object.
[25:44] Unless you click on this. So if I check on this, you can see that it grows in size because the size out here is 500 by 500. Now, now I have control when I say size to content, which means that I'm actually taking the control away from the parent.
[25:57] And I'm saying, okay, I want to size this myself and I don't want you to size it for me. But now it doesn't matter what the size of this image is, or this particular size x and the size y out here is for the slot.
[26:10] So now it's going to be completely dependent on what my image size is. So I can go ahead and I can, I don't know, I can probably take the entire, this is one two eight zero by 720. Then I can say one two eight zero by 720.
[26:24] Okay, that's how big it can get. And of course, I can probably stretch it out as well. No, I can't. That's because I go back here zero zero. So this is that. And of course, if I don't want to size it by content, and then I can stretch it out like that zero zero.
[26:45] Now I can stretch it out. But at the same time, this is just a blank image which has no text texture values in it. But of course, if I say this, and it doesn't matter what I make the size to be, it's always going to be 120 or one two eight zero by 720.
[27:03] And of course, I can move this around. And that's going to be only the position but the scale is not going to be reflected here. So even if I increase the size by let's say like this, it doesn't matter. It's always going to be there.
[27:16] Now this is, if I say I want to increase the size like that, and then I want to increase the height by this much. And then I want to give it a tint of let's say blue.
[27:26] And then if I let's say I change the screen size to surface pro, and it's going to fill the screen size that's going to work pretty fine if I say HTC one pro trade but that's not going to do it. That's because it sizing it to content.
[27:39] Okay, but it's just staying there. It's just staying there. And if I say don't size it to content, and then it's going to be taking the hundred by 30 value. And now if I the anchor is going to be lost, even though the anchor has been set.
[27:54] It's not going to fill anything up. Now, if I let's say I make this to 500 by 500. Okay, and I say, okay, I'm going to change the screen size to landscape. And you can see that it's actually sitting in the death center of all the screen sizes.
[28:11] I can go up to 27 inch monitor is still sitting in the center. I can go up to a 4k digital cinema and still sitting in the center. Okay, and 4k ultra HD 4k 720p. That's the default. That's also sitting there pretty fine. So no issues at all.
[28:28] So, even if I go to 19 inch monitor, so everything works. That's because of the anchor. Okay, that's what we saw in the previous video, but you learn something new in the fact that the sizing, when you unless you click on size to content, it's not going to let you overwrite the values of the size X and the size y values inside the slot.
[28:46] That's because it's a child of the canvas panel, but the moment you click on this, and that's going to take up the whole thing. But then again, this is not what we need because the moment we change the screen size, it's going to be, you know, it's still going to be sitting there. The anchors are fine, but it's not going to fill up the screen.
[29:04] If you really want to fill up the screen, then this is what you'll have to do. You can delete that. Or what you can do is you can bring in, let's say, a border. There's another thing, something called a border. Now a border also looks like an image. But I think I'll just bring it down to center and point five and point.
[29:25] Okay, and I'll get the brush. I'll say image none. Okay, that I can see what's inside there. Now, of course, I can change this to something size of let's say 200 by 200. Okay, now if I bring in something inside the border, let's say I bring in an image, and it's going to fill it up. Okay, and of course, I can give it a tent.
[29:50] Make this red in color. Yeah, and I'll just call this red, red, red. Okay, and I'll bring in another image. And of course, you can see that you can't parent an image with an image. It always has to be some sort of panel. Because I can't do that. That's because the border has just one. Now, if you click on this image and you can say that I want to center this like that. So that's actually absolutely center horizontally and vertically. And if you want, you can get rid of all the padding as well.
[30:17] So I can say don't pad absolute debt center. Alright, and now we can do a bunch of things. Now this is what enables you to size it up. Now if I say horizontally aligned fill and horizontally aligned fill, that does that. And and if I do this, I'll say this this so you're out here you don't have this restriction for you know, horizontal and the vertical
[30:46] alignment being overridden by the horizontal and the vertical alignments here. That's because this says what the content is. Okay, and out here, this is the exact same content of let's say I want this to be this is red. So this is the content. But this actually lets you control it from outside. And if I do that, and this and I come back here, you can see that it this is also changed. So they all interchangeable they both interchangeable out here. So make it zero.
[31:14] Okay, you'll see that in the red image down here, you do not see the same properties. So this is the exact same situation that we had run into when we actually created child elements for a horizontal panel right. So that's what this means. So let me just go ahead and delete this and I'll bring in something called let's say panel, I'll bring in a vertical box.
[31:39] Okay, now a vertical box is a child, direct child of canvas panel. So it's happy. It does all of this and has no issues doing that. So I'll just again set it up in the center and zero the positions of x and y and then to make it in the death center. I'll bring the pivot down to the center as well.
[31:59] Now this is got 100 by 300. Of course, I can increase the size by let's say 300 by 30 and let's say 300 by 600. Okay, if you notice that the pivot still stays in the center so it grows from all the directions proportionately. Okay, so now if I let's say I add a bunch of things I add, let's say I go back here, I add an image like that.
[32:29] And I'll just make this red. Then I'll make I'll have another image. I'll make this green. Okay, and another I'll make this blue RGB. Okay, and so first let me add a progress bar as well inside the vertical box.
[32:48] So they have a progress bar as well. So now if you see, they're all vertically aligned and they're stacked over on top of each other. Okay, so let me actually give them some colors that we can differentiate it easily. So this is red. So zero and zero. That's red.
[33:02] Then go to green. And this will be zero one and zero. That's green. Then you go to blue. That will be zero zero and one. Okay. And of course the progress bar has nothing it says fill. Now if I tell them all to fill.
[33:20] Let's say I say I tell them all to fill. Okay, that's 100%. And because this is not 100. This is not fill. This is auto it takes whatever is remaining after the red has taken it up. Now if I say fill, and that also taking 100, 100% of it, 100% of its size, 100% of its size. And if I say fill for the progress bar as well, and you can see that this also takes the same thing.
[33:43] Now, I can change this to let's say green. And also the percentage I'll make it point five. And also the style I'll make the background color to be dead.
[33:59] Okay, so that indicates a proper progress bar. And of course this is not really looking like a progress bar right now because this is just looking like colored boxes. So a red box below it box on top of green box on top of blue box. And then there are like two horizontally stacked boxes one is green and one is red, and they are placed horizontally.
[34:18] Okay, so in order to change that. So if I let's say I make this horizontally aligned center and horizontally aligned center and I can see that it gets really tiny. And you can also see that you cannot really change, even if we change the padding, let's say from the right, I say five.
[34:36] And from the left, I say 150 or something. It's not going to change the size in any manner. So it's not that you're stuck here, you can still change it. So what you'll have to do is you'll have to wrap this with a special element.
[34:49] Wrap this with a special box. If you're just size this up. So you can write click, you can say wrap with and you can say wrap it with a size box. Now you have the size box. And now you can say, I want this to be not you have this child layout. Okay, what it does is size box what it does is when you wrap it up with a size box, it looks at all the children.
[35:09] And then it says, Okay, how much do I want the with override to be now we want override the width of this particular element, the vertical box because vertical boxes right now having a control on all of these guys, okay, all of these boxes.
[35:22] Now they don't have individual control of how much size they need to be. Now, even if I give it a size of, let's say 128 by 128, it's not going to matter, because it cannot override the size that it's been given by the vertical box itself.
[35:37] So that's why you wrap things up with a size box if you need them. Now I've wrapped the progress bar with a size box. So now I can go over to the size box I can say with override and height override. So right now it says zero. So I can probably increase the size like that.
[35:55] Okay, and I can just probably look further in and maybe 294. So I'll just say 296 or 300. 300 is good. So that's the size of vertical box that's 300 and 600. I'll just make it 300 by let's say 100. So that's not even 100. I think 30 is good.
[36:17] But now that looks like progress bar, a proper progress bar. Now, again, if you really want this to be aligned, horizontally aligned center, then you can do that. But then again, if you want to lose that, so I'll just say do this. In fact, even if you want to say this and this, and if I increase the size, it's not going to override that.
[36:37] So I'll just say this and this, I can also do that. But then again, the size box is still doing the same thing. So I can say auto and that's going to not fill it up. So I'll just keep it at this. Okay. And now the progress bar, I can say, let's say this and this it's not going to override anything because it's already been over it in with that.
[37:02] So if I go back to size box and if I now override the size as 300 and override the height as with as 300 and height to be 30 is still not going to do that because I have not set this up as horizontally align fill. So if I go back here and if I say this and this now it fills it up horizontally and vertically.
[37:21] And if I say just do that, then only fill it up and this is what he aligned in the top, but it'll still fill up horizontally. And if I do that, then it'll just horizontally aligned to the left and what he learned to the top. So it's at the top left.
[37:35] Okay. And so if you really want the size, then you can do that. And if you don't want the size, then you can always change the size out here. So instead of 300 I can make it 150 and that will still look like a progress bar.
[37:47] And you can also activate and you can also work around with this progress bar like it. You can always do that. So if you do that and that works like a progress bar.
[37:55] Okay. So just keep this in mind that different panels again, I'm repeating this different panels have different properties, a vertical box and horizontal box work similarly a vertical box horizontal box a group, I believe what's that called a border and then you have a grid panel.
[38:14] And then you have a uniform grid panel, all of these guys they work pretty much similarly. So now these are grouping, you know, grouping objects, like they are containers, that's the right word for it. But they are containers that take in a lot of these elements and they depending on the kind of container that you have chosen if it's a horizontal one then it's going to stack all the container if it's going to stack all the objects in the container in a horizontal fashion.
[38:40] And if it's a vertical it's going to stack one about another and uniform grid panel is what when you use when you want to stack them all up in a, you know, in a proper grid like fashion and the same with the grid panel, where you can do a bunch of things.
[38:53] Now we'll look at all of this, but this is the basics of sizing so you have to understand that this is never going to be overridden by you can never override the positions of the vertical that's dictated by the vertical box, unless you are playing around with the padding.
[39:09] Or unless you're playing around with the horizontal alignment, or you're playing around the size which just has two properties that auto which only request as much room as it reads out here, only request at as much room as it needs based on the widgets desired size and fill is based on the percentage.
[39:27] Okay, and that's it. And that's about sizing. Okay, welcome back. So in this video, we'll take a look at the canvas panel and how to make a very simple UI for most of the games that have you guys like that will make it using the canvas panel alone and will not use anything else.
[39:44] And you will not use any horizontal boxes or vertical boxes or any of those other fancy panels. So we'll just try and make something very extremely simple, quite minimalistic in nature that most of the games will have all the time.
[39:56] Okay. And so for that, I'll make a new user interface. I'll close them all up close these guys. And I'll make a user interface. I'll call this Richard Cluckin.
[40:06] And I'll name this how to handle spanner, handle spanner in UMG. In fact, I don't really need to give these big names, but I'm used to it. If you talk it here, first thing I'm going to need is I let me just mention this line something out here. Okay, out here, I'm going to need something, some image out here, I'm going to need a progress bar, which dictates your health.
[40:34] And out here, I'm going to need some sort of button to move around. Let's say, let's imagine that this is no mobile game. So I'm going to change this to say, HTC one landscape. Okay. So this is a mobile game. So let's imagine that we're working on a mobile game.
[40:51] And I want some information out here, which gives you ammo and some distance information out here. And then something out here as well. Okay, so first thing is let me try and make a crosshair. Let's say I make a crosshair. So for that, let me look for something online.
[41:11] So if I go to Google, or you can also use bang if you so like. And I'll just search for crosshair. Okay, then I go to images. And then I just get some crosshair that I like. I think I like this particular crosshair. It's quite simple. Okay, I'll just get this.
[41:32] I'll say save picture as and I'll just go over to my location where I saved my project. Okay, out here, I'll just make a new folder called images or something or I'll just call this.
[41:45] Or in fact, I won't make this here. I'll just delete it. I'll go back here. I'll go to raw assets and save that as a JPEG. That's okay, because I need to change this to a PNG later on. So I'll just save it anyways. I'll close that. I'll go over to my, where that saved.
[42:05] Let's say, try. Okay, okay, raw assets. I'll right click and I'll say open with I'll open it with pain.net. You can open it with Photoshop if you already know Photoshop. Okay, and let's say I want to make this resize to right now it's 238 by 240, which is massive. So I'll just make this 128 by 128.
[42:35] That's enough. Or maybe not. Maybe I'll just make it to 512 by 512 for 256 by 256. Okay, and then I'll just bring in the magic wand, delete that. Okay, and then I'll just say, I'll just bring this in.
[42:52] I'll say control shift X. And I think I'll further or you know what, I'll just bring in this and I'll click this or click this. I'll say control shift X. I'll say control I control shift X. And now this gives me the exact crosshair, just the shape of the crosshair.
[43:13] And I'll save this as go back here. I'll go open my project folder. I'll go over to the content. And let me inside widgets. I'm going to create in fact, you can do that here inside here. Go back to my content browser inside widgets. I'll create a new folder called images.
[43:32] And now I can save that control shift is to save as I first I'll change this to PNG. And real engine content, widgets, images. And I'll just name this crosshair. Okay, and it does all of that. I'll say, okay, fine. I'm a close pain.net.
[43:52] Now, if I come over and this will give me a pop up and I'll just say import, go ahead and import it. Because it has detected some file has been added. So it's asking us whether we want to, you know, import it. Now, open this up. These are all settings that we have not going to go through everything now.
[44:10] These are all the compression settings that we're not worried about right now. In fact, what we're worried about is a picture group. So we can change this to UI so that it has a specific signature and nothing else needed to be changed. So I'll just close that.
[44:25] And inside here, I'll first bring in a crosshair. The first thing is I'll drag an image and I'll just drop it here. I'll obviously make it a child of finance panel because that's the main panel out there. And I'll rename this to crosshair, crosshair. Okay, and now I want this to be whatever size I want it to be.
[44:45] So first thing is I'm going to set it up to be in the center and then I'll give it an offset. Okay, set it up to the center and I'll say zero and zero.
[44:56] And I'll also say point five and point five to bring it down to the center as the pivot point of that.
[45:04] And now I think I'll just select this and I'll use my arrow keys to move it up because that's normally not it's not always in the center of the screen. The crosshair is always like 33% from the top. So this is somewhere I feel is the right place.
[45:19] Now I can bring in the image. Okay, I can with the crosshair click and go back here and I can just click on this little arrow and this will bring in the image.
[45:28] I say size to content, it will bring that here. Okay, so now if I hit compile and I don't think I'll see anything. Yeah, that's because we haven't hooked up. We haven't hooked us up to show in the project. Okay, so now we have the crosshair and let's see. Let's say we need something like help.
[45:48] Maybe somewhere here and some image out here to give us some information, some buttons to move around. Let's say I will choose a button and I'll just bring it down here first. Okay, and this will be for maybe let's say.
[46:03] Just remember that this is a mobile game so using the user will use this left thumb to look around and his right thumb to actually walk ahead and move and this will be for the camera planning and this will be for walking ahead or I believe you can interchange it if you want to.
[46:23] But I think I'll keep it in this way. I'll just use this to look around and so for that I'll need let's say for I'll need for buttons to move around or something. Let's say, huh.
[46:41] Okay, let me see if I can find an image which.
[46:52] Okay, this is this is actually pretty nasty. Because it and I end up clicking on that and it's so quick.
[47:02] It's almost impossible. Okay, for that I think I can go to this and I can go engine content and I can look for something out here. Let's say if I look at mobile resources and let's say I look at the HUB and these are all these are all of these things that you have.
[47:27] This is for the mobile heart direction pad and this is for the mobile heart direction back to the different types of direction fans. Now we need this the thumb and the background so I think I'll use this. I'll come back here and I'll click on this.
[47:42] Okay, and that's what that is. Now I'll change this to draw as an image. Okay, and then I'll size the content. Okay, and maybe I'll just increase the size. Let's say what is the size that's just 64 by 64 right.
[47:58] So maybe I'll just increase this to let's say 128 by 128. Okay, and for the 26 by 26 that's good. And I'll change the anchor for this to be on the bottom left. Okay, and I think I should first I'll just do this first and then I'll bring it up and because it's size to content.
[48:28] What the size here does not matter. I can say 10,000 and it's not going to matter. That's because the size to content overrides everything else. The alignment of course is going to be this is zero and and this is one. So I'll just make it zero and one.
[48:44] Okay, and then I can probably give it some offset. I can click on this and I can give it some offset like this. Maybe 50 to the left from position y position x and 50 solution. No, minus 50 on position y.
[49:00] So that puts it somewhere there and it's going to stay there. Okay, and of course this is just a button and I'll just call this.
[49:08] Let's say not going to be functional just designing the UI just using the canvas panel so that you understand how the anchors and everything works. And so this will be VPN pan camera.
[49:21] And of course, I do not think the five dragon image and drop it here again, drop that image as well. And this is VPN cameras six by two to six and twice say, say, because this is that so I think I can go back here and I will say, why don't you buy one?
[49:47] And of course, that's not going to increase because this is changed to something like that. So I increase the size to five and two by five and two. That's too huge. I think 256 by 256. That's fine.
[50:03] And this image can be somewhere horizontal fill and this. Okay, and then of course I can get rid of the padding.
[50:13] All right, this and draw this as an image and this will be this particular and I'll just do that. And of course, if I turn this off.
[50:28] It's not showing that here. That's because image color in a fast key. That's okay. All right, transform pivot clipping inherit. Let's say transform pivot is okay. And this is not getting the anchors because now the button is the parent.
[50:50] So even if I say size to content, that's gonna be that as size to content is five and two by five and two and image by say this not going to help.
[51:02] That's because this not going to help. So what I can do is I can just delete that and I just say size to content and then just can go back here and this will be to the six by six. Okay, and I can just drag an image and just drop it here.
[51:22] And I'll just call this image thumbstick. And this can have the same anchors as this. So this is anchor at say I'll just call this anchor at bottom left and size to content as well size to content and let's see.
[51:44] I just position this out here as well. So now this is 100 by 30. And then again, I'll say, I think it was zero and one, right? Yeah, zero and one. So zero and one, there you go. Now, I can give it the same kind of position. So 50 and minus 50.
[52:05] Okay, and that's out there. Now, of course, it does not have the same size. So if I go back here and if I look at this, this is also this is actually two to six by two to six. Now, with that click, I do that. Okay, you can actually see that it's really light.
[52:25] So it's actually pretty light. So it's really hard to see. But anyways, if I bring that to the fourth one, it's not going to help. But that that to six by two to six. And even if I maybe change the image, now you can see that it's actually taking some shape.
[52:45] It was working even earlier, but we could not see it. So that's why. So if I bring it to a red or a green, you can see that the border is changing color. I'll just bring it to a red, just for fun. And zero and okay, so there you have that thumbstick.
[53:04] And of course, it's not looking brilliant. That's because the background itself is black and you're not able to see it. So now we have your left thumbstick and where the player can look around and you have the crosshair.
[53:16] And in fact, no, you can actually parent this to that. And this will take up everything. And even if I do that, and now it's actually taking up shape. And you can see the borders lighting up. And if I do this, no, not really.
[53:32] But anyways, the tint is this and everything is fine color and opacity. And that's the brush and the size. And if I do that, I think also keep that as one zero zero. That's red, a bit red, and that's looking pretty cool.
[53:51] And then you have the button, a BTN pan camera. Now you can click and you can copy and you can click here and you can paste. So that becomes the BTN.
[54:02] It just renames the button and it puts it back and puts it at the same anchor point. The anchor is at and resets everything. And that's it. And so I'll just rename this to BTN, I guess, move player.
[54:18] And this will be towards bottom right. Okay. And again, I'll do that. And this will be one and zero, like that. And I'll give it the same kind of pairing. And this will be minus 50 and 50.
[54:37] So that it's in the same place. Now for this, we can move layer that then it is going to be image. I just call this IMG thumbstick PG and IMG thumbstick move thumbstick PG.
[54:56] Okay, and this can be something else, the color for this can be something else. This can be green, zero, one, zero, green, zero, one, zero. So now we have this. And next up, just a compile save.
[55:18] I think we can change this move layer button to something else. And of course, we have not changed anything from how we're, how we don't need it, but for pressed, we can have the same button.
[55:31] We can say, we can do this. Come back here. I just clicked on this so that it took me to where it is in the content browser. And I can do the same thing for BTN pressed.
[55:44] Okay, draw it as an image and get the same two to six by two to six. Okay, and instead, the tint will be something like, I don't know, let's say grayish, you know, you know that it's being pressed.
[56:00] But then again, you have this is not exactly how this works, because this is more like a thumbstick. So you keep on pressing it and moving it around. So that's a different thing.
[56:09] We're not focusing on the behavior of the button itself. We're just trying to focus on how to place things on a canvas panel and move things around.
[56:17] So I think I'm okay with that. And I'll just hit compile save. And this is, I think I'll make this something different. So if I come here, I think I can make that as mobile hv direction pad.
[56:30] Okay, come here and then change that to this. Okay, and there you go. So now you have this and then you have for the moment. Okay, now we have these two buttons, which will work fine.
[56:42] And then let's say you want a progress bar in the center. So again, I'll bring in a progress bar and just dump it there. And I'll just call this helper.
[56:53] And I want to anchor it. Let's say I'll just track this first. And I just drag this in here. And I just drop it here.
[57:05] Like that. And I'll say I want to anchor it to mid center. Okay, and then I'll say zero and zero. And then again, this is point five and point five. That brings it up.
[57:18] No point five and one that brings it up like that. Now I can just click on this and I can move it a little bit up like this.
[57:27] I think I'm good there. Let me make this touch. Yeah, that's good. Okay, and of course, let's give it size to I don't think I don't think I'll need a background image. I don't have one.
[57:41] So I'll just manually increase the size. So I'll just say, say 500 by 35. Okay, that's good enough.
[57:53] And of course, the background image can be, I don't know, maybe an image and not an image. It's got no image. So if I say none, and I still can't change the color, I'll just background image can be one zero zero.
[58:09] And it can be an image like that. Okay, with the gradient, even though it's got none. And the progress can be, let's say if I say point five, and you can see that progress is happening.
[58:23] But then again, I don't want this to be point five one, I want this to be one and zero. Okay, and they go. So now you have some you have something that looks like a progress bar and and then we can just call this.
[58:37] I think 500 by I'll just give it a proper position minus 90. Okay, just put it there. In fact, I'll just make this box so that I have solid color instead of gradient. And I'll just have a text block beneath it.
[58:53] I just place that there right away and I'll size the content. I'll again put it at the same place and again zero and zero and position. I don't care because it's size to content. And I'll say point five and one.
[59:09] Once I have selected that, I'll just move this up. Okay, and I'll just say help. Okay, and of course I'll increase the font size. I go to font here, at least font size to somewhere like 30 or I think that's okay.
[59:30] And I can also I can also change the color of the text. I can say here. I think this is a better color for player health. Okay, so now we have that. And once it's all done, we're going to hook this up to our level blueprint, simple level blueprint and see that everything works fine.
[59:52] And of course, if you play this, it's not going to see anything because it's not hooked up. Okay, so now we have all of these elements. Now we'll just place something out here and out here. So we just place, you know, an ammo count out here.
[60:07] So I can place a text block. And then again, I'll say I want this to be out here.
[60:15] Size to content. I'll say right away, ammo and colon space. And I'll just call this, let's say I have to 25 and of course I can change the size on size to 30 or 40. That's good.
[60:36] And then you have it's everything is anchored fine and it doesn't matter what the size is. And I think I can. And that's exactly the way I want, because it's already hooked up to the top left anchor and the pivot point is also here.
[60:52] So if I say if I say 00 it's already there. So I say 0.5.5 that's going to have some issues. So I think I'm okay with this. I'll just move this up a little bit.
[61:02] And I think that's okay. And maybe out here. I don't know what. Okay, fine. So for now I'll just go with this. And out here in the level blueprint, I'll first save this level just for fun.
[61:14] And just save and I'll create a new folder called maps.
[61:20] And I'll save this for UI.
[61:24] U. M. D.
[61:26] There you go.
[61:28] All right. So now go to level blueprint and get rid of these.
[61:34] Inside even big and play. I'll just say create widget. Okay. And the widget we just have. Well, we have quite a lot of now. We just say how to canvas my name. That's what we know. That's what we need. And this will be added to the viewport as simple as that.
[61:53] So if you want to test any of the widgets, you just come here and we change the name of the widget and we can test it right there.
[61:57] Now if I hit play, I can see that I can you have the cursor. I have the crosshair. I have the player health. And I also have my deep ad and the thumbs.
[62:09] Now if I say shift F1 and if I try and close the hover needs to be changed is looking ugly. So if I come here and look at this, the hover. I'll just change the hover for now.
[62:20] This is the BTN move player and the hover. I just get rid of it as none. There's no hover because it's a mobile platform sort of just trying to simulate it. It's not a mobile platform.
[62:35] Compile save. Okay. And now if I had play, I can see that. Okay. If I had shift F1, I'm going to get the cursor out. I can see this. And of course, this as well. Pretty good.
[62:47] And if I try and resize, okay, let's let me first maximize it and see that everything stays at the same position and not move a lot. So if I do that, and you can see that everything has stayed in the same position, the deep ad is still here.
[63:01] The thumb stick is still here. The player health and the text as well as the progress bar is still here and the ammo counter is still here.
[63:07] Now what happens if I move resize my window manually? If I do that, you can see that it's still trying its best to, you know, resize itself. Now that this would be a normal size of a phone, right? This is what you see.
[63:22] And not bad at all. So the ammo is still there. And if I move around, imagine that I'm using my, my thumb stick, my left thumb stick to look around and then I'm using the right one to move. So that's pretty good.
[63:36] So that's how we use your canvas panel and rearrange them in the way and you can create absolutely a very simple UI for your game just using canvas panel. But of course, if you're making something really complex, then you're going to need a lot of other things.
[63:51] You're going to need other panels as well. You might, and then you might also need some special effects and you'll need some input spin boxes and so on, depending on your need. But this is good enough for a very simple UI.
[64:05] If your UI, if the UI of your game is going to be as simple as this, nothing like it. Okay. So that was about creating a very simple UI using your canvas panel inside UNG. And this is how you hook things up to show on your, on your screen space.
[64:22] This is how you hook up widgets to show up on your screen space. Okay.



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
