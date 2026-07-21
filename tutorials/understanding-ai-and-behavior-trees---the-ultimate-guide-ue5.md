---
title: Understanding AI and Behavior Trees - The Ultimate Guide [UE5]
source: YouTube
url: https://www.youtube.com/watch?v=-hXFCSxAYEI
author: Darklore Creations
ingested: 2026-07-20
ue_version: "Not specified (UE5.x)"
tags: [blueprint, animation, pipeline, advanced, expert]
extraction_status: complete
frames_dir: tutorials/frames/understanding-ai-and-behavior-trees---the-ultimate-guide-ue5/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Understanding AI and Behavior Trees - The Ultimate Guide [UE5]

**Source:** [YouTube](https://www.youtube.com/watch?v=-hXFCSxAYEI)
**Author:** Darklore Creations
**Duration:** 42m20s | 31 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Intro [0:00]
**Transcript (timestamped):**
[0:00] So you wanna make an AI in Unreal Engine? You wanna do the idling, investigating, patrolling and some dynamic combat?
[0:08] Every tutorial is telling you to create these three things, but when you finish it, it's either a part of a long series or series that has long since been abandoned.
[0:17] Welcome to my ultimate guide to AI!
[0:20] Disclaimer, this video expects from its viewers that they understand the basics of Unreal Engine and Blueprints.
[0:25] This video is also a guide, not a tutorial, so you won't see me code everything.
[0:29] Rather, I will show you everything needed to replicate this while explaining to you what it does.
[0:34] So if you want to copy the code, feel free to pause the video and do so.


### Behavior Tree Explanation [0:38]
**Transcript (timestamped):**
[0:39] Let's start with these three things I already showed you.
[0:42] This is an AI controller. All you need to know is that it can start and stop the AI.
[0:46] It also feeds information about AI surroundings to the behavior tree.
[0:51] This is the mentioned behavior tree. It contains a tree of nodes that make the AI's decision making.
[0:57] This last thing is called a blackboard, and it essentially just stores data you need stored for behavior tree's decisions.
[1:03] You can find them like everything else in Unreal. Just right-click and type into the search bar what you want.
[1:10] Before I start actually making the logic, we have to talk about rules.
[1:14] Behavior trees start their logic from top to bottom and from left to right.
[1:18] This rule is on top of all the other rules that each behavior tree node has.
[1:22] The root is where the logic starts.
[1:24] First, if I would want to check if the AI is hostile, I would use selector.
[1:29] You might think selector selects and executes only one thing and you'd be correct, but it's the way it selects you need to know.
[1:36] Selector executes things, but it does so by going from left to right and succeeding if single one executes properly.
[1:45] Sequence on the other hand tries to execute everything in sequence.
[1:49] If either part is not executed properly, everything afterwards won't be executed as well.
[1:55] Simpa Parallel is different, because there is this blue thing we never seen before.
[2:00] These blue things are called task, and for now just accept that they exist.
[2:05] Simpa Parallel can execute this one task alongside a whole tree of options.
[2:10] Also, you can set in details panel if it should immediately abort the secondary tree as task is finished,
[2:16] or if it should wait for the tree to finish as well.
[2:20] Now for the task nodes.
[2:22] Every task is a code just like blueprint that is represented in an action.
[2:26] Everything should end with some kind of task, otherwise the AI can be stuck.
[2:30] Also, tasks should always start with event receive and end with either finish execute or abort.
[2:36] Unreal has a lot of these tasks already coded and you should experiment with them.
[2:41] Decorators are conditions that helps behavior tree with the flow of execution, and they can be attached to anything.
[2:48] They often communicate with blackboard keys to execute what is needed.
[2:52] Unreal again has a nice set of decorators already.
[2:57] Services are the last thing before we can move on.
[3:00] They are like decorators and can be attached to anything, but they are event ticks rather than checks.
[3:05] They are often used to update blackboard keys at runtime.


### Basic Setup [3:10]
**Transcript (timestamped):**
[3:10] Now I know this is a lot of boring information handed to you in a minute, but it will make more sense as I go through my AI example.
[3:17] Before going deeper, I put it up Elden Ring and did some research.
[3:21] At first, you might think its AI is separated into bosses, NPCs and basic enemies.
[3:27] But to me, it all seemed to be built around one well-made universal AI system.
[3:32] That's why I created an actor component called AI component to hold all the core AI data.
[3:38] This makes it much easier to manage and edit AI behavior later on.
[3:43] Then I connected my enemy blueprint with the AI controller.
[3:47] And also with AI component and the AI controller with AI component, through which I start the behavior tree.
[3:55] I tested it and it worked.
[3:57] From here, I could start iterating and testing features as I added them.


### Non-Hostile Setup [4:00]
**Transcript (timestamped):**
[4:02] The AI needed to first check if it was hostile towards the player.
[4:05] So I created a Boolean in the blackboard called Hostile and added two selectors in the behavior tree.
[4:12] To check whether the AI was not hostile, I added a blackboard decorator, set the key to Hostile and set the query to isNotSet.
[4:21] I also enabled a boards so the AI could instantly switch to Hostile whenever the result changed.


### Hit Reaction [4:27]
**Transcript (timestamped):**
[4:28] The non-hostile behavior only had two states, idle, which was just a wait node, and hit reaction, a sequence for when the AI takes damage.
[4:38] To detect when the AI was being hit, I created an interface which allows two different blueprints communicate between each other.
[4:46] In my case, it's player character and AI component.
[4:50] This way, I could send information through a function like who attacked and how much damage was dealt.
[4:56] To add the interface, just go to class settings and add it.
[5:01] I also created an enum containing all AI states I wanted for non-combat phases.
[5:07] Inside the AI component, I received the hit event from interface which is called upon dealing damage in my player blueprint.
[5:15] I also made a handy pure function and then stored the attacking actor in blackboard while changing AI state to hit reaction.
[5:23] And then updated my health bar logic here.
[5:27] In the blackboard, I added two variables, but to get them properly, I had to also click this small arrow to open a menu
[5:34] and set one to actor and the other one to my newly made enum.
[5:39] Back in the behavior tree, I added yet another blackboard decorator to check for hit reaction,
[5:45] which I didn't want to abort because reacting to hit should be a priority, while the idle task should abort whenever AI should react to hit.
[5:55] For the hit reaction itself, I had to create a custom task.
[5:59] Inside it, I added a variable of the type blackboard key and called it attacking actor.
[6:04] Making it editable makes it so I could link it to any blackboard key in my behavior tree.
[6:10] With that, I calculated the angle from which the AI was hit.
[6:14] In Unreal, 0 degrees is forward and 180 or minus 180 degrees is backwards.
[6:21] And the minus sides represents the right, while the positive sides represents the left.
[6:28] I realized I'd need another enum for all hit directions, so I could easily switch between them.
[6:35] Using that enum, I selected the proper hit reaction animation, casted it to the character, played the animation montage
[6:42] and made the task wait until the animation is finished before calling finish execute.
[6:49] For hit animations, I created a map inside the AI component, where the key is direction enum and the values are the animation montages.
[6:58] This lets me easily manage all hit reactions in one place and retrieve them directly into the custom task.
[7:06] The AI should also become hostile when it loses enough health.
[7:10] For that, I created a simple task to change any blackboard boolean.
[7:15] I also created another task to change AI state back to idle and plug both into the hit reaction logic.
[7:24] To control when the AI becomes hostile, I made a custom decorator called health percentage check.


### Custom Decorator [7:25]
**Transcript (timestamped):**
[7:32] Inside the AI component, I added a hostile HP threshold variable with a slider range from 0 to 100.
[7:39] To make a custom decorator check, I had to overwrite perform condition check AI.
[7:45] Then I simply checked if the current health is less than or equal to the HP threshold.
[7:51] Lastly, I attached this decorator to the hostility task in the behavior tree.
[7:56] Now the AI can't execute hostile behavior until its health drops below the threshold.


### Optional Task [8:02]
**Transcript (timestamped):**
[8:02] And to make sure that the task doesn't fail, meaning the whole sequence fails when the conditions are not met,
[8:09] I added a forced success decorator to make the task optional.


### Testing Hit Reaction / Idle [8:14]
**Transcript (timestamped):**
[8:15] With all of this setup, I could finally test if the hit reactions and hostility transition were working correctly.
[8:24] With the non-hostile behavior finished, I moved on to the hostile behavior, specifically the hostile passive state.


### Hostile Passive State Setup [8:25]
**Transcript (timestamped):**
[8:31] This state includes idling, patrolling, investigating and returning to the spawn point.
[8:41] First, I added two new Boolean Blackboard keys for combat state and patrol.
[8:45] Then I copied this to set combat state also to true, because if the player attacks NPC and makes it angry,
[8:52] the NPC should fight back, not just become hostile and do nothing.
[8:56] But it also has to be before NPC becomes hostile, otherwise this would abort and it wouldn't immediately switch to combat.
[9:04] Then I added a selector with the decorator that checks if AI is not in combat state.
[9:09] Inside this selector, I placed another selector specifically for idle and going back to the spawn point,
[9:15] but only if the AI is not currently patrolling or investigating.
[9:21] To make this work, I added a decorator checking patrol state, a decorator for investigation state,
[9:27] so AI will abort this behavior when it should investigate.
[9:30] Lastly, a wait task as a idle and a sequence for returning home.


### Returning to Spawn Point [9:33]
**Transcript (timestamped):**
[9:36] For the return to spawn behavior, I also added two new Blackboard keys for spawn location and spawn rotation.
[9:42] First, the AI needs to rotate towards this spawn point.
[9:45] For that, I used premade task called rotate to Blackboard entry with precision of 1.
[9:51] This might not work properly for you, however.
[9:54] If you don't have disabled in your enemy blueprint, use controller rotation yaw
[9:58] and also enabled use controller desired rotation ink movement component.
[10:04] After AI rotates towards spawn point, it should move back to it.
[10:08] For that, I also used premade task called move to and lastly it should rotate again once it reaches the spot,
[10:15] but now to a spawn rotation.
[10:17] To check whether the AI should be in idle or going back, I had to create a new decorator to check if AI is near specified location.
[10:25] I added an acceptable radius and inverse toggle just for flexibility.
[10:30] You might wonder why I didn't just use Unreal's built-in is-at-location decorator.
[10:35] The reason is simple. It can't abort when the conditions change.


### Updating Blackboard on Start [10:39]
**Transcript (timestamped):**
[10:40] With so many keys being added, I needed a centralized way to manage them.
[10:45] In my AI component, I created a set BlackboardValues custom event where I set the initial values like spawn location, spawn rotation and other key data.
[10:55] This is called in the setup behavior tree event.
[10:59] Now, by simply dragging the AI around in the editor and simulating, you can see it returning to its spawn point.


### Testing Returning to Spawn Point [11:00]
**Transcript (timestamped):**
[11:07] With the idle behavior done, it was time to make the AI patrol.
[11:11] Elden Ring's AI often patrols, so I added three patrol types.


### Patrol [11:16]
**Transcript (timestamped):**
[11:16] One time patrol that follows the route once and then stops patrolling.
[11:20] Loop patrol which follows the route continuously in a loop.
[11:24] And PimpongPetrol that follows the route and then walked back the same way.
[11:30] To set up a patrol route, I created an ActorBloopRind containing just a spline to define patrol path.
[11:36] In the AI component, I added a PetroRoot variable and made it exposed on spawn.
[11:41] I also created an enum for all patrol types.
[11:44] Then I made a findNextPetrolIndex function with four new variables.
[11:50] A private PetroRindex and patrol direction, an editable should wait and wait time variables.
[11:57] These two handle if AI should wait after it finishes patrolling before resuming their journey again.
[12:04] The function switches based on a patrol type and then does the logic for each type.
[12:09] In nutshell, it's incrementing PetroRindex and getting the next location of spline point while also checking if it's not the last spline point.
[12:20] With the logic done, I created a new behavior task for patrol with three blackboard keys.
[12:32] Patrol, point of interest and spawn location. I also added the point of interest as blackboard key.
[12:39] Firstly, I called the newly made function and saved the index location as point of interest.
[12:44] Then I handled the waiting and lastly I checked if it was only one time patrol because for that I wanted to turn off patrolling while also updating the spawn location to where it ended patrolling, just to avoid some bugs.
[12:58] In the behavior tree, I added the patrol task which again just handles the data, nothing else.
[13:03] Then I rotated AI towards the point of interest, which is the next patrol point and lastly with move2, AI moves towards that point.
[13:12] Now this can look forever or go just once based on preferences.


### Investigation [13:16]
**Transcript (timestamped):**
[13:16] Investigation takes highest priority within the passive hostile state, so it goes before idle and patrol, meaning it's left most behavior.
[13:25] In investigation mode, the AI rotates towards the point of interest, moves towards it, waits for like 5 seconds and if nothing happens, returns to idle, meaning it will first return towards spawn point because it's not near spawn location.
[13:40] To make investigation work, I had to open AI controller and add AI perception component.
[13:46] This is how AI gets data about its surroundings and for mine, I added 3 senses, sight, hearing and damage.
[13:53] I don't think I need to explain sight radius, hearing range etc.
[13:58] Because you can hover over it and it will tell you what it is.
[14:01] What I want to point out though is detection by affiliation, which I said to all true in every sense, because I'm not doing group type enemies for this video.
[14:10] What you should also take into consideration is max age, which just says how long will AI remember what it heard or seen or whatever your sense is.
[14:20] To debug AI senses, first go to your project settings and gameplay debugger to see what your activation key is.
[14:26] Now, when you enable it and press 5, you will see based on the colors you selected in the AI perception hearing and sight range with many other stuff like if AI spotted player or when was the player last seen.
[14:39] Using report notes makes AI to actually receive these informations in AI perception.
[14:46] With this data, I can get on perception updated event from AI perception component and for each updated actor, meaning AI heard or saw or was damaged by something, I ran loop and passed the data into 3 functions.
[15:01] Handle damage, sight and hearing.
[15:04] For the damage function, I first got the correct sense and checked if something was actually sensed.
[15:10] If yes, I saved the sense actor to a blackboard actor object named target and checked if AI is hostile.
[15:17] If it was, I naturally wanted it to immediately go to combat state.
[15:21] The site starts the same, but I first checked if save point of interest is different than this new stimulus location while also checking if AI is hostile and if something was actually sensed.
[15:33] Then, I checked if AI is not in combat state already, because if it is, I don't want to do anything.
[15:39] But if it isn't, I saved the new stimuli location as point of interest and then reset investigation state by setting it to idle and immediately to investigation state.
[15:49] This way, if AI is already investigating and hears something new, it will go towards that new sound.
[15:55] Lastly, hearing is the same, but I checked everything that I checked inside at one time together and then I do the same stuff as inside function.
[16:04] Now to make the investigation system work, I created an investigation service in Behaviour Tree.
[16:10] Remember, these are ticks which can update your blackboard keys, but before I could code it, I created a new actor object blackboard key called target and new variable in AI component for agro distance.
[16:23] In the investigation service, I first checked if target is actually valid and then I checked if target is currently being perceived by AI.
[16:32] If it is, I set target's location as new point of interest and afterwards check if target is in agro distance of this particular AI.
[16:42] If it is, I switch immediately to combat state.


### Testing Patrol / Investigation [16:45]
**Transcript (timestamped):**
[16:46] Now I can finally test the passive state of this AI.
[16:49] First, let's see if patrol works.
[16:51] I open my enemy blueprint and select the AI component.
[16:54] Here I enable patrol and set it to circle looping and also it should wait for 3 seconds.
[17:01] Then in the world, I select enemy and scroll down to the AI component in details panel.
[17:07] Here I can set up patrol route for this specific enemy.
[17:10] To have something to select, I drag and drop patrol route to the world and select the second point.
[17:16] Now I can make the route and add new points by simply holding alt on my keyboard and dragging.
[17:24] Having made this, I add the route to my enemy and simulate.
[17:47] Now let's try being bomb patrol.
[17:49] Lastly, I'm just going to use patrol route.
[18:15] Lastly, I'm just going to use patrol route.
[18:20] You can see the AI turned patrol off and started to just idle.
[18:31] To see if spawn point was updated, let's drag him.
[18:37] Now I will disable patrolling and check if investigation works.
[18:40] For this, in my player blueprint, I just set up 2 events that will make sound and make damage to the AI.
[18:46] When I make sound outside of his perception, nothing happens,
[18:50] but when I do it inside, AI hears it and investigates.
[19:07] Damage on the other hand can be done anywhere and it immediately switches into being hostile.
[19:13] The only bug now is when I sneak behind him and attack him.
[19:19] You can see AI doesn't care.
[19:22] To fix this, I can add report damage event into AI component interface.


### Combat State explanation [19:32]
**Transcript (timestamped):**
[19:33] To recreate the kind of complex AI scene in Elden Ring, I spent countless hours thinking about the best approach.
[19:39] In the end, I decided to structure my AI around 3 combat distances, far, mid and close.
[19:45] Each zone determines how the AI behaves.
[19:47] For example, in the far zone, the AI can use range attacks or gap closers to get closer to the target,
[19:53] and in close range, it can get really aggressive, chaining multiple combo attacks or choosing to create distance to reposition itself.
[20:01] These different zones already make the AI feel dynamic, but that's not everything.
[20:05] I also wanted to make random decisions based on the probability of each action within the zone.
[20:10] This lets me fine tune enemies to be passive, aggressive or evasive that frustrates the players.
[20:16] The AI's core actions ended up being close distance, move backwards, make distance, dash and strafe,
[20:23] which eat combat zone having 3 attack placeholders that can be used for whatever.
[20:28] For me, first one represents single attack, another one combo and the third one is a special attack.


### Combat State Setup [20:35]
**Transcript (timestamped):**
[20:35] The first step was setting up an enum for combat zones and a structure holding all action probabilities.
[20:41] I then made an enum for combat actions, including 3 that are actually reactions,
[20:46] turned over target, hit reaction and far away state.
[20:50] Another enum held the attack placeholders and I created a structure for attack data containing an array of animation montages,
[20:57] the attack type based on the placeholders, attack weight for probability, a health threshold to unlock attacks like a boss second phase
[21:06] and the main and max angle defining where the attack can be performed.
[21:10] To save myself headaches later, I also set default values for all float variables.
[21:16] With this setup, in my AI component, I created an array of attack data,
[21:21] an array for probabilities for each combat zone and added two floats to define where mid and far zone starts.
[21:27] Close zone begins where mid ends, making it easy to calculate.


### Combat Brain Service [21:31]
**Transcript (timestamped):**
[21:31] Next came the decision making brain, which was the hardest part.
[21:35] I built a service with all the blackboard keys I'd need, some which didn't even exist yet, but I would create them later.
[21:42] In the event received AI, the first task was to get and save the distance between AI and its target.
[21:48] Then the AI checks for reactions in priority order.
[21:51] First is hit reaction.
[21:53] To implement this, I also added two floats in my AI component, a private received damage variable and non private poise variable,
[22:02] which determines how much flat damage the AI can take before reacting.
[22:06] I also made two functions for setting and getting received damage.
[22:10] And whenever the AI was hit, I updated this via an interface I had already set up.
[22:18] In the service, a pure function checks if received damage is equal to or greater than poise,
[22:24] and if it is, the selected combat action becomes hit reaction,
[22:27] mimicking the behavior of non hostile AI that switches actions based on an enum.
[22:33] The next priority is turned towards target.
[22:36] Another pure function checks if the AI needs to rotate based on the proper angle.
[22:40] If so, the AI performs a turned-over-target action.
[22:44] The last reaction is far away check, for when the AI strays too far from its spawn point.
[22:50] I also added two variables in my AI component for this.
[22:53] One to enable this behavior, so bosses wouldn't use it because they don't need it,
[22:58] and another defining the distance at which it applies.
[23:02] A pure function compares the distance to this variable and sets the selected action to far away if needed.
[23:09] I also performed these checks in the event received deactivation just to prevent some bugs.
[23:15] Once the reactions were set, I moved to selecting proper actions.
[23:19] This happens in event received search start AI, triggered whenever the selector starts searching for something to execute,
[23:26] or in other words, when the AI finishes its action.
[23:29] I set the control-pwn variable, verified that all reactions were false,
[23:34] and then determined the AI's current combat zone using a pure function.
[23:38] With the zone known, I could switch on Enum and select actions.
[23:42] I've wrote a function that converts all probabilities into an array, then another function that chooses one randomly.
[23:48] By the way, you can use this function to randomly select anything.
[23:52] And then, switches on the chosen index to select the action from the action array.
[23:57] For strafing, I also used BlackboardKey to switch directions dynamically based on the AI's last strafing move.
[24:04] This can be improved drastically, but for the purpose of this video it's enough.
[24:08] Choosing an attack required a dedicated function.
[24:11] I set selected combo and selected attack to zero.
[24:14] Selected combo maps the attack data index, and selected attack is the specific animation index.
[24:20] I looped through all attacks checking if the combat zone matches, if the AI held meets threshold,
[24:26] and if the target is within the correct angle.
[24:28] Pallet attacks then are stored in the local arrays.
[24:32] After looping, I randomly selected one based on probabilities and returned the attack index as selected combo.
[24:39] Thanks to setting selected attack to zero, it will always pick the first animation index.
[24:44] Back in the main action selection, if no valid attack was found, the AI defaults to straf.
[24:49] Otherwise, the selected action becomes attack.
[25:02] To handle combos, I created a custom event in the service checking the same conditions as before.
[25:10] Then I copied a function that chooses random attack, removed the unnecessary local arrays,
[25:15] and ensured the array index matches the selected combo.
[25:19] I also checked if the AI is in proper distance for continuing the combo.
[25:23] If true, the AI increments selected attack and continues the combo.
[25:28] I also added checks to prevent infinite loops.
[25:31] For example, if there is only one animation, or if the combo is complete, the AI won't repeat it unnecessarily.
[25:37] I also verified that the last action was an attack before continuing the combo.
[25:43] In the event graph, I checked if the combo function succeeded, and if so, I set selected action to none,
[25:49] and then back to attack, resetting it, and ensuring the AI continues properly.
[25:55] Another critical part is updating the combat zone with every tick.
[25:59] For example, if the target moves closer, the AI should immediately decide its next action,
[26:04] unless it's currently attacking.
[26:07] I tracked the current combat zone in private enum and updated it each tick.
[26:11] Changing the zone forces the AI to search for a new action with settings selected action to none.
[26:19] For combos, I grab a character reference in the event receive activation AI.
[26:24] Funnily enough, this runs after the search.
[26:28] I also created a Montage selection called idle for every combo animation to allow the AI to switch to a new animation
[26:35] if another combo attack can be executed.
[26:38] During the tick in the service, I checked if the current montage section is idle to continue the combos.
[26:46] I also had to update turn towards target for special attack angles.
[26:49] If the AI should rotate towards the target behind it, I checked if attack is available in that angle
[26:54] and forced the AI to select it.
[26:56] This ensures the AI has learnable patterns, but you could also add a weighted random bull check if you prefer unpredictability.
[27:06] After completing the brain, I populated the blackboard with all the new keys.
[27:14] Then I moved on to creating the action sequences.


### Hit Reaction / Turn Towards Target [27:16]
**Transcript (timestamped):**
[27:17] The highest priority has read reaction, followed by turn towards target with a task that sets and clears focus.
[27:23] Setting focus makes the AI always look at its target.
[27:26] These two clear the focus.


### Close Distance [27:30]
**Transcript (timestamped):**
[27:30] Closing distance focuses on the target and moves forward with a task to change movement speed
[27:35] based on the newly created movement variables in the AI component.
[27:39] For this, I also needed to create an enum with all the movement types.
[27:44] Moving backwards also uses focus and variable speed, combined with a simple parallel note to move but also end after randomized duration.


### EQS Moving Backwards [27:45]
**Transcript (timestamped):**
[27:53] To make the AI walk backwards while facing the target, I used AQS, Environmental Query System.
[27:59] To imagine what it actually is, create an AQS testing pond and drag it into the world.
[28:04] Now, when you search in the detail spanner for AQS, you can set a query template, but there are none available,
[28:10] so let's create one for walking backwards from its target.
[28:16] Now, edit as a template and you see nothing.
[28:18] When you open an AQS, it looks quite similar to the behavior tree.
[28:22] Again, it starts from the root and when you drag down from it, you can see multiple options.
[28:27] To see what it actually does, click on anything with points.
[28:30] But for going backwards, I will be using grid.
[28:33] Now, you see generated points around the testing pond and you can also see that it checks for the target.
[28:39] You can also see that it checks for any obstacles by itself.
[28:42] You can get any or specific point by assigning tests by right clicking.
[28:47] Let's choose a distance test and set float value next to something like 500.
[28:52] You see it filter the points while also assign a numbers to it.
[28:56] That is the score and the bigger the score, the better the chance of selecting that particular point is.
[29:02] If you want just to filter or score, you can change the test purpose.
[29:06] Or if you want it not to select center, you can add minimum to it and it will do its magic.
[29:12] Projection data is used so the points are projected onto the nav mesh and not just everywhere.
[29:17] Up and down is the distance from nav mesh where it can check points for projections.
[29:22] So for example, if you don't want your points projected on a wall, you set this to a small number, maybe something like 300.
[29:31] The offset just offsets points so they are not in the ground because it may cause issues with move to task or any other stuff.
[29:39] Now back to the problem at hand.
[29:42] For moving backwards, I used a grid and filtered points using dot test.
[29:46] For points behind the AI, I set minimum value to minus one, which will select everything behind itself.
[29:52] But this is still way too many points and I needed just a straight line, otherwise AI would move erratically.
[29:59] So I set max value to minus 0.96.
[30:03] The closer the number to minus one, the smaller the angle of points will be selected.
[30:08] Now we have points but they are not scored.
[30:11] To do that, I added another test based on the distance, which will be just for scoring.
[30:16] You see that the highest number we have have the points furthest back, which is the opposite of what I want.
[30:22] So the only thing I need to do is set scoring equation from linear to inverse linear.
[30:28] Now I'm gonna set the radius of the simple grid to 800 and also change the navigation filter to recast filter while selecting the post projection offset to 32.
[30:39] Back in the behavior tree, I set the query template to the one I created and set the blackboard key to point of interest.
[30:46] The blackboard key is the point that was selected by the AQS.
[30:50] In run mode, I can set what points it should select and I will choose single random item from best 5%.
[30:56] I also want this service to run each with 0.1 second.
[31:00] If I didn't use a simple parallel that discards this move to, this task would run forever because it would never reach the point of interest, which is updating each 0.1 second.
[31:09] But to have smooth movement, you have to do it like this.


### EQS Strafe [31:13]
**Transcript (timestamped):**
[31:13] The next action also uses AQS and that is strafing.
[31:18] Firstly again, it will focus on the target, then change the movement speed to strafe and then yet again uses a simple parallel with randomized time,
[31:27] but this time it will have a selector with two move twos.
[31:31] Both are the point of interest, but they also need a blackboard decorator that checks if the AI should strafe to the left or to the right.
[31:39] Now because I want the AI to strafe around the player, AQS firstly needs to know who the player is.
[31:46] For that I had to create AQS context blueprint.
[31:49] I needed to provide just a single actor to the AQS, so I will overwrite that function.
[31:55] Now I just get the target from the blackboard and send it in.
[31:59] I also had to create yet another AQS context blueprint, but now I needed to provide it with a single location.
[32:06] This one is to check if the points are on the left side or on the right side, and I needed to select just the left side points.
[32:13] So again, I get the target and then I calculate on which side the points are.
[32:17] To get also the right side points, I duplicate this and just change the yaw from minus 90 to plus 90.
[32:24] With this blueprint done, I created an AQS for strafe left and generated points on the circle.
[32:30] Then I set space between points to be 150 and the circle center is the target context,
[32:36] or in other words, the AI's target in the blackboard.
[32:39] The projection data is said to be the same as in moving backwards.
[32:43] To score points, I added a distance test and set it to inverse linear.
[32:47] The last test will be dot which will be between two points, from context strafe left to the context square,
[32:54] which is the AI using this AQS.
[32:57] Line will also be from context strafe left.
[33:00] Filter type will be maximum with the value of 0.6 and the scoring again inverse linear.
[33:08] Now just copy this AQS for strafe right and the only change is in dot test.
[33:12] Instead of both lines from the strafe left, they will be strafe right.
[33:17] Back in the behavior tree, I added the AQS services, selected the random from best 5%,
[33:23] set the blackboard key to point of interest and for the interval, I used 0.01.
[33:29] To make sure move to task gets updated point of interest,
[33:33] I had to check observed blackboard value in all move dos with AQS in this behavior system.
[33:38] Otherwise, it might not get the proper updated point of interest through the AQS.
[33:43] Also, because I wanted to generate points on circle at the target distance and not a flat value,
[33:49] in both strafe left and strafe right, I set circle radius to be query params.
[33:54] This lets me in AQS service specify the flat value or set it as a blackboard key,
[34:00] which I set to target distance.


### Attacking [34:02]
**Transcript (timestamped):**
[34:03] For attacks, the AI doesn't focus on the target continuously.
[34:07] Rotation should only happen during certain parts of the attack, which I will set up later.
[34:12] I also change movement because attack is first and foremost making the AI move into the range
[34:17] before executing the attack.
[34:20] Then I made a task with 3 blackboard keys.
[34:23] On event receive execute AI, I set controlled palm to be private variable just so the graph isn't packed with lines.
[34:30] Then I get the selected combo and get its proper distance zone, which I check with combat distance zone.
[34:37] This pure function is the same as in the service, I just copied and pasted it here.
[34:42] If AI is in the proper combat zone, I cast it to character to play an montage
[34:47] and the montage I want to play is the selected attack.
[34:50] Then I wait until the animation is finished and finish the execute.
[34:54] Because there is actually this delay, I had to set in the service when I did the combo, the selected action to none and again to the attack.
[35:03] But it has to be here so the AI plays the whole animation if it cannot combo the attack.
[35:08] Now on the other hand, if AI is not in the correct combat zone, it will first move towards the target
[35:14] and the acceptable radius is where each zone starts.


### Dash / Make Distance [35:18]
**Transcript (timestamped):**
[35:19] With that done, we have two last combat actions which are almost the same.
[35:23] First is dash and we will focus on the target and use another newly created task with these blackboard keys.
[35:29] It also needs a new structure which will have just any montage and direction to where AI should dash.
[35:35] In AI component, I had to create an array of dash structure for all dashes.
[35:41] This I guess is based on preference, but I firstly got these private references
[35:45] then looped through all dashes and switched on combat distance zone enum.
[35:49] I yet again copied this pure function here.
[35:53] Now if AI is in far zone, I want it to dash only towards its target.
[35:57] If it's in the mid zone, it can dash left, right and towards its target again.
[36:02] And if it's in close zone, I only want it to dash backwards.
[36:07] Now the make distance focuses on the target and has a simple task that just plays the any montage.
[36:13] I also had to make an array of animation montages in AI component for all make distance animations.
[36:19] Finally, the far away state handles when the target is far away from the AI spawn.


### Far Away State [36:20]
**Transcript (timestamped):**
[36:24] Here, the AI focuses on the target, adjusts its speed and does the strafe logic for a few seconds.
[36:30] If the target doesn't come closer, it clears focus, sets AI state to idle and stops the combat.
[36:36] Changing AI state to idle makes it return to spawn.
[36:40] But this has to be done before AI stops combat, otherwise it would abort this and never execute this task.


### Setup for Combat Test [36:50]
**Transcript (timestamped):**
[36:50] Test combat lets first add attacks that AI can use for every zone.
[36:54] I will use the first in each zone for single attacks, the second for combos and the last for special attacks.
[37:01] But let's not forget that close zone 3 is set up to be attack that can be used when target is behind the AI.
[37:07] So that one will be for that.
[37:10] Now I set far zone to start in like 850 distance and mid zone in 400.
[37:16] In the far zone, I mainly wanted to close distance, but it can also use some attacks.
[37:22] Mainly the gap closer one.
[37:24] Let's also add strafe and dash.
[37:27] For mid zone, I wanted to mainly strafe while having bigger chance to use mid zone attacks.
[37:32] I will also allow the gap closer here with dashing and closing distance.
[37:37] And in the close zone, I want AI to mainly use combo attacks, but it can use mid zone attacks while being able to dash or move backwards.
[37:46] I sadly don't have animation for making distance, but I will use dash backwards for that.


### Bug Fixes [37:51]
**Transcript (timestamped):**
[37:52] Future me here, before we go to the testing, I really hated how moving backwards was so jittery, so I had to redo it.
[37:59] Instead of using expensive AQS that didn't even work properly, I made a service with these blackboard keys and calculated retreat direction and then made a box trace that checks for everything in the path excluding itself.
[38:13] If there is something, I just selected combat action to none, so AI will decide on next action.
[38:19] And if it can go there, I updated the point of interest.
[38:22] I set the service to run and check every 2 seconds.
[38:25] There are also two things that we're making some stupid bugs.
[38:28] One is in the brain combat service in check combo function.
[38:32] I forgot to add return node without success on loop complete.
[38:35] If you won't add this, the AI might succeed if it loops through everything, but if it does so, it hasn't found any attack, so the last attack might loop.
[38:43] Lastly, in play-dash montage task, there is no shuffle before we loop through array, which means, for example in mid-zone, it will always pick the first animation it finds and the first animation is always the same.
[38:55] And now, back to the testing.


### Testing Combat [38:57]
**Transcript (timestamped):**
[39:43] Now, just as a bonus, I will show you how I handled any bugs.


### Attack Rotation [40:10]
**Transcript (timestamped):**
[40:10] Now, just as a bonus, I will show you how I handled animation part of turning towards the target and rotating AI towards player while attacking.
[40:18] In the animation blueprint for my enemy, I calculated how big is the angle to where AI has to rotate by getting his current rotation and his new designated rotation.
[40:28] Then, in locomotion, I simply used two states for left and right animation with transition rules that check how big the angle is.
[40:39] For attack rotation, I made two anim-notifies and used it in every attack anim montage.
[40:44] And yet again, in animation blueprint, I set a gate that opens and closes based on notifies and then get the target from blackboard and rotate towards him with reinterp2.


### AI Edit Showcase [40:55]
**Transcript (timestamped):**
[40:56] With everything done, you can see there are numerous things I can adjust through the AI component, like hostility and its threshold when it becomes hostile, patrolling, aggro distance, all of the attacks it can use, all dashes, all movement speeds,
[41:10] hit reactions and when it should react to the hit based on the flat damage, far away state and when it should apply, make distance animations and mainly how the AI should behave when it's in combat.
[41:21] This is quite a lot, but there are still so many things that you can adjust or add to make it even better.
[41:26] I wasn't making this with the mindset that I'm gonna make the best AI, but only good enough base for everybody because no matter how hard I looked, there wasn't any really dynamic AI tutorials anywhere.


### Outro [41:37]
**Transcript (timestamped):**
[41:37] If you have made it to this part, I cannot thank you enough for your time.
[41:42] Hopefully this video taught you something and if yes, consider liking, sharing or commenting what you liked or what you didn't. All feedback is appreciated.
[41:51] I want to make more guides that cover topics fully, so I also made a Patreon where you can support this unemployed student.
[41:59] There you can find project files for this and more upcoming stuff.
[42:03] The project file doesn't only have AI, but also the player part that you've seen in this video.
[42:08] The only thing that it's missing are the animations because they are bought from the store.
[42:13] You can find link in the description if you liked them and well, that's it. See ya!



---

## Captured Frames

- [1:00] tutorials/frames/understanding-ai-and-behavior-trees---the-ultimate-guide-ue5/frame_000.jpg
- [5:30] tutorials/frames/understanding-ai-and-behavior-trees---the-ultimate-guide-ue5/frame_001.jpg
- [11:30] tutorials/frames/understanding-ai-and-behavior-trees---the-ultimate-guide-ue5/frame_002.jpg
- [14:00] tutorials/frames/understanding-ai-and-behavior-trees---the-ultimate-guide-ue5/frame_003.jpg
- [20:40] tutorials/frames/understanding-ai-and-behavior-trees---the-ultimate-guide-ue5/frame_004.jpg
- [28:05] tutorials/frames/understanding-ai-and-behavior-trees---the-ultimate-guide-ue5/frame_005.jpg
- [32:00] tutorials/frames/understanding-ai-and-behavior-trees---the-ultimate-guide-ue5/frame_006.jpg
- [39:00] tutorials/frames/understanding-ai-and-behavior-trees---the-ultimate-guide-ue5/frame_007.jpg

---

## Structured Notes

### Core Technique
Full Elden-Ring-inspired dynamic melee combat AI built with **Behavior Tree + Blackboard + AI Controller + AI Perception + Environment Query System (EQS)** — covering non-hostile idle/hit-reaction, passive-hostile patrol/investigation/return-to-spawn, and a 3-zone (far/mid/close) probability-driven combat brain with strafing, dashing, and combo attacks.

### Summary
Dense 42-minute "ultimate guide" (a guide, not a step-by-step tutorial — the creator explains concepts and shows finished Blueprints rather than typing every node live). Opens with Behavior Tree fundamentals: AI Controller (starts/stops the tree, feeds it perception data), Behavior Tree (decision-making node graph), Blackboard (shared data store); execution flow is strictly top-to-bottom/left-to-right; **Selector** tries children left-to-right and succeeds on the first success, **Sequence** requires every child to succeed in order, **Simple Parallel** runs one task alongside a whole sub-tree with a configurable abort/wait-for-finish relationship; **Tasks** are executable leaf logic (must start with Event Receive Execute and end with Finish Execute/Abort); **Decorators** are conditions attached to any node (often reading Blackboard keys); **Services** are per-tick updates usually used to refresh Blackboard keys. Architecture: a single reusable **AI Component** (actor component) holds all core AI data/logic, referenced by both the Enemy Blueprint and its AI Controller, which starts the Behavior Tree. Non-hostile state: a `Hostile` Blackboard bool gates a Selector between idle (Wait task) and hit-reaction (a Sequence triggered via a Blueprint Interface call from the player's damage logic into the AI Component, storing the attacking actor and an AI-state enum in the Blackboard); hit-reaction computes a hit-direction enum from the angle between the AI and attacker (0°=forward, ±180°=back, negative=right, positive=left in Unreal's convention) to pick a directional animation montage from a TMap; a custom decorator (`Health Percentage Check`, overriding `PerformConditionCheckAI`) flips `Hostile` once health drops under a configurable threshold, gated with a Force Success decorator so failure doesn't cascade-fail the sequence. Hostile-passive state adds `CombatState` and `Patrol` bools driving idle/return-to-spawn (via `Rotate to Blackboard Entry` + `Move To` + a custom "near location" decorator built because the built-in `Is At Location` decorator can't abort on change), three patrol modes (once/loop/ping-pong) driven by a spline-based Patrol Route actor and a `FindNextPatrolIndex` function, and an **AI Perception component** (Sight/Hearing/Damage senses, Detection by Affiliation, Max Age) feeding an `OnPerceptionUpdated` event that routes to Handle Damage/Sight/Hearing functions and a Behavior Tree **Investigation service** that promotes a perceived stimulus location to a Blackboard `Target`/point-of-interest and escalates to combat when within aggro distance. The combat brain is the most complex part: a per-tick **Combat Brain Service** computes distance-to-target, checks reactions in priority order (hit-reaction via a poise/received-damage threshold, turn-towards-target, far-away-from-spawn check), determines the current combat zone (far/mid/close, configurable distance thresholds), and picks a weighted-random action (close distance, move backwards, make distance, dash, strafe, or one of 3 attack placeholders — single/combo/special) from a per-zone probability array; attack selection loops eligible `AttackData` structs (animation montages, angle range, health-threshold unlock, zone, weight) and supports multi-hit combos via a montage-idle-section check. **EQS** is used for two AI movements: walking backwards while facing the target (a Grid generator filtered by a Dot test for points behind the AI, scored Distance Inverse Linear, tuned via Projection Data/radius) and strafing left/right around the target (a Circle generator around an EQS Context Blueprint that resolves the player actor + left/right offset locations, filtered/scored with Dot + Distance tests) — both wired into the tree via an EQS-driving service and a `Move To` with "observed blackboard value" enabled so the destination updates live. The creator also shares a late bug-fix pass: replacing the jittery EQS-based backward movement with a service + box-trace approach, and two real bugs found (missing "return node without success" on a loop in the combo-check function; missing shuffle before iterating the dash-animation array). Ends with an animation-blueprint note on attack-rotation gating via anim notifies + `RInterpTo`, and a tour of all AI Component-exposed tuning parameters (hostility threshold, patrol settings, aggro distance, attacks, dashes, movement speeds, hit reactions, far-away state, make-distance animations).

