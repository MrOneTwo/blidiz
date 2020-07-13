# Blidiz - experiment in using MIDI controller in a 3D CG workflow

Yes, Blidiz is a bad name.

The idea here is to use a MIDI controller to easily transfer meshes from ZBrush to Blender or Marmoset Toolbag.
I would call this *an experiment in creating pipes connecting my favourite CG apps*. This, in of itself, might
never be useful or convenient.

Let me explain what this is a bit better. Imagine you sculpt in ZBrush but you render in another app. This project
allows you to press a button on a MIDI controller to export the currently selected subtool, to a predefined
directory. A second Python script observes that predefined directory. As soon as it sees any changes (file modified
or created) in that directory, it sends a command to a server, which runs in Blender's Python environment.
That command tells Blender to update the asset in the Blender project.

Imagine a world where your numerous apps can easily talk to each other, without the silly dance of exporting and
importing. Yes, I know that GoZ exists but lets be honest, it's a bit underwhelming. I don't want a very limited
plugin that connects two apps. I want a flexible infrastracture to push data around.

## How to set this up

I've recorded a demo of how this setup works. It's an experiment so nothing here is convenient ;)

[LINK TO THE VIDEO](https://www.youtube.com/watch?v=NbS9NZiRaGI)

