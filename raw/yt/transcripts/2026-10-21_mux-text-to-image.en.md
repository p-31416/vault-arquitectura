---
tipo: transcript
fuente: archademy.ai (curso AI x Gaudi, area de participantes)
modulo: text-to-image
titulo: Text-to-Image
idioma: en
fecha_creacion: 2026-10-21
tags: [yt, transcript, curso-ai-gaudi, mux, text-to-image]
---

# Text-to-Image — en

> Transcripcion automatica de los subtitulos del modulo del curso (Mux).
> Origen: https://vz-4ced3a48-15e.b-cdn.net/b4331c95-55f3-422a-a313-e498cb0a01bb/captions/en.vtt
> Duracion de la pista de subtitulos: 00:47:07,000 --> 00:47:09,927

[00:00:01] Hello everybody and welcome to part two.
[00:00:03] This part is about text to image and it will be more focused on application,
[00:00:10] so we will actually use workflows,
[00:00:13] we will test a lot. Since part one,
[00:00:15] the introduction, was more theoretical and foundational.
[00:00:18] Here we will actually go and generate,
[00:00:21] we will use Comfy Cloud and LoRAs etc.
[00:00:29] Before we start, I want to contextualize a bit what we're about to do.
[00:00:34] What you see here in front of you is a schematic representation of
[00:00:39] the design phase or in general the creative process.
[00:00:43] So on the left side here, you see that everything us architects or designers do,
[00:00:49] we always start from an idea. After this idea,
[00:00:53] you see that there is like this big non
[00:00:57] linear phase that is going between knowledge sharing,
[00:01:03] design tasks, and communication.
[00:01:05] And then afterwards it straightens out back to more fabrication and visualization.
[00:01:10] And often this cycle repeats X amount of times,
[00:01:13] but in general we have a nonlinear approach.
[00:01:18] Where text to image is usually very applicable
[00:01:24] is in the early phases when you just have an idea
[00:01:27] And you want to communicate what you're thinking,
[00:01:29] but you don't need a lot of control yet.
[00:01:32] Generally, this control is
[00:01:36] is necessary more in the later phases here.
[00:01:41] but for text to image early phases are more applicable.
[00:01:46] And the reason why that is, is because in the beginning we don't need that control
[00:01:51] to actually change specific things,
[00:01:54] we just want to communicate
[00:01:56] An idea.
[00:01:59] What we see here is a double diamond model.
[00:02:01] It's a theoretical framework that shows that we always start with
[00:02:06] a specific point and then we start to diverge.
[00:02:11] Diverging means to go wider, to test a lot of things,
[00:02:15] see what the options are. And at some point we flip it around and
[00:02:20] we start to converge again. Where text to image is applicable is in the
[00:02:25] in the early phase when we want to
[00:02:27] see which option options we have and to test a lot of things out.
[00:02:32] After that, image to image is more applicable.
[00:02:36] So that is the next module where we will have way more control than text to image.
[00:02:42] But also yeah it's a different phase so for now we're going to focus
[00:02:46] on the text to image but later image to image image to video everything will
[00:02:51] be more applicable there.
[00:02:57] Like I said, it was going to be more practical.
[00:03:00] So we're going to
[00:03:01] go right into Miro.
[00:03:08] As you can see here, I've prepared module 2 text to image.
[00:03:12] For now it is empty. But when you access the board,
[00:03:16] it will be filled with some with some images so you can download the workflows.
[00:03:22] I've prepared it here in Comfy for you.
[00:03:27] And as you have seen in the previous module,
[00:03:29] this is the most basic workflow possible.
[00:03:33] We start with checkpoint, then we have a prompt,
[00:03:35] negative prompt, Empty Latent Image,
[00:03:38] which defined the output ratio of our image.
[00:03:42] Then we have the KSampler,
[00:03:44] this was the stove, remember, where we put all the settings and we tweak a bit.
[00:03:50] Then we have the decode, which makes back an image out of our
[00:03:56] AI world and then we have the Save Image.
[00:04:02] This tutorial I'm going to do with a very,
[00:04:04] very simple prompt. It's going to be Concrete House in Desert Rocky Landscape.
[00:04:10] The reason why is because this workflow you're seeing here is for a model,
[00:04:17] it's called DreamShaper, but essentially it's a Stable Diffusion 1.5 model,
[00:04:23] which means that by now this is a super old model.
[00:04:27] This came out in 2022. So it's
[00:04:31] Visually going to be a bit underwhelming,
[00:04:34] but it's good to learn the basics.
[00:04:37] Positive prompt we saw. The negative prompt is cat,
[00:04:42] dog, and waterpark. And you will see later why.
[00:04:46] So, as we saw, we're gonna click on run.
[00:04:49] This will enable everything on this canvas.
[00:04:53] You can see the job is queued and the image is being generated.
[00:04:59] Since this is a super light.
[00:05:01] model it was super quick. What we see here is a concrete house in the desert
[00:05:07] and a rocky landscape. Now of course I don't have to explain to you that this
[00:05:10] is visually not super interesting.
[00:05:13] Why do I show you this? It's to show all the functions here.
[00:05:20] So if we go into the KSampler and we keep the prompt,
[00:05:24] negative prompt everything the Empty Latent Image,
[00:05:26] we keep all that intact so we know that the changes that we will
[00:05:31] About to see is not due to prompt changes,
[00:05:35] it's just the settings. So let's start up top.
[00:05:40] We see the seed. Remember,
[00:05:42] this is the starting position of the pixels.
[00:05:44] If we click here, we can change the how the workflow will handle
[00:05:51] the seed. For now, it's fixed value.
[00:05:54] So as it says, when we generate an image.
[00:05:58] The seed will always be the same.
[00:05:59] So it will always start from the same configuration of pixels.
[00:06:04] When we go to randomize value,
[00:06:07] it will always be a completely different seed,
[00:06:11] which means
[00:06:14] Let us actually right-click here,
[00:06:17] duplicate, and then I will show you what the impact is.
[00:06:21] So we keep our workflow intact.
[00:06:25] And with the second one, I'm going to click here and click on randomize value.
[00:06:32] Now, for now it hasn't changed that because it says shuffles
[00:06:37] the value randomly after each generation.
[00:06:40] So for now the seed is still.
[00:06:43] The same. So if we click on run.
[00:06:47] We see that the seed has changed already.
[00:06:52] Now it's being generated. So
[00:07:03] Let me check.
[00:07:07] Okay, I had to reload the page because my internet was a bit slow,
[00:07:11] but as you see here, it's a different image.
[00:07:15] Now it also chose a concrete house in the desert with a rocky landscape,
[00:07:20] but it's a different image. If we generate again,
[00:07:23] keep an eye out on this part,
[00:07:26] we'll see it changes the seed again.
[00:07:30] And every time you click here,
[00:07:32] the seed will change because we clicked on randomize value.
[00:07:37] Right. Now if we click on fixed value and rerun.
[00:07:47] The workflow.
[00:07:55] You will see that it generates a different image,
[00:07:57] but for now the seed is fixed.
[00:08:01] So if we click run again, it will be the same image because we locked the seed,
[00:08:05] right? So it didn't change at all.
[00:08:09] We can click this a million times,
[00:08:11] it will always be exactly the same image.
[00:08:13] Now we haven't changed the prompt,
[00:08:16] we haven't changed the negative prompt.
[00:08:20] Now we won't change the seed.
[00:08:24] Because we know if we change the seed,
[00:08:26] it will be a different image. If we keep the seed,
[00:08:29] it will always be kind of similar.
[00:08:31] Let's go back to our previous example.
[00:08:35] Just to make sure if I click run,
[00:08:39] it will be again the same starting image.
[00:08:41] And actually, I will go into Miro and
[00:08:51] place this image here for you so we can see the comparison between later
[00:08:57] or like newer workflows and newer models.
[00:09:03] So
[00:09:07] Now we know what the seed does.
[00:09:08] We will play with the steps. The steps,
[00:09:10] remember, it's the amount of iterations that the model takes to create the image.
[00:09:16] If we put it at five.
[00:09:20] With the same prompt, same seed,
[00:09:21] everything, we will see that the image completely gets under-generated.
[00:09:28] Why? Because we cut the generation part off.
[00:09:31] It was still generating and we said stop,
[00:09:33] stop at five steps. Of course,
[00:09:35] you can see that it's not a good result.
[00:09:37] So if we do 10, if we redo,
[00:09:41] then it will take the same generation path and it will stop at 10.
[00:09:45] And you can already see that is way better than before.
[00:09:50] Now if we put it at twenty again.
[00:09:56] Again, it's exactly the same as before.
[00:09:59] So in this way it's deterministic.
[00:10:01] It's not random. You can trace back why something happened the way it did.
[00:10:05] CFG is the amount of creativity.
[00:10:09] So when you hover over here, it also shows you what it is.
[00:10:13] So if you can't remember or if you don't know,
[00:10:16] either ask your Comfy expert or just hover over
[00:10:22] the value.
[00:10:26] So if we put this at one
[00:10:30] Let's see what happens.
[00:10:35] it completely gets underbaked because the higher values result
[00:10:39] in images more closely matching prompt,
[00:10:42] which means if we put it very low,
[00:10:44] the model can do whatever it wants.
[00:10:46] It has a lot of freedom, but in this case it's not enough.
[00:10:50] If we put it at 20
[00:10:57] It tries to do so literally what the prompt says that it over saturates
[00:11:04] and over-crushes the pixels. And that is why for this workflow,
[00:11:08] 8 is the best. How do I know this?
[00:11:12] It's very simple. I just go to the prompt coach
[00:11:19] or let's say the other one. I just go to your Comfy expert and then I,
[00:11:25] for example.
[00:11:27] I'd take, let's say, a very bad image,
[00:11:31] so we put it at one.
[00:11:38] I would screenshot this page.
[00:11:44] So we have a screenshot and then I would paste it in here and
[00:11:48] say why is
[00:11:52] my output image not good.
[00:11:57] You don't even have to use perfect phrasing
[00:12:03] and then it will tell me in about a minute,
[00:12:07] okay. I see you're using a Stable Diffusion 1.5 workflow.
[00:12:12] It's trying to troubleshoot it.
[00:12:14] And then it will say, okay, the CFG is way too low,
[00:12:17] put it at 8, for example. That being said,
[00:12:22] let's go to the next workflow to see the impacts of a different one.
[00:12:28] I've prepared it here already.
[00:12:30] And what you can see is that the workflow in itself is not different.
[00:12:33] The only thing that is different is this model.
[00:12:36] This is a Stable Diffusion XL model,
[00:12:39] and you can see it here.
[00:12:42] You can also go to template, go to model filter.
[00:12:48] And click on SDXL, and then you have for example SDXL simple.
[00:12:53] This is not a simple workflow,
[00:12:56] so this is a bit overwhelming.
[00:12:58] So let's close that one.
[00:13:02] you can also try this one. Here you can see it's already if
[00:13:08] we delete this one.
[00:13:12] It's already simpler. But for now,
[00:13:14] for this tutorial, I would just stick with the ones I provide because they're
[00:13:18] the most pure. It's just the essence and it's not nothing more than that.
[00:13:23] If we take the same prompt,
[00:13:26] etc., everything the same, and we run it.
[00:13:35] We'll see that this image is already visually way more interesting compared to
[00:13:41] the last one. Now I don't have to explain everything again because it's just
[00:13:47] the same. So I will provide this image
[00:13:54] here so you can just check it out.
[00:13:56] Then we're going to go with FLUX.1.
[00:14:03] Again, I have prepared the workflows for you.
[00:14:08] If we drag and drop here, you can see this is a way different workflow.
[00:14:13] Let's close this markdown file.
[00:14:15] And here we have the same prompt:
[00:14:18] concrete house and desert, rocky landscape.
[00:14:20] As we can see here, the resolution is set to 1024 by 1024.
[00:14:26] This is because the model FLUX is trained on higher resolution images.
[00:14:32] So it's actually better at 1024.
[00:14:36] than 512 by 512.
[00:14:38] But in general you can play around with this.
[00:14:42] If we go in the subgraph, we can see that this is the real workflow behind
[00:14:48] the behind the subgraph. But for now if we click on run,
[00:14:53] we will see the increase of image quality compared to the older models.
[00:15:03] Here we can see how it is being generated.
[00:15:10] As you can see this is again way more interesting.
[00:15:13] Maybe if you zoom in a lot you it's still pixelated,
[00:15:18] it's not super realistic I would say,
[00:15:21] but in general this is a good image I would say.
[00:15:30] Also, see this is a bigger resolution,
[00:15:32] so I have to scale it down a bit.
[00:15:35] Now, this was just a build-up because we're arriving at FLUX.2.
[00:15:41] The model that we will be using is called klein 9B.
[00:15:45] again, you can use the workflow I will provide here,
[00:15:49] or you just go in the template set
[00:15:55] and you click on your search for FLUX.
[00:16:00] klein. So, all the workflows... that was by accident.
[00:16:09] All workflows that are native to Comfy,
[00:16:12] you will find here. And you can see the difference in models.
[00:16:15] So this is FLUX.2. This is the model family.
[00:16:19] Then we have klein 4B. What this means is klein is just a way of saying it's
[00:16:26] a small file, so it's not as heavy on your computer as the other ones.
[00:16:30] And it is trained on 4 billion parameters.
[00:16:33] Here we see klein
[00:16:36] 9B, this is the one that we will be using.
[00:16:38] It's trained on 9 billion. So it just it's a smarter model,
[00:16:41] but also a more heavy one. So if we click here,
[00:16:45] we can see that this workflow is
[00:16:51] Pretty basic looking. If we enter a subgraph,
[00:16:54] it's nothing crazy, but you don't have to change anything in here,
[00:16:58] so just stick with this one. Okay,
[00:17:03] I will get my template.
[00:17:09] Just to keep it consistent.
[00:17:15] Concrete house in desert rocky landscape,
[00:17:18] 1024 by 1024 pixels, nothing special.
[00:17:22] If we click on run, you will see that this output quality,
[00:17:25] architecturally, visually, everything is again way more interesting than
[00:17:31] the previous ones. But it also takes way longer to generate because it's
[00:17:36] a heavier model, it's a newer one,
[00:17:38] it's trained on way more images than the older ones.
[00:17:43] So I mean this is a very cool image.
[00:17:46] so that's good. Again I will provide it here.
[00:17:48] ...
[00:18:07] So this was a very rapid demonstration on the older models versus the newer ones.
[00:18:14] And you can see that there is a reason why these newer models
[00:18:18] are way more interesting to use.
[00:18:19] These ones, let's say these first two ones,
[00:18:22] they're not interesting to use today because of the quality lacking.
[00:18:27] I would say FLUX.1 in some cases can still be interesting,
[00:18:31] but most of the time, FLUX.2,
[00:18:33] especially this one.
[00:18:35] is by far the best option for you.
[00:18:37] And that's why I really recommend using Comfy Cloud because otherwise
[00:18:42] it will probably take so long to generate it locally.
[00:18:48] Now there's a few things that we could do here.
[00:18:52] Either you iterate a lot on the prompting.
[00:18:55] So you would go to your Comfy expert or your prompt coach.
[00:19:01] We'll show you.
[00:19:04] Okay, I went to the prompt coach we have set up together,
[00:19:08] which in general was just the instructions like this,
[00:19:12] as you find on Miro.
[00:19:17] So prompt coach setup, it just copy pasted this.
[00:19:23] in my favorite LLM, which is Claude.
[00:19:25] I paste it in here. I just say start.
[00:19:29] It will ask me for which model are you trying to make something.
[00:19:34] And
[00:19:37] also something to improve. So I will say concrete housing desert,
[00:19:42] rocky landscape, and the model is FLUX.2 klein.
[00:19:46] So if we go
[00:19:51] So think about everything it knows,
[00:19:53] of course, nothing special.
[00:20:00] So here he gave me three options,
[00:20:02] reference Tadao Ando, Rick Joy,
[00:20:05] or Kogan. So I would say let's say option 01.
[00:20:14] So I like tadao ando and it will give me something like this.
[00:20:19] But then specifically for FLUX.2.
[00:20:24] And as you can see here, FLUX.2,
[00:20:26] this prompt coach, it knows that FLUX.2 understands JSON prompting.
[00:20:32] And as we saw before, JSON prompting is just the way
[00:20:35] how this is organized.
[00:20:40] The information structured here.
[00:20:44] So I would copy this.
[00:20:51] I would make it a bit bigger and then I would paste the JSON prompt in here.
[00:20:57] Now what is going to happen when we generate this?
[00:21:00] I haven't read the full prompt.
[00:21:02] it's glitching a bit.
[00:21:05] So I'm actually I don't know what it's going to generate.
[00:21:09] I can see it took some color palettes.
[00:21:14] So it made this very basic looking volume.
[00:21:22] What the advantage of this JSON prompt is that I can if I want
[00:21:28] to change something about the scene,
[00:21:30] I would do it here. If I want to change something for the description,
[00:21:34] it's here. If I want to change the style or the colors,
[00:21:39] the lighting, the mood, the background,
[00:21:41] composition, everything, I would know where exactly I have to change the prompt.
[00:21:48] Okay, so that's what you can do here.
[00:21:51] If you have a clear idea about anything you want,
[00:21:54] you can you can really surgically change the prompt in here.
[00:22:03] Now often these prompt coach is tempted to make it overcomplicated.
[00:22:09] So I would say make it max fifty words,
[00:22:16] no JSON structure.
[00:22:22] to keep it a bit more simple because in this early design phase
[00:22:26] I don't know whatever the constraints are.
[00:22:34] Okay, so it gave me this prompt deep focus.
[00:22:37] Let's try this one.
[00:22:44] And see what happens.
[00:22:47] Of course this is a pretty basic idea of having a concrete structure in
[00:22:53] the in the desert. You can be way more experimental with this and really
[00:22:59] try to push push the boundaries.
[00:23:06] As you can see, this is the visual qualities are pretty interesting with
[00:23:12] the with the sun and the background.
[00:23:14] I really I really like the visual aesthetics here.
[00:23:17] Now the next part of the presentation.
[00:23:25] Let me swap it like this.
[00:23:31] Okay, is FLUX.2 klein workflow,
[00:23:37] impact of prompt types we just saw.
[00:23:39] And actually another thing I will be adding is showing you
[00:23:44] how to implement a LoRA on this workflow.
[00:23:50] And so you can see the actual impact of the LoRA as we're generating images.
[00:23:59] Okay, we saw how to make these interesting
[00:24:03] images from just text.
[00:24:08] Now we will advance to implementing a LoRA.
[00:24:11] Let's go in the workflow and we will actually go back to
[00:24:17] the one we had before, which was
[00:24:25] This one I'll reset it to the
[00:24:31] Starting position as it was before so you will recognize it.
[00:24:38] As you can see, sometimes it's a bit it's a bit slow,
[00:24:43] also because you're using a cloud service,
[00:24:46] so sometimes the connection it takes a few seconds.
[00:24:48] Generally it's super super quick.
[00:24:51] If it's slow, if it's not generating and it's not giving any error codes,
[00:24:56] you can just refresh it and it will probably solve a lot,
[00:25:01] even if it says this. So let's see what happens.
[00:25:11] Okay, I refreshed it, and we have this image.
[00:25:16] Now we're going to add a LoRA to this workflow.
[00:25:20] So we enter the subgraph, and this is going to be a bit more technical,
[00:25:23] but just follow my steps. So what we do is we go up here and we double-click.
[00:25:29] We're just going to type
[00:25:34] in Load LoRA. And as you can see here on the right side.
[00:25:40] It's a logo of Comfy So this is an official node that Comfy made themselves,
[00:25:45] so it works super well. Sometimes you see other names.
[00:25:48] these are just other people who are making their
[00:25:53] own nodes and then Comfy verifies them.
[00:25:58] So they're all safe, so you don't have to worry about that.
[00:26:02] But just for now click on this first one.
[00:26:06] Then you can drag and drop it anywhere for this.
[00:26:10] Workflow I would drop it on top.
[00:26:13] It's gone. So let's try again.
[00:26:19] So just paste it here. Now,
[00:26:22] of course, since it's not linked to the workflow,
[00:26:24] it won't work. Now, your question can be where do I link it
[00:26:30] in between this without screwing the workflow over?
[00:26:33] It's super simple. So you see that we need a model input and we have
[00:26:39] a model output. Now, if you look somewhere where there is
[00:26:44] an output that says model, it's only this one.
[00:26:48] So there is, let's say you want to connect it.
[00:26:50] There's only one way where you can actually connect it,
[00:26:53] and it's this one. Let's say you I would like to connect it here.
[00:26:57] It's not possible. It's not it's turning gray because it's a different input,
[00:27:02] right? It's a different kind of information.
[00:27:04] So you cannot actually do anything wrong because this is the only way it will link.
[00:27:09] Let's say I want to link it here and I leave it,
[00:27:14] it just nothing happens.
[00:27:17] I can also take it from here and link it.
[00:27:20] You see this one is linked, but behind here,
[00:27:23] behind this one, if I move it,
[00:27:27] you can still see that this model is linked to the next one.
[00:27:32] So if you do this, it bypasses and now this chain gets connected.
[00:27:41] Don't be intimidated by this, it looks harder than it actually is.
[00:27:44] So now we can see that the model is actually linked,
[00:27:50] or the node is linked within the workflow.
[00:27:54] What we have to do now is import a LoRA model in our account so we can activate it.
[00:28:00] How we will be doing this
[00:28:02] is explained well on Miro.
[00:28:07] It's this document, it's a PDF.
[00:28:11] made by Ismail Salid, so big shout out to him.
[00:28:14] for if it's not clear, you can follow this one
[00:28:18] and that way you know how to import models into your
[00:28:25] Comfy Cloud account. But we will do it together.
[00:28:28] Just this is a backup for if it's not clear,
[00:28:31] follow it here. So you go to the website called Hugging Face.
[00:28:39] As you can see here on top, I provided the link here so you can just
[00:28:44] use it if it's not clear. You make a new account,
[00:28:49] so you say sign up.
[00:28:52] When you have made your account,
[00:28:54] you can see here on top. I've made a new one here.
[00:28:57] there's a lot of information on this website,
[00:29:01] and what Hugging Face essentially is,
[00:29:02] is the biggest AI platform. So you can go here and click on models,
[00:29:07] and you'll find a lot of open source models,
[00:29:10] LoRA's as well. It's super, super technical in some way,
[00:29:16] but how we will be using is to find,
[00:29:20] for example, FLUX.2.
[00:29:24] So if you click here.
[00:29:28] Here you will actually be able to download FLUX.2 klein 9B,
[00:29:32] and you don't have to do this because Comfy Cloud already did this for us.
[00:29:37] But for anybody who is trying to run it locally,
[00:29:40] so you actually want to use it on your own PC,
[00:29:43] then you would have to download it.
[00:29:45] this big file here. But for now,
[00:29:48] this is not necessary. What we want to do if we go back is we want to
[00:29:55] be able to load a LoRA.
[00:29:57] in our workflow. The steps we have to do are the following.
[00:30:05] First thing we need to do is actually go to Black Forest Labs FLUX.2 klein 9B.
[00:30:11] If you don't know how to do it,
[00:30:12] just click here. FLUX.2 klein.
[00:30:19] And it will appear on top. You click on here,
[00:30:23] and this is the model card.
[00:30:26] So it has a lot of information about the model,
[00:30:29] how to run it, limitations, documentations.
[00:30:32] If you're interested, you can check it out here.
[00:30:34] What we have to do is click on agree and access repository.
[00:30:42] Files and versions. So this is just for educational purposes that
[00:30:46] I'm showing you how to do it. it's linked to a
[00:30:53] To Black Forest Labs, so you can also see the amount of downloads they
[00:30:59] had last month, etc. Okay, now we actually say that we agree with
[00:31:05] the terms of FLUX or of Black Forest Labs.
[00:31:09] So the hardest part is actually done.
[00:31:11] Now we go here on the right side,
[00:31:14] we go to New Model,
[00:31:18] we give it a name.
[00:31:21] This name kind of depends on which one you are using.
[00:31:24] So on Miro, I have prepared something.
[00:31:29] In this course, there is a LoRA included.
[00:31:34] It's called Rhino to Image LoRA Basic.
[00:31:37] It's a safetensors file that you will find in the folder that you receive from
[00:31:43] the course. Now, since this is my full-time job.
[00:31:47] And I'm testing a lot of LoRAs,
[00:31:49] I'm making a lot of them myself.
[00:31:51] I've also made a premium LoRA I'll also be showcasing you.
[00:31:56] you don't have to buy it, but if you're interested in it,
[00:32:00] you can find it on my website and I'll quickly show it here.
[00:32:05] It's a very, very simple website.
[00:32:08] The only thing that you can actually find are my workflows.
[00:32:13] and it's this one.
[00:32:17] So here on the right side, as you can see,
[00:32:19] I have given a very big discount.
[00:32:22] Normally it's 100, now it's going to be 49.
[00:32:25] and why I believe this is worth it is because if you click here,
[00:32:31] you will see the before and the after.
[00:32:33] Now this is part of the second or sorry the third module,
[00:32:38] which is image to image, but you can see the quality of this LoRA.
[00:32:42] is super super good and it's because I trained it a long time so you
[00:32:47] can go from this
[00:32:51] to this but we can also use it for text to image.
[00:32:54] So if you're interested, click here add to cart.
[00:32:57] This discount will only be the time that the competition is actually running.
[00:33:02] So after that the discount will be gone.
[00:33:08] Now which one you're using doesn't matter.
[00:33:11] You can follow the steps with both of them,
[00:33:13] either the free one or the premium one.
[00:33:16] The difference is just the quality of or like the visual quality of
[00:33:22] the premium one is better, of course.
[00:33:25] So you take that file. In my case,
[00:33:28] it's going to be the premium one.
[00:33:33] You give it a name, whatever it is,
[00:33:35] that's
[00:33:38] Take this one.
[00:33:44] Doesn't matter whatever you call it,
[00:33:45] like whatever you want. We keep it private.
[00:33:49] So we don't click on public because otherwise it will be exposed
[00:33:52] to everybody publicly. We click on private,
[00:33:55] this is super important. And then we click on create model.
[00:33:59] And now we have made a new model.
[00:34:02] Now, since we haven't uploaded anything,
[00:34:04] it's empty. So we go to files and versions and we can see that there is nothing yet.
[00:34:09] It's just
[00:34:11] An initial commit and some git attributes,
[00:34:13] but it's empty. So the next step is to click on contribute on the right side,
[00:34:19] and here we can click on upload files.
[00:34:23] The folder you received contains the free one,
[00:34:28] it will be very clear where it is,
[00:34:30] or on my website you have the premium one.
[00:34:34] So
[00:34:38] You just drag and drop it in here.
[00:34:40] As you can see, Rhino to Image LoRA premium is in there.
[00:34:45] And then we just click on commit changes here.
[00:34:52] As you can see it's uploading,
[00:34:54] so we upload the LoRA file,
[00:34:57] which is a safetensors file, to our Hugging Face account.
[00:35:01] And now we can see it is here.
[00:35:03] It's called Thomas Rhino to Image LoRA Premium.
[00:35:07] And then this is the actual file.
[00:35:10] As you can see, it's about 127 megabytes.
[00:35:14] You can download it back here,
[00:35:16] but of course we don't have to do that.
[00:35:20] Now where is the next step?
[00:35:24] It's going again, clicking on account,
[00:35:27] and now we have to click on access tokens because we have to give
[00:35:32] our comfy cloud account access to this repository.
[00:35:37] So we click on access tokens, create new token.
[00:35:44] You give it a name, but before we give the name,
[00:35:47] we have to click on read. So it's not fine-grained or write,
[00:35:52] it's just read. This means that the Hugging Face repository only gives access
[00:35:59] to read our files, nothing else.
[00:36:01] We give it a name, just say Comfy Cloud,
[00:36:07] doesn't matter what it is, the name,
[00:36:09] and you click on create token.
[00:36:12] Now
[00:36:13] This token you will see here, it's you have to make this private.
[00:36:18] Since this is a fake account, it doesn't matter that you know what this is,
[00:36:23] but it's super important that you keep this one private because this is
[00:36:27] a token that will give access to your account,
[00:36:33] to whatever you uploaded. so if this is posted on the internet,
[00:36:38] other people can access it. So it's a like a it's a password.
[00:36:42] Let's call it a password. But for now it doesn't matter that for me you can see it.
[00:36:48] I would click on copy.
[00:36:54] Then I go back to Comfy Cloud,
[00:36:58] I go to settings, and here you can see secrets.
[00:37:03] Now you can see that I have already done it,
[00:37:07] of course, otherwise I couldn't do this course.
[00:37:11] I would click on add secrets.
[00:37:17] You can give it a name and here you paste in your new value like this
[00:37:25] and you click on save. The provider,
[00:37:28] before clicking on save, you have to select hugging face.
[00:37:33] Okay, that's super important. I cannot do it because I already have
[00:37:37] my token selected, but click on hugging face,
[00:37:40] give it a random name, and click on save.
[00:37:48] Then after that we go back to Comfy and we're almost done.
[00:37:52] So you only have to do this once,
[00:37:55] and afterwards it's way simpler.
[00:37:57] So we go back to our account. We click on our account.
[00:38:02] Here we can see the model we just uploaded,
[00:38:06] the LoRA. if you first try it with the with the basic
[00:38:12] one and later with the premium one,
[00:38:14] so you just have to do the steps twice,
[00:38:16] then
[00:38:17] of course there will be two models here.
[00:38:19] Makes sense. It's not rocket science.
[00:38:24] We go to files and versions, and here
[00:38:29] you have to right-click on this download button,
[00:38:34] right? So not double click. You can also do it here,
[00:38:39] but you just have to right-click either on this button or here,
[00:38:43] and then you can click on copy link address.
[00:38:47] Okay. So we click here,
[00:38:52] it says link address.
[00:38:53] Copied?
[00:38:57] For the last time we're going to go to Comfy.
[00:38:59] ...
[00:39:04] We click on Model Library, Import
[00:39:10] and here we paste the link.
[00:39:14] If we click on continue, for my setup it's not going to work,
[00:39:18] but for you it will work.
[00:39:21] If anything doesn't work, maybe it happens,
[00:39:26] maybe you missed a step or a detail.
[00:39:28] Don't worry, just go to
[00:39:35] This one and here every step that we did is explained.
[00:39:42] in a different way.
[00:39:45] Just follow the steps. Okay. Then if it still doesn't work,
[00:39:52] rewatch this video. And if it still doesn't work,
[00:39:55] use your Comfy expert because it will guide you through the process.
[00:40:01] Okay, if you did all this well and you refresh the page,
[00:40:07] you can click on Load LoRA.
[00:40:12] You can go to my models and here this LoRA will be available now.
[00:40:17] So it has a different name for me here because this was during the testing.
[00:40:24] And now the LoRA is linked to our workflow.
[00:40:26] I understand that this may be a lot of steps.
[00:40:29] It's pretty it looks super technical,
[00:40:33] but just follow the simple steps that I did,
[00:40:35] and you will be able to link the LoRA in this text
[00:40:40] to image workflow. Let's see what the impact is.
[00:40:44] So we click on run. And now the prompt,
[00:40:48] everything is still the same, but we're just adding the LoRA on our
[00:40:55] base model which is FLUX.2 and you will see what the impact in terms
[00:41:01] of style is.
[00:41:05] Okay, the workflow has loaded and this is the result.
[00:41:08] Now you can ask yourself what is the big difference here?
[00:41:12] Because of course we can see that the building is different,
[00:41:14] but now I'm just talking about visual characteristics.
[00:41:18] So I will add it to
[00:41:23] The Miro so we can just put it side by side.
[00:41:31] And this is actually with LoRA strength 100%.
[00:41:35] So the difference is that both
[00:41:39] are interesting images. The only difference is that this right
[00:41:45] one is influenced by this slightly analogue grain,
[00:41:49] and that is because my LoRA is trained on 35 millimeter architectural photography.
[00:41:55] So you can still use the basic one,
[00:41:59] you don't have to use a LoRA.
[00:42:01] but if you're interested you can find it in here.
[00:42:07] Go into the workflow and we go into the enter subgraph.
[00:42:10] You will see that we can play around with the strength.
[00:42:14] So if we put it at 0.5, click enter,
[00:42:18] and we click on run. Now that this LoRA will only be activated for 50%,
[00:42:24] so it won't be as dominant to change the image as
[00:42:29] as we did now. So again,
[00:42:32] you can see how the image gets generated,
[00:42:35] how the model is
[00:42:37] Correcting itself to give you a nice image.
[00:42:42] And this is the result. This is interesting because
[00:42:48] If we compare it here in the Miro,
[00:42:51] I will actually put it here.
[00:42:57] Like this.
[00:43:13] So this left one is without a LoRA,
[00:43:15] this one is with fifty percent,
[00:43:17] and here it is with one hundred percent.
[00:43:24] So that is that. Now you can find new LoRAs,
[00:43:27] you can find different ones, and everyone,
[00:43:30] every LoRA has a different impact.
[00:43:33] Now, why am I such a big fan, you might ask,
[00:43:37] for this LoRA? It's in the next in this next module
[00:43:43] we will see that we can turn this basic Rhino image into this high
[00:43:50] resolution render.
[00:43:53] By just providing a reference image of a marble block.
[00:43:58] And this is actually where the LoRA really,
[00:44:02] really comes into use. Because if you don't use it,
[00:44:05] it will become a bit plasticky.
[00:44:07] I will just give you I'll give you an example.
[00:44:12] So for example, this is when you don't use a LoRA.
[00:44:17] It's a bit plasticky, saturated,
[00:44:20] it's super crunchy.
[00:44:23] And the same workflow, same prompt,
[00:44:25] but with a LoRA is this one. It's way more soft,
[00:44:29] it's super subtle architecturally,
[00:44:34] it's way more interesting in my opinion.
[00:44:37] so make sure to check this one out.
[00:44:41] There's also Spectrum coming.
[00:44:44] I will explain what this is in the next module,
[00:44:48] and also a different LoRA. But for this
[00:44:52] For course purposes, I have given fifty percent discount as long
[00:44:57] as the competition is running.
[00:45:03] Now back to text to image. We saw four models.
[00:45:08] So we saw Stable Diffusion 1.5,
[00:45:10] Stable Diffusion XL, FLUX.1, and FLUX.2.
[00:45:14] We have seen how to actually utilize a LoRA,
[00:45:19] which is a process with a lot of different steps,
[00:45:25] but you just have to do it once,
[00:45:26] and then your LoRA is in your Comfy account and you can always access it.
[00:45:32] Very easily. Next thing we could do is play around a bit more with
[00:45:39] the prompt coach. So if you have a specific idea,
[00:45:42] always put it in a prompt coach first,
[00:45:44] spar with the with the AI bot on your ideas,
[00:45:49] and then copy paste and try it out.
[00:45:53] Play a bit with the parameters.
[00:45:56] If it doesn't work, just go back to the previous settings and
[00:46:00] you can always download.
[00:46:02] this template here. So download it.
[00:46:10] Mm.
[00:46:13] Go in comfy.
[00:46:18] Drag and drop and you will have the exact same prompt settings seed as I did.
[00:46:28] Okay, everybody, this is the end of module two,
[00:46:31] text to image. On the right side of the Miro board,
[00:46:36] all the way here, I provided extra resources for anyone who's interested.
[00:46:41] You can always just click on here,
[00:46:44] download the image, and you will see the whole workflow with the prompt,
[00:46:50] etc. Since this is actually something that I was using for testing ideas,
[00:46:56] for example, this tower.
[00:46:59] So check it out, it's extra to the course.
[00:47:07] Thank you and see you at module three.
