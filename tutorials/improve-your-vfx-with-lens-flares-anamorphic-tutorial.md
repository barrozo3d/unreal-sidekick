---
title: Improve Your VFX with Lens Flares (Anamorphic Tutorial)
source: YouTube
url: https://www.youtube.com/watch?v=hFM_jGd46as
author: Josh Toonen
ingested: 2026-06-23
ue_version: "[PENDING]"
tags: []
extraction_status: pending
frames_dir: tutorials/frames/improve-your-vfx-with-lens-flares-anamorphic-tutorial/
frame_count: 13
---

# Improve Your VFX with Lens Flares (Anamorphic Tutorial)

**Source:** [YouTube](https://www.youtube.com/watch?v=hFM_jGd46as)
**Author:** Josh Toonen
**Duration:** 17m40s | 13 section(s)

---

## Raw Data (for Claude Code extraction)


### The Secret to Cinematic Hollywood films [0:00]
**Transcript:** What if you could make your visual effects look as cinematic as the Hollywood classics?  We're talking alien,  Blade Runner, and Raiders of the Lost are.  How can you recreate the look of these iconic films?  Umm...  The hidden secret is they're filmed on an anamorphic lens.  Anamorphic lenses define the look of the 80s and 90s and they're still used today.  Even this lens, it has all the imperfections of a real anamorphic lens.  So what goes behind this iconic look and how can you recreate it for your own films?  Believe it or not, it's never been easier by taking your CG renders and transforming them  to look like they were shot through an anamorphic lens.  What's up?  My name's Josh Tunin and for the last 8 years I've worked on Hollywood visual effects  as an artist and supervisor on movies like Star Wars, Dungeons & Dragons, and across the  Spider-Verse.  And I started using Unreal Engine on set for the virtual production of TV shows like Avatar  the Last Airbender.  I started off as a self-taught visual effects artist learning right here on YouTube.  And I want to give away all the secrets I've learned along the way and teach you the  three steps to recreate the classic anamorphic look every single time.  So let's dive into the anamorphic masterclass.  Now there's two key features of every anamorphic lens, the Boka and the lens flares.

**Frame:** tutorials\frames\improve-your-vfx-with-lens-flares-anamorphic-tutorial\frame_000.jpg

### The Anamorphic Masterclass [1:07]
**Transcript:** So today I'm going to teach you the artistic side of compositing.  Take your raw CG renders and transform them into a shot that looks like it could come  through a real camera lens.  And I've proved all of your visual effects shots by the end of this video.  Now compositing is just Photoshop for video.  Now don't worry, all of these techniques can be applied inside of After Effects, but  if you've gone into a movie theater, 99% of those movies weren't made with After Effects,  they're all made using Nuke.  I'm going to teach you the technical side, but more important than that, you need to learn  how to see.  A compositor is only as good as their creative eye.  If you can't see what's wrong with your shot and you're unsure of what to do next to improve  it, that means you need to be collecting reference.  Amateurs will guess how the visual effects are supposed to look but pros use reference  every single time.  Find the movies that you love and the different films that inspire you and use those as your  reference for your own visual effects and movies.

**Frame:** tutorials\frames\improve-your-vfx-with-lens-flares-anamorphic-tutorial\frame_001.jpg

### Matching the Defocus + Bokeh [2:11]
**Transcript:** First step is matching the defocus of a real anamorphic lens.  The Boka shape or the lens orbs that you'll see in the background are more of a thin oval  shape.  It makes reflections and light sources larger than life, where a spherical lens is more  of a circle and it's super simple and straightforward to apply after the fact inside of Nuke to  get really high quality depth of field and match that anamorphic look.  I love working with anamorphic because you have this beautiful fall off behind them.  That's the beauty of anamorphic, worse faracle.  You've got less glass to go through so it's sharper with the depth of the field is deeper  and it's just a matter of what you're looking for through the viewfinder.  Using the ZD focus node and rendering out a world depth pass out of Unreal Engine, you  can get perfect anamorphic Boka every single time.  The one thing to note here is that you want to make sure in Unreal that you're disabling  depth of field or disabling your focus settings.  This will make sure that your image is perfectly sharp when we're importing it or reading it  into Nuke so that we can add all that depth of field after the fact and we're not doubling  up on that depth of field which is going to give us a blurry and unrealistic image.  Look at this pass directly out of Unreal.  All we have to do is apply the ZD focus node and change the depth channel to our world depth

**Frame:** tutorials\frames\improve-your-vfx-with-lens-flares-anamorphic-tutorial\frame_002.jpg

### How to Add Defocus in Nuke (Zdefocus) [3:23]
**Transcript:** dot red channel.  Now with this little focal point in the center of our scene, you can animate that focal point  so you can move that plane of focus throughout the duration of your shot which is exactly  what would happen on a real movie set.  We can always preview that focal plane set up to see exactly where we're focusing inside  of our 3D scene.  Now wherever we focus our camera, we'll get that perfectly sharp but that background  will progressively get more and more out of focus the further into depth we look.  Then all we have to do to transform this from a spherical lens to an anamorphic lens

**Frame:** tutorials\frames\improve-your-vfx-with-lens-flares-anamorphic-tutorial\frame_003.jpg

### Turn your Spherical Bokeh to Anamorphic [4:00]
**Transcript:** is change the shape of our Boka and with the ZD focus node we can add in our own custom  texture to use as our Bokishin.  Right here I've included this kernel texture which you can get included in the Unreal  to Nuke Masterclass.  I'm just blurring it out slightly and plugging it into our ZD focus node.  Now the last trick here so that we get this vertical thinned out anamorphic lens is  I'm changing the filter type from disk which is our default spherical shape over to image.  Then just select input channels and now we're using that RGB image as our anamorphic Boka.  But one other node you should know is the convolve node.  This is really similar to ZD focus where it's going to let us use a filter input and  an image input at a transform into our kernel node and let's scale this down to a really  small number.  Now we can start to see that anamorphic shape appearing across our entire image.  Now basically what's happening here is for every pixel in our scene it's taking that  filter image and applying that onto every single pixel.  So you ZD focus whenever you can but use the convolve node if you ever need to cheat  your depth of field and get a specific Boka shape for your final image.  Now don't worry all of these techniques can be applied inside of After Effects but if  you want to work at Visual Effects Studios and you want the skills to be job ready in  just one day I'll take you from a complete beginner inside of Nuke to compositing your  shots with confidence.  Join the Unreal to Nuke Masterclass at unrealforbffx.com slash Nuke and get started today.  You'll get the tools templates to transform your CG renders so they look like your favorite

**Frame:** tutorials\frames\improve-your-vfx-with-lens-flares-anamorphic-tutorial\frame_004.jpg

### Creating Anamorphic Lens Flares [5:35]
**Transcript:** Hollywood films.  Let's check out some footage with real anamorphic lenses and see how they work.  So I created this simple scene to test out an anamorphic lens and you can see that all  of the flaring comes from when the light source is pointing directly at the camera.  Now these lens flares are huge and the closer that light source gets to your camera the  larger your flares are going to be.  Now there's also several lens flares and artifacts that are being created here.  We can see around our light source we have this wide streak that goes laterally across  the entire frame.  We also have these spikes coming from the light source but we also have these other lens  flares that are on the opposite side of our light source.  The movement of these artifacts are perfectly inverted from the original light source.  Another way to think about this is if you just rotated your image 180 degrees you would  get the same exact movement of these additional lens flares.  Now remember this because it's going to come in handy later.  Lastly something to notice here is that even though this light source is behind little  Godzilla you can see that the lens flare is actually layered on top.  Now how does this work?  As light is traveling into your camera the very last thing light travels through is the  camera lens itself.  That means that your lens flares aren't going to be far away in the background they're  literally happening at the point closest to the camera happening inside the lens itself.  So that's why lens flares are always the last thing to add into your shot.  What's so special about an anamorphic lens?  So the biggest difference is that there's usually some additional layers of glass inside

**Frame:** tutorials\frames\improve-your-vfx-with-lens-flares-anamorphic-tutorial\frame_005.jpg

### Spherical vs Anamorphic Flares [7:30]
**Transcript:** an anamorphic lens.  This gives light more opportunity to bounce around and create these random artifacts so  when we're going to upgrade our CG renders we want to think how can we add extra randomness  and take some of this real life footage and apply it to our CG renders.  Now let's look at Ready Player One which is a completely CG movie but they're recreating  the anamorphic look in every single shot.  You can see all of the attention to detail that the compositor took here to add in that  anamorphic look.  If you pause on any frame here you'll see that there's anamorphic artifacts across  this entire shot.  Blue flares streaking across the background but they're also coming from all these different  headlights.  Having these pop in and out as soon as an actor covers them we're recreating that look  of a real anamorphic lens.  And now they're making them brighter, darker and scaling them in and out to add little  moments of character coming from this camera lens.  You can see in a shot like this how all of the detail comes together to create a lot  of depth and movement across this entire shot.  It's really important to know that lights will only flare out when they're pointed directly  at a camera lens.  If they're pointed somewhere else or the camera rotates in a different direction that  lens flare will go away.  Let's dive in and show you exactly how you can recreate this exact look in your own

**Frame:** tutorials\frames\improve-your-vfx-with-lens-flares-anamorphic-tutorial\frame_006.jpg

### Download my Lens Flares + Comp in Nuke [9:03]
**Transcript:** renders.  I've actually included a free mini pack of anamorphic layers and footage.  You can download that and apply it to your own renders.  The first thing I like to do is find the footage and then create a frame hold node or just  hold a single frame and look at what sort of texture and detail I want to add into my  final shot.  Ideally, you'll grab footage from one camera lens and use it across your entire sequence.  All we have to do is create a merge node and put our lens flare over our background.  But more importantly, we want to change our operation from over to plus because all light  is additive.  All you need to do is create a new crop node and set your softness to something like  100.  Now we can move this around our scene or even animate the transformation throughout the  duration of our shot.  These flares are not monochromatic.  They're not a single color.  There are multiple colors within each artifact that's inside the lens.  Some are orange, some are blue, and some are shifting colors between the red, green,  and blue channel.  And this is why it's so important to really analyze real life footage.  We want to recreate the look and the color of real life footage just like this.  We could also change the hue to tint our lens flare to the color we want.  In this case, I really like that blue and green look of this original lens flare.  So it's really easy to add it on top.  If you just add a single still frame on top of your background, it's not going to look  very believable.  So to keep things simple, I like to add two keyframes to the transformation track.  Set one at our first frame and we'll move this towards the bottom of our frame.  We get a lot more depth and parallax and it starts to feel like that lens flare and light  source is in front of Mr. Freeze.  Another technique, if you've exported your 3D camera from Unreal into Nuke, we can simply

**Frame:** tutorials\frames\improve-your-vfx-with-lens-flares-anamorphic-tutorial\frame_007.jpg

### 3D Lens Flares using Nuke [10:46]
**Transcript:** paste that into our scene.  Now, I'm going to use a node called an image plane to plug in to our crop node.  And we're going to set this to a really low distance.

**Frame:** tutorials\frames\improve-your-vfx-with-lens-flares-anamorphic-tutorial\frame_008.jpg

### Create Lens Flares Automatically [11:00]
**Transcript:** You can see that by changing the distance of our image plane, we're moving a card further  or closer to our camera, a real 3D card in 3D space that's working correctly in our shot.  Now we can preview this scene and dynamically change the location and position of this  real life lens flare right here inside of Nuke.  As a last step, it's nice to add a fade in and fade out animation to add a little more  movement and randomness to this shot and take a look.  And there we go, just like that, with a couple clicks, we already have a very believable  lens flare in our 3D scene.  But it might be a little painful and annoying if we have to go in and hand track or hand  place every flare in 3D space.  So what if there was a more automatic way to immediately apply an anamorphic filter to  your entire shot and it'll take care of all that work for you?  Well that's the exact question I was asking back in the day when I was working on X-Men  Dark Phoenix.  The first shot I was assigned was this shot of Storm.  You can see there's lightning bolts shooting out of her fingers and everywhere.

**Frame:** tutorials\frames\improve-your-vfx-with-lens-flares-anamorphic-tutorial\frame_009.jpg

### How I added Lens Flares to X:Men Dark Phoenix [12:03]
**Transcript:** Obviously, it's just begging to have some lens flares added into this shot.  So I went out and took a look at what are the other movies out there that have done  a similar effect and how do they make it look completely photoreal.  I ended up looking at this behind the scenes breakdown of Spider-Man 2.  Seeing Electro, even if you don't love the character design because it's quite a bit  different from the comics, just focus in here on the anamorphic techniques that they're  applying to these shots.  You'll see that shooting out of Electro's fingers are all of these strands of lighting  bolts and you can see all of these beautiful flares coming off of each lightening bolt.  Now this didn't look like they had used some pre-existing footage so I realized right  then and there that they were using a technique with the convolved node inside of new.  Using the convolved node, I was able to generate these anamorphic lens flares without tracking  a single thing without using a 3D camera.  This was just generated using the original CG render and nothing else.  So let's dive in and show you how.  Now if you remember how the convolved node works is that it's going to take every pixel  in your scene and apply a texture to that pixel.  So the brighter the pixels are, originally more your custom image will stand out.  So the way we'll use the convolved node here is we're going to take this image of a lens  flair and for every pixel in our Unreal render, we're going to apply this image.  The really important thing here is I've created a keyer node and I'm keying out the highlights.  Then by pre-multiplying it, I'm basically getting rid of everything that's not the brightest  lights in the scene.  This will make it a lot easier to isolate our lights and because this is the only thing  inside of our scene when we go to convolve this original light, we'll get a really crisp  and clear result with the final lens flares matching our original footage.  Now because we're using the convolved node, we don't need to track anything, it's just  going to analyze our footage and whether the brightest pixels are, it's going to add  that lens flair texture to it.  Now this is an excellent start, but there's a couple steps we can take to push this even  further.

**Frame:** tutorials\frames\improve-your-vfx-with-lens-flares-anamorphic-tutorial\frame_010.jpg

### Take Your Lens Flares to the Next Level [14:10]
**Transcript:** Using the spot flair node from New Capitia, we can squash this lens flair down, we can  clamp out the brightest highlights and I've just added a little line going through this  to give us more texture so this element becomes more visible and contrasty in our final  scene and combining it with just the highlights in our scene, just the headlights from our  two tanks and convolving the two together to get even more detail.  And just like that, we've added another element to this anamorphic flair.  But let's keep going.  If we wanted to add another streak onto this shot, but create more depth and parallax,  all we would have to do is take our original highlights and just the headlights and scaling  it up to a value of four.  Now this is going to take all of the motion of our original light sources, like the headlights  of this tank.  But by scaling this up before the convolve, we can create a secondary lens flair that  adds another level of parallax and movement, but it's all driven by that original play.  Another thing we can do is add the inverse motion to another lens orb and that'll help improve  this anamorphic look.  Here you can see the inverse motion on the bottom of this screen.  Now it's tracking and moving based on the position of this camera, but it's flipped  to the entire opposite side of this screen.  So to recreate this in nuke, all we have to do is create a transform node and rotate  this by 180 degrees.  And now if we use this and key, just the brightest areas of this footage, I'm just grabbing  another lens texture and using that as the image for this convolve.  And now we can see we have a basic setup where we've taken that original lens flair and  rotated it to the opposite side.  But let's keep modifying this and build this out.  Because the best way to do this is to build multiple layers of these different lens effects  to build out your final lens flair.  By adding in several layers of these different convolves at different scales and depths, we  can really customize the look of our fake anamorphic lens.  So as one last step, you can add a transform and scale the width down to 0.5 on any of these  elements.  If you want to transform them from a spherical shape into an anamorphic shape, by squashing  that original texture before convolving it, we'll end up modifying the look and create  a final anamorphic lens flair.  Now you have the techniques.  Now you know how to add depth of field and lens flares into your own shots and make them  look perfectly photo real.  But if you want to continue and take your shots even further and upgrade and improve your  CG renders and you'll want to know about the Unreal Tanook Masterclass.

**Frame:** tutorials\frames\improve-your-vfx-with-lens-flares-anamorphic-tutorial\frame_011.jpg

### Master Nuke in a Single Day [16:45]
**Transcript:** You'll go from a complete beginner in Nuke to transforming your renders to that Hollywood  visual effects look all in a single day.  We'll walk you through everything you need to know to take advantage of Unreal and Nuke  and use both of their strengths together.  This is every template, every technique and every cheat sheet that I've created to give  you the complete Unreal Tanook workflow in just a single day.  I streamlined the entire process so you can dramatically improve your skill set and freelance  work using Unreal.  You can skip through all of the trial and error and use all of my personal workflows and  frameworks to match the looks of your favorite Hollywood films.  It should take six months or a year to level up your skills and Unreal.  You can learn everything in just a single day.  So if you're ready to level up your renders and get the skills to be job ready at a  visual effects studio, enjoy me and the Unreal Tanook Masterclass and go to Unreal for  VFX.com slash Nuke and get started today.  Otherwise subscribe to the channel.  Thanks for watching and I'll see you next time.  Peace.

**Frame:** tutorials\frames\improve-your-vfx-with-lens-flares-anamorphic-tutorial\frame_012.jpg


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
