---
tipo: transcript
fuente: archademy.ai (curso AI x Gaudi, area de participantes)
modulo: image-to-video
titulo: Image-to-Video
idioma: en
fecha_creacion: 2026-10-21
tags: [yt, transcript, curso-ai-gaudi, mux, image-to-video]
---

# Image-to-Video — en

> Transcripcion automatica de los subtitulos del modulo del curso (Mux).
> Origen: https://vz-4ced3a48-15e.b-cdn.net/b0e1ea14-2be9-47ae-8515-cf3c5cbe00ea/captions/en.vtt
> Duracion de la pista de subtitulos: 00:26:18,946 --> 00:26:22,222

[00:00:04] Welcome to part four, image to video.
[00:00:12] What we see here is the like a small recap of our previous chapter,
[00:00:18] which was image to image, where we take an image and we transform
[00:00:21] it into a different image. Now the last step in presentation often is
[00:00:27] to make a video out of this. This is probably not going to be new for everybody,
[00:00:32] but your questions may still be how do we actually do it?
[00:00:37] How do we do it well, and what are some techniques to do it well?
[00:00:43] Now, a very basic example here is to make a transition between the first image
[00:00:49] and the last image, and then it morphs together.
[00:00:53] Now, this already has a bit of AI slop feeling to it,
[00:00:58] so this is not a great example,
[00:01:00] but it's the easiest one to start with.
[00:01:05] And this is what we call image to video.
[00:01:11] When we open the template, we can see the following.
[00:01:14] It's a cartoon of a woman and three outfits and the prompt.
[00:01:20] If we restructure it so we can actually read it,
[00:01:24] it's a very detailed prompt on how
[00:01:29] the model should place these clothes on her.
[00:01:33] For us, this is not really interesting since we will just be using one image.
[00:01:39] So, what we will do.
[00:01:42] We can drag and drop them. This one,
[00:01:45] so the one that is connected to image four and image three,
[00:01:50] we will Ctrl+B, or right click and click on bypass.
[00:01:56] Since we will not be using it for this tutorial.
[00:02:04] In this one, we just drag and drop an image.
[00:02:08] For now, I will be showing you an example using an image we generated
[00:02:13] in the last module, which was this facade with the railing
[00:02:19] we edited on. And actually,
[00:02:23] we're going to bypass the third one as well.
[00:02:26] So click on bypass.
[00:02:33] Now how this works is this works on API.
[00:02:36] So we can see that we can see the amount of credits that it will take.
[00:02:41] It's a lot. 320 credits per run is a lot.
[00:02:47] it has to do with the resolution.
[00:02:49] If we wanted low resolution, it's only 148.
[00:02:53] If we bump it up to 4K,
[00:02:57] so a 4K video out of this image is going to cost
[00:03:02] 1,600 credits.
[00:03:04] So that is a lot. That is like if I count quickly,
[00:03:09] it kinda depends on your plan,
[00:03:14] but it's like at least five to ten euros just for
[00:03:19] one image like one video. So for now we're going to keep it actually pretty
[00:03:25] low as an example. If you're very confident about this and you want to
[00:03:31] To actually make a video for a client or for the competition.
[00:03:34] Test first at 480 and then you can always go back
[00:03:38] to 1080 later on. Now this prompt has to go because it's not relevant for us.
[00:03:44] The ratio I would do adaptive because I'm not sure which ratio this is.
[00:03:51] If you know what ratio it is, you can click on the one presented here.
[00:03:58] Now another big impact on the credits is how long do you want the video to be?
[00:04:03] If you just say seven or eight seconds,
[00:04:06] it's about 170 credits.
[00:04:10] If we bump it up to 15, of course,
[00:04:13] it's going to be double. So the most expensive video you could make is 4K.
[00:04:19] That is about 3,400 to 3,500 credits,
[00:04:26] which is a lot.
[00:04:28] so let's not do that and keep it at
[00:04:34] Something like this.
[00:04:37] To test. Now the biggest thing is the prompt.
[00:04:41] How do we prompt this? We go to our prompt coach.
[00:04:46] I typed start and then I will
[00:04:53] upload this image and
[00:04:56] say Seedance
[00:04:59] 2.0 since while setting up this prompt coach we said that if we just
[00:05:06] say Seedance 2.0 it the model knows how to write
[00:05:10] the prompt specifically for this model so we don't have to worry about
[00:05:15] how to prompt something. I want
[00:05:18] to cinematically zoom in.
[00:05:24] On the railing in the loggia.
[00:05:30] Let's say this is an important detail that I want to show in my presentation
[00:05:35] for any kind of reasons. I prompted here.
[00:05:38] So now the agent already knows what the starting image will be and it knows
[00:05:44] how to instruct Seedance to actually do the action.
[00:05:50] So we will go here and
[00:05:54] paste the prompt in once we have it.
[00:05:59] Okay, the model was done, so it gave it this very long JSON prompt.
[00:06:03] I haven't actually read it, so I just click on copy.
[00:06:09] I go in here and I paste it in here.
[00:06:13] Now I would really recommend reading it through because sometimes it
[00:06:17] may tell things that are not true.
[00:06:19] I'm gonna keep for now the Chinese part here,
[00:06:24] but you can delete it if you want.
[00:06:27] So we just click on run.
[00:06:29] And then the model will start to generate,
[00:06:33] as we can see it becomes blue,
[00:06:34] the output video will be here.
[00:06:41] So the workflow that we will be using,
[00:06:44] if you go to the templates and filter based
[00:06:48] on Seedance 2.0, it's this last one.
[00:06:53] Now all of them show what they do.
[00:06:56] So if you have multiple reference images and you want to link them together,
[00:07:02] use this one. If you have a first and a last frame,
[00:07:06] so as we saw in the PowerPoint,
[00:07:08] use this one for
[00:07:11] The most simple one is this one.
[00:07:14] So we click on here, and what we see is a base image,
[00:07:18] this node.
[00:07:22] Which the prompt we will delete.
[00:07:24] I will provide the
[00:07:31] Starting image. This is the one that we generated in module three using
[00:07:37] image to image where we edited the railing and we made this loggia.
[00:07:44] Now, what we would have to do
[00:07:47] is we go in our prompt coach.
[00:07:52] Remember module one, this is something we set up together,
[00:07:56] and in the instructions we said.
[00:07:59] Or we provided all the information which also included the instructions
[00:08:04] on how to prompt for Seedance 2.0.
[00:08:11] Okay, so I would say something like this.
[00:08:19] So Seedance 2.0, I want to cinematically zoom in on the railing
[00:08:24] in the loggia. Even this isn't super well prompted
[00:08:31] because of course there's only one loggia,
[00:08:33] so this is a bit confusing, but you get the point.
[00:08:35] it provided this long prompt,
[00:08:38] I copy it.
[00:08:41] Then we go in here and I've already done it because as
[00:08:47] you can see that is the information here?
[00:08:51] No. this took like two minutes to generate so we don't lose too much time,
[00:08:57] but I just took this prompt.
[00:09:02] And I provided it in this text part.
[00:09:05] The settings I used was Seedance 2.0.
[00:09:09] The prompt is here. The resolution I put at 720 pixels.
[00:09:14] Ratio I put on adaptive because I don't know what ratio this exactly is.
[00:09:20] So it's safer to do adaptive. The duration is how many seconds the video will take.
[00:09:26] of course, the longer the more expensive it will be.
[00:09:30] I click on
[00:09:32] Generate audio because if I toggle it off,
[00:09:34] it's not becoming cheaper. So then I can just leave it on.
[00:09:38] The seed is like something I don't really care about in this workflow,
[00:09:43] so I can just keep it as it is.
[00:09:45] Now if we want high resolution,
[00:09:48] so for example, 4K, then you can see that the credits are super super like
[00:09:54] it jumps up. If we put it at 15 seconds,
[00:09:58] 4K it's like almost 30 euros for a video.
[00:10:02] So this is a lot or like twenty euros I think for a video if we generate
[00:10:08] it like this. so I keep it at seven with seven twenty pixels because
[00:10:14] for now we're testing a bit, so that's enough.
[00:10:20] Then this is the result.
[00:10:30] So as you can see it does what it instructed to do,
[00:10:35] it zooms in on the image. But since our prompt wasn't super interesting,
[00:10:42] the output is not interesting as well.
[00:10:49] Now, the question could be: how do I get more control over what
[00:10:55] the video is actually showing?
[00:10:57] Since in this input image, it's quite obvious that the railing that
[00:11:02] we want to show is here. So it's not super hard to zoom in on there.
[00:11:08] What if we want something more specific that is hard to explain by words?
[00:11:14] For example,
[00:11:17] Another example in the in the prompt coach that I just started
[00:11:23] was I made some annotations on the image and I said,
[00:11:28] okay, this red detail here, how the railing is connected to this wall
[00:11:34] and how the panel, or the window mullions,
[00:11:40] are connected to this to this corner,
[00:11:45] I would
[00:11:46] say.
[00:11:46] I'll just give it two colors and then I said Seedance 2.0 so it knows which model
[00:11:52] it is for. First make the video zoom in on the red circled railing detail
[00:11:57] and after it zooms in on the blue circle.
[00:12:01] The video is eight seconds long.
[00:12:03] This is also an important one because then the model can prompt specifically
[00:12:09] and it should say something like: from second one to four,
[00:12:13] do this, four to eight, do that.
[00:12:16] Right. So I took this prompt. As you can see here,
[00:12:21] the note, the feedback from the prompt coach, was: upload
[00:12:25] the clean render, not the annotated PNG.
[00:12:28] Now I didn't listen to this advice,
[00:12:30] so
[00:12:34] If we go in here, I provided the same image.
[00:12:40] I took the this prompt,
[00:12:45] so I said copy.
[00:12:48] I pasted in here, the settings were the same,
[00:12:51] so I put it at eight seconds, and this is the output.
[00:12:59] So it does super well zoom in exactly on that spot and then afterwards
[00:13:04] it zooms in on the window mullion.
[00:13:07] Now I'm very happy with the first part where it actually goes exactly there.
[00:13:14] This one I imagined more like the corner,
[00:13:17] but this is my first try. So then I would go back into Claude,
[00:13:22] to my prompt coach, and either I would say make it more specific.
[00:13:28] ...
[00:13:33] And make sure it zooms in.
[00:13:40] The blue circled corner.
[00:13:45] For example, something that I expected it to do,
[00:13:49] to be honest, was instead of zooming in first.
[00:13:59] And then immediately cutting to the next scene,
[00:14:01] I thought it would do an extra transition,
[00:14:03] but I didn't specify this. So I would say make sure
[00:14:08] it does a smooth transition.
[00:14:18] Between the first shots zoom in on the
[00:14:31] Red detail.
[00:14:37] And the second shot.
[00:14:43] Blue corner detail.
[00:14:48] Make sure it's
[00:14:50] all one continuous shot
[00:14:56] and no
[00:15:04] Smooth.
[00:15:08] So something like this. this is again maybe not the best way to say it,
[00:15:14] but then my prompt coach can give me a
[00:15:18] new input one and I can retry.
[00:15:23] Now what you could also do is download this video and input it in here.
[00:15:29] I'm not going to do that, but it's an option if you like.
[00:15:37] So I'm not going to run this video but you get the idea.
[00:15:41] I will provide all the videos
[00:15:48] that we generated here so I can download it.
[00:15:55] And then you have access to it as well.
[00:15:57] For these videos, it's the same.
[00:16:00] So if you download them and you drag and drop them in Comfy you can also
[00:16:05] see the prompt. So don't worry about that.
[00:16:09] So the example we saw here was first describing where you want to zoom in.
[00:16:14] The second one was actually annotating I want exactly this part to be zoom in,
[00:16:21] and then this one.
[00:16:24] we can also add like an arrow here saying okay,
[00:16:27] after the first zoom in, follow the green arrow to this detail and
[00:16:31] it will probably do that. we could also do to make it more simple,
[00:16:36] one shot saying zoom in on the red detail of like four seconds,
[00:16:41] and then another one, zoom in on the blue one,
[00:16:44] blue circle, and then montage it together.
[00:16:47] There's endless ways of doing this.
[00:16:49] ...
[00:16:51] But the idea to have control is to just make annotations on the input image.
[00:17:03] Okay, I hope this is a bit clearer for now.
[00:17:07] So we start from a single image and we go into a video.
[00:17:11] the next template we're going to use is already pre-made,
[00:17:18] so we download the video.
[00:17:24] And then we drag and drop it in Comfy.
[00:17:27] And you can see the workflow.
[00:17:31] Don't mind these errors,
[00:17:34] it's because the input images that I provided are actually not
[00:17:39] the they're not there anymore because sometimes it doesn't remember
[00:17:45] them in the metadata,
[00:17:49] but doesn't really matter because it's just an example.
[00:17:53] This workflow takes more than just one image and turns it into a sequence of shots.
[00:17:59] Essentially, this is the result.
[00:18:04] So this is just one video of seven seconds.
[00:18:08] It takes multiple shots and makes something like
[00:18:15] this. How I made this is I went to templates and it's this template.
[00:18:22] So you can see this one is almost the same as this one.
[00:18:28] Prompt again. I just went into my prompt coach.
[00:18:33] I uploaded several shots of the building.
[00:18:44] I have added them here below so you can see.
[00:18:47] You can just try it for yourself,
[00:18:49] download these and put them in these slots.
[00:18:55] So you can drag and drop them in there or click on this button to add them here.
[00:19:01] Take the same images provided in the prompt coach,
[00:19:06] say whatever you want, it will write the prompt and you paste it into Comfy.
[00:19:12] and then you will get the result as seen here.
[00:19:17] So that is one thing. There is another workflow that
[00:19:23] we will try ourselves, which is again just a single
[00:19:30] Image input.
[00:19:34] And it's this prompt so fixed
[00:19:39] tripod time lapse building remains completely static clouds drift
[00:19:46] slowly across the sky etc so I will prepare
[00:19:50] it okay fast forward I have changed the prompt a little bit
[00:19:57] and what I want to show you here is that I first tried
[00:20:03] it to put it in the prompt coach so a fixed tripod time lapse
[00:20:09] And the result was not bad at all.
[00:20:12] I'll turn the music off.
[00:20:18] It wasn't bad because it is a time lapse and you see things are moving.
[00:20:22] So this was this
[00:20:28] was done using like a very long prompt,
[00:20:32] I think.
[00:20:38] Not this. If I show you here,
[00:20:42] open as workflow in a new tab. I can go back to the prompt.
[00:20:47] You see, it was again a very long prompt.
[00:20:49] that was the output of the prompt coach.
[00:20:52] Now it wasn't that special, so I tried again.
[00:20:57] Maybe I should just pick this as a prompt,
[00:21:00] so not overcomplicated, and see what the result is.
[00:21:05] ...
[00:21:15] And this was actually more what I expected.
[00:21:19] So sometimes this prompt coach isn't always the best way to actually make
[00:21:25] a prompt better. So just try a different way.
[00:21:29] and this is in my opinion a nice result.
[00:21:33] So here we saw three workflows.
[00:21:35] on the right side again on Miro,
[00:21:38] I have put a lot of different resources.
[00:21:43] For example, here video to video.
[00:21:46] What this is, is it takes a video,
[00:21:50] the workflow turns a seven-second video into a 14-second one,
[00:21:56] it could be interesting during editing of videos.
[00:21:59] So maybe for a lot of people this is not applicable,
[00:22:04] but often when you're editing something and you want to slow down a video
[00:22:08] and you do it
[00:22:10] in Adobe After Effects or Adobe Premiere Pro or something,
[00:22:13] it starts to look very choppy because the frames are being stretched.
[00:22:19] So you can kind of see that it is slowed down.
[00:22:22] With this workflow, so if you download this video and you import it in Comfy,
[00:22:28] let's do it.
[00:22:31] So if we download this one, go in Comfy.
[00:22:41] Drag and drop it in here. You can see this is my workflow
[00:22:45] for video frame interpolation and the results.
[00:22:53] It's just it's the same video,
[00:22:56] so this is a different test I did.
[00:22:59] but it's double the length for every frame of the video.
[00:23:04] the model generates another frame.
[00:23:08] So it just doubles the amount of frames,
[00:23:10] which is cool for editing. So check that out if you think that is interesting.
[00:23:16] and here are some more videos like this one,
[00:23:21] for example.
[00:23:27] Also using Seedance. This is another model, called LTX.
[00:23:31] I'm not going to show you the entire workflow.
[00:23:38] but you can check it out. These examples are interesting as well.
[00:23:45] So just download them and see if you can do something with it.
[00:23:49] I can delete this one.
[00:23:52] Here was another project we did.
[00:24:01] Bit of a weird one, but could be interesting.
[00:24:04] and then an extra thing: if you're working with Claude and you have
[00:24:10] a bit more experience, you know about skills.
[00:24:13] If you don't know what a skill is,
[00:24:15] don't worry, you can look it up on the internet.
[00:24:17] but there is a specific skill made for Seedance.
[00:24:24] So if you want, you can click here on more.
[00:24:36] Export as markdown and then you can import it into Claude as a skill,
[00:24:41] and this will make prompts
[00:24:43] specifically for Seedance 2.0.
[00:24:49] But this is not necessary, it's a bit like the project instructions,
[00:24:52] like the prompt coach we prompt coach we did,
[00:24:55] but in a in a different way. So check that out.
[00:24:59] Then you have Google Omni, which is the most advanced video model from
[00:25:05] Google where I tried this prompt to get like all seasons.
[00:25:12] Yeah.
[00:25:15] And as you can see it's pretty capable.
[00:25:18] so if you're interested in that.
[00:25:21] And you can also go to these links and check out these examples.
[00:25:26] But it's a lot of a lot of the times it's the same.
[00:25:29] just making a video out of a image.
[00:25:39] One last thing I would like to add here is under resources you will find models
[00:25:44] links. And this website is pretty interesting if you open it.
[00:25:48] There are a lot of prompts for Seedance 2.0.
[00:25:52] you can see trending prompts,
[00:25:54] and here you can
[00:25:58] sort or filter, maybe something like architecture
[00:26:02] or animation.
[00:26:06] I don't know what your goal is,
[00:26:08] but this is a nice website for inspiration to just see a lot of things that
[00:26:15] that are possible.
[00:26:18] That being said, I'm going to end module four here.
