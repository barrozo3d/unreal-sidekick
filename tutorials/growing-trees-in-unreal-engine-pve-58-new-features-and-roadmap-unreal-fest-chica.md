---
title: Growing Trees in Unreal Engine: PVE 5.8 New Features and Roadmap | Unreal Fest Chicago 2026
source: YouTube
url: https://www.youtube.com/watch?v=zfFq5e8Pxz0
author: Unreal Engine
ingested: 2026-08-06
ue_version: "UE 5.8 (Experimental) — Procedural Vegetation Editor (PVE), added 5.7, expanded 5.8"
tags: [pcg, nanite, modelling, geometry, materials, advanced, ue5-8]
extraction_status: complete
frames_dir: tutorials/frames/growing-trees-in-unreal-engine-pve-58-new-features-and-roadmap-unreal-fest-chica/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# Growing Trees in Unreal Engine: PVE 5.8 New Features and Roadmap | Unreal Fest Chicago 2026

**Source:** [YouTube](https://www.youtube.com/watch?v=zfFq5e8Pxz0)
**Author:** Unreal Engine
**Duration:** 37m55s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] Work on everybody to growing trees instead of Unreal.
[0:04] Just quick, who am I? I'm Simon Barley. I'm the Live Meditation Artist at Epic.
[0:10] I lead the team creating mega plans and various foliage content, R&D and so on.
[0:14] I've also been part of the PV development, but today I'm representing all the hard work for the whole PV team.
[0:21] So the agenda for today. We'll do a quick recap of what PV is.
[0:27] We're over some of the underlying design principles. New feature highlights.
[0:31] Don't worry, there'll be plenty. Growing trees, hard works, and covering some advanced workflows as well.
[0:36] And we'll end with a quick glimpse of the roadmap ahead.
[0:43] So what is PV? We didn't catch it last year, and this is just a quick recap.
[0:47] It is a node-based editor for creating foliage, trees, plants, and all in between.
[0:53] It's built upon PCG, so a lot of the UI and offering will be similar.
[0:58] And there are some features shared between the two editors as well.
[1:01] The aim for PV is to consolidate different types of foliage creation workflows
[1:05] and enable the use to mix and match different approaches as a see fit.
[1:09] At the time, we are supporting NANET foliage, but we are looking at bringing in a lot system as well later on for non-NANET platforms.
[1:17] PV leverages megoplanets, the new vegetation preset library available on FAB as well.
[1:22] And PV is still experimental in 5.8, as there are a lot more things you want to explore and want to add as well.
[1:31] So what is megoplanets?
[1:33] Together with PV in 5.7, we also roll out megoplanets.
[1:37] They're available on FAB, and they will serve as our kind of growing library of tree assets and presets you can plug directly into PV.
[1:45] You can modify them or build your own versions using the supplied components and presets.
[1:49] For 5.8, megoplanets will shift its offering to reflect all the new additions to this version as well.
[1:57] And the idea behind it is to supply users with high fidelity parts and components they can use to build their own trees from.
[2:04] And it will also offer some drag and drop assets as well for those looking to just fill out their scenes and rolls quickly.
[2:14] PV and megoplanets supports non-NANET foliage for now.
[2:17] That is a big paradigm shift on how to offer high fidelity and non-NANET foliage while keeping the disk and memory cost low.
[2:24] It also uses the dynamic wind plug-in, as seen on the Witcher 4 demo for example.
[2:29] And it makes use of voxels in the distance to ensure we can drop very complex meshes quickly to more cheaper voxels.
[2:36] And the plus side, there's no lot popping and a good sense of volume across the whole scene.
[2:45] So, in 5.8, now it's your turn to actually start building from scratch.
[2:50] Previously, the input data we had was kind of black boxed, using kind of a preset system.
[2:55] Although I know some of the users out there were able to figure out how to get that data to work as well on their end.
[3:01] But now we're opening up the whole system so they can build and grow their own trees from scratch.
[3:07] You can take advantage of fully simulated growth, recursive scattering workflows, you can import and sample 3D meshes and 2D images and much more.
[3:15] So, the sign of philosophy behind PVE is actually being able to tap into the simulation with growth when you need to.
[3:26] And generate a good base or even grow the full tree if you want to.
[3:30] And then what you should be able to do is move on to recursive scatter, so basically do curves on curves.
[3:35] So if you want to build out your secondary branches layer by layer, you can do that as well.
[3:39] And finally, you want to be able to get there and actually art directly on to your result.
[3:45] So you can move points around, rotate branches and then of course after all this plug it back in again and do the whole flow once more.
[3:56] So what we want for the end user is to be able to plug in all these stages into each other and it should function properly.
[4:02] You should be able to do this in several stages.
[4:04] And you can also tap into the poster form and nodes that we did offer back in 5.7 as well.
[4:09] So you can not just try to edit your growth.
[4:14] So, we will start to cover all these new nodes we have brought for this version.
[4:18] There is quite a few things here at the back.
[4:21] There is a lot of new features, new exciting workflows to try and explore.
[4:28] So, without further ado, let's dive right into it.
[4:30] Do hold on to your socks because they are going to get pretty detailed and a little bit nerdy.
[4:37] First and foremost, this is the workhorse of the system, the Grover node.
[4:41] This is the one that drives the whole simulation algorithm in the background.
[4:48] And we can alter the various inputs and affect the outputs.
[4:51] As you can see on these input pins here.
[4:53] You can see things like gravity, amount of cycles, synencems, trunk radius, phototropism, etc.
[5:00] And you can also be plugged into other growers to continue the other simulation from the previous input as well.
[5:07] There are quite a few features here, but I will go through them one by one.
[5:14] The Grover itself is using a multi-bounds ray tracing light detection for the Gold simulation itself.
[5:19] It supports collision and interaction with external meshes.
[5:22] It has a gravity that uses a beam deflection model.
[5:25] It has a natural shading of branches due to light and age and nenses.
[5:30] Built in hormone control and emulation control to control your bifurcation and dominance.
[5:36] It supports all primary fill of taxes that tend to find in nature.
[5:40] The foliage in this Grover stage is represented by small cars that are basically there to represent the shadow created by the canopy.
[5:47] And the meshing is a very simplified version just for simulation purposes.
[5:52] Once you change it to these attributes, you will rerun the simulation and make your new tree with the new settings.
[6:01] Why Botanical Simulation?
[6:04] We think it is the best way to get natural looking shapes by using botanical principles and naming conventions.
[6:11] There is a lot of data we can actually pull from research papers or even wood manufacturers.
[6:16] It shares the same terminology as well.
[6:19] And it creates a little bit more of a unified language around how to use it.
[6:26] So how does it work?
[6:28] The growth algorithm uses the light detection and synenses.
[6:31] We are looking for optimal light conditions.
[6:34] And then doing shading or pruning branches based on light conditions basically.
[6:38] The light direction simulation is based on a kind of top level dome light.
[6:43] We can change that on the tree.
[6:46] But it is able to generate very realistic structures this way because it is actually behaving like a tree or a plant wood in nature.
[6:51] So going back to all these pins and all these strange names, what do they do?
[6:56] So we go through them all and see what we are up to.
[6:59] Starting with how do we get the trees to actually grow?
[7:02] For that we need to look at the growth cycles.
[7:05] Adding growth cycles will grow your tree larger and older.
[7:09] But it is not a complete one to one to age as trees have several cycles in one year.
[7:13] So we are going to look at the growth cycles.
[7:15] The growth cycle is actually a tree larger and older.
[7:18] But it is not a complete one to one to age as trees have several cycles in one year.
[7:22] But it does hold true that more cycles equals an older tree and less cycles equals a younger tree.
[7:31] The building blocks of your tree structure is full of taxi.
[7:34] This is the various arrangements and patterns you can find in plants.
[7:37] We support all the major ones and we can split them all into trunk branches and foliards separately.
[7:42] In this node we also control things like axial angle.
[7:46] Basically what angle the branches start growing at.
[7:49] Additional full of taxi rotations if you want to offset your full of taxi patterns and stagger.
[7:53] Which basically will turn each segment of the branch away from the previous one.
[7:58] So it creates a slight zigzag pattern that we see in nature on branches.
[8:06] So these are the full of taxi supported.
[8:08] Spiral is basically growing in a helix pattern around itself.
[8:12] All donating.
[8:14] Every other branch will be on the opposite side of the previous one.
[8:17] Opposite each node grows two branches identical on each side.
[8:21] World each node grows several branches in a 360 degrees around itself.
[8:25] They can also be a random number of branches per node.
[8:28] And the Q set.
[8:30] It's basically opposite but each row will turn 90 degrees from the previous one.
[8:39] En av de män driver som kommer att skapa i tränningen är fototropisen.
[8:43] Det vill dikta hur det ska ha i grunden av liten.
[8:47] Ska det försöka rena för primal liten i alla gånger.
[8:50] Ska det försöka avvara sin egen skadda.
[8:52] Säga de här världarna och biologer som har en stor effekt på hela kanal.
[8:57] Om vi tänker på en populär tränning i naturen.
[9:00] De tenden att grå av branschen väldigt bra i skogen.
[9:02] De kommer att ta upp och fisk i skogen.
[9:05] Och andra försöker optimera för att skada av branschen.
[9:08] De kan skruva av branschen.
[9:14] Här ser vi att fototropisen inte har fungerat.
[9:17] Men först, som jag har sagt, är det att skada upp branschen.
[9:20] Men när vi skadar upp branschen börjar det avvara sin egen skad.
[9:23] Även till den här poängen där det sker.
[9:26] Det kan bli en intressant resultat.
[9:29] Och sen åka igen till skogen.
[9:32] Ochcingan ska inom rabatet svata om det väx ju inte.
[9:44] повblirthets dollarn enjoyed for s
[9:48] kar χänsade.
[9:52] Väl milieu inbrill셨's mixture and
[9:56] throughout the world, har kafخت uts på
[10:00] Man kan också kontrollera elastis.
[10:02] Det är som hårdvård vs soft-vård, om det är bänd eller inte.
[10:10] I det gråtskommandet kan man kontrollera dina generella gråtssättningar.
[10:16] Som i segmentlängden för ett steg.
[10:18] Plänsen är max till högare och branschen är max till högare.
[10:23] Man kan också kontrollera probabiliteten i den här siffrorna.
[10:26] Man kan kontrollera förgående och gråtssäkringen
[10:29] i gråtssättning eller branschen.
[10:35] Man kan kontrollera rampan,
[10:37] där branschen försäkringen försäkterar branschen
[10:39] på trädet i sitt livscykel.
[10:44] Man kan kontrollera den här nöd,
[10:46] om budden är möjligt att reaktiva det i livet eller inte.
[10:50] Det finns några koncepten att vara bästa i gråttabeln.
[10:53] Apikal prioriter och auksiljer prioriter.
[10:56] De har alla enkla dörrar av dem,
[10:58] så de är de siffrorna branschen efter det.
[11:01] Apikal prioriter är hur mycket de ska ta av min träd
[11:05] för att få uppgångs för alla gråtscykeln.
[11:10] Och en liten version av det är hur lång branschen är
[11:13] för att gråta från det.
[11:15] Och auksiljer är det som sker
[11:17] på de siffrorna branschen från sin tredje träd.
[11:20] Hur mycket de ska ta av det?
[11:27] I det här exemplen har jag sett
[11:29] att apikal prioriter är ganska aggressiv.
[11:32] De försöker att få uppgångs för de siffrorna.
[11:36] Men i den här siffrorna
[11:38] vill jag slå ner lite
[11:40] för att få en liten kärn.
[11:42] Och på den här siffrorna
[11:44] har jag sett att apikal prioriter
[11:46] är lite längre än den.
[11:48] Och i den här siffrorna
[11:50] har jag sett att de är liten.
[11:52] Och i den här siffrorna
[11:54] är det ganska common
[11:56] för att få uppgångs för alla gråtscykeln.
[12:03] Du har också access till
[12:05] objektförlöshet i gråtscykeln.
[12:07] Så du vill gråta en träd
[12:09] i en liten eller en liten träd
[12:11] och samla och ta av det.
[12:13] Och grå och ta av det.
[12:15] Du kan också ha den här form
[12:17] och trinna trädet
[12:19] så att du kan ta av en del av det.
[12:21] Om det intervjuer.
[12:25] Och vi går till senasens
[12:27] som är en fanfansig namn för äg.
[12:29] Men det här kan kontrollera hur
[12:31] sensitiv det är att skälla branschen
[12:33] som är baserad på gravitation och stress
[12:35] och liten konditioner som går älgare.
[12:38] Låg liten konditioner
[12:40] är att om det är liten konditioner
[12:42] branschen kommer att stå och falla.
[12:44] Och äg är en övergång
[12:46] branschen blir drivare och mer brittare
[12:48] och börjar att bräka av de till gravitet.
[12:52] Och här kan du se att
[12:54] en träd som har hög stress för liten
[12:56] är att ha mest branschen och liten i gråtscykeln.
[12:59] Och den andra trädet har en liten stress
[13:01] som har resultat i en mer brunt träd
[13:03] som skedde mest branschen som en grån.
[13:05] Som de optimella konditionerna inte var möt.
[13:12] Välkomna.
[13:13] Det är en naturlig fenomen
[13:15] som sker trädstads- och kodominens branscher.
[13:18] Det är en common characteristic
[13:20] av en av tre specieer.
[13:21] Som du kan se trädstads- och trädstads-
[13:23] i alla de största sidorna.
[13:24] Det är användet som en hormon
[13:26] som kallar cykl.
[13:27] Det är en gråscykel
[13:28] som sker en fullsaturitet.
[13:30] Det kan få trädstads- och sprid.
[13:35] Det här sker.
[13:36] Det bortar valor för ett cykel.
[13:38] Och när det sker
[13:39] trädstads- och trädstads-
[13:40] kan du också definiera hur många sprid
[13:42] ska skapa på den här punkt.
[13:44] Man kan också kontrollera
[13:45] den här speeden
[13:46] av att byta upp trädstads-
[13:48] och trädstads-
[13:49] i den här exemplen.
[13:50] Det här är rädd.
[13:51] Det är väldigt trädstads-
[13:52] och jag har talat om trädstads-
[13:54] och trädstads-
[13:55] till tre trädstads-
[14:02] under det debugga visualisationen
[14:04] i din porträngdspel.
[14:06] Man kan se alla de här
[14:08] hormon och attryckor
[14:09] i porträngdspel.
[14:11] Och de är listade på gränskvinn.
[14:18] En annan tips är att du kan dra ut
[14:20] inputpins från gråscykel
[14:22] och skapa eksternal släpp
[14:24] som kan få dig att reusesa
[14:26] släpp mellan olika gråscykels.
[14:28] Eller du kan göra lite mat
[14:30] och logisk på dem också
[14:31] och input dem också.
[14:32] Så du kan göra det.
[14:34] Det kurser upp med det.
[14:35] Det enkels en massa modeller
[14:36] att jobba med i generellt.
[14:41] Och du kan också...
[14:42] Om du är färdig med den gråscykeln
[14:43] du har gjort,
[14:44] kan du också sätta den
[14:45] som ett data-asset.
[14:46] Så när du skapar en ny gråscykel
[14:48] kan du samla den
[14:49] och få den samla trädstads-
[14:51] och du kan fortsätta modellifiktningen.
[14:54] Det är en väldigt snabbt sätt
[14:56] att göra många varierar så snabbt.
[15:02] Alltså, är det alldeles bra?
[15:04] Jag hade en bra information där
[15:05] för en minut,
[15:06] men det är många nya
[15:09] och ett extremt system
[15:10] att försöka att skapa.
[15:12] Men hur kan alla
[15:14] komma ihop?
[15:16] Så här kan jag byta en gråscykel
[15:18] från min träd.
[15:19] Jag har dragit ut min bin
[15:20] och vill ha kontroll.
[15:21] Jag har gjort modellifikeringen
[15:23] och har tågat på den
[15:24] till att jag var färdiga med resulten.
[15:26] Jag har tågat till världens...
[15:28] Ja, till att vara färdiga.
[15:30] Det är en konferent trädstads-
[15:33] och jag försökte skapa en hinnoki-
[15:35] eller jappanisk cykel
[15:36] i den här siffrorna.
[15:39] Jag har inte haft att stoppa här
[15:40] för att jag också har access
[15:41] till alla post-formernot.
[15:43] Jag kan då non-destruktivt
[15:44] edita detta i alla fall.
[15:49] Det är ganska coolt med den här systemet
[15:50] att jag kan också gå tillbaka
[15:52] i tid, essentiellt,
[15:53] till en annan del av growthen
[15:55] och utgåta det som en ny trädstads-
[15:57] för att jag har access till denna trädstads-
[15:59] och jappanisk cykel.
[16:01] Och så har jag kanske haft att skapa
[16:02] några saker för alla
[16:03] vs. alla jordgränser
[16:05] men med väldigt många
[16:06] minst edit
[16:07] ska du ha en helt ny trädstads-
[16:09] väldigt snabbt.
[16:16] Så det är några visuellt exempel.
[16:17] Om alla texter och alla
[16:18] ljus är allt som kan använda
[16:20] trädstads-
[16:21] så är det det vi får.
[16:26] Det är en jappanisk cykel
[16:28] som är en omföringsfrån
[16:30] och så är det denna som finns
[16:31] i alla fall i denna är.
[16:33] Och så har jag kanske
[16:35] ett spinnband som kan
[16:36] använda trädstads-
[16:38] och en ny trädstads-
[16:40] eller en ny trädstads-
[16:42] och en ny trädstads-
[16:44] eller en ny trädstads-
[16:46] som är en massa trädstads-
[16:48] så är det en riktig trädstads-
[16:50] och en ny trädstads-
[16:52] och en ny trädstads-
[16:54] och en ny trädstads-
[16:56] Alla operaterna och nivåer som du har är avdelade till dig.
[17:00] Du vill inte kunna hålla med för att samla sig i form av det här.
[17:04] Du planar på att göra mer öppna på det.
[17:07] Du kan även ta ett bransch från en 2D-image och grafa den till din 3D-extractiv mesh.
[17:13] Det finns många sätt att få resultat.
[17:17] Från sidan.
[17:20] 2D-images är importat över texturan, undan mer.
[17:24] Du kan bara använda det bygg drawers sauce och locka mot.
[17:28] Vi вр�zes därför för ihop ett kombinerat skörd mash.
[17:32] För 1D-systemet, het
[17:34] produkabeladasilton i Ske firefighter하� inappropriar.
[17:37] Man påklar vad som tarsekolven tankar.
[17:40] Havs möjligheter att ha vägar eller somvar purchase.
[17:43] Christos Michael Tr잔 Stillsty indispensable.
[17:52] Dusk Красgårdrestill, members pole.
[17:56] Si pracern puls estimators spineées All won
[18:02] här vi disproportionately arbiliet har slår, så nejaklt Könndas
[18:06] i K kneeset impot geographical option med
[18:10] snab Franz kan grupos domulle osträckat varver Abidin
[18:13] gravy den sendforsen helt
[18:22] det mesht upprrs en gröt hemma fast thanked
[18:25] gärna cubesas som kokot oss ju schizophrenia
[18:35] attach E Derifius det toad importer
[18:37] mörkfrot med noi som Den bake ej brandtjust
[18:40] litt on the nose för det scale mot det
[18:42] Så kan vereg text� en flottendor Imported Image djup Batist
[18:47] Zable kang6r, Revolve dstatic Aranastergef assisted
[18:52] F Piram 갖고
[18:55] Etsיikelig Ar o &ン serie���r Monte
[19:05] Full 뉴스 flyttades och denφο почkvarnasättaren avslood
[19:11] hand el i säga som extrem EmmAmerican D now.
[19:22] Ikkan sim defeated svär dash documentaries här fence.
[19:28] De är origa runt.
[19:34] Up anhí, för längs planes en par lä buddies hittinnen tre.
[19:37] Dov men drog.
[19:40] Men även du robkar i svårt Trig aj kan den에게 paired utilize.
[19:47] En dot sendel ök purchase ona de deggre vad du rejoice mig Trigs fränst
[19:51] bens Zhónvalas bittens bor Spondetreat cost inte
[19:55] nog kall det graphbytle se coco och tyst hijud.
[19:58] det här så tot shielder.
[20:02] Att financer att boll.
[20:07] Det blir en son feller torpedo och tar av sanning wo kanssa så
[20:11] elected och tok och stimulerat trips och
[20:15] 爱ter br Mikey Bay.
[20:21] Det olmaz till dangens eller med gravt add tog comment CG
[20:25] Och så plockade jag den till en gråvare igen.
[20:27] Jag räddade några simulater, som 4 cykels.
[20:30] Det blev en liten triggård.
[20:38] Nu kan jag se graffade flöden i aktien.
[20:41] Jag gråv min simpla trig.
[20:43] Och så på den smålade gråvare där på sidan.
[20:46] Jag gråv den triggen.
[20:48] Och då, på graffpaletten och på graffdistributor,
[20:51] skälla den triggen under triggen.
[20:54] Och så, i alla fall, gråv den igen.
[21:01] Och här är något som vi kallar det 5 minutter språk.
[21:04] Obvistligen en trädmark pendel på denna.
[21:07] Man kan faktiskt grå en entire bransch,
[21:09] om man vill, och så att man kan grå en stick.
[21:11] Man kan sticka branschen under den sticken.
[21:14] Och så har man en trig.
[21:15] Det kan vara väldigt snabbt,
[21:17] en liten mål att skrava en ganska vajig vajig asset.
[21:22] Och de finns delar av att skrava verksamhet
[21:25] och hearrit mer.
[21:26] Detta är bra, sih.
[21:28] Men jag vill vi ska fråga hudarna om bean Timothy.
[21:33] explain,
[21:51] dräde beslutet som fyr⋅82 uppest JUN Edisительно Al remind
[21:54] R comed Rezend av det Skärna och Chev để Saxi ett beet louder
[21:55] Sajapotende点.
[22:05] Det post Tuesday vari colektединåita kan figured traced
[22:08] att jag brann en non destruktur i interakt med H&Œ SH.
[22:15] Så främst fåradd vid ur gränskade geokånerget affektet
[22:18] lid viser atomictegeht.
[22:19] Drake prim Wolf Perform measures i kan move dem人民.
[22:23] Ende tre OS geht efterhåll tú Lion�s slöts telefon namn,
[22:28] portstEven Lauren.
[22:35] Hanns jag tänkte goga addresses, Stockholm efterbandes en till
[22:47] Vi måste restriktera att det är den här formen.
[22:50] Om du vill göra en kubisk hälsik, kan du använda en kubisk.
[22:53] Restrykta gråterna.
[23:00] Vi har ett trunktexternodor som kan bäcka trunktexten.
[23:04] Det är simulat till att vi gör megaplaner.
[23:06] Vi kan göra generationstrypp i en text.
[23:10] Det fungerar med att selectera text från disk-
[23:12] och bäcka dem till ett targetlokation i kontonbränsle.
[23:16] Du kan sätta upp alla texternodor, paddning och exakt säsongen.
[23:23] Det är ett exempel på hur det ser ut.
[23:26] Vi har loadat tre olika generationer från min trid.
[23:28] De är alla separat targlar.
[23:30] De är kombinade i en text och kan mappa de olika ranges.
[23:35] Jag kan också avsätta en tajling om jag vill.
[23:40] När du är redo med det, plugger du den i en meshbuilder-node.
[23:43] Den får UV-information från den här nod.
[23:46] Man mappar den rätt.
[23:50] Jag är bäckad att vi ska använda mat.
[23:56] Vi har inte så skönt.
[23:58] Vi har skönt alla common-mat-node som kan driva custom-behållning.
[24:01] Det är inget direkt från PCG.
[24:03] Vi har också aktierat till samma läge.
[24:07] Då kan Forget
[24:27] skötvor uppsatta.
[24:31] Det understear med meshbuilder.
[24:34] creekfefiken.
[24:35] Nu kan jag ans榜ts till Ago-Nuys so sam aquesta
[24:41] kapten fram tredj��요 som kan gör att vi ser på att det
[24:45] vill jag att, eller återvirra det är inte större än det
[24:48] för att de verkar på detЁnges och Cavill var genomska
[24:52] den är också orobar naturligare så att ni också ♥
[24:55] örung traced efter på sport legs responsutz
[24:58] arv порterna av cm sigded under oss as well.
[25:05] Men dragdrapp i den en pin.
[25:10] You just create that attribute, but as a separate slab.
[25:19] The profile order comes with 10 different trunk profiles, provided from the plug in.
[25:24] Men vi planar om riting mor, with mega plans, as the common line.
[25:30] But this is responsible for basically creating the trunk flair at the bottom of your tree.
[25:35] En folies distribution dom iВыter Gek ked
[25:39] i aúnvånat så bounces i spel humma resolve gravy rekt obok.
[25:44] CONDITION system allow en idé distribut För competitions Elementum erased
[25:50] är ironic, BTS i avt proceeds i Jedi full Contra raise or Silenta OM
[25:57] bør ett stycken där det ärتم bär, har en överbyttning uppanken
[26:00] benedigt. Det är du satt åter bene och du lu lockar pair av step i step.
[26:03] Det gör det lite mer lätt att kontrollera.
[26:06] Det är en distans-baserad maskning mellan noderna.
[26:14] Den nya konditionen spår baserat på ett set av attrymme.
[26:18] Det är attrymme som liten, öppelängning, tipp, häls, hitt, och generation.
[26:25] Det namnar sig att sätta denna data upp och sätta den med den branschen som har de mest,
[26:30] och de kan inte ha en sån typ av attrymme som tråk har.
[26:34] De har mestat dem upp.
[26:39] Här är ett exempel där vi kan se att jag sätter på hälskonditionen
[26:43] i min skadring.
[26:44] Det börjar att lägga på min bransch för att sätta upp paletten
[26:48] att ha den här attrymme.
[26:52] Lätt att sätta upp det, så är det mer att hälskt att tråk kommer.
[27:00] Det är en del av attrymme som är för att sätta upp det.
[27:09] Nu kan vi sätta upp det här attrymme.
[27:12] Nu kan vi sätta upp det här attrymme.
[27:15] Nu kan vi sätta upp det här attrymme.
[27:17] Nu kan vi sätta upp det här attrymme.
[27:20] Du kan också sätta upp en null entris i branschpillen nu.
[27:27] Du kan använda dem som maskning element.
[27:29] Vi har inte en direkt peng system, men vi kan använda en invisibla bransch
[27:33] för att maska ut branschen som inte är allow till att spåna.
[27:36] De är bara skåret när du tar pass den.
[27:43] Vi har också en helt ny mod till det som heter parametrik.
[27:51] Det kan förgå hormon-sätta från en gråvar.
[27:55] Det är en mer skattering av branschdensitet.
[28:00] Du kan starta en end-generation, för exempel.
[28:06] Det är mer sätting än det.
[28:09] Det är bättre för nån typ av tris.
[28:12] Det ger dig direkt kontroll.
[28:15] Du kan göra en step med parametrik för specifika saker.
[28:19] Du kan gå till hormon-sättingen på en sätting.
[28:23] Vissa visar det.
[28:30] Nu är det en vektorhandling system.
[28:33] Det är en handfull vektorbaser som du kan skapa den.
[28:37] Det ger dig en ramkontroll som representerar länk av tränningen.
[28:42] Det ger dig en länk av branschbaseringen.
[28:46] Hur mycket av den här vektor ska få effekt i foliet?
[28:50] Du kan supporta ämning och fästviktor.
[28:53] Ämning och fästviktor är vilken mål som är fästgivare.
[28:57] Vi får också supporta utav att avsluta de här vänsterna.
[29:03] Vi har också en separat rollpitch och en jawkontroll.
[29:08] Vi får en lite mer variering.
[29:12] Det är en av de här vänsterna för vektor.
[29:16] Pläntgraderingen är i högst av tränningen.
[29:20] En användes för branschgraderingen är att branschbaseringen från start till finish
[29:25] kan användas som kontroll.
[29:33] Nu kan vi se hur vi kan skapa de här vänsterna.
[29:37] Jag gör en negativ Z som kommer att få dem ner i början.
[29:41] Jag gör också foliet flätten, som är en flätten.
[29:47] Jag kan också se hur de mest optimala länk som kommer från branschen.
[30:08] Vi ska шö shirttinskna till segments och template narrowgård.
[30:12] Jag inser till det som om vi kan spfullstyrra bilen som visar pledizerekon iron原因
[30:18] eller visar att branschen intenserar och Baum är värdig på lik difficile för att utv marshall.
[30:23] Vi vet att det är nivår İyi normally직 karriers gr勾 till piliu.
[30:28] Vi skrev att det var början av buddies konditionu sponsor utan att man också kör tankar i avslutning jazz.
[30:35] det byggt.
[30:40] Erma happiness ioisetagu
[30:43] 숨t 아이 snitt aplettatiem
[30:46] Boxindo babello odds
[30:52] icke tevis standarden subgravs, hygien, åsiktets
[30:58] CloudsCam och release kan ha bi kan dy Mustafa
[31:04] Men det är också en v Lions innocence stain i回atson Assid skal också besHI Pro Busanes�ra
[31:13] êter sie in Aspr Strykerнокet harrils On the high level todo feudery
[31:20] som r κα observations Gaardal den gay Host planting logic insус jobb net
[31:29] under die sud bjad av sk upset kund nöjes ρ in k comunicabs tå olivesenung
[31:32] Så om du skriver gravidi, det skriver gråvar, men också skadar av branschen.
[31:42] Så, vi hoppar in på det här, så ser vi ut.
[31:44] På toppleveln, när vi åker på subnet, är det hur det ser ut.
[31:47] Och på borten är det parametrar vi har förbjudit från hela sällan.
[31:53] Så vi hoppar in på den första subgrafen.
[31:56] Det är bara en gråvar som generellt bara sker en steg.
[32:00] Som bas av träd.
[32:02] Och då har vi skadat en par parametrar som kan driva
[32:06] där vi kan skada mer branschen
[32:11] med den graffning systemen.
[32:14] Så vi är också gråvar en set av allihjälpbranschen och en set av dödbranschen.
[32:22] Och på den andra delen, har vi skadat actualbranschen.
[32:25] Så vi är basically kontrollering av branschen i detaljer
[32:28] med en enkel parametrar, men det sker både död och allihjälpbranschen.
[32:33] Och då har de flera som säger att dödbranschen har mer cykels än allihjälp.
[32:38] Så automatiskt har de en relacies till varandra.
[32:41] Om vi bara skadar branschen i detaljer, så har vi en simplare dödbranschen
[32:44] och en mer komplex ljudbranschen.
[32:49] Och det här är hur vi ser ut.
[32:51] Så vi har en range av 8 cykels och 15 cykels för de allihjälpbranschen
[32:55] som vi kan skada från.
[32:57] Och då kan vi få med den som är gråvariga till det.
[32:59] Men då ser vi dödbranschen som inte går ännu längre.
[33:02] De har mycket fler cykels än de allihjälpbranschen.
[33:09] Och här är en del som driver lite av den här logiken.
[33:12] Det är en massa basic operations som mest remapperar parametrar
[33:15] till en 0-1 range.
[33:17] Och en predeterminat safe range som vi felt på de här ljudbranschen
[33:21] för de här cykels.
[33:23] Så vi kan se om alla driver och parametrar på den här toppen
[33:26] producerar en bra resultat i någon konfiguration.
[33:31] Och en del som vi gör här är en del av en trunk.
[33:34] Så vi vet hur det kan bli start och hur vi kan starta
[33:37] att mixa en del av en k-properter till vårt tråd.
[33:43] Den här delen av den här subgrafen kan se lite avsäkta.
[33:46] Det är faktiskt ganska lätt.
[33:49] Vi kan använda en switchnode för exempel
[33:51] för att driva vilken profilodare vi vill använda
[33:54] om jag vill använda det att skapa från tre olika profil.
[33:57] Jag har ju exposed dem och har också skitnodat.
[33:59] Och du kan också använda en singel parametra
[34:01] att jumpa mellan tre olika profil.
[34:06] Och här är hur vi kontrollerat de här mörkna
[34:08] av tråd.
[34:10] Här kan vi se att vi har sändningsnodor för de här.
[34:13] Och de är basically copies of one another
[34:15] but with different noise settings.
[34:17] Och vi har intermulti-selection
[34:19] och de är just drag a slider
[34:21] i att det blir en annan noise on this tree.
[34:28] Och det last section,
[34:29] vi har just remapping en resolution slider
[34:31] till den entire tree.
[34:32] Och den ser ju det i en range.
[34:34] Så en meaningful resolution,
[34:36] zero less resolution.
[34:38] Och den är drivande av en mesh optimization
[34:40] i den mesh-builden itself.
[34:43] Så du får en väldigt simpla,
[34:44] just one slider
[34:45] to control the entire resolution of your tree.
[34:51] Och det refitnod,
[34:52] which is a refitnod
[34:53] which has been seen throughout this part of presentation.
[34:55] It's not a native node itself,
[34:57] it's something rebuilt with a subgraph.
[34:59] Which kind of shows you that it can build small tools
[35:01] and small utilities yourself.
[35:03] Whatever you might need.
[35:05] You can save this out as a proper subgraph asset.
[35:08] And you can just build up your own function library
[35:10] and keep calling it a new grower nodes,
[35:12] for example, or systems.
[35:17] Så,
[35:18] the next part of this whole setup
[35:19] is that we have the foliage distribution network.
[35:22] And this one is a bit unique in that
[35:23] we are allowing the user to define their palette
[35:25] on the top level,
[35:26] so they load whatever branches they want.
[35:30] And then we are passing on the decay value
[35:32] since we had the seneson data from the grower
[35:35] to also drive the scattering of the foliage.
[35:37] Basically, we are multiplying it together
[35:39] with the light value on the scattering itself.
[35:41] So the more decay you have,
[35:43] the more dead branches will start appearing as well.
[35:49] And yet to recap what we just did.
[35:51] Here again, as a result on the top level.
[35:53] A very few set of parameters
[35:55] that can drive a whole tree setup.
[36:07] love
[36:12] Some Food Development.
[36:14] We are planning to do
[36:17] is add more advanced viewport tools,
[36:18] maybe a bit more
[36:21] modeling tool support stuff like that
[36:22] directly in the viewport.
[36:24] We want to support custom meshes
[36:26] like photogrammeted trunks
[36:28] through your own custom sculpted meshes
[36:29] as well to bring into the system.
[36:31] We want to enable decorations
[36:33] or broken branches, small nubs, gashes,
[36:35] branches, small nubs, gashas, burl, etc.
[36:37] The spawn of your tree as well.
[36:40] We want to also look into having a full Atlas tool suite within the tools you can bring in
[36:46] textures of your leaves and actually mesh them and create branches from them directly in the TV as well.
[36:52] We do want to add a state of the art of the system for non-landard platforms as well here.
[36:56] I the things we're looking into, we would like to look into maybe utilizing space colonisation as well.
[37:08] Alla different styles of building, maybe even expose L systems if you want to have that available as well.
[37:15] If you want to add a lot more manual drawing in the viewport, you can maybe even draw your tree directly in the viewport and use that as a shape.
[37:22] Like I said, more sculpting and more modelling functionality you would like to add.
[37:27] And we're looking into having more integrated PCG interoperability as well.
[37:39] Ja, det var det här.



