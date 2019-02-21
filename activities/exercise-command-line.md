# Basics of the Command Line Interface

Demonstrations during class assume use of Mac OS/Unix style terminal commands. However, commands for both unix and windows environments are offered below. See the linked resources at the bottom for greater detail.

## Description

This activity aims to present basic skills for using the "[command line](https://en.wikipedia.org/wiki/Command-line_interface)" on Mac and Windows operating systems. A competent digital preservationist should have a basic level of comfort and competence with this interface for a few reasons: primarily because some tools require operation from the command line, but also because it can be a quick and efficient way to perform some actions, such as generating basic information about files and systems.

Keep in mind the difference between the command line and the visual interfaces that may seem more comfortable. We’re mostly used to interacting with computers via a GUI (sounds like “gooey”); that is, a Graphical User Interface that allows you to interact with the system visually, through clicking, dragging and dropping, pointing and tapping, etc. In some cases, such as word processors, we call this WYSIWYG (“what you see is what you get”), when what you see on the screen is comparable to what you would expect to see when the file is printed out on a page. In the command line interface (CLI), as when we are looking at markup files in a text editor, you can see what you do to get what you want. In some ways, it is a more transparent way to get a desired result because you have greater knowledge of what you have asked the computer to do, as well as what the computer is doing.

_Note: where you see “Mac” below, this generally designates a UNIX-wide command, “Windows” is generally DOS-like._

## General Actions
As of 2019, this tutorial is being adapted to working in a UNIX environment using the bash shell.
Bash commands have a typical syntax structure, which can be summarized like this:

```
command options arguments
```

The **command** is the short bit of text that you use to invoke a program, such as `ls`,
`mkdir`, or `find`. The **options** are additional flags that give the program more
information about what you want it to do (e.g. `ls -a` or `mkdir -v`),
or allow you provide additional information (e.g., `find -type f`). Finally, **arguments**
are where you provide the program with information and input, often a file or file path. For example,
`ls` requires the filepath of the location in which you want the files listed.

There are many commands, some of which are covered below. It can be confusing at first
to remember all of the different commands, but don't worry - you're not alone, and
there are a lot of options to find out more information. One easy way to get more
details within the shell is to use `man` (short for manual), which will bring up
documentation for the command, which you have provided as an argument. For example,
`man find` tells you all about the ways you can use `find`.

Another useful, and user-friendly, resource for searching for commands is [Explain Shell](https://explainshell.com/). A resource geared specifically toward archivists and librarians is the [_Script Ahoy_](https://dd388.github.io/crals/) resource.

### Navigation
* determining where you are (Unix: `pwd` / DOS: `cd`)
* moving within the directory structure (`cd`)
* moving files (`mv`)

### Managing Files
* creating directories (`mkdir`)
* viewing/opening files (Unix: open / DOS: <type the file>; OR viewers like less(Unix)/more(Win); OR editors: vi, nano, ted and notepad)
* copying/moving files (Mac: `cp` / `mv` / Windows: copy con/move)

### Create File Lists
* listing contents of a current directory (Mac: `ls` / Windows: `dir` )
* using operators (hyphen and slash, depending on your system):
  * show all files (a)
  * recursion (-R or /s)
  * details (-l) (Mac only; you won’t need this on windows)
  * NB: these are just a few useful operators, there are many others!
* So, a basic UNIX command that lists file details and the hidden files is `ls -la`.
* You can further define a specific path if you want the command to list files in another directory: `la -la /{MY Directory}/{MY subdirectory}`
* outputting lists (print to file: `>`)

### Finding files
The `find` command is a useful way to find files. The syntax is somewhat more complicated than
other commands, but it can be a powerful way to get an overview of items in a particular drive or directory.
One of the things tha makes `find` useful is that you can give it very detailed instructions about where to
look and what to look for. The syntax for `find` is as follows:

* `find` + `{location you want to search}` + `{options that you want to search for, designated by hyphen flags, like -type or -name of object, followed by the arguments for each`

For example:

* `find . -type f -name '*.txt'`

In the above:
* `find` initiates the find program,
* `.` indicates to search the current directory (you could specify
a different path here); note that in this case, the command is _recursive_, which means that
it will search any directories contained in the current path (`.`), but that is another thing you can
control if you investigate the options for this program further,
* `-type f` defines what type of object to look for, in this case `f` designates files
(you can also use `d` for directories or find other options here using the `man` page)
* `-name '*.txt'` limits the results to anything that has a string ending with the text `.txt`
in the name of the object.

In the reflection activity, you are asked to describe what the output of this command would be.

### Other commands of interest
* `df` gives information about the file system usage
* `md5` creates an md5 checksum value
* `hexdump` gives a hex view of the file, useful for searching for magic numbers
* `vi` is an editor but it can be used to open up binary files for inspection

### General Rules of Thumb
* Know the basic architecture of the file structure environment (some places you’ll expect many directories/folders, others you will expect mostly files)
* Have a general idea of the ways you might use this for basic digital preservation tasks (navigating, listing, describing).
* In performing preservation actions, you typically want everything to be reversible and tested in advance. Reversibility is not a hallmark of the command line (nor should it be assumed in a GUI environment).
* Don't be afraid of the command line, do be cautious: there are not always built-in safeguards as in the GUI environment. If you delete something from the command line, for example, it will not be moved to the trash before deletion - it will be removed immediately. This is not a cause for alarm, but it is a reminder to make sure you are doing exactly what you want, know how to do it (or ask someone who does), and don't proceed too quickly.

## Reflection Activity
Can you answer these questions?
* Imagine that you have opened a window that gives access to the command line. What is the path of the directory or folder that you are in? What command would you use to answer this question?
* What command would you use to move to another directory or folder?
* Can you list the contents of the directory or folder?
  * Can you get a basic list and an advanced list (that shows permissions, file size, path, etc)?
* What are the `.` and `..` directories?
* Use the command line to generate a list of files in a directory that is output to a file. List the command that you would use on your system in your answer (and specify what system you’re using).
* Above and in class we used the `find` command. Look at the find command `find . -type f -name '*.txt'` (described above). What would you expect the output of this command to be? Use your knowledge from our discussion, or test this in the shell to see what happens.
* In what sorts of situations do you think that the command line interface would be useful or advantageous over the GUI? Give at least one example.
* Do you feel more comfortable using the command line? Why or why not?


### Credits and Additional Resources
See these additional resources for more detailed information:

* B. Lyons, [Introduction to Using the Command Line Interface](https://www.weareavp.com/an-introduction-to-using-the-command-line-interface-to-work-with-files-and-directories/) (2014); versions for both MAC and Windows OS.
* C. Severance, _Python for Everybody_: tips for [Mac](https://www.py4e.com/software-mac.php), tips for [Windows](https://www.py4e.com/software-win.php).
* [Copy, Create, Rename and Remove Unix Directories](http://documentation.its.umich.edu/node/295)
* Wikipedia, [Find (Unix)](https://en.wikipedia.org/wiki/Find_(Unix))
