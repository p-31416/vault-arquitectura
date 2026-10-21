---
tipo: transcript
fuente: archademy.ai (curso AI x Gaudi, area de participantes)
modulo: gaudi-workflow
titulo: The Gaudí Workflow
idioma: en
fecha_creacion: 2026-10-21
tags: [yt, transcript, curso-ai-gaudi, mux, gaudi-workflow]
---

# The Gaudí Workflow — en

> Transcripcion automatica de los subtitulos del modulo del curso (Mux).
> Origen: https://vz-4ced3a48-15e.b-cdn.net/4233014c-96df-4e45-9860-6ddb7dcc5923/captions/en.vtt
> Duracion de la pista de subtitulos: 00:35:37,168 --> 00:35:42,130

[00:00:00] Hello and welcome everybody to module seven.
[00:00:03] This is the final module of this course and it will be about Gaudí.
[00:00:09] Now, as you saw the previous module,
[00:00:11] the panel discussion, we already had like a contextualization about Gaudí,
[00:00:17] but this one is going to be more in depth.
[00:00:20] We have developed a workflow that we call the Gaudí workflow.
[00:00:25] Before actually diving into the topics of this course,
[00:00:29] as you can see here, of this module,
[00:00:32] I will give the word to Cas.
[00:00:36] Cas Esbach is an architect from the Netherlands.
[00:00:42] Make sure to check him out because he's very,
[00:00:45] very talented. He's inspiring to me in a lot of ways.
[00:00:51] I think...
[00:00:53] It's definitely one to check out.
[00:00:56] Cas is currently a professor at SCAD before
[00:01:02] he was an architect at BIG and MVRDV.
[00:01:05] So he has a real foundation of architectural experience,
[00:01:09] let's say in the traditional way,
[00:01:11] but in the later phases of his time at MVRDV,
[00:01:15] he really got into generative AI and he gave a lot of courses himself.
[00:01:23] and I actually partnered with him to create this course for you guys.
[00:01:28] So now I'm going to give the word to Cas.
[00:01:35] Yes, thanks Thomas for that introduction.
[00:01:38] I'm Cas Esbach. I'm also a jury member on this competition.
[00:01:43] I thought it would be good that, before
[00:01:49] we really touch on the workflow,
[00:01:51] I want to take you guys a step back and really talk about Gaudí himself,
[00:01:55] right? The reason we're all here.
[00:01:57] Antoni Gaudí was a Catalan architect who worked in Barcelona around
[00:02:00] the turn of 20th century from the 1880s up until his death.
[00:02:05] in 1926. You probably know his work,
[00:02:08] you know, the buildings like the Sagrada Família,
[00:02:10] Casa Batlló, Casa Milà, and Park Güell are some of
[00:02:14] the most recognizable architectural pieces in the world.
[00:02:17] Here the Sagrada Família, here Batlló,
[00:02:20] Milà, and Güell.
[00:02:23] He took over the Sagrada Família in 1883 and ended up devoting the rest
[00:02:28] of his life to it, working on it right until he died.
[00:02:34] What I think his buildings are known for are his organic forms,
[00:02:38] the flowing, the shapes, these things that architects aren't easily able
[00:02:44] to draw and let alone that it's really hard to build these things.
[00:02:47] But I think it's good that when we talk about Gaudí,
[00:02:50] we don't really talk about how his buildings look,
[00:02:52] but we focus on the way the buildings work and specifically about
[00:02:58] how he integrated tools into his design process to create these buildings.
[00:03:04] Church of Colònia Güell Gaudí built a hanging chain model and he spent close
[00:03:09] to a decade refining it. Important thing is to understand this is it's
[00:03:14] not a sketch or drawing in a way,
[00:03:18] it's a physical calculator that helped him build the building.
[00:03:22] Because when you hang a chain,
[00:03:24] you can imagine with multiple weights at certain points,
[00:03:27] you craft a shape that's able to carry itself on,
[00:03:31] to carry its own.
[00:03:33] It's built on pure tension so that when you reverse it,
[00:03:36] you flip it upside down, you get one form that stands in pure compression,
[00:03:41] which is exactly what masonry and stone are great
[00:03:46] at dealing with compression. So in a real sense,
[00:03:51] Gaudí was using gravity to resolve a structural problem for him,
[00:03:55] a structural problem he probably wasn't able to solve.
[00:04:00] or to calculate in a way, but he was able to,
[00:04:02] let's say, simplify it, translate it as abstracted in a way through,
[00:04:08] say, using a model. And that's also how we should really think about Gaudí.
[00:04:14] He's not really somebody that trusted or used drawings or abstraction,
[00:04:19] though he preferred to work through physical models because they
[00:04:22] let him understand space directly rather than
[00:04:27] Let's say creating an abstract representation,
[00:04:29] a drawing, which then would have you interpret space through that,
[00:04:33] a rendering, right? His entire design process ran through the tools he used,
[00:04:38] not through the drawings of the final result.
[00:04:40] In other words, Gaudí wasn't just producing a building,
[00:04:47] was producing a tool that would help him shape a building.
[00:04:51] And I think that's the part that really matters for what we're doing.
[00:04:57] Now these curves aren't a stylistic decision.
[00:04:59] Well, they are, but they're a result of a design process where
[00:05:06] the direct output of a structural system results in its efficiency,
[00:05:11] right? The efficiency results in the shape and that shape is a,
[00:05:17] is an answer to a physical problem.
[00:05:19] So when, when Thomas is going to be explaining that Gaudí workflow,
[00:05:24] when you're looking
[00:05:28] To train an AI model, let's say more traditionally with images,
[00:05:33] you will get things like curves and undulating surfaces and texture in material.
[00:05:38] But what you won't get is the conceptual transfer.
[00:05:41] So you'll get a stylistic transfer.
[00:05:43] You won't get a conceptual transfer,
[00:05:46] right? And between the copying of the appearance and understanding
[00:05:51] the underlying logic, there will be a gap.
[00:05:54] And that's the one we need to close.
[00:05:57] And that's the whole point of this module.
[00:05:59] So none of the work that you are going to be doing should be about copying Gaudí's
[00:06:04] aesthetic, or making something that just looks like Gaudí. It should not be that.
[00:06:08] It's about using AI as a tool to let us understand structural logic
[00:06:15] and form instead of drawing a shape and hoping it stands the test of time.
[00:06:19] And that's why I will pass it back to
[00:06:25] Thomas right now. Thank you.
[00:06:30] Thank you, Cas, for the interesting introduction about Gaudí.
[00:06:35] Right now, we're going to continue with the demonstration.
[00:06:39] But first, I'm going to give you my take on what we're about to do.
[00:06:43] My take on this is the following.
[00:06:47] The role of the architect is shifting from production to judgment.
[00:06:52] Production architects will become judgment architects.
[00:06:57] But what I mean by production architects is architects who
[00:06:59] are constantly producing things.
[00:07:01] I think the production part will be more and more assisted
[00:07:07] by AI and therefore the real job of the architects will be judging,
[00:07:12] judging the output of AI generated content.
[00:07:17] You can see AI today as the hanging model of Gaudí.
[00:07:22] a system more capable than us at generating possibilities.
[00:07:27] Gaudí kept human judgment while letting a bigger system do the computing.
[00:07:33] And I know this is probably a hot take and a lot of you might not fully agree with
[00:07:39] me on this, but this is my take on this.
[00:07:44] it's an introduction to the workflow that follows.
[00:07:47] Often people reduce Gaudí's work to aesthetics.
[00:07:52] For example, his mosaic and bright colors.
[00:07:55] But this misses the point. His real oeuvre was more about spatial thinking
[00:08:01] and architectural relations, the biomimicry we talked about.
[00:08:05] The power of Gaudí's approach was in his biomimicry rather than
[00:08:11] his recognizable aesthetics. So by now you might be thinking,
[00:08:16] okay, so what are we actually going to do?
[00:08:19] We won't
[00:08:21] try to reduce the essence of Gaudí to for example a LoRA.
[00:08:27] We will try to find the essence of Gaudí in the following workflow.
[00:08:32] I call it the Rhino to Gaudí workflow.
[00:08:35] And the way we will experiment with this,
[00:08:40] it's always going to start from a 3D model.
[00:08:43] So we take a screenshot of a 3D model.
[00:08:45] This means that when you're doing the competition,
[00:08:48] the initial phase and the initial ideation must come from you.
[00:08:54] So you must build a 3D model.
[00:08:57] which can be very...
[00:09:01] very vague or very abstract like this one here.
[00:09:05] But we need that as a starting point.
[00:09:08] As we saw before with the custom LoRA I made,
[00:09:12] we can take a material and we can apply it on this geometry.
[00:09:17] Of course, we also have to provide a prompt where we say in this case,
[00:09:21] for example, this is a multi-story open-air outdoor climate museum
[00:09:28] and the structure is made of this natural stone.
[00:09:31] So how are we actually going to do this?
[00:09:34] This is on Miro, so you will just find everything you need on there.
[00:09:39] The first step will be to set up a Gaudí assistant.
[00:09:42] Then we have some examples of the workflow.
[00:09:46] And here we're going to put all the live demo.
[00:09:54] results.
[00:09:58] The first thing we will have to do is go to the Gaudí assistant.
[00:10:02] So this assistant is essentially a set of project instructions that fully understands
[00:10:09] how to transform our model into a more Gaudí-like 3D model.
[00:10:15] So we just select everything here.
[00:10:18] We copy it. We go to our favorite LLM and we make a new project called Rhino
[00:10:24] to Image Gaudí.
[00:10:26] Then we go to instructions. We click here and we provide this whole instruction.
[00:10:33] Now I think it didn't select the actual JSON.
[00:10:43] So how we can do this better is we click here
[00:10:49] and we click on export as markdown.
[00:10:53] Then we will download it.
[00:10:58] It will be in your downloads folder.
[00:11:07] As you can see here, you right click on it,
[00:11:10] open with Notepad.
[00:11:17] Okay, so it opens like this. I'll do it one more time.
[00:11:22] So we right click it, open with Notepad.
[00:11:26] And then you select all the text.
[00:11:33] and you provide it.
[00:11:37] in here. You will see that it keeps the structure better.
[00:11:42] We click on save instructions.
[00:11:44] Then we need a screenshot of our 3D model.
[00:11:52] In my case I will be using this one,
[00:11:55] just a very basic 3D model of a massing.
[00:12:04] I will type start.
[00:12:09] and see what happens.
[00:12:19] Now the model asked me what program fills the revealed interior.
[00:12:24] So it just asked what the use case is here.
[00:12:27] And here you just have to answer the questions.
[00:12:30] So in your case, it might be an exposition or a museum.
[00:12:34] In my case, it's a residential.
[00:12:42] And mixed use building.
[00:12:47] How much do we want it to be like Gaudí?
[00:12:50] So moderate, full structural Gaudí,
[00:12:52] near maximal or hold nothing back.
[00:12:55] I will take seven for now just to show
[00:13:01] it, but not too extreme. You can play around with this.
[00:13:04] Lead moves: keep my three proposals.
[00:13:07] So.
[00:13:11] Each bay becomes a tall parabolic void framed by catenary
[00:13:16] rib or ribs following the... yeah,
[00:13:20] wow, this is very specific. Let's say all three.
[00:13:28] So provide a lot of information about what your vision is
[00:13:32] for making this more Gaudí. So I would really advise you to make it
[00:13:38] as specific as possible. Add a lot of information here.
[00:13:41] So right, for example, the walls become like this,
[00:13:46] or you provide another reference image and you really give a lot of information.
[00:13:51] Unlike me,
[00:13:56] I just.
[00:13:57] selected yes or no and I didn't provide a lot of information.
[00:14:04] So you copy this and now we go into Comfy and we quickly make a new workflow.
[00:14:10] We do that by double clicking,
[00:14:12] clicking load image.
[00:14:15] Here, of course, we load the same image as before.
[00:14:19] We zoom in. Then we double click again.
[00:14:24] We type Nano Banana 2. Since this is a model that we will be using for this step,
[00:14:30] we connect image like this.
[00:14:37] We take this node and we release it.
[00:14:40] Here we click on Save Image or you type it up here
[00:14:44] and it's automatically connected.
[00:14:48] We double click and we type compare images.
[00:14:54] This one by Comfy.
[00:14:58] Image A we connect here, image B we connect here and that's it.
[00:15:05] Okay. Now if this is a bit too quick,
[00:15:09] don't worry because the images,
[00:15:12] this one, this image and this one,
[00:15:16] they have the workflow embedded in them.
[00:15:19] So you can just download them and drag and drop them in Comfy and you will have
[00:15:23] the same workflow. So you don't have to build it yourself.
[00:15:27] The settings resolution we put at 2K.
[00:15:30] Thinking level we put at high and the rest we can keep.
[00:15:36] You can put a aspect ratio but it's not necessary.
[00:15:40] And here we put the prompt that the agent gave us.
[00:15:49] Then we click on Run.
[00:15:54] And this is the result. if we zoom in here,
[00:15:57] we just hover over the image.
[00:16:01] We can see that our 3D model gets transformed into something that
[00:16:08] Nano Banana thinks is more Gaudí-esque according to our agent.
[00:16:13] So if we zoom in, it's interesting that the main geometry gets followed almost
[00:16:19] exactly. And all the infill of the planes,
[00:16:24] This is where it gets interesting.
[00:16:27] Now, of course, if you go back here and you really look at the prompt
[00:16:32] and you customize this prompt to your liking,
[00:16:35] or here you provide way more information,
[00:16:39] it will become better and better.
[00:16:41] I'm just showing the workflow since I am 100 % sure that it works.
[00:16:46] It's the same workflow I used here.
[00:16:52] to this image. I answered some questions about what I thought that could
[00:16:58] be cool to get these kind of tree-trunk features on the columns.
[00:17:04] And then in the next step, we turned it into a realistic image.
[00:17:09] But as you can see for the geometry,
[00:17:11] that is super important that we lock it in here.
[00:17:14] So what we're actually doing is we're taking two steps.
[00:17:20] And in the first step, so from here to here,
[00:17:23] we're locking down the geometry and from here to here,
[00:17:27] we're applying aesthetics. taking this
[00:17:34] thing of generating an image and we split it into geometry and aesthetics.
[00:17:39] And the geometry is then based on Gaudí and the aesthetics is based
[00:17:44] on whatever input we provide.
[00:17:50] So here we can see if we like it or not.
[00:17:53] I would always recommend to do another run to see the difference.
[00:17:59] Actually, I like this one a lot because I like the shapes of the facade like that.
[00:18:05] So I would download it already.
[00:18:09] And while this one is generating,
[00:18:12] I will provide it here on Miro.
[00:18:26] and let's see when this one is ready.
[00:18:29] So this one is ready.
[00:18:32] It's a bit crazy. So as you can see,
[00:18:37] it followed the geometry, but added like a different,
[00:18:40] like an extra floor on the ground.
[00:18:42] So I'm going to stick with the first version,
[00:18:46] this one.
[00:18:49] You must remember that in the project instructions,
[00:18:52] I put seven, so I could have put more or less,
[00:18:56] or you could change the instructions to make it more Gaudí-esque or apply your idea
[00:19:02] about what Gaudí is. This is just an example.
[00:19:05] Okay, for the next step to make it realistic,
[00:19:08] it's essentially just the Rhino to Image workflow.
[00:19:11] So we go to our Rhino to Image project we made before.
[00:19:18] provide our.
[00:19:22] massing we just generated then
[00:19:26] we provide a material for me I'm going to choose
[00:19:38] this red marble since we use it in our previous example as well.
[00:19:43] I'm going to give a bit of context, saying residential building
[00:19:50] in Barcelona.
[00:19:57] and see what happens.
[00:20:01] Now, while this one is generating,
[00:20:05] we can go back to Comfy and remember that when
[00:20:11] you download this one, you will have another Rhino to Image workflow.
[00:20:16] So we download this one.
[00:20:21] We go and we drag and drop it in here,
[00:20:27] which opens up
[00:20:30] workflow that I used to generate this one as you can see.
[00:20:33] So this materiality is prompt.
[00:20:37] Of course we're going to change it using this one.
[00:20:44] and this one. Since those two were also the input of the agent,
[00:20:50] the prompt is ready. So we copy it.
[00:20:54] We replace it here.
[00:20:57] We make sure that everything is set into place.
[00:21:01] Again, here you can choose which LoRA you use,
[00:21:06] either the premium or the basic one.
[00:21:08] Of course, I'm going to do it with the premium one to see what the result is.
[00:21:16] And this is what the workflow did.
[00:21:19] So it applied the material exactly over the geometry.
[00:21:23] so again, in this step the geometry doesn't get changed,
[00:21:27] just the material application.
[00:21:29] Now this is of course a view,
[00:21:34] which is more from a distance.
[00:21:37] I feel like the LoRA and the workflow works better when you do a zoom
[00:21:42] or like close up of a facade detail.
[00:21:45] So I will redo the whole workflow to show you again how it works.
[00:21:49] And I really advise you to think about what Gaudí means to you,
[00:21:55] how you could interpret his biomimetic approach
[00:22:02] and really apply it on your project.
[00:22:05] Probably a view like this.
[00:22:08] I mean, from a distance, showing the whole building is not the best approach.
[00:22:14] I feel like a facade detail like this or close
[00:22:20] up works better because you can see that
[00:22:24] it focuses on small details better.
[00:22:32] So I'll provide this image here and then.
[00:22:37] I will do another example.
[00:22:56] For the second example, we're going to use-
[00:23:07] The following.
[00:23:11] So this massing, it's a massing we have already seen before as well.
[00:23:18] And another example was this facade structure that is kind of waved.
[00:23:24] So same steps,
[00:23:27] we go to Comfy, we go back to
[00:23:30] our previous workflow provided in here.
[00:23:36] We need the prompt, so we go to our...
[00:23:41] Gaudí workflow or Gaudí agent which
[00:23:46] is this one you provide it here
[00:24:00] So with this one I'm going to provide a bit more information.
[00:24:03] So I'm going to say the gray is the main structure.
[00:24:09] Facade
[00:24:12] of a
[00:24:14] residential building
[00:24:20] in Barcelona.
[00:24:30] ...
[00:24:38] are railings
[00:24:43] of the balconies.
[00:24:48] Not just.
[00:25:01] The cyan part, I accidentally clicked on regenerate,
[00:25:05] but it's not a problem because it will do exactly the same.
[00:25:08] So I will say that the cyan part are windows.
[00:25:14] So when it regenerates,
[00:25:18] it will ask me the same. So I don't have to worry about me clicking the wrong thing.
[00:25:25] Then I would also say,
[00:25:27] the program: it's a residential building, I already said that. Sacred elements:
[00:25:32] the rhythm of the facade
[00:25:37] and the dimensions is sacred
[00:25:43] what also helps here is to give the dimensions so for example here
[00:25:49] i know that i modeled it that the distance between the floor and
[00:25:54] the ceiling is three meters so
[00:25:58] ceiling height is three meters.
[00:26:01] This helps the model understand the scale because
[00:26:08] if we say it's six meters then the scale is completely different of course.
[00:26:16] Gaudí scale. Let's put it at eight for now.
[00:26:24] So just follow the questions. It will ask as much questions as
[00:26:28] it needs to understand your goal.
[00:26:41] So it's generating another prompt.
[00:26:43] For this tutorial, I'm not actually reading the prompt,
[00:26:47] but I really recommend doing so because sometimes the LLM hallucinates
[00:26:53] and it writes super weird stuff.
[00:26:54] And then you're troubleshooting when it's just the prompt.
[00:26:58] So we keep the same settings.
[00:27:01] We click on run.
[00:27:07] while this one is running because it always takes like 30 seconds we can
[00:27:11] go back to this workflow and update our image
[00:27:19] And we can choose a new reference.
[00:27:23] Let's say you have...
[00:27:29] instead of a material, more like a facade that you would like to
[00:27:33] try of another architect,
[00:27:36] for example.
[00:27:40] Let's actually try this one. It's
[00:27:43] a very expressionist facade and also maybe the blue
[00:27:48] and the color will relate a bit more to Gaudí as well.
[00:27:59] Okay, we can go back to.
[00:28:08] This one is not generated or it is generated.
[00:28:14] For some reason this node didn't get triggered but that's why we have this safe
[00:28:19] image node because we can still see that it really did a very interesting
[00:28:23] job actually. It really made it very biomorphic.
[00:28:28] So let's download it.
[00:28:33] And we go back to the Rhino to Image workflow.
[00:28:39] provide this image.
[00:28:43] with this reference, we say again,
[00:28:46] like residential, the side.
[00:28:54] And whatever you want to say.
[00:29:02] loggias, I don't know, whatever you want to prompt.
[00:29:06] The more information you give,
[00:29:08] the better. I'm just going to keep it like this,
[00:29:10] which is probably not enough, but it will work anyway,
[00:29:15] I believe.
[00:29:20] We go back to our Rhino to Image workflow and here you can see we're going
[00:29:25] a lot of back and forth. So you have to be very organized.
[00:29:28] Otherwise it gets too much. Since we have two workflows in Comfy and
[00:29:33] we also have two projects in Claude or in your LLM.
[00:29:37] Make sure to have like your own system of organizing everything.
[00:29:41] So where is the building located?
[00:29:43] Let's say Barcelona.
[00:29:47] scale of the residential project.
[00:29:49] Every floor is three meters.
[00:29:57] I know this is not really the same question,
[00:29:59] but I think you get the point.
[00:30:01] The better your input, the more input,
[00:30:05] the better the output will be.
[00:30:12] So before we can actually generate an image,
[00:30:15] we also have to provide the correct input image,
[00:30:18] of course.
[00:30:24] then
[00:30:29] we click on run
[00:30:36] and see what happens. So here we can see what is being generated.
[00:30:44] It's always nice to see this little preview.
[00:31:01] And here you can see that it actually translated it perfectly,
[00:31:06] I would say, because it understood that this,
[00:31:08] for example, is a chair and this is a,
[00:31:11] yeah, this is good. I would be happy with this result.
[00:31:15] Yeah.
[00:31:21] It's so satisfying to see the before and the after because the LoRA
[00:31:25] is trained so well that it actually follows geometry exactly.
[00:31:31] Okay, so this one I will provide here.
[00:31:41] together with the reference image,
[00:31:45] which was this one.
[00:31:54] And by the time that you're watching this,
[00:31:55] there will be more examples since these are just a few examples.
[00:32:01] ...
[00:32:04] And then you could try them out.
[00:32:06] You can always download them like this.
[00:32:09] And it's this workflow for Gaudí is mostly in this first step.
[00:32:16] So make sure that you actually read.
[00:32:21] these instructions and make your own version of this because this is what
[00:32:26] I think is good and what I think is Gaudí's constructive logic and this
[00:32:31] is your start point but don't just copy this one and use it change this
[00:32:38] one if you for example say no for me Gaudí is more like this then put
[00:32:43] it in this instruction because then the output will be more personalized
[00:32:47] to you so the way you
[00:32:51] or the amount of customization you apply to this prompt,
[00:32:56] the better it will be. And the better it will make whatever
[00:33:02] you think of as Gaudí.
[00:33:08] So by now I hope the workflow is somewhat clear and that you can start
[00:33:13] to experiment with it. To make it a bit more clear,
[00:33:17] I changed the Miro board and I added some annotations to clarify my goal.
[00:33:23] As we saw before,
[00:33:26] so it's two image-to-image steps.
[00:33:29] The first step is really to lock down the geometry, to impose some extra
[00:33:36] spatial qualities.
[00:33:37] related to Gaudí. And then in the second step,
[00:33:41] we add texture, aesthetics and realism.
[00:33:45] Let's say it like that. When we have this stone reference on top,
[00:33:50] you can see it gets applied well when we take the same geometry as here on top.
[00:33:55] But we apply a different one. Of course,
[00:33:59] this becomes a different space while following the exact same geometry.
[00:34:06] Here's another example. And then of course,
[00:34:09] these ones are the ones we just made.
[00:34:12] Now I want to repeat this one for the second step.
[00:34:17] to make it more realistic, you need the LoRA and included in the course
[00:34:23] is the basic one that you will find in the folder and the premium one,
[00:34:27] the one that I have been using.
[00:34:29] yes, this one, the bottom one is available on my website.
[00:34:36] So make sure to check that one out.
[00:34:38] There's a lot of different tests that could be interesting to do,
[00:34:45] but the thing that I believe works the best is this more zoomed
[00:34:51] in version on a facade or a detail or let's say an entrance
[00:34:56] to the building or something like that.
[00:35:00] Try to always make it from eye height because the LoRA is
[00:35:04] pretty much trained on all images
[00:35:07] and photography that
[00:35:13] are taken from eye height. So don't try to make a drone shot,
[00:35:17] for example, with this because it's probably not going to work.
[00:35:19] try to keep it like this.
[00:35:28] So that being said, we're gonna end module seven about Gaudí here.
[00:35:32] And since this is the last module,
[00:35:34] we're also ending the course here.
[00:35:37] Thank you for watching and good luck with the competition.
