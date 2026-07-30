---
title: A Deep Dive into GPU Crashes in UE5 | Inside Unreal
source: YouTube
url: https://www.youtube.com/watch?v=Ib_nFhgF4vk
author: Unreal Engine
ingested: 2026-07-30
ue_version: "UE5 (general, discussion spans older and newer UE5.x releases including UE5.8-era residency defaults)"
tags: [gpu-crash, directx12, rhi, rdg, debugging, aftermath, dred, residency, page-fault, shipping-build, performance]
extraction_status: complete
frames_dir: tutorials/frames/a-deep-dive-into-gpu-crashes-in-ue5-inside-unreal/
frame_count: 8
frame_status: complete
frame_selection: content-anchored (manual timestamps chosen from transcript, not blind percentages)
---

# A Deep Dive into GPU Crashes in UE5 | Inside Unreal

**Source:** [YouTube](https://www.youtube.com/watch?v=Ib_nFhgF4vk)
**Author:** Unreal Engine
**Duration:** 75m15s | 1 section(s)

---

## Raw Data (for Claude Code extraction)

Frames captured — see "Captured Frames" section below.


### Full Content [0:00]
**Transcript (timestamped):**
[0:00] ics,
[0:04] coworkers.
[4:39] Hello, hello, everyone, and welcome back to Inside Unreal, a show where we learn, explore,
[4:46] and celebrate everything unreal. I am your host, Dan Hutnick, and today I am joined by a very
[4:54] special guest, Kuiwen Zhang, who is here to talk to us about some practical tips.
[5:02] Back to Inside Unreal, a show where we learn, explore, and we're getting a little audio feedback from you.
[5:11] I think it stopped. Okay, no worries. But it's here to share with us some tips on
[5:16] investigating and fixing GPU crashes inside UE5. So welcome to the show, Kuiwen. Why don't you go
[5:24] ahead and let folks know a little bit about you. Hello. Hello, everybody. I'm Kuiwen from
[5:32] Cersei Studio. I have been working in computer graphics for more than 10 years and in the game
[5:38] industry for about eight years. I have participated in the development of products such as Game 4
[5:44] Peace and PUBG Mobile. And I'm currently the engine lead on the Fit Trigger product,
[5:50] which is a Stalelight cartoon shooter game. Having used UE5 since early, as one of the early
[5:58] adopters, I'm very excited about the visual improvements UE5 has brought us, especially for
[6:05] open world projects. However, because the Direct Desk 12 is too flexible, we also encounter
[6:12] many GPU crashes. For a while, these GPU crashes become a real nightmare for us.
[6:18] But now, as we have a deeper understanding of UE5 and with technical support from Epic and
[6:26] hardware vendors, we have finally resolved most of them. We have also noticed that Epic and
[6:33] hardware vendors have done a lot of work on debugging tools this year, which I will also
[6:40] cover in this talk. You could say it's the right time, right place. Or I'm very happy to be here
[6:47] to share our experience with everyone and contribute to the Unreal community together.
[6:53] Yes, and we're very happy to have you here. This is the kind of issue that I don't think
[6:58] everybody deals with all the time, but when it happens, it's extremely frustrating and can be
[7:03] very hard to know where to start, how to solve it, especially if you are an artist who doesn't have a
[7:08] whole lot of programming background experience and things like that. So definitely glad to have
[7:13] you here to come and talk to us about this. I know we have a lot to talk about here. I know
[7:19] that you brought some slides and stuff to go through before we jump into that though. If anybody has
[7:24] any questions for you when here during this talk, if you are watching the video live,
[7:30] please put in the chat question in brackets followed by your question, and we will gather as
[7:35] many of those as we can and toss them towards the end of the show. If you have any questions that are
[7:41] beyond the scope of this particular topic here, that's okay. Please head over to the Epic Developer
[7:47] Community, the EDC, where we have our forums, documentation, tutorials from Epic staff and
[7:52] community alike, and so much more. But with that, I think I'm ready to jump in.
[7:59] Okay, thank you then. Let's do it. So let's start. The story starts with DRX-12. In DRX-11,
[8:11] the driver did a lot of work for you, including hardware tracking, validation checks, and so on.
[8:17] But DRX-12 moves in the opposite direction. The driver should not guess your intent.
[8:25] The engine should explicitly describe what it wants. So DRX-12 does not automatically make your
[8:34] program faster. It gives a well-designed engine the opportunity to be faster. If you change something
[8:41] roughly, DRX-12 will kind of easily become slower and more fragile, which means more GPU crashes.
[8:50] This picture is giving me PTSD. I also feel the same.
[8:58] I can hear the sound of it popping up. Even though there's no sound here, I can hear it in my head.
[9:06] Oh, this is a nightmare fuel, bro. So okay, let's go on. I'm going to give you an overview.
[9:16] We will focus on GPU crashes on PCs, especially under DRX-12. Some of the experience can also
[9:22] apply to DRX-11 and the consoles. Firstly, we will look at what a GPU crash is,
[9:30] the categories of GPU crashes, and how they happen. Secondly, we will introduce the debugging workflow,
[9:38] including how to use different debugging tools and what each tool is best suited for.
[9:46] Then we will discuss common GPU crash scenarios, where I will share some real cases we encountered
[9:54] in production. After that, we will go through our best practice, including testing methods,
[10:02] automatic workflows, and release considerations. Finally, we will briefly
[10:08] cover some other frequent crash issues related to GPUs and graphics APIs.
[10:15] So, firstly, what is a GPU crash? Let's compare the GPU mechanism with CPUs. The CPU execution
[10:25] model is relatively straightforward. The system executes instructions
[10:33] sequentially once a program crashed. The system can generate a mini dump based on the state at
[10:42] that moment, including register state, call stacks, and so on. In Unreal Engine, if a CPU crash occurred,
[10:53] the call stack will also appear in the log. But the GPU is controlled by the CPU through
[11:02] graphics API calls. The CPU does not know exactly how the GPU executes those commands.
[11:11] The GPU also does not notify the CPU when it finished running. And even when the GPU encountered
[11:19] error and crashed, the CPU may not know immediately. So the CPU only learns that the GPU has crashed from
[11:29] the return value of a subsequent API call. In addition, because the GPU is massively
[11:38] parallel, without debugging tools, we often do not even know which API call caused the GPU crash,
[11:46] let alone which function or operation was responsible. So,
[11:57] most graphics API call return code, which is each result. If the GPU has crashed,
[12:06] the next API call will return an error each result. After that, we can call get device
[12:13] remove reason to obtain a more specific crash reason.
[12:21] So there are also cases where no graphics API call happens for a long time afterwards.
[12:28] In that situation, the system's TDR mechanism will be triggered. TDR stands for timeout
[12:36] detection and recovery. It is a Windows mechanism for detecting that the CPU appears stuck,
[12:44] residing the graphics stuck, and trying to recover the desktop without forcing the whole
[12:52] machine to reboot. So if you receive a TDR error, there are two possibilities. First one is a task
[13:01] run for too long and was killed by the system. The other is the GPU had already crashed for
[13:08] some other reason and the TDR detected it. Let's briefly go through these crash reasons first.
[13:19] The most common crash reason is device removed. It can be caused by hardware removal or
[13:26] driver reset. Sometimes a task times out and triggers the TDR, but the crash reason we get
[13:36] is still device removed rather than hung. This depends on the driver. The driver reports the
[13:46] consequence. Now, the most of this is root cause. Beyond these cases, the real underlying error is
[13:54] very often some kind of page four. A GPU page four means that the GPU access the address that could
[14:03] not be legally translated. The system or driver usually cannot simply skip this access and continue.
[14:15] So it makes the device as lost or removed and request the application to recreate the device.
[14:26] This is where device removed comes from. Another common crash reason is device hung. This usually
[14:34] means the GPU stopped making progress while executing work from your application. This is the
[14:42] one most associated with bad GPU work, such as infinity loop or extremely long works.
[14:53] These two are the most common reasons. So device removed tells you the old device is no longer
[15:01] usable and device reset tells you one more possible reason that the device was reset by the OS or
[15:08] driver. But you will notice that these crashes and do not prove was enough information by themselves.
[15:18] So next we will talk about the debugging workflow for GPU crashes.
[15:27] So what should we do when we encounter a GPU crash? First, we check the API return value,
[15:35] which is the error category mentioned earlier. Is this device removed hung or something else?
[15:45] But the error category is too broad, so we also need more detailed information. This information
[15:52] can usually be obtained from the log when debugging tools are enabled. Once we understand the problem,
[16:01] we need to find a way to fix it and that requires location more detailed information.
[16:12] There are pretty problems we can identify the suspicious events around the time of the crash.
[16:20] For deeper investigation, we need tools that can provide hardware level information, such as
[16:26] other mass, the RGD and the DX stamp. I will introduce how to use these tools and collect
[16:35] information in the next few slides of this park. If we still do not have enough information,
[16:44] we may need to enable the D3D debug layer or GPU based validation to reproduce the issue.
[16:52] However, these options have a heavy performance cost, so we usually enable them only in automated
[16:59] tests. Next comes analyze and classification.
[17:10] Multishader and state set up issues are relatively easy to fix. Once we have enough information,
[17:19] if the issue is residency related, it may be a resource flag problem. If it is UAF for
[17:32] use after free, it may be a resource management problem. If the issue is very strange and the
[17:43] driver is old, it may also be an earlier driver bug.
[17:51] And then the family just fix it. Next, I will introduce each tool one by one.
[17:58] The first one is D3D debug, also known as the DR-12 debug layer. It requires GPU graphics tools
[18:08] to be installed on the machine. You can find it in the system setting. Otherwise,
[18:14] enabling it can cause a crash at the runtime. There are two ways to enable the debug layer.
[18:22] The first is through DX-CPL, the debug-desk control panel, where you can enable the debug layer and
[18:31] GPU validation for selected programs. For UAF, the more convenient way is to modify console
[18:38] variables or use launch arguments. In actual testing, you can use the D3D log learnings parameter to
[18:50] expose more issues, just like this.
[18:56] The D3D-12 debug layer validates many CPU-side API contract violations, such as resource barrier
[19:06] errors, descriptor errors, and so on. For example, let's say the shader expires four SRVs, but the
[19:16] descriptor table contains only three SRVs. If the debug layer is not enabled, DR-12 may not catch
[19:26] it at draw time. It may simply let the GPU execute and the GPU may read a wrong descriptor. This is why
[19:36] DR-12 is powerful but dangerous.
[19:43] If the debug layer is enabled, it will report an error like this, allowing us to find the
[19:49] problem before it actually causes a crash. In this example, I missed a transition call,
[19:58] and the D3D-debar layer gave me a warning message. In practice, D3D-debar can catch many
[20:06] potential issues. It is useful to automatically test regularly and check the logs for any
[20:15] debug layer warnings. That said, the debug layer is still a CPU-side tool. What if we want to
[20:23] check further on the GPU side? There is an upgraded version of D3D-debar, GPU-based validation,
[20:34] commonly abbreviated as GVV. GVV is an enhanced mode of the debug layer, but it checks at the
[20:42] later point when the GPU actually executes the command. As an enhanced version of D3D-debar,
[20:51] GVV requires D3D-debar to be enabled first. Here is an example. If I pull the
[21:01] sync color buffer render target into the described table as an SRV, the normal debug layer does not
[21:09] know which SRV the shader will actually sample at runtime, so it will not report a result state error.
[21:18] GPU-based validation, however, performs additional checks at GPU execution time.
[21:26] Through shader instrumentation, common list patching and similar techniques, it checks the
[21:36] descriptors and results states actually accessed by the shader on the GPU side. So when the shader
[21:46] samples the result, GVV can detect that the result state is incorrect and report
[21:54] GPU-based validation incompatible results state such as errors.
[22:04] So through shader instrumentation is very common, so as you can see the GPU validation can find
[22:15] many results that only appear during actual GPU access, but this also means it introduces
[22:24] higher runtime overhead. The next one is dried. Our device removed extended data.
[22:34] It is a native DX12 diagnostic feature explicitly built to help developers
[22:45] track down GPU crashes. It mainly provides two major features, auto break-ramps.
[22:52] This one used to record recent GPU work while pit-forged reporting does exactly what the
[23:02] name suggests it. If device removal is caused by a GPU pit-forged, dried reports are matching
[23:11] the locations, nodes for active and recently free runtime objects. So this is what the auto
[23:26] break-ramps output looks like. Here is a lot of markers in the common list. And this one is the
[23:37] GPU pit-forged reporting structures.
[23:43] Recramps is a diagnostic tool that acts like a GPU cost-ex, helping track rendering commands and
[23:54] track the exact point of a graphics crash. However, note that this so-called cost-ex
[24:03] is at the API core level. It can tell us which path or draw call is recently
[24:11] execution team, but not which function inside the shader is being called.
[24:19] Regarding break-ramps, CD projects write a very detailed talk on the topic at Unreal Fest
[24:28] before. If you are interested in it, you can check it later.
[24:34] The difference between UeBrew Crumbs and Dried Break-ramps is that UeBrew Crumbs records
[24:41] all markers submitted in the current frame and displays them hierarchically. So it usually provides
[24:50] more context than Dried. Dried on the other hand shows the common list and includes more low-level
[25:01] API calls. However, because of GPU parallelism, neither of them can perfectly identify which draw
[25:11] or dispatch calls the problem. You can see that break-ramps may show many active events.
[25:21] So you don't know which one is the one caused the GPU crash. Dried may list
[25:29] two events here and one beginning event because this is parallel.
[25:37] Anyway, these two still cannot identify which shader function or even which instruction causes
[25:45] the average problem. If we want to go deeper, what can we do? Today, major winners provide us some
[25:55] options. The first one is Aftermath. Aftermath is NVIDIA's GPU crash debugging tool. It provides
[26:04] a large amount of information and is very helpful for GPU debugging.
[26:10] There are two ways to use Aftermath to monitor GPU crashes. One is to integrate the
[26:19] Aftermath SDK into the application, which is what UE5 does. The other is to run Aftermath monitor
[26:27] in the background, which is a software shown here. After Aftermath is enabled, when the
[26:37] programmer crashed, it generates an NVGPU-down file. This file can be opened in inside graphics
[26:49] and contains various crash-related information. In general, enabling the monitor provides more
[26:58] information, although some information can only be viewed by opening the file in inside graphics pro.
[27:07] The UE5 has already integrated the Aftermath SDK. In UE5, Aftermath can be enabled through
[27:21] console variables or launch arguments. One thing to note is that before the latest R615 driver,
[27:32] Aftermath did not support the D3D debug layer. Also, if a RENDOCK auto-attach is enabled,
[27:40] creating the Aftermath device may return not compatible with D3D debug layer error.
[27:49] Aftermath has several feature flags that can be configured through these UE5
[27:56] console variables to provide more information. For example, resource tracking is very helpful
[28:02] when debugging page 4. Another important option here is dump shader debugging for
[28:09] for crashes inside shaders. It can generate a file named NVG. Together with the shader
[28:17] binary and the PDB files, these can help identify the exact source line that causes the problem.
[28:27] Like this, we can locate the issue very precisely.
[28:36] By the way, most of the information in NVGPU-down file can actually be opened
[28:44] through Aftermath SDK. UE5 outputs a lot of debugging information in this area, so once
[28:53] Aftermath is enabled, you can get a lot of useful information directly from the log.
[29:05] For example, the crashes shader hash can use to locate the specific shader field.
[29:12] If call stack capture is enabled, we can also get the function where the crash occurred.
[29:21] For P4 crashes, we can see the 14VA and the related sources and so on. It is extremely convenient.
[29:31] Here is some good news. Last week, Aftermath released its latest update for this year.
[29:43] According to the official release notes with the upcoming R61 file driver, NVGP files will be
[29:53] eventually merged into the NVGPU-down files. They also made memory optimizations,
[30:01] and in our previous testing, Aftermath did indeed have some high memory usage.
[30:09] It also looks like they added support for resource lifetime and residency events,
[30:16] which will be very helpful for investigating residency-related crashes.
[30:23] More importantly, the latest Aftermath while supporting enabling the D3D development layer at the same time.
[30:33] This will be very convenient for internal testing.
[30:40] I expect the new driver should be released soon, and I'm really looking forward to it.
[30:48] In terms of AMD, the AMD reading GPU detective is an AMD's GPU crash analysis tool.
[31:04] Similar to in radius Aftermath, but currently it is not provided as an SDK.
[31:10] It needs to run in the background and be attached to the application to capture crash information.
[31:18] The crash information has both a simplified version and a detailed version,
[31:24] and it is output as a text file that can be opened directly, which is very friendly for AI analysis.
[31:33] However, the need to attach it makes it less convenient for the real or intermittent crashes.
[31:44] In the future, when Microsoft will open the DX-down files,
[31:55] the new drivers should be able to capture crashes without requiring a background tool.
[32:02] Anyway, for these consistently reproducible crashes,
[32:09] AMD currently provides the most information because it includes Results Residency State.
[32:18] I will go into more detail later with the troubleshooting case,
[32:23] but right now let's still focus on debug tools.
[32:28] UIS supports Intel GPU crash dumps based on the description.
[32:35] It seems to be a background-like mechanism, but we haven't used it yet.
[32:43] If you have a crash on the Intel device, you can try it.
[32:49] And this year's GDC, Microsoft shares a new way to debug GPU crashes, that is direct-text-down files.
[33:04] So to do this year is a big year.
[33:08] At the moment, direct-text-down files are still in previews and feedback collection.
[33:15] Their main goal is to provide a unified GPU crash investigation workflow that works across all hardware.
[33:27] The way to use it is to first integrate the SDK.
[33:32] Note that it currently only supports development builds and cannot be used for public release builds.
[33:40] Microsoft has a new way to use it.
[33:44] Microsoft currently provides several ways to generate DX-down files.
[33:51] We tried them and found that the different methods produce slightly different information,
[33:58] but the final details were still different on the official release.
[34:03] The generated DX-down file can be opened and analyzed in the PIX app.
[34:12] For the GDC presentation, NVIDIA, AMD, Intel, and Qualcomm will all support this in the future.
[34:21] Looking at the recent updates to Aftermath and RGD, they also appear to be moving towards supporting
[34:30] this standard.
[34:32] The exact timing for official public release support is still unclear.
[34:38] I imagine the Unreal team is also preparing to integrate it right.
[34:49] The next I will withdraw some concrete crash examples and explain the troubleshooting process
[34:57] in more details.
[34:58] Let's look at the pitfall series.
[35:04] In DLS-12, the GPU usually accesses resources through GPU virtual addresses or VA.
[35:14] Descriptors, root descriptors, and acceleration structures eventually lead to GPU VA.
[35:23] The GPU MMU translates the VA through PIDG table,
[35:29] maintained by the driver and WDDIME or VMM.
[35:35] If the VA has no valid mapping points to release the resource, all the backing heap is non-resident.
[35:45] The translation will be for and a pitfall will occur.
[35:52] The pitfall itself only means that the GPU accesses invalid and currently
[36:00] in a successful virtual drive.
[36:02] The real root cause still needs to be investigated based on the source.
[36:13] So there are several possible causes here.
[36:17] Firstly, such as SM error, after mesh will be showed SM error at the GPU downfall.
[36:32] So that usually means the SM or streaming multiprocessor accesses an
[36:40] available address, which is essentially an auto bounce.
[36:46] This type of issue is relatively easy to fix.
[36:50] After mesh RGD or DXDump can all provide the exact instruction location of the crash.
[37:00] Then we can add some auto bounce protections.
[37:03] But there is one special case here, SM crash address 0x00.
[37:13] This may be caused by an unbound uniform buffer or it may be related to the architecture or driver.
[37:23] Like this.
[37:24] Next one, MMU fault.
[37:30] This usually means that an error occurred while translating a VA.
[37:38] This indicated that the current VA is no longer valid.
[37:43] The most likely causes are that the result was evicted or released.
[37:49] But it can also be caused by incorrect resource binding.
[37:54] We also encountered some residency related issues.
[38:00] So let me first introduce the concept.
[38:04] In DRUG-DOS 12, residency refers to the state of the resources video memory.
[38:14] So whether it is present in memory that the GPU can directly access is
[38:23] there are two states here, resident and evicted.
[38:28] Compared with DRUG-DOS 11, DRUG-DOS 12 is more explicit.
[38:34] The application or engine needs to actively track the VRAM budget and ensure that resources are
[38:43] resident before the GPU use them.
[38:47] In contrast to resident, evicted means the resource object still exists.
[38:54] But the video memory is temporarily not in GPU accessible.
[39:04] This is different from released or destroyed.
[39:07] Released means the resource object or its underlying locations has already been freed.
[39:16] So the resource no longer exists.
[39:18] When VRAM pressure is high, the system or engine can evaluate the temporary
[39:25] and use the resources to free budget.
[39:28] But if a GPU command exists, this evicted resource, it can cause a pitch forward.
[39:38] In short, the core core of residency management is to balance performance VRAM usage and the
[39:47] resource validations.
[39:54] UE5's residency management is based on DRUG-DOS 12 residency third-party libraries.
[40:06] This is the official usage description.
[40:10] In UE5, each common list creates a residency site which stores the
[40:18] site of all resources and heaps that need to be resident when the common list is executed.
[40:27] One difference between the latest UE5 version and the earlier residency management is that
[40:34] resources are created as evicted by default.
[40:39] On one hand, this can avoid implicit system memory paging.
[40:45] On the other hand, it causes make resident to be called more often,
[40:52] which also makes the system more tolerant of normal cases.
[41:04] So let's look at a case where a residency error caused a pitch forward.
[41:10] This example is a good opportunity to explain how to analyze the crash caused with AMD-RDD.
[41:21] First, from the basic information, we can see that this is a pitch forward crash.
[41:27] And we open the virtual drive where the crash happened.
[41:34] Through the resource timeline, we found that the heaps that were evicted here.
[41:42] This is highly suspicious because UE5 textures are mainly managed in these heaps.
[41:50] We found that heaps resource ID and use it, we can search for the virtual drive bound to 8.
[42:00] Tada! The 14 results happened to be inside the heap, which confirms our suspicion.
[42:12] Now, for a similar example, if aftermast is enabled,
[42:17] an NVGPU down file will be generated in the record forward and the crashes.
[42:28] If aftermast shader debug info is also enabled, the crash occurs inside a specific shader.
[42:41] The NVGPU files will also be generated. Of course, as mentioned there, these two
[42:49] files will be merged into one in the new driver.
[42:54] In general, after citing the shader, search passes inside graphics to point to the shader
[43:03] sample folder and said, well, automatically search for shader samples. Of course,
[43:09] shader samples need to be enabled first in the console variable.
[43:15] But in a real project, the number of shaders can be very, very huge and the shader search can
[43:23] easily take more than I think 10 minutes, which significantly hurt efficiency.
[43:31] So, I strongly recommend first find the corresponding shader hash in the log and copy
[43:46] this one to find the real shader files. Then put them into the same crash folder.
[43:55] It's a log shader search to complete it almost instantly.
[44:02] For pitfall examples in aftermast shader source view, we can see the last executed location
[44:14] with the yellow point and the exact instruction that calls the crash with the red icon.
[44:24] However, the current driver does not yet support residency events. At the moment,
[44:32] I personally feel that the residency information in aftermast is not very accurate enough.
[44:41] So, we will need to be waiting for the later version.
[44:46] I used the latest version of inside, so this view comes here. And if you use the older one,
[45:00] you won't see that. During some of the earlier RDG refactoring work,
[45:10] we run into many pitfall crashes related to buffers, especially structured buffers.
[45:17] So, aftermast, we found that these resources had already been destroyed. That is very strange
[45:26] like this, because it's not evicted, it's just destroyed and GPU uses it after that.
[45:36] At first, we suspected that the easel might be caused by buffer sizing. However, after
[45:46] increasing the initial buffer sizes, the situation did not improve. We also tried
[45:52] disabling various parallel execution options, but the crashes still occurred. After a series of
[46:03] baby tests, we started to suspect that this was an RDG resource management issue. However,
[46:10] due to our project version plans, we did not have enough time at that point to make deeper
[46:19] modifications to the RDG module. Eventually, we discovered something quite interesting.
[46:27] When we changed the problematic GPU-sync-related buffers into texture-based implementations,
[46:37] the crash almost disappeared. Our analysis was that texture resource management is
[46:47] relatively more conservative. First, texture is still really more on the long-established
[46:57] whole render target system. Secondly, even when a texture resource becomes invalid,
[47:03] its underlying memory is more likely to be reused by later texture locations
[47:11] rather than being immediately released. This provides a possible workaround. If you encounter
[47:20] similar paid-for issues, one thing worth trying is to reimplement the results as a texture instead
[47:30] of a buffer. However, our final analysis was that the root cause was likely a read-write
[47:38] risk involving the external be extracted and be produced. This issue was later fixed in
[47:51] newer UI versions, so the newer version is more stable.
[48:02] This is an example of a Shader Infinity loop causing TDR.
[48:09] Aftermath shows the status as timeout and the device state is hung.
[48:19] Most hung cases mean the shader is still ringing. Although we have also encountered hung cases
[48:28] caused by auto-bounds copy buffer region operations, anyway, using the same method
[48:36] aftermath data shows that the hung indeed occurred inside the shader, and the last executed location
[48:47] is indeed the Infinity loop. RDG can also show the crushed task and shader.
[48:56] Or in my screenshot, the compile options were not sized, so the shader name was not available.
[49:09] However, the shader can still be found through the hash and the following assembly instructions
[49:18] also indicate the crushed location.
[49:25] Currently, drivers are much more tolerant of instruction errors. So these days, instruction
[49:34] error is more likely to be caused by a neural conditions, such as upgrading the driver without
[49:43] cleaning the shader catch or other abnormal user-side operations.
[49:56] Okay, next I will introduce some experiences from real projects.
[50:03] First is UE5's GPU debug shader. You can trigger a crush through the GPUDevugCrush command.
[50:11] It provides the following options and is very useful when testing mechanisms such as RHI and RDG.
[50:20] One thing to note is that in UE5.8, resources are created with the flag that creates not resident
[50:32] flag by default. So if you want to trigger a GPUDevugCrush paid for it, you need to enable
[50:44] console variable called resource.started.resident or just disable the residency management macro.
[50:53] Because many GPU crushes are intermittent crush reporting and collecting are extremely important.
[51:07] Most crush reporting platforms support customized automation workflows such as
[51:17] automatically download GPU crush reports and processing log information with scripts
[51:24] or sending it to AI for analysis and generating analysis reports and fix suggestions.
[51:32] So this is our pipeline.
[51:42] As AI compatibility continues to improve, we have built an automated crush and analysis pipeline.
[51:57] So by integrating with the crush reporting platform and M2,
[52:06] the pipeline can automatically process reported crushes, provide accumulated knowledge to AI and
[52:14] analyze new crush cases. Currently, the pipeline is integrated with the
[52:23] aftermath SDK in our project. However, when the desktop is released,
[52:32] I think it's very easily to extend it in the future to support crushes across our hardware platforms.
[52:43] To reproduce more GPU issue, we also wrote many automatic scripts that
[52:50] remind the game during idle time. These are the different configurations we use on different
[53:01] machines. The reason why GPU has two different configurations is that before the R615 driver
[53:11] updates, aftermath and D3D debug layer were not compatible with each other. So we have
[53:19] half of our machine to run the aftermath and the other to run the D3D debug.
[53:28] Instead, we use enhanced version GPU validations.
[53:36] The GPU crush debugging option enables multiple GPU debugging tools, including
[53:43] aftermath, Droid and Brick Cramps. It also enables track all allocations
[53:52] that is very useful for debug pitfall issues.
[54:00] As mentioned earlier, to expose as many issues as possible, we also run multiple background
[54:07] programs to try to fill out the VROM.
[54:18] During automated testing, besides these debugging tools and launch arguments,
[54:25] we also use various console variables to investigate the issues.
[54:30] These settings can also be added to automated scripts.
[54:35] To get more information, we use development, build and enable a series of markers to provide
[54:43] more context. For crash investigation, the most important thing is reproduction.
[54:52] We have summarized several ways to increase reproduction probabilities, which can be used
[55:02] as reference. The most effective method is to increase VROM usage.
[55:11] Both you, your residents manager and hardware driver make certain decisions based on the
[55:20] remaining VROM budget. In practice, we found that on some AMD machines, if there is plenty of
[55:29] available VROM, the eviction may not actually happen.
[55:36] In addition to increased VROM usage, there are also a series of options here.
[55:44] If changing one of them makes the crash happen more often, that is a useful signal. For example,
[55:51] lowering residency debug budgets can trigger residency behaviors more often for stress testing.
[56:01] If crashes increase at that point, the crash may be residency related.
[56:08] Note that many of these options are dangerous and should not be configured in test or shipping bills.
[56:16] In addition, we can remind the ABA tests to verify certain hypotheses.
[56:29] For example, many issues make people suspect the synchronization problems caused by
[56:39] parallelism. In that case, you can disable different parallel switches and check whether the issues
[56:46] still reproduce. At least some switches here, some of them feature overlaps.
[56:56] We can also rule out whether the problem is related to residence manager or barriers
[57:04] or various RDD debug options. If disabled debug test 12 VROM diff rack makes the crash disappear,
[57:16] then the issue is related to the poor management.
[57:24] So that is an important question. Which debugging tool can be enabled in a release field?
[57:33] Because we have many crashes that only appear once.
[57:41] So this is our conditions.
[57:46] A3D debug and GPU validation have a very large performance impact and they require the graphics
[57:54] tools to be enabled to run. So therefore, they are not suitable for release bills.
[58:02] They can be enabled during internal compatibility testing to catch certain issues.
[58:09] Brickramps also have a noticeable performance cost. In our project, enabling the release
[58:17] FPS by about 7 to 9 frames. Well, the information they provide is limited, so I would not strongly
[58:29] recommend them either. Dread has a relatively low performance overhead, although it does not
[58:38] provide a large amount of information, it can still serve as useful supplementary data.
[58:47] After mass, if only shader info is enabled, it has relatively low overhead, roughly a
[58:57] three-frame FPS drop in our project. However, early versions of after mass can have considerable
[59:09] memory usage if the project already has high memory usage, this need to be considered carefully.
[59:18] After mass combined with resource tracking and the D3D12
[59:28] track all applications is very helpful for the paid-for investigation.
[59:34] Based on the current description, DXDump also looks suitable for release bills.
[59:42] We can test it performance later.
[59:48] Besides engine sightings, when releasing the game, we should also guide the users as much as possible
[59:58] to take actions that improve the stability, such as cleaning the shader catch and upgrading the
[60:09] drivers. Increasing virtual memory size is an effective way to avoid OEM that is out of memory
[60:18] issues. Some overlay software that monitors frame rate can also affect stability, so just tell your
[60:30] user disable it. For some game projects that started earlier, they may still be using older
[60:44] UE5 version. Some projects update the engine regularly, while others have already shipped
[60:52] and may not want to keep upgrading the engine, so they remain on early UE5 version. For these
[61:01] users, I have some GPU crash-related upgrade recommendations. First, the debug tool.
[61:10] UE5's after mass module updated both last year and this year, making investigations more convenient.
[61:20] In particular, the shader hash passing part can greatly improve efficiency.
[61:27] Since after mass is also a relatively isolated module, the risk is not high, so I strongly
[61:36] recommend upgrading it. In the latest UE version, RHI and RDG management are also more mature.
[61:46] If conditions are low, I recommend upgrading them as well. However, I have to say that these
[61:54] changes have a large impact and require minor internal testing. If a full upgrade is not possible,
[62:05] updating only the debugging information modules can still help.
[62:10] Residence management has also received some updates. The goal of newer UE version seems to be
[62:21] put more residency control into UE's residency manager and reduce immediate VRAM usage when
[62:31] resources are created. Overall, VRAM usage and the VORI random implicit pages by the system
[62:44] with online. Making the residency behaviors more predictable and easier to debug.
[62:59] I think the new version has some protection mechanisms. If you have the
[63:14] residency related crushes, just upgrade this part. If you project use bandless bit heavily,
[63:24] I also recommend upgrading the descriptor range module. It also fix an important gap
[63:32] that residency tracking for bandless descriptor ranges. Rdg as I said before, we made the
[63:44] buffer and structure buffer crushes. The new version of Rdg is more mature, so
[63:54] just upgrade it if you have the condition. Finally, I will briefly mention some other
[64:06] GPU related crushes that we frequently encountered. One is PSO easel.
[64:18] But most PSO creating easel can be denoted in detail by enabling the debug there. For cases that
[64:28] are difficult to reproduce, our approach is to generate an internal mapping table from PSO
[64:35] hash to shader name. This at least allows us to identify the problematic shader and then inspect
[64:46] it further. So present value is the top three crush in our project. They often have the
[65:01] boundary between the engine, DSGI, and the swap train, the window system.
[65:10] One issue we saw that is early DRSS frame generation versions did not work well with frame generation
[65:21] with enabling or when the frame generation was enabling and the window was resized,
[65:29] all the display mode has changed. Another common issue is invalid for screen or
[65:39] tiering settings. For example, the DSGI present a low tiering request swap train to support tiering.
[65:52] If prison fails because of a temporary state transition, retrain a few times
[65:59] can help. But if the error is device removed or device resized, we should treat it as a real
[66:07] GPU crush. So that's all. If you encounter any GPU crushes, feel free to reach out and discuss them
[66:16] with me. I'm very interested in this topic. That was great. There was a very deep dive.
[66:26] A lot of folks here, I've seen a couple people talking about crashing issues they had here.
[66:32] Actually, I'll read this chat message real quick where it says,
[66:36] definitely install aftermath. This sounds handy. You've already gotten one person on board.
[66:43] Awesome. Thank you so much for going through all of that. That was a lot of talking. So I'll
[66:47] give your voice a second to recover before we jump into the Q&A side of everything. With that,
[66:53] if you have any questions for our guest here specifically about GPU crashes with Unreal Engine
[67:00] 5, please leave in the chat question followed by or sorry, chat question in brackets followed by your
[67:07] question and we will gather as many of them as we can and toss them over to our guest here.
[67:14] This one, I think it's just a fun interesting one, which is what was the most difficult or confusing
[67:21] GPU crash that you've had to solve so far?
[67:28] I think it was the buffer and structure buffer crash we talked before because at that time we
[67:40] don't know we don't gain too much in the aftermath. So we don't know we can
[67:48] enabling these feature flags. So if you don't have the resource flags enabled, you can't
[67:59] know what is the things going. Absolutely. I think that was the most difficult one.
[68:08] Yeah. We had another one here. I think you've largely touched on it, but maybe we could
[68:12] simplify it into a single question here. One of the questions we had is what is the main
[68:20] tool you use most often? Sounds like aftermath came up quite a fair bit, but what is the one that
[68:27] ends up being the most consistently used with your debugging?
[68:32] Actually, it's aftermath, right? Because aftermath can
[68:43] engage with the UI, so you don't need to run it by the ground. So you can,
[68:51] many cases, you can run it on the game just.
[68:56] Another question that we had here was, is the residency underscore status
[69:07] excuse me, an issue on the GPU side or the programming of when the GPU driver is set up to pull the data?
[69:15] I think the residency is the program thing, it's not the driver thing. The driver always
[69:28] always the way I'm all may
[69:35] release this, may effect these things as the VRAM well, well reached.
[69:48] So when you VRAM, you don't have enough VRAM, so you the driver will do something, but
[69:57] most of the time is the resident manager to
[70:03] effect and make resident. Yes. Another question we had here was, can the issue,
[70:14] I'm assuming the issue meaning GPU crash, also be in the way that your game calls a feature?
[70:21] And if the player system is to say update slash correct driver, but doesn't properly,
[70:27] sorry, doesn't respond properly to the way your game does?
[70:35] I think some of them actually need to update the driver, but you still have some way to avoid it.
[70:49] But I actually hope this driver is very needed.
[70:59] Absolutely. Another question we had here is, how often do you think corrupted PSO cash
[71:05] happens, like a corrupted shader or object that causes a crash on view?
[71:10] I think this is a hardware forever thing, so I don't know.
[71:20] No worries. Another question we had was, do you also use render doc or do you think that
[71:26] UE insights provides more than enough information? If you've even used render doc before?
[71:35] I think these things are not used to debug GPU crash, but actually we use render doc and
[71:46] the UE insights. The render doc is to check the rendering pipeline or check the render
[71:56] area. And the UE insights is more like to perform your CPU performance.
[72:06] Another question we had here is, does turning off async compute eliminate TDR crashes?
[72:12] In my opinion, I don't think so.
[72:25] I think async compute just is to reduce the whole GPU time, not the single
[72:38] task time, but the TDR is caused by the single GPU task. So I think that's not related.
[72:53] Final question for you. I know that we threw a lot, this is covered quite a lot, which is amazing.
[73:00] And maybe this is all of it, but is there any other advice that you would give folks
[73:07] when encountering these sorts of issues in their own projects or in their own experiences?
[73:16] I think I said everything in this talk. If you have other GPU crash, you can contact me.
[73:26] Perfect. Perfect. Well, actually I'm very interested in this.
[73:35] Well, we appreciate you sharing that interest with us and coming on to have this conversation
[73:40] and provide us with all of this information. As someone who again thankfully hasn't had to
[73:46] deal with this very often, when it does happen, it's extremely frustrating. So having a pipeline to
[73:51] solve it is amazing and we appreciate you sharing yours with us.
[73:58] With that, everybody, that is going to wrap up today's session of Inside Unreal. Again,
[74:05] huge thank you to WeWenn for coming on and sharing all this information and a huge thank you to you
[74:10] all for watching as well. The show would not be what it is without you, your time, and your
[74:16] questions. And if any of you came partway through the stream, don't worry. We have all of our
[74:22] streams saved as video on demand format so that you can view them on both our Twitch
[74:27] and YouTube channels. And we also have all of the updates and information on our other
[74:34] socials at YouTube or at Unreal Engine. And you can also keep up with the latest news,
[74:40] shoutouts, and other information again at our socials at Unreal Engine. And lastly,
[74:45] a lot of talking. Lastly, if you haven't already, please head over to the EDC, the Epic Developer
[74:51] Community, where we have all of our documentation, tutorials, forums, and so much more. So again,
[74:59] thank you, big shout out to you for joining us today and giving us this talk. And we will see
[75:04] everyone else on the next episode of Inside Unreal. Bye, everybody.



---

## Captured Frames

- [9:16] tutorials/frames/a-deep-dive-into-gpu-crashes-in-ue5-inside-unreal/frame_000.jpg
- [15:27] tutorials/frames/a-deep-dive-into-gpu-crashes-in-ue5-inside-unreal/frame_001.jpg
- [23:26] tutorials/frames/a-deep-dive-into-gpu-crashes-in-ue5-inside-unreal/frame_002.jpg
- [29:05] tutorials/frames/a-deep-dive-into-gpu-crashes-in-ue5-inside-unreal/frame_003.jpg
- [41:34] tutorials/frames/a-deep-dive-into-gpu-crashes-in-ue5-inside-unreal/frame_004.jpg
- [44:02] tutorials/frames/a-deep-dive-into-gpu-crashes-in-ue5-inside-unreal/frame_005.jpg
- [52:43] tutorials/frames/a-deep-dive-into-gpu-crashes-in-ue5-inside-unreal/frame_006.jpg
- [57:46] tutorials/frames/a-deep-dive-into-gpu-crashes-in-ue5-inside-unreal/frame_007.jpg

---

## Structured Notes

### Core Technique
A systematic workflow for diagnosing and fixing DirectX12 GPU crashes in UE5 — classify the crash (Device Removed vs. Device Hung, page fault vs. other), escalate through a tool ladder (D3D Debug Layer → GPU-Based Validation → DRED → vendor tools: NVIDIA Aftermath / AMD RGD / Intel GPU crash dumps / the emerging cross-vendor DirectX DMP standard), then apply targeted fixes for the most common root-cause categories (out-of-bounds/SM errors, residency/eviction page faults, use-after-free, shader infinite loops/TDR).

### Summary
An Inside Unreal interview with Kuiwen Jiang (engine lead, Cersei Studio / "Fit Trigger") on the studio's multi-year experience hunting down DX12 GPU crashes in UE5 open-world production. Covers why DX12's explicit, driver-doesn't-guess design makes crashes both more preventable and more fragile than DX11; the two main crash categories the CPU actually observes (Device Removed vs. Device Hung, both usually rooted in a GPU page fault or an infinite/very-long shader); the debugging tool ladder from cheap/broad (API return codes, engine log) to expensive/precise (D3D Debug Layer, GPU-Based Validation, DRED breadcrumbs, then vendor crash-dump tools NVIDIA Aftermath, AMD RGD, Intel's mechanism, and the new cross-vendor DirectX DMP standard shown at this year's GDC); real production case studies (an AMD-RGD-diagnosed residency/eviction page fault where a UE5 texture heap had been evicted out from under a live GPU reference, and a mysterious structured-buffer use-after-free during RDG refactoring that was worked around by switching the resource to a texture); the studio's automated AI-assisted crash-reporting pipeline; concrete repro/stress techniques (deliberately fill VRAM, lower residency debug budgets, toggle parallel-execution switches, run A/B tests disabling individual debug options); and a release-build tool-cost table weighing which debugging tools are safe/worthwhile to ship with vs. internal-only.

### Key Steps
**Understand the crash categories:**
1. GPU crashes are asynchronous from the CPU's perspective — the CPU only learns something went wrong when a subsequent graphics API call returns an error `HRESULT`, at which point `GetDeviceRemovedReason()` gives a coarse category.
2. **Device Removed**: usually a GPU page fault (GPU addressed memory that couldn't be translated) — the driver can't safely continue, so it tears down and asks the app to recreate the device. **Device Hung**: the GPU stopped making forward progress mid-work (classic cause: an infinite loop or extremely long-running shader), often surfacing via Windows' TDR (Timeout Detection and Recovery) mechanism, which can also fire for legitimately-too-long-but-not-broken work.

**Debugging workflow / tool ladder (frame_002, frame_006 tool-comparison table):**
3. Start cheap: check the API return `HRESULT` category, then check the UE5 log for any debug-layer warnings already being captured.
4. **D3D12 Debug Layer**: requires Windows Graphics Tools installed; enable via `DXCPL` (DirectX Control Panel) per-program, or via UE5 console variables/launch args (`-d3ddebug`, `-d3dloglargeleaks`-style flags mentioned). Catches CPU-side API contract violations (resource barrier errors, descriptor mismatches) *before* they reach the GPU — e.g. missing a resource-transition/barrier call.
5. **GPU-Based Validation (GBV)**: an enhanced mode of the debug layer (requires the debug layer enabled first) that instruments shaders/patches command lists to catch errors only visible when the GPU actually executes — e.g. a shader sampling a resource that's bound in the wrong resource state, which the plain debug layer can't see. Heavier runtime overhead than the base debug layer; the talk explicitly says both D3D Debug Layer and GBV are "not suitable for release builds" — internal/automated-test only.
6. **DRED (Device Removed Extended Data)**: native DX12 diagnostic with two main features — Auto-Breadcrumbs (records recent GPU command-list markers so you can see the last-executed / in-flight commands at crash time, frame_002) and Page Fault reporting (lists active/recently-freed resources and heaps near the faulting VA). Lower overhead than breadcrumbs-heavy alternatives but coarse — command-list-level granularity only, and can't pin down which specific draw/dispatch or shader instruction crashed due to GPU parallelism (several events may show "in flight" simultaneously).
7. **UE's own "GPU breadcrumbs"** are a separate, higher-level marker system (hierarchical, records all markers submitted per-frame) distinct from DRED's own breadcrumbs — UE's usually gives more context but DRED's includes lower-level API call detail; neither alone can prove which exact call crashed.
8. **NVIDIA Aftermath**: richest single tool covered. Two integration modes — SDK-embedded in the app (what UE5 does) or a standalone background monitor. On crash, generates an `.nv-gpudmp` file openable in NVIDIA Nsight Graphics, containing page-fault VA/resource info, shader hash, and (if call-stack capture + "dump shader debug info" console vars are enabled) exact shader source line via paired shader-binary/PDB files (frame_003, frame_005 — page-fault info block with GPU VA, resource dimensions, residency state; Aftermath's shader-source view highlights last-executed instruction in yellow and the crashing instruction in red). Controlled via UE5 console variables (resource tracking cvar is specifically called out as valuable for page-fault debugging). Caveat: pre-R615 NVIDIA driver, Aftermath was incompatible with the D3D debug layer being enabled simultaneously (fixed in the newer driver per the talk) and also conflicts with RenderDoc auto-attach. An upcoming driver update was said to merge the separate shader-debug-info file into the main dump, reduce memory overhead (older Aftermath versions could use significant memory), and add resource lifetime/residency event tracking.
9. **AMD RGD (Radeon GPU Detective)**: AMD's equivalent, currently requires a standalone background tool attached to the app (no SDK yet) — less convenient for rare/intermittent crashes but currently the most residency-state-detailed option for AMD when a crash IS reproducible, outputting both a summary and a detailed text report (notably AI-analysis-friendly since it's plain text). Case study (frame_004, frame_005): a page-fault crash traced via RGD's resource timeline to a heap that had been evicted — cross-referencing the heap's resource ID against the faulting virtual address confirmed the crashing resource lived inside that evicted heap, proving a residency/eviction bug rather than a "real" out-of-bounds access.
10. **Intel** provides its own GPU crash dump mechanism (background-tool-like); the studio hadn't used it in practice.
11. **DirectX DMP files** (new at this GDC, still preview/feedback stage): Microsoft's attempt at one unified, cross-vendor crash-dump format, opened via the PIX app; requires SDK integration and currently only works in development builds, not shipping/public release builds. NVIDIA, AMD, Intel, and Qualcomm are all expected to support it eventually, and both Aftermath and RGD appear to be moving toward compatibility with it.

**Common root-cause categories:**
12. **SM (streaming multiprocessor) out-of-bounds access**: relatively easy once Aftermath/RGD/DXDump gives the exact crashing instruction — add bounds checks. Special case: a crash address of exactly `0x0` may indicate an unbound uniform/constant buffer rather than a normal OOB.
13. **MMU/page fault from evicted or released resources**: DX12 makes residency explicit — the app/engine must track VRAM budget and ensure resources are resident before GPU use. "Evicted" (object still exists, memory temporarily inaccessible) is distinct from "released/destroyed" (object gone entirely) — confusing the two is a common source of these bugs. UE5's residency system sits on a DX12 residency third-party library; a notable recent-UE5 behavior change is that resources are now created as evicted-by-default (avoids implicit OS-level paging, but means `MakeResident()` gets called more often — good default for typical cases, worth knowing when debugging).
14. **Structured-buffer use-after-free during RDG work** (real case study, ~45:17-47:51 in transcript): buffers reported as *destroyed* (not evicted) yet still GPU-referenced. Ruled out buffer sizing and parallel-execution options as causes; strongly suspected but couldn't fully root-cause an RDG resource-management issue under project time constraints. Workaround that made the crash "almost disappear": reimplement the problematic resource as a **texture instead of a buffer** — texture resource lifetime management in UE's long-established render-target system is more conservative (a freed texture's memory is more likely to get reused by a later texture allocation than immediately released), which happens to paper over the underlying race. Final suspected root cause: a read/write race around resource extraction/production, later fixed upstream in newer UE5 versions.
15. **Shader infinite loop → TDR/Device Hung**: Aftermath reports "timeout"/"hung" status with the last-executed location inside the offending loop; also reachable via UE5's own `GPUDebugCrash` console command for deliberately testing RHI/RDG crash-handling paths (note: in newer UE5 versions where resources default to non-resident, you must set `r.Resource.StartsResident` (or disable the residency-management macro) for the debug-crash command's page-fault mode to actually trigger).

**Production practices (frame_007, frame_006):**
16. Build an automated crash pipeline: ingest crash reports from your crash-reporting platform, build a shader-hash → shader-name lookup index (searching the full shader cache for a matching hash can otherwise take 10+ minutes — precomputing the index avoids that), run Aftermath preprocessing (`AftermathTest.exe`) to match DXIL/PDB debug info and generate a full crash-dump JSON + report, then feed that into an AI step for root-cause analysis/report drafting, with results synced to IM/chat tools and a running internal knowledge base of previously-seen crashes.
17. To *increase* reproduction odds during stress/soak testing: deliberately raise VRAM pressure (background apps eating VRAM), lower residency debug budget cvars, toggle async/parallel-execution switches on and off (A/B-style) to isolate synchronization-related suspects, and toggle individual RDG/DX12 debug options (e.g. disabling `d3d12.VRAMDiffTrack`) to see if a category of crash disappears — if disabling a specific option makes crashes stop, that's a strong signal the bug is in that subsystem. Warns that these debug cvars are dangerous and must never ship in test/shipping builds.
18. **What's safe to ship / enable in release**, per the studio's own cost table (frame_006): D3D Debug Layer and GPU-Based Validation — internal validation only, very high/extremely high cost, never ship. Breadcrumbs — usable but "depends," medium cost, measured ~7-9 FPS drop when enabled in their project, and the info yield was judged not worth it. DRED — low cost, safe to ship, good for coarse "device removed" triage. Aftermath (shader-info-only mode) — low-medium cost (~3 FPS drop in their project), safe to ship with control, best for NVIDIA crash dumps; watch memory usage on already memory-heavy projects, especially older Aftermath versions. RGD — no shipping SDK currently (external attach only), best for AMD-reproducible crashes. DXDump — external/future candidate, TBD cost, aimed at cross-IHV workflows.
19. User-facing mitigations to recommend alongside engine-side fixes: have players clear shader cache, update GPU drivers, increase virtual/paging memory size (helps with out-of-memory-flavored instability), and disable third-party frame-rate overlay software (can itself destabilize the DX12 device).
20. Upgrade guidance for projects still on older UE5 releases: prioritize upgrading the (relatively isolated, low-risk) Aftermath module first — recent updates added shader-hash-based lookup speedups; RHI/RDG upgrades bring real residency/stability improvements (especially for buffer/structured-buffer crashes) but are higher-risk, larger-surface-area changes requiring real regression testing — if a full engine upgrade isn't feasible, upgrading just the debug-info modules alone still helps. Projects using bindless resources heavily should specifically prioritize the descriptor-range module upgrade, which fixed a residency-tracking gap for bindless descriptor ranges.
21. Other frequently-seen non-shader GPU-adjacent crash sources mentioned briefly: PSO (Pipeline State Object) creation failures (mitigated by building an internal PSO-hash → shader-name map to identify the problem shader for hard-to-repro cases) and DXGI/swapchain-boundary Present() failures — some are transient (retry a few times, e.g. state-transition-related Present failures, or issues from resizing a window while frame generation is active) but Device Removed / Device Reset returned from Present() should be treated as a genuine GPU crash, not retried away.

### UE Systems / Blueprints / Settings
Not a hands-on Blueprint/editor tutorial — this is an engine/RHI-level debugging talk. Relevant UE5 console variables/commands mentioned: `GPUDebugCrash` (deliberately trigger a test GPU crash; requires `r.Resource.StartsResident`-style override on newer UE5 defaults to reach the page-fault path), Aftermath enable/feature-flag cvars (resource tracking, dump-shader-debug-info, call-stack capture), D3D debug-layer / D3D log launch args, `d3d12.VRAMDiffTrack` (residency debug diff-tracking, toggle to isolate residency-related crashes), residency debug budget cvars (lower to stress-test eviction behavior), parallel-execution toggle cvars (for ruling out sync-related races). Systems discussed: RHI (Render Hardware Interface), RDG (Render Dependency Graph / render graph resource management), UE5's DX12-residency-manager (built on a third-party DX12 residency library), UE5's own GPU-breadcrumbs marker system (distinct from DRED's breadcrumbs).

### Difficulty
Advanced/Expert — this is low-level GPU/DirectX12 systems debugging aimed at engine programmers, not artists or general gameplay developers (the speakers explicitly acknowledge it's a niche, frustrating problem space).

### UE Version
Not tied to one specific version — discussion spans multiple UE5.x releases, explicitly contrasting older vs. newer UE5 residency-management defaults (calls out UE5.8-era behavior where resources are created non-resident by default) and gives separate upgrade advice for teams still on older UE5 branches.

### Tags
gpu-crash, directx12, rhi, rdg, debugging, aftermath, dred, residency, page-fault, shipping-build, performance

---

## Related Entries
None yet with overlapping GPU-crash/DirectX12-debugging tags — first low-level RHI/GPU-crash-debugging entry in this library.
