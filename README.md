# Blidiz

Yeah it's a bad name.

The idea here is to use a MIDI controller to easily transfer meshes from ZBrush to Blender or Marmoset Toolbag.
I would call this *an experiment in creating pipes connecting my favourite CG apps*. This, in of itself, might
never be useful or convenient.

Let me explain what this is a bit better. Imagine you sculpt in ZBrush and you render somewhere else. This project
allows you to press a button on a MIDI controller and that will export the currently selected subtool to a predefined
directory. Second Python process sees a change in the target directory occured so it sends a command to a server,
which runs in Blender's Python environment, to update the asset in the Blender project. Blender's server loads the
updated asset.

Imagine a world where your numerous apps can easily talk to each other, without the silly dance of exporting and
importing. Yes, I know that GoZ exists but lets be honest, it's a bit underwhelming. I don't want a very limited
plugin that connects two apps. I want a flexible infrastracture to push data around.

## How to set this up

TODO: explain
TODO: add link to a youtube presentation