---

## Captured Frames

- [0:08] tutorials/frames/growing-trees-in-unreal-engine-pve-58-new-features-and-roadmap-unreal-fest-chica/frame_000.jpg
- [4:41] tutorials/frames/growing-trees-in-unreal-engine-pve-58-new-features-and-roadmap-unreal-fest-chica/frame_001.jpg
- [8:08] tutorials/frames/growing-trees-in-unreal-engine-pve-58-new-features-and-roadmap-unreal-fest-chica/frame_002.jpg
- [16:20] tutorials/frames/growing-trees-in-unreal-engine-pve-58-new-features-and-roadmap-unreal-fest-chica/frame_003.jpg
- [17:07] tutorials/frames/growing-trees-in-unreal-engine-pve-58-new-features-and-roadmap-unreal-fest-chica/frame_004.jpg
- [23:00] tutorials/frames/growing-trees-in-unreal-engine-pve-58-new-features-and-roadmap-unreal-fest-chica/frame_005.jpg
- [25:19] tutorials/frames/growing-trees-in-unreal-engine-pve-58-new-features-and-roadmap-unreal-fest-chica/frame_006.jpg
- [36:12] tutorials/frames/growing-trees-in-unreal-engine-pve-58-new-features-and-roadmap-unreal-fest-chica/frame_007.jpg

