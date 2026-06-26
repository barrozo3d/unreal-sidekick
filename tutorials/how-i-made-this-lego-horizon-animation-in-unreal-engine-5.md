---
title: How I Made this LEGO Horizon animation in Unreal Engine 5
source: YouTube
url: https://www.youtube.com/watch?v=AomczYcvBYM
author: Josh Toonen
ingested: 2026-06-23
ue_version: "UE5"
tags: [animation, stop-motion, production-breakdown, lighting, control-rig, sequencer, crowd, cinematics, lego]
extraction_status: complete
frames_dir: tutorials/frames/how-i-made-this-lego-horizon-animation-in-unreal-engine-5/
frame_count: 15
---

# How I Made this LEGO Horizon animation in Unreal Engine 5

**Source:** [YouTube](https://www.youtube.com/watch?v=AomczYcvBYM)
**Author:** Josh Toonen
**Duration:** 23m26s | 15 section(s)

---

## Raw Data (for Claude Code extraction)


### We're animating the theme song for LEGO Horizon Adventures [0:00]
**Transcript:** If you grew up building LEGO sets like I did, then I know you've had the thought.  Wouldn't it be crazy to make my own LEGO animated film?  Well, last year that dream came true. When I got the call to make this animation for LEGO Horizon Adventure's theme song.  Combining the world of Horizon with the world of LEGO.  And I want to take you behind the scenes, showing you every step along the way.  And I'll share the exact production roadmap you can follow to make your own animated films yourself.  What's up? My name's Josh Tunin. I'm a director.  And for the last nine years, I've worked as a visual effects artist and supervisor working on movies like Star Wars Rise of Skywalker, Dungeons & Dragons, and Across the Spideyverse.  But I started out just like you as a self-taught visual effects artist learning right here on YouTube.  Bideverse was my first feature animated film. And ever since, I've been obsessed with making my own fully animated short films with Unreal Engine.  In fact, the first time I used Unreal Engine at a real visual effects studio was back in 2022 when I joined Pixamundo.  The Academy Award winning visual effects studio behind the Game of Thrones dragons.  But this time, I was working on set, offering the LED volume for TV shows like Star Trek Discovery.  All powered by Unreal Engine. And I started to realize how powerful this could be to make animated films with a fraction of the time and budget.  And that leads us to where this LEGO project got started.

**Frame:** tutorials\frames\how-i-made-this-lego-horizon-animation-in-unreal-engine-5\frame_000.jpg

### How this project got started [1:11]
**Transcript:** October of last year, I got word from Pixamundo asking if I could help direct and supervisor project for the next LEGO video game.  LEGO Horizon Adventures. Combining the incredible world of Horizon, or you play as A-Loy hunting machines across the vast wasteland,  but LEGO Bide into a fun couch co-op experience. And honestly, LEGO Horizon is one of the most stunning LEGO games ever created.  And the coolest part is this game was made using Unreal Engine 5, which means we could share all the assets directly from the game to make sure our animation  shared the same exact world.  So it's official. We're making the theme song to LEGO Horizon Adventures title post post apocalyptic dance party, written by MXM2.  So this stage, everything starts with the concept. What are the goals we're trying to accomplish in this piece?

**Frame:** tutorials\frames\how-i-made-this-lego-horizon-animation-in-unreal-engine-5\frame_001.jpg

### Inspiration + Concept [1:56]
**Transcript:** Well, first off, we need to show off the gameplay, the fun action-packed combat, where every arrow knocks off another destructible LEGO brick as you destroy a machine.  You also need to show off the world of Horizon, full of lush, overgrown jungles, Arctic forests, and environments from the actual game.  Plus, we need to show off the machines. These are the awesome mechanical dinos that you'll only find in Horizon,  like the Tallneck walking through the jungle and Thunderjaw, one of the unforgettable boss fights from your original game.  It makes it feel deadly and dangerous. But most important of all, we need to make it LEGO.  So to me, that means recreating that stop-motion look.  Awesome!  And no cheating, no bending or warping things around just to make it convenient.  Everything you see should be possible in real life.  That also means real world scale and imperfections, like fingerprints on the faces and adding details that you'll only see up close.  Now, the LEGO movie did a lot of things right, and success leaves clues.  After going through the movie and taking a ton of screenshots, you'll immediately notice how careful they are to imitate photo realism,  using anamorphic lenses and tons of bounce lighting.  The LEGO Batman movie really built on top of this by adding in more lens flares and fog and volume metrics.  All the things you'd see on a stage or on a real film set.  I was also pulling stills and videos of EDM concerts to see how we can make this party feel alive  and build a stadium where everyone from the village is coming together.

**Frame:** tutorials\frames\how-i-made-this-lego-horizon-animation-in-unreal-engine-5\frame_002.jpg

### The First Pitch [3:22]
**Transcript:** So let's talk about the first pitch. This is actually done by Simon Rizzo, the art director on this project.  He first developed this idea to kickstart it and get everything off the ground.  And there were two things that the clients had reviewed and approved already.  He already had an approved design for MXMTunes mini-figure.  And we had a first pass of concept frames that the client had some feedback on.  It starts off with Maya or MXMTune building out her LEGO sets on the couch  before a portal opens and she swept off into the world of horizon and they have a dance party.  Now, the clients bought off on the concept overall, but they had one big note,  which was instead of building this in a coliseum, let's do this in the home world of the game,  Now I was brought on after this first pitch, but it was super helpful to have a few of these  things locked down already. This project was unique because there were so many approvals between  Sony, MXMTune, LEGO and Gorilla, the studio behind the horizon franchise.  So the character designs locked, they sent over the 3D models of Mother's Heart,  so Simon could build on top of it and transform it into our dance arena.  Now all these concepts were an amazing start and painted a clear picture of MXMTune  dropping into this new world. But the reality is we can't just have a dance party  for 3 minutes straight. So the critical question I need to answer is what's the story?

**Frame:** tutorials\frames\how-i-made-this-lego-horizon-animation-in-unreal-engine-5\frame_003.jpg

### Writing the Story [4:34]
**Transcript:** If you want to write a story, your audience actually cares about and your characters need to go  through these 3 stages. Desire, conflict and transformation. Desire starts with what does our  character want, we need to spell it out for our audience. In our case, Maya wants to build back the  world and invite everyone to the party. But step number 2 is conflict, what's getting in their way.  And that's the fighting between the villagers and the machines, fighting it out for territory.  Now the transformation happens after being invited to the party, they put their differences aside  and they can all dance together as one united village. So now with a rough framework of the story,  I had to come back to reality and figure out the schedule. Now there were some critical deadlines

**Frame:** tutorials\frames\how-i-made-this-lego-horizon-animation-in-unreal-engine-5\frame_004.jpg

### The Production Schedule [5:12]
**Transcript:** that were going to keep us off the treadmill the entire time during this project.  And thanks to Powerhouse producer Linda and our project manager, Dugu, we were able to map out  the entire project before things got crazy to make sure we could hit all of our deadlines in time.  Now our first delivery was going to be for CES, a trade show down to Las Vegas. Sony's putting  a booth together to promote the game and collaboration with the event landing on January 7th.  Now the reality is we need it done before then, so for us, that meant we need to finish everything  before Christmas break. Before everyone went on their vacations and holidays because I don't want  to cut anyone's vacation short. And for this deadline, we would need one minute of fully polished  animation. Then the second delivery for the full theme song would be on February 28th.  That means two minutes of extra animation built out along with animated crowds,  all the characters, and globe-trouting across multiple locations, and our shots of the portal  at the beginning and end. So we're already fighting against the clock, but to make things even  harder, we have our live action shoot in just two weeks. And the second problem is we don't have  any animators, so I'll have to crew up this team from scratch. So this gave us two weeks to prep

**Frame:** tutorials\frames\how-i-made-this-lego-horizon-animation-in-unreal-engine-5\frame_005.jpg

### Creating the Storyboards [6:20]
**Transcript:** for the live action shoot and two weeks to finish at first pass of the storyboards.  This is crucial because the storyboard is where you actually make your film and tell your story.  Your storyboard doesn't work, all that fancy lighting and animation won't save it.  Now typically, I like to start by writing out a shot list in a word doc, but this time I tried a new  technique that you might find helpful. Because we already had the song available, I just went into  Premiere, which I used for editing, and started writing out my shots to the beat of the music.  This way I could imagine any location, any setup, like a wide medium or close-up, and  start sketching out sequences and ideas fast to the beat of the song. Then, instead of sketching  out storyboards on paper, for me it's way faster and easier to create screenshots and unreal,  using our LEGO mini figure of MXM2. This way I can try out so many ideas and camera angles  all in real time. And this part is super fun and inspiring, and I prefer to start with screenshots  instead of animating my cameras because I can take 10 screenshots in the time it takes me to  animate one single camera. So every day I'm trying to create as many shots as possible.  This is the fun part when you're actually creating your film, and quickly trying out lighting  combinations and moving the environment around to make the perfect shot. We were able to share  those same 3d models between LEGO Horizon Adventures and our own project. This way we could get 3d  models from the actual game and tear them apart to build our own modular pieces and create our  shots just like we're playing with real LEGO sets. And this was great because we could start off  with our hero characters, Aloy and Varro. Plus we knew we'd have a gigantic crowd of villagers,  so we recreated over 20 characters in total. We also had access to the buildings and ruins,  like watchtowers, billboards, skyscrapers, ivy, broken down cars, you name it. This gave us a huge  head start on the environment. But the fun would be cut a little short because with the tight  deadlines there was no room for error. The number one saying on the show is the only thing we need to  do to get to the finish line is never stop. If we don't stop we're gonna make it. This brings us to

**Frame:** tutorials\frames\how-i-made-this-lego-horizon-animation-in-unreal-engine-5\frame_006.jpg

### The Live Action shoot [8:18]
**Transcript:** the live action shoot. We're gonna start an end with Maya or MXMTune building and playing with the  newly released LEGO Horizon Adventures set, where you can build the machines from the game,  featuring Sawtooth, a shell walker, along with Varro and Aloy herself. Now the location had to be  in LA because that's where MXMTune and Sony were based and available, and to make sure that everything  was done in time we worked with Blue Hour Labs to assemble the on-set crew. For the location we had  a few options for rentals and I want to make sure we had a place that felt like home, with lots of  greenery and plants to match the vibe of the game. But in the end for practical reasons we ended up  at a spot about 20 minutes away from the Sony lot. But to be honest I was a bit nervous about all the  white walls and the couch and everything just looking a little bit too clean. But thankfully we had  some great options from Daniella in the art department, sent over a lookbook that's exactly what  we needed, along with plants, some guitars and small details that made it feel like home for Maya.  So I flew out to LA for two days, the pre-light and the shoot day. In the meantime we already started  lining up interviews for animators so that first morning while I was down there I had a call with  Joe Bonilla. He was an animator in town and it turns out his first film he ever made was a LEGO  stop-motion movie. His real was great and it seemed like a really good fit. But before I knew it I was  already late for the pre-light so I rushed down to the location to check it out in person.  Mitch Mullins helped step up to direct the live action portion and came loaded with ideas,  along with Ben Miserp who was the DP. They did a great job of making this living room feel  bright, warm and lived in. Our pre-light day allowed us to go through every single shot set up  and see it through the real camera lens. We're even experimenting with a pro lens to make these  LEGO mini figures feel huge and it turned into a really great close-up of A-Loy before we see  her for the first time in the game. So after running through each setup everything was locked and  ready for the next day so we can breeze through our entire shot list once everyone had arrived on set.  And for once we had plenty of time and we're actually out of schedule.  So at the end of the shoot day I left with a footage in hand ready to start the edit and animation.

**Frame:** tutorials\frames\how-i-made-this-lego-horizon-animation-in-unreal-engine-5\frame_007.jpg

### Building the Environments [10:23]
**Transcript:** So after the shoot I checked in on our progress on the environments. By now Simon was nearly done  with recreating Mother's Heart from the game and transforming it into our Dancerina.  Now we started building this during the daytime but we needed to throw party so I knew this would  look awesome by turning off the lights and making a moonlight look. Now we can create foggy stage  lighting with an interactive dance floor that glows yellow as characters jump up and down.  As it was being developed I'd continue on building storyboards and this really helped to design  the color palette and all the camera angles for the dance scenes at night. There were two main  spotlights that were blue and pink and poured color into our scene and we added torches in the  background to add orange and red and we had the yellow interactive light coming from underneath  the dance floor. Then to get the stadium working we had to scatter and animate this entire crowd  of 300 characters. Then to really finish this off we added confetti to add pops of color and make  it feel like a party. Now this is a great start and it came together really fast but I thought it was  just as important to show off the gigantic world of horizon. Part of the game is hunting through  the jungle, zip lining between majestic nature and ruins and in the game machines are running wild  fighting against the villagers for territory. So our opening shot had to establish and showcase  all the unique elements of horizon with overgrown post-apocalyptic terrain and the gang skyscrapers  with machines overtaking the world and whenever I think of horizon my mind immediately jumps to the  tall mac. I love this design and we were able to use the real character from the game so it fit  right in. Another important lesson is design through the camera lens. You only need to build  what the camera sees if you're making a film instead of making a game. So most of the time we're  only building through the camera and it's completely empty to the left and right of frame.  We also added rotation to the leaves on all the trees and falling leaves that are blowing in the wind.  We also added in the torch and added that random rotation so it gave it the stop motion look.  And all these elements are animated at different frame rates. We kept expanding the world by  climbing buildings and leaping across cliffs and we built these cool stop motion waterfalls made  by Mufi, a tech artist on the team. All based off the amazing details Gorilla built into the  original game. Mufi also built out the interactive floor so that we wouldn't have to animate anything  by hand. They're all driven by blueprints. And in just a few days we were able to build out our  version of the environments and everything was starting to shape up. But now it's time to focus on

**Frame:** tutorials\frames\how-i-made-this-lego-horizon-animation-in-unreal-engine-5\frame_008.jpg

### Animating the Characters [12:45]
**Transcript:** the animation. Now even though we're animating LEGO characters the animation is not going to be easy  because we have not one, not two, but three hero characters that we need in this film animated in  every shot. That's not including the giant machines and crowds of dancing villagers.  And by the time I added the first draft to my storyboard ready we already had 70 shots in the final  edit. So I needed a team of unstoppable animators to bring this to life and we had three animators  up for the challenge. In animation your animators are your actors so if you want to get the right  performance you need to cast the right animators for each shot. The first was Jo Bonilla. We finally  pulled the trigger and brought him onto the team. Joe's demo reel had some really strong performances so  we gave a lot of the dancing shots to him. Second was Nicole Herb, an industry veteran and animation  mentor who has worked on more movies than you can count. And Nicole was our mercenary. We can  hand her any shot and she can tackle it no problem. And finally Nav Singh, who is on the visual  effects team at Piximundo. He has loads of experience in traditional visual effects and a  pretty cool YouTube channel that I'll link below. Nav has a background working on dragons and creatures  so he gave all the shots of the machines to him. But this was his first time ever using Unreal  Engine. But he was ready to learn and that's all I needed to hear. Now the biggest animation  challenges were first creating the stop motion look which in most cases meant putting limitations  on our own work. We would limit the frame rate and limit our poses to only what could happen with  a real minifigure. But that didn't stop us from making huge over the top poses. We want to cheat  gravity and exaggerate all their motion to make it feel as over the top as possible. Another thing  that helped was making sure everyone was a little bit off balance. Everyone's rocking left and  right like they're about to fall over and this added some really great energy to all the characters.  Whenever possible we'd also try to lower our frame rate, animating it 12 frames per second instead  of 24 frames per second. And sometimes completely freezing poses in midair. Now our camera was always  rendering out at 24 frames per second but we'd adjust our characters to make them slower and make  the coolest shot possible. This also meant no motion blur or it wouldn't look stop motion. And the  last challenge was going to be showing off all this action without anything feeling too violent  because it is a family game after all. Now I am not a character animator myself so my main job is  to communicate. This is done through review sessions called daily's where we review work every single  day sometimes twice a day. Animation can sometimes feel like you're working in slow motion. So it's  super important to give feedback to make sure we're all working towards the same goal. Sometimes I'll  just draw on top of the final renders or we'll shoot live action reference of ourselves trying to  dance along and find out the right pace and rhythm to all of our dances. For this entire project  every one of us had a real Lego mini figure next to our desk because in every shot we were looking  for the most interesting pose possible. If something doesn't feel right we go straight to a real life  mini figure to understand why and come up with a new idea. Now the way I like to work is to build  everything inside of Unreal 5 which means every character and every animation was created inside  of sequencer and control rig. And after a few weeks of experimenting we started to find some  nice rhythm and dance moves that worked on these Lego mini fix. But what really took into the next  level was adding facial animation. Mufid was our one man army on the project and he built out a  custom face rig for all of our characters so we could adjust and animate expressions inside of  sequencer. And this was that missing ingredient that made all our characters feel alive. We found that  hand drawn expressions looked the best with these big goofy smiles. Try to get that hand drawn feel  any opportunity that we add. And by adding blinks and squinting between all these different dance moves  everything started to really come together. Next let's talk about animating the creatures.

**Frame:** tutorials\frames\how-i-made-this-lego-horizon-animation-in-unreal-engine-5\frame_009.jpg

### Animating the Machines [16:32]
**Transcript:** Now one of the first enemies you face in Lego Horizon Ventures are the watchers. Because of their  size I was thinking it'd be really fun to have MXM tune running and rebuild him and bring him back  to life. This would be her first of many friends along the way that would follow her along for the  party. So to make this work we built out a custom control rig so we could pose and animate him on  the fly and even dance along with Aloy and Maya out on the dance floor. But we also had the big  machines like Thunderjaw and Sawtooth. Now a huge advantage of working directly with Gorilla  was starting from the creature animations they used in the game. I thought it'd be hilarious to end  this piece with Thunderjaw this giant T-Rex hardening on the dance floor. And we knew we'd only have  Thunderjaw in here for a few shots. So I want to find out if we could repurpose the existing  animation clips and invent a new dance move out of these instead of making something from scratch  which would require us to make a brand new rig. I was able to combine multiple clips together  and use the motion blending tools to make new dance moves out of the existing attack animations.  Then by using additive tracks we can manipulate and adjust the animation to get the perfect pose  through the camera lens. I also added the audio and music into sequencer and that way I could  assemble the clips to the beat of the music. And using these two methods we were able to animate  everything inside of Unreal. Next let's talk about lighting. In this case the mission was simple.

**Frame:** tutorials\frames\how-i-made-this-lego-horizon-animation-in-unreal-engine-5\frame_010.jpg

### Stylized Lighting in Unreal 5 [17:48]
**Transcript:** I love the expression every frame of painting but in our case every frame should look like the  cover art for the next Horizon Adventures Lego set. Bright, clear, colorful and characters popping  off the background. The only difference is we're using a better cinema quality lens and we'll use  all the tricks you'll find out of film set like fog, atmosphere and animating our lights.  But whenever possible I love shooting my own reference footage to see how light reacts with  my own eyes. And that's exactly what I did with the Lego Tall Necks set. Now people always look at  me like I'm crazy when I tell them this but I always prefer to light something in real life even  if it's just toys and action figures to see how the services could react. But this was perfect  because now I have the real prop to study anytime. The whole point is to try out ideas in lighting  combinations to find something new. So I threw in some colored LED lights and light tubes behind  and change the color and intensity to find looks and color combinations that you'd find in a dance  party. And this is also when I realized just how reflective these Lego pieces are. Every plastic  brick is super shiny and reflective and we need to replicate that in our version too. Plus we could  create these colorful reflections as rim lights around our characters. So now I can see exactly what  the footage should look like through a real camera lens. But you want to know our biggest mistake  when lighting these tiny characters. When placing lights most people are focused on the position  or the color or intensity but there's a missing ingredient that changes everything about your lights  and that's the size of the light. And real life these mini figures are tiny so most lights are  going to be huge by comparison. So when lighting this and on real we need to exaggerate the size of  the lights and it helps to boost the bounce lighting because it makes the whole world feel smaller.  For the nighttime dance sequence I let this along with Salva Gomez and Simon and we face every  challenge on this sequence. Especially maintaining the blue, purple and yellow color palette across  a series of shots like this. We also had to animate the stage lights and spot lights to add extra  energy and bounce to the scene. Plus we needed to balance the fog and keep our hero characters  clean when they're close up to the camera and make sure everyone else falls into the background.  Then we'd animate the speakers and the background characters and have confetti raining down from  the sky. And then to finish off each shot I'd add my one click compositing template and a  pass of lens flares. For the daytime scenes we were able to study the live action footage that we  shot on set. And you can see how the mini figures and LEGO bricks react to the sunlight in real life.  And frankly, LEGO Horizon Adventures is one of the best looking LEGO games out there. So we were  constantly studying the gameplay and just trying to recreate that amazing world and look that they  built. And then 30 shots later that got us all the way through our first delivery on Christmas Eve  to get everything in before CES. After some last minute changes we got everything approved and  writing the showcase on the CES stage floor. And before we knew it CES was underway. There's an

**Frame:** tutorials\frames\how-i-made-this-lego-horizon-animation-in-unreal-engine-5\frame_011.jpg

### The First Delivery for CES [20:43]
**Transcript:** incredible booth that showed off the collaboration between Sony, Gorilla and LEGO for Horizon Adventures.  It was super cool and they brought out a live action a-loy hunting down a watcher right there for the  crowd. But our job was not over yet. After this big push we had to go back and finish the entire  theme which had two minutes of animation left. And at this point the problems were just beginning.  While we were scheduling out the next two months we also had a key team member leave in the middle  of production. This is the stage I like to call the murky middle and it happens in every single film  and visual effects project. You spend all this time, months of effort and the film still isn't good  yet. So just remember, trust the process and if you need to find something new to get excited about.  Even when you're feeling behind and things are going to plan, the only way you can fail is if you  stop. But the good news is now we had more time to develop the action scenes and flesh out the story.

**Frame:** tutorials\frames\how-i-made-this-lego-horizon-animation-in-unreal-engine-5\frame_012.jpg

### Designing the Action Scenes [21:32]
**Transcript:** First let's look at our bow and arrow sequels. As I said I'm trying to recreate moments from the  game so we start by ziplining down the mountain and using the focus to highlight the enemies.  At first all she sees is a watcher before we see a sawtooth lurking behind her and Varyl.  So we built this action scene around Maya taking down sawtooth and saving the day.  I also wanted to show off more of the environments in Vistas. This is one of my favorite aspects of  Horizon Zero Dawn and it's the incredible landscapes you'd only find right here. We knew this would end  if I invited Thunderjaw after visiting his cave but we got to stop for a moment and overlook  the mountain's opportunity. As the story changed we actually ended up making two versions of this shot.  One for our CES version and one for the final animation. And then we get to the entrance of Thunderjaw's

**Frame:** tutorials\frames\how-i-made-this-lego-horizon-animation-in-unreal-engine-5\frame_013.jpg

### Thunderjaw's Cave [22:19]
**Transcript:** cave. This is the final boss fight in the game so we had to make it special and we really  wanted to respect this arena from the game itself. Thanks to Gorilla we were able to start from  the same geometry and we just pushed the fog and atmospheric even further. Adding in smoke and  exhaust to make it feel dangerous until Maya faces off with Thunderjaw himself. But instead of  shooting him down we'll invite him to the party. And both villagers and machines come together  to celebrate at the end. We ended the short by finishing off these portal shots connecting our  real world to our Lego world. Saying goodbye after reuniting the world of Horizon.

**Frame:** tutorials\frames\how-i-made-this-lego-horizon-animation-in-unreal-engine-5\frame_014.jpg


---

## Structured Notes

### Core Technique
Professional animated short for LEGO Horizon Adventures (Sony/LEGO/Gorilla) made in UE5: stop-motion look via 12fps character animation + no motion blur + frozen midair poses; custom face rig with hand-drawn expressions; environment built only through camera; creature animation via game clip blending + additive tracks; 300-character crowd; lighting referenced from real LEGO sets with physical LED rigs; storyboards as UE5 screenshots to music in Premiere.

### Summary
Josh Toonen directs the official LEGO Horizon Adventures theme song animation (Pixomundo/Sony). Complete end-to-end production breakdown: concept approval → storyboards as UE5 screenshots synced to song in Premiere (10× faster than animating cameras) → live action shoot with MXMTune → environment build from game assets (Gorilla-provided) → 3 animators using Control Rig/Sequencer → creature animation from existing game clips blended into dance moves → one-click compositing + lens flares. Stop-motion look: 12fps, no motion blur, frozen poses, physical minifigure at every desk. Lighting key: huge light sizes relative to tiny figures, boosted bounce, physically referenced with real LEGO + LED rigs. Blueprint-driven interactive dance floor; stop-motion waterfall; 300+ crowd; confetti. Additive tracks used to adjust creature animation per shot in camera.

### Key Steps

**Pre-production:**
1. Beat-match shot list in Premiere with song audio → write shots at each beat
2. Create storyboards as UE5 screenshots using minifigure + environment → 10 screenshots per animated camera
3. Reference: LEGO movie/Batman for anamorphic look + bounce lighting; EDM concert references for party feel; real LEGO set under LED rigs for lighting study

**Stop-motion animation rules:**
1. Animate at 12fps (keyframe every 2 frames); camera renders at 24fps
2. No motion blur (kills stop-motion look)
3. Freeze poses mid-air — lean into it
4. Slight off-balance: characters always tilted, rocking left/right
5. Physical minifigure on desk at all times — pose reference for every shot
6. Exaggerate motion, cheat gravity, oversized poses within physical joint limits

**Facial animation:**
1. Custom face rig built per character (by tech artist Mufid) → Sequencer-driven
2. Hand-drawn-look expressions: big goofy smiles, squints
3. Add blink poses between dance moves

**Environment:**
1. Import game geometry from Gorilla (direct asset sharing — game also UE5)
2. Build only through camera lens — everything outside frame stays empty
3. Animated leaf rotation + falling leaves via material/blueprint
4. Blueprint-driven interactive dance floor (no manual animation)
5. Stop-motion waterfall via blueprint (Tech artist Mufid)
6. Scatter 300+ crowd characters; animate confetti
7. Fog/atmosphere + animated spotlights for dance arena

**Creature animation:**
1. Start from Gorilla's existing in-game animation clips (walk/attack cycles)
2. Combine multiple clips → motion blending tools → new dance move
3. Additive tracks in Sequencer → adjust per-shot framing
4. Import audio into Sequencer → assemble animation to beat

**Lighting approach:**
1. Use large light sizes (mini figures are tiny → real lights are enormous by comparison)
2. Boost bounce lighting intensity (makes world feel smaller/more LEGO-like)
3. Animate stage spotlights + speakers for dance energy
4. Color palette: blue/pink main spots, orange torches, yellow interactive floor
5. Fog and atmosphere control per shot; hero characters clean close-up, crowd falls into BG

**Compositing:**
1. One-click compositing template per shot
2. Lens flares pass
3. Review daily (sometimes twice/day); draw feedback on frames; live-action dance reference for rhythm

### UE Systems / Blueprints / Settings
- **Control Rig in Sequencer**: all character animation keyed here; used for stop-motion pose work
- **Additive animation tracks**: applied on top of base creature animation to adjust per-shot without baking new clips
- **Motion blending tools**: combine multiple Sequencer animation clips into new motion sequences
- **Blueprint-driven interactive floor**: characters trigger light events underneath dance floor; no manual keyframes
- **Audio in Sequencer**: import song → animate everything to music beat
- **Custom face rig**: built by tech artist per character; Sequencer-driven; enables expression animation without MoCap
- **Asset sharing from game**: UE5 game assets (Gorilla's Horizon) imported directly into separate UE5 project; same asset pipeline ensures visual consistency

### Difficulty
Advanced (professional production, team of 5+)

### UE Version
UE5

### Tags
[animation, stop-motion, production-breakdown, lighting, control-rig, sequencer, crowd, cinematics, lego]

---

## Related Entries
- give-me-14-minutes-and-youll-make-cinematic-renders.md (animated lights + fog cards — same lighting philosophy)
- how-i-made-a-godzilla-cinematic-in-unreal-engine-5.md (same author — fog cards, compositing template)
- how-i-made-this-aaa-battle-scene-in-unreal-engine-5.md (production breakdown with similar crowd/stagger approach)
