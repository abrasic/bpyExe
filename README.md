# bpyExe
Blender Python Executor. Primarily used for macroing functions with Stream Deck.

## Prerequisites
- Blender 2.80 or higher.
- [Stream Deck Software](https://www.elgato.com/en/downloads) with SuperMacro installed
    * To install SuperMacro, select `More Actions...` in the Stream Deck software then find/search for `SuperMacro`.
    <img src="https://raw.githubusercontent.com/abrasic/bpyExe/main/assets/sd_moreactions.png" height="400px">
    <img src="https://raw.githubusercontent.com/abrasic/bpyExe/main/assets/sd_install.png" height="200px">
    
## Creating a Super Macro for Blender
With SuperMacro installed, you should have a `Super Macro [BarRaider]` dropdown in the side menu of your Stream Deck panel. Drag-and-drop a `Super Macro` item onto one of your buttons. Upon doing so, your new button should appear on your Stream Deck display.

<img src="https://raw.githubusercontent.com/abrasic/bpyExe/main/assets/sd_supermacro.gif" height="320px">

Next, we need to give the button some macros. The settings currently works best for my workflow is the following:
* Paste the following code into the `Short-Press Macro` box in the bottom panel of your newly made button:
```
{{VarSet:code:***YOUR BPY CODE GOES HERE***}}
{{VarSetFromClipboard:o}}
{{SetClipboard:$code}}
{{ALT}{Y}}
{{Ctrl}{V}}
{{Enter}}{{Enter}}
{{SetClipboard:$o}}
```
**IMPORTANT: Make sure to add your code in the third argument in the first line!**

**IMPORTANT: `{{ALT}{Y}}` is the default hotkey for the script. If you changed this, you must change it in the macro as well.**

In short: The macro pastes the code you specified in the first line. It also saves your clipboard before using it, ten after the macro is performed, it will set your clipboard back to the original string before it was ran.

## Finding functions in blender
Most scene properties you change inside blender has a `bpy` function that blender executes to perform that action. To access the code that it makes, create a new `Info` window inside blender, then execute any command in blender that you want to automate. When you execute that command, a new line will display that shows what blender executed to run that command.

In this gif example, the `Info` window shows the `bpy` code that was performed by blender when I set the Timeline to frame 50.

<img src="https://raw.githubusercontent.com/abrasic/bpyExe/main/assets/sd_bpy.gif" height="320px">

So, if I ever wanted to make a macro that takes me to frame 50, I would input `bpy.context.scene.frame_current = 50` into the first line's variable.

It's recommened though that if a hotkey already exists for it, or if it's possible to assign it one (right-click and check if a `Assign Shortcut` exists), just make a simple macro that executes it. For example, setting your 3D cusror to a selected object would just be `{{Shift}{S}}{{2}}`. No need for all this!

## So, what's the point of this when you can just assign shortcuts?
Practically every important function in Blender has a hotkey. And you can even assign your own! The problem here lies that  some hotkeys or functions I use inside blender all the time cannot be performed by certain functions, or they take a lot of time to perform. Some examples include:
   * Changing `IntProperty` or `StringProperty` settings
   * Showing/hiding certain object/bone constraints for optimization
   * Scatter 4.0: Showing/hiding certain particle layers for optimization
   * Executing third-party plugins with no keymap support

Even though this may cater to only my own problems, I decided to release this to the public for anyone to try.