### Key Steps
1. Set up the core trio: an **AI Controller** Blueprint, a **Behavior Tree** asset, and a **Blackboard** asset; centralize all AI data/logic in a reusable **AI Component** referenced by both the Enemy Blueprint and its AI Controller (which starts the tree).
2. Non-hostile state: `Hostile` Blackboard bool → Selector (`IsNotSet` decorator with Observer Aborts enabled) → Idle (Wait task, aborts on hit-reaction) / Hit Reaction (Sequence, does not abort — priority). Hit detection via a Blueprint Interface between the player and the AI Component; compute hit-direction angle (Unreal convention: 0°=fwd, ±180°=back, −=right, +=left) → enum → TMap lookup for the directional montage → play, wait for finish, Finish Execute.
3. Add a custom `Health Percentage Check` decorator (override `PerformConditionCheckAI`, compare current health % to an AI-Component-exposed HP threshold slider) on the hostility-flip task, wrapped in Force Success so a failed check doesn't fail the whole sequence.
4. Hostile-passive state: `CombatState`/`Patrol` bools gate idle/return-to-spawn vs. combat; return-to-spawn uses `Rotate to Blackboard Entry` (precision 1; requires disabling "Use Controller Rotation Yaw" and enabling "Use Controller Desired Rotation" on the movement component) → `Move To` → rotate to spawn rotation, gated by a custom "near location" decorator (radius + inverse toggle) since the built-in `Is At Location` decorator can't abort on condition change.
5. Patrol: build a spline-based Patrol Route actor, expose it as an "expose on spawn" variable on the AI Component, implement 3 modes (once/loop/ping-pong) via a `FindNextPatrolIndex` function tracking a private patrol index/direction, wait/should-wait timing, and a custom Patrol task (rotate to point of interest → Move To).
6. Investigation: add an **AI Perception** component to the AI Controller with Sight/Hearing/Damage senses (Detection by Affiliation all-true for non-grouped enemies; tune Max Age for memory duration); debug via Project Settings → Gameplay Debugger activation key, then press `5` in PIE to visualize perception ranges/state. On `OnPerceptionUpdated`, route each updated actor through Handle Damage / Handle Sight / Handle Hearing functions that set a Blackboard `Target` object and point-of-interest location, and an Investigation **service** on the tree promotes a perceived stimulus to point-of-interest and escalates to `CombatState` once within a configurable aggro distance.
7. Combat brain: build enums for Combat Zone (far/mid/close) and Combat Action (incl. reaction-only entries: turn-towards-target, hit-reaction, far-away), an `AttackData` struct array (montages, attack type, weight, HP-threshold unlock, min/max angle), and per-zone action-probability arrays; a per-tick **Combat Brain Service** computes distance, checks reactions in priority order (hit-reaction via a poise/received-damage comparison, turn-towards-target via an angle check, far-away-from-spawn), determines current zone, and — on `Event Receive Search Start AI` (i.e. whenever the tree needs a new action) — picks a weighted-random action via a reusable "probabilities-to-array + random pick" function pair; attack selection filters `AttackData` by zone/HP-threshold/angle before the weighted pick, and combo continuation is handled via a dedicated custom event that checks montage-idle-section state and distance before incrementing the selected attack index.
8. Build the combat action sequences: Hit Reaction / Turn Towards Target (Set/Clear Focus tasks) → Close Distance (Set Focus + Move Forward with a movement-speed task) → Move Backwards and Strafe (both via **EQS**, see below) → Attacking (checks combat-zone match before playing the selected attack montage, or moves into range first) → Dash / Make Distance (struct array of montage + direction, filtered by current zone) → Far Away State (strafes briefly, then clears focus/returns to idle-spawn if the target doesn't close the distance — done before stopping combat, to avoid a self-abort race).
9. **EQS for backward movement:** create an EQS Testing Pond + Query Template using a Grid generator, a Dot test (min value ≈ −1, max ≈ −0.96 to select a narrow cone directly behind the AI), a Distance test set to Inverse Linear scoring, Projection Data tuned (radius, recast filter, post-projection offset ~32) — drive it from a tree service picking "single random item from best 5%" at a 0.1s interval, wrapped in a Simple Parallel with a randomized-duration end condition so the Move To task doesn't run forever chasing a constantly-updating point.
10. **EQS for strafing:** two EQS Context Blueprints (one resolving the target actor via `Provide Single Actor`, one resolving a left/right offset location via `Provide Single Location`, duplicated with yaw ±90°) feed a Circle generator (150 spacing, radius set via Query Params so it can be driven by a `TargetDistance` Blackboard key) scored with Distance (Inverse Linear) + Dot tests; wire the resulting EQS query into a Move To task with **Observed Blackboard Value** enabled so it re-paths as the point-of-interest updates live.
11. Bug-fix pass: replace jittery EQS-driven backward movement with a plain service (compute retreat direction, box-trace the path, reset the action to None if blocked, else update point-of-interest, checked every 2s) — noted as more reliable than EQS for this case; fix a missing "loop complete, no success" return node in the combo-check function (otherwise a full-loop-without-match could still report success and repeat the last attack); add a Shuffle before iterating the dash-animation array (otherwise dash always picks the same first animation).
12. Animation-side attack rotation: in the Anim Blueprint, compute the delta between current and target rotation for left/right locomotion blend states; gate attack-time rotation with two Anim Notifies per attack montage opening/closing a "rotation gate," then `RInterpTo` toward the Blackboard target while the gate is open.

### UE Systems / Blueprints / Settings
- **Core actors/assets:** AI Controller, Behavior Tree, Blackboard, AI Component (custom actor component holding all AI data/logic), Patrol Route actor (spline-based).
- **Behavior Tree nodes:** Selector, Sequence, Simple Parallel (with abort/wait-for-finish toggle), custom Tasks (Hit Reaction, Patrol, Combat actions, Dash, Attacking, etc.), Blackboard decorators (`IsNotSet`, custom Health Percentage Check, custom Near-Location, Force Success), Services (Investigation service, Combat Brain service, EQS-driving services).
- **AI Perception:** Sight/Hearing/Damage senses, Detection by Affiliation, Max Age, `OnPerceptionUpdated` event; Gameplay Debugger key (Project Settings) + `5` hotkey in PIE for visualization.
- **EQS (Environment Query System):** EQS Testing Pond actor, Query Template editor (Grid / Circle generators), Dot test, Distance test (Linear/Inverse Linear scoring), Projection Data (radius, recast filter, post-projection offset), EQS Context Blueprints (`Provide Single Actor`, `Provide Single Location`), Query Params (for runtime-driven radius), "Observed Blackboard Value" toggle on Move To.
- **Movement/animation nodes:** `Rotate to Blackboard Entry`, `Move To`, `Use Controller Rotation Yaw` / `Use Controller Desired Rotation`, Play Montage tasks, Anim Notifies for rotation gating, `RInterpTo`.
- **Blueprint Interfaces:** used for player→AI-Component hit/damage communication (attacker actor + damage amount) and AI Perception damage reporting.
- **Key data structures:** enums (AI State, Hit Direction, Combat Zone, Combat Action, Attack Placeholder, Patrol Type, Movement Type), `AttackData` struct (montage array, attack type, weight, HP-threshold, min/max angle), Dash struct (montage + direction), TMap<enum, AnimMontage> for hit reactions.

### Difficulty
Advanced/Expert — assumes solid Blueprint fluency; combines Behavior Tree, Blackboard, AI Perception, EQS, custom C++-free Blueprint tasks/decorators/services, animation blueprints, and a hand-rolled weighted-probability action-selection system into one production-style combat AI.

### UE Version
Not explicitly stated (recent UE5.x; uses standard Behavior Tree/EQS/AI Perception systems, not the newer State Tree plugin).

### Tags
blueprint, animation, pipeline, advanced, expert

---

## Related Entries
- `tutorials/unreal-engine-5-tutorial---state-trees-part-1-overview.md` — direct architectural alternative/comparison (State Tree vs. Behavior Tree), ingested in this same session; shares tags: blueprint, animation, pipeline.
- No other ingested unreal-sidekick tutorial currently covers Behavior Trees, AI Perception, or EQS — this is new coverage territory for AI/gameplay-adjacent content within the skill's primarily cinematics/VFX focus.