---

## Structured Notes

> **Transcript quality note:** The Whisper auto-transcript degrades into garbled/hallucinated Swedish for roughly the 8:39–34:00 stretch (a known Whisper failure mode on accented/noisy conference-hall audio). The notes below combine the coherent English portions of the transcript, the 8 captured frames (slide text + node-graph screenshots), and targeted web verification of the product names ("PVE" and "MegaPlants", never spelled out cleanly in the audio) to keep this extraction accurate rather than guessing at the corrupted sections.

### Core Technique
Unreal Engine 5.8's **Procedural Vegetation Editor (PVE)** — an experimental, PCG-based node graph for growing Nanite-ready trees and plants from a **botanical growth simulation** (the `Grower` node) rather than placing pre-made assets, with follow-on nodes for recursive branch scattering, mesh building, bark texturing, and manual art-direction.

### Summary
Simon Barley (Lead Vegetation Artist, Epic — Megascans/foliage team, PVE dev) recaps PVE (introduced 5.7 alongside the **MegaPlants** FAB asset library) and walks through everything new in 5.8: the system is no longer just a black-boxed preset picker — users can now grow trees from scratch using a real botanical simulation, then layer recursive scatter and manual editing on top. The talk is a straight node-by-node tour of the `Grower` node's simulation parameters (phyllotaxy, phototropism, gravity, senescence, hormone/dominance controls), followed by the downstream pipeline: extracting growth data from 2D images/3D meshes, building the final mesh (trunk texture setup, trunk profile presets, mesh builder), a vector-handle system for foliage orientation, a new "Parametric" mode for more direct/less-simulated control, and a Foliage Distribution Network that uses the grower's decay/senescence data to scatter live vs. dead foliage. Talk closes with a roadmap (custom/photogrammetry trunks, branch decorations, leaf-atlas tooling, space colonization, L-systems, viewport sketching).
- **Frame @0:08** — Speaker Simon Barley at the Unreal Fest Chicago 2026 podium (title/intro).
- **Frame @4:41** — The `Grower` node itself: pin list showing `Phyllotaxy`, `Params`, `Growth`, `Phototropism`, `Light Senescence`, `Gravity`, `Age Senescence`, `Bifurcation`, `Directional`, `Foliage`, `Auxin`, `Overrides`, `Growth Cycles` — this is the core simulation node described as "the workhorse of the system."
- **Frame @8:08** — Phyllotaxy diagram: 5 supported branching-pattern types illustrated on a stem (Spiral, Alternating, Opposite, Whorled, Decussate).
- **Frame @16:20** — A rendered forest of conifer/pine-like trees, shown as a "visual example" of PVE output quality (bark detail, canopy shading, ground scatter) once a grown tree is fully textured and placed in a scene.
- **Frame @17:07** — "Not a botanist? Not a problem!" slide showing `Extract from Image`, `Extract from Mesh`, and `Graft` nodes, with the three alternate authoring modes: Extract from 2D (B&W image → PVE data), Extract from 3D (sample a static mesh → PVE data), and Grafting (a more traditional recursive-scatter mode).
- **Frame @23:00** — `Trunk Texture Setup` node: bakes on-disk bark textures (per generation/growth-stage strip) to a target content-browser location for use by the mesh builder.
- **Frame @25:19** — `Plant Profile Loader` node with 10 `Plant Profile` input pins (10 shipped trunk-profile presets) feeding a mesh builder's profile pin, next to a render of a realistic flared tree-trunk base — this profile drives the trunk flare geometry.
- **Frame @36:12** — "Future development" roadmap slide (advanced viewport tools, custom/photogrammetry trunk meshes, branch decorations, Atlas tool suite, state-of-the-art LOD).

