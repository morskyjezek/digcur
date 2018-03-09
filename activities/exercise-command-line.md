# Basics of the Command Line Interface

Demonstrations during class assume use of Mac OS/Unix style terminal commands. However, commands for both unix and windows environments are offered below. See the linked resources at the bottom for greater detail. 

## Description

This activity aims to present basic skills for using the "[command line](https://en.wikipedia.org/wiki/Command-line_interface)" on Mac and Windows operating systems. A competent digital preservationist should have a basic level of comfort and competence with this interface for a few reasons: primarily because some tools require operation from the command line, but also because it can be a quick and efficient way to perform some actions, such as generating basic information about files and systems.

Keep in mind the difference between the command line and the visual interfaces that may seem more comfortable. We’re mostly used to interacting with computers via a GUI (sounds like “gooey”); that is, a Graphical User Interface that allows you to interact with the system visually, through clicking, dragging and dropping, pointing and tapping, etc. In some cases, such as word processors, we call this WYSIWYG (“what you see is what you get”), when what you see on the screen is comparable to what you would expect to see when the file is printed out on a page. In the command line interface (CLI), as when we are looking at markup files in a text editor, you can see what you do to get what you want. In some ways, it is a more transparent way to get a desired result because you have greater knowledge of what you have asked the computer to do, as well as what the computer is doing.

_Note: where you see “Mac” below, this generally designates a UNIX-wide command, “Windows” is generally DOS-like._ 

## General Actions

### Navigation
* determining where you are (Mac: ```pwd``` / Windows: ``cd``)
* moving within the directory structure (``cd``)

### Managing Files
* creating directories (```mkdir```)
* viewing/opening files (Mac: open / Windows: <type the file>; OR viewers like less(Mac)/more(Win); OR editors: vi, ted and notepad)
* copying/moving files (Mac: ``cp`` / ``mv`` / Windows: copy con/move)

### Create File Lists
* listing contents of a current directory (Mac: ``ls`` / Windows: ``dir`` ) 
* using operators (hyphen and slash, depending on your system):
  * show all files (a)
  * recursion (-R or /s)
  * details (-l) (Mac only; you won’t need this on windows)
  * NB: these are just a few useful operators, there are many others!
* outputting lists (print to file: “>”)

### General Rules of Thumb
* Know the basic architecture of the file structure environment (some places you’ll expect many directories/folders, others you will expect mostly files)
* Have a general idea of the ways you might use this for basic digital preservation tasks (navigating, listing, describing).
* In performing preservation actions, you typically want everything to be reversible and tested in advance. Reversibility is not a hallmark of the command line (nor should it be assumed in a GUI environment). 
* Don't be afraid of the command line, do be cautious: there are not always built-in safeguards as in the GUI environment. If you delete something from the command line, for example, it will not be moved to the trash before deletion - it will be removed immediately. This is not a cause for alarm, but it is a reminder to make sure you are doing exactly what you want, know how to do it (or ask someone who does), and don't proceed too quickly. 

## Reflection Activity
Can you answer these questions? Open a window that gives you access to the command line:
* What is the name of the directory or folder that you are in?
* How would you move to another directory or folder?
* Can you list the contents of the directory or folder?
* Can you get a basic list and an advanced list (that shows permissions, file size, path, etc)?

* What is the basic command for listing items in a folder or directory? Please give both Mac and Windows commands.
* What are some basic differences between command line on Mac & Windows?
* Use the command line to generate a list of files in a directory that is output to a file. List the command that you would use on your system below (and specify what system you’re using).
* In what sorts of situations do you think that the command line interface would be useful or advantageous over the GUI? Give at least one example.
* Do you feel more comfortable using the command line? Why or why not?


### Credits
See these additional resources for more detailed information:
* B. Lyons, [Introduction to Using the Command Line Interface](https://www.weareavp.com/an-introduction-to-using-the-command-line-interface-to-work-with-files-and-directories/) (2014); versions for both MAC and Windows OS. 
* C. Severance, _Python for Everybody_: tips for [Mac](https://www.py4e.com/software-mac.php), tips for [Windows](https://www.py4e.com/software-win.php).
