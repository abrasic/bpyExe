# bpyExe
Blender Python Executor. Useful for macro software (preferrably Stream Deck).
Should support all types of macro software (Razer Synapse, iCue, Stream Deck, etc...)

At this time, bpyExe is extremely un-user-friendly.

## Installation
1. Download the latest script in Releases.
2. Install the script in blender via `Edit > Preferences > Add-ons > Install...`
3. Ensure in the `Edit` tab, `Run Python Code` is shown at the bottom of the menu.
4. If no hotkey is assigned, right-click the option and assign one (Default is `Ctrl+[`, otherwise make sure you pick a hotkey that isn't in use by another function in blender)
5. In your macro software, ensure you have a proper set of rules that generally does the following:
  * Store the string already in your clipboard in a variable
  * Set your clipboard to the bpy command you want to execute in the macro (see `Finding functions in blender` below)
  * `Ctrl + [` (or whatever your assigned hotkey for bpyExe is) to display the Run command
  * `Enter` TWICE. Once to unfocus on text box, then again to confirm.
  * Set your cliboard to your old string of test from Step 1.

## Finding functions in blender
Create a new `Info` window inside blender, then execute any command in blender that you want to automate. When you execute that command, a new line will display that shows what blender executed to run that command.