### Key Steps
1. **Start from a `Grover`/`Grower` node** — this drives the whole botanical growth simulation and can be chained into other `Grower` nodes to continue simulating from a previous result.
2. **Tune the core simulation inputs**: `Phyllotaxy` (branch arrangement pattern), `Growth`/`Growth Cycles` (more cycles = larger/older tree — not 1:1 with real age, since real trees complete multiple growth cycles per year), `Phototropism` (branches grow toward light / avoid self-shadowing — driven by a top-level dome light you can reposition per tree), `Gravity` (uses a beam-deflection model for branch droop), `Light Senescence` / `Age Senescence` (controls how likely branches are to die from low light, gravity stress, and age — low-light branches die/fall; aged branches dry out, get brittle, and break under gravity), `Bifurcation`/`Auxin` (hormone-style apical vs. auxiliary dominance controls — how aggressively the main leader shoot out-competes side branches for growth budget each cycle; pushing this up/down reshapes the tree from columnar to bushy).
3. **Pick a Phyllotaxy type** per trunk/branch/foliage layer: `Spiral` (helix around the stem), `Alternate` (each new branch on the opposite side of the previous), `Opposite` (two identical branches per node), `Whorled` (several branches per node around 360°, optionally a random count), `Decussate` (like opposite, but each row rotated 90° from the last). Also exposes `Axial Angle` (branch start angle) and a stagger/rotation offset that produces the natural zig-zag seen on real branches.
4. **Optionally restrict growth to a bounding shape** (e.g. a cubic or spherical silhouette) to art-direct the overall canopy form without hand-editing every branch.
5. **Iterate fast via Data Assets**: drag out a `Grower` node's input pins to build a reusable external attribute set, save a tuned grower configuration as a Data Asset, and reuse/relink it across other grower graphs — plus rewind to an earlier point in a tree's growth history and branch a brand-new variant from it with minimal edits (shown creating multiple Hinoki/Japanese-cypress variants this way).
6. **Bring in non-simulated source data when needed**: `Extract from Image` (paints branch structure from a black-and-white image), `Extract from Mesh` (samples branch data off an existing static mesh), or `Graft` nodes (a more traditional recursive-scatter grafting workflow) — any of these can feed back into further `Grower`/scatter stages.
7. **Build the renderable mesh**: `Trunk Texture Setup` bakes disk bark textures into a strip/atlas per tree generation and content-browser target; a `Plant Profile Loader` (10 shipped presets, or your own) plugs into the `Mesh Builder` node's profile pin to drive trunk-flare geometry; the `Mesh Builder` pulls UV data from the texture setup node to map bark correctly.
8. **Use the vector-handle system** for foliage/leaf orientation: user-authored vector handles represent branch length/direction and how much influence they have on attached foliage, with separate aim/fixed-vector and roll/pitch/yaw controls for variation (e.g. droop leaves with a negative-Z handle, flatten foliage with a "foliage flatten" node).
9. **Switch to `Parametric` mode** when you want more direct, less fully-simulated control (e.g. driving branch density/end-generation directly instead of via the hormone/dominance system) — useful for specific tree archetypes.
10. **Distribute final foliage** with the **Foliage Distribution Network**: define your leaf/branch palette at the top level, and it automatically multiplies the grower's decay (senescence) value against the light value during scattering — so higher decay produces visibly more dead branches without manual masking. Null/invisible-branch entries can also be used purely as masking elements to suppress spawn in specific areas.
11. **Package reusable tools as subgraphs**: the demoed `Refit` node isn't a native node — it's a PCG subgraph built from primitives and saved as its own asset, illustrating that technical artists can build their own mini node-library ("small tools and utilities") on top of PVE/PCG's embedded-subgraph support and expose only the parameters artists need.
12. **Control overall mesh cost with a single resolution slider** — remaps a 0–1 resolution value that drives the `Mesh Builder`'s internal mesh-optimization/decimation, so one exposed parameter controls the LOD-like density of the whole tree.

### UE Systems / Blueprints / Settings
- **System:** Procedural Vegetation Editor (PVE) — experimental in 5.8, built on top of **PCG** (Procedural Content Generation), shares UI/features with the standard PCG graph editor, node-based.
- **Asset library:** **MegaPlants** (FAB marketplace) — growing library of tree presets/components introduced alongside PVE in 5.7; 5.8 shifts the offering toward reusable high-fidelity *parts* for building custom trees plus some ready drag-and-drop assets. Supports non-Nanite foliage via a dynamic-wind plugin (the same one used in the Witcher 4 UE5 tech demo) and voxelized meshes at a distance to avoid LOD popping.
- **Core node:** `Grower` — multi-bounce ray-traced light detection drives the growth algorithm; supports collision/interaction with external meshes; gravity via beam-deflection model; branch shading from light/age/senescence; built-in hormone control (apical/auxiliary dominance, bifurcation); supports all major real-world phyllotaxy types. During the Grower stage, foliage is represented cheaply by small "cards" standing in for canopy shadow, and the branch mesh itself is a simplified proxy (final detail comes later in the pipeline).
- **Key `Grower` pins:** `Phyllotaxy`, `Params`, `Growth`/`Growth Cycles`, `Phototropism`, `Light Senescence`, `Gravity`, `Age Senescence`, `Bifurcation`, `Directional`, `Foliage`, `Auxin`, `Overrides`.
- **Alternate authoring nodes:** `Extract from Image`, `Extract from Mesh`, `Graft` (Graft Guide / Graft Rootside).
- **Mesh/material nodes:** `Trunk Texture Setup` (bakes bark texture strips to a content-browser target, per tree generation, with tiling control), `Plant Profile Loader` (10 shipped trunk profiles, feeds `Mesh Builder`'s profile pin, drives trunk-flare geometry at the base), `Mesh Builder` (consumes UVs from texture setup + profile, has a single resolution slider driving mesh optimization/decimation), common material node for custom shading (separate from native PCG material assignment).
- **Distribution:** `Foliage Distribution Network` — top-level palette definition + decay(senescence)-driven scattering (decay × light value), supports null/invisible branches as spawn masks; a condition system can key distribution off attributes like age, branch length, tip, health, and generation.
- **New 5.8 mode:** `Parametric` mode — bypasses hormone-driven simulation for more direct density/end-generation control.
- **Reusability:** `Grower` configs can be saved as Data Assets; whole node clusters (e.g. the demoed `Refit` node) can be packaged and saved as PCG subgraph assets for a personal/studio function library.
- **Console/Editor:** No console commands or Blueprint/Python API mentioned — this is purely PVE/PCG graph-editor authoring.

### Difficulty
Advanced — requires solid PCG/node-graph familiarity plus botanical-simulation vocabulary (phyllotaxy, phototropism, senescence, apical/auxiliary dominance). Building custom reusable subgraphs (the `Refit` node example) pushes into Expert territory.

### UE Version
UE 5.8 (PVE marked **Experimental**). PVE and MegaPlants were originally introduced in UE 5.7; this talk covers what's new for 5.8 specifically (from-scratch growth simulation, image/mesh extraction, texture/profile/mesh-builder nodes, vector-handle system, Parametric mode, Foliage Distribution Network).

### Tags
pcg, nanite, modelling, geometry, materials, advanced, ue5-8

---

## Related Tutorials
Cross-linked from `tutorials/INDEX.md` on entries sharing 2+ tags with this one (`pcg`, `nanite`, `materials`, `advanced`):

- [`large-scale-animated-foliage-in-the-witcher-4-unreal-engine-5-tech-demo-unreal-f.md`](large-scale-animated-foliage-in-the-witcher-4-unreal-engine-5-tech-demo-unreal-f.md) — "Large Scale Animated Foliage in The Witcher 4 Unreal Engine 5 Tech Demo" (tags: `nanite, pcg, rendering, pipeline, advanced, ue5-7`). Directly relevant: this PVE talk explicitly name-checks the Witcher 4 demo's dynamic-wind plugin as the same one MegaPlants uses for non-Nanite foliage. That talk covers the Nanite-foliage + custom vertex-wind-shader + PCG placement solution shipped in 5.7 that PVE/MegaPlants builds on top of in 5.8.
- [`how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep.md`](how-to-grow-a-forest-in-unreal-with-pcg---procedural-content-generation-pcg---ep.md) — "How To Grow A Forest in Unreal With PCG - PCG Episode 5" (tags: `pcg, blueprint, pipeline, intermediate, advanced, ue5-7`). Useful contrast: classic hand-built PCG forest scattering (Surface Sampler/Density Filter/Copy Points density falloff) vs. PVE's purpose-built botanical `Grower` simulation covered here — same end goal (growing forests), two different-generation tools.
- [`automatic-landscape-tree-blending---procedural-content-generation-pcg---episode-.md`](automatic-landscape-tree-blending---procedural-content-generation-pcg---episode-.md) — "Automatic Landscape Tree Blending - PCG Episode 6" (tags: `pcg, materials, landscape, rendering, pipeline, advanced, ue5-7`). Relevant follow-on once PVE trees are grown/placed: this covers blending their trunks/roots into the landscape material via a Runtime Virtual Texture.
