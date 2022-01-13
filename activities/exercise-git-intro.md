# Introduction to and Using Git

Git is a versioning tool, which has become widely used for distributed code development and maintenance through shared respositories, like GitHub. It has also become increasingly widely used to publish materials, share and contribute to open drafts of educational materials and library projects, and as a home for metadata tools and remediation examples. This document walks through some of the
basics of GitHub. For a more in-depth look, see the resources below.

You are looking at a Git "repo" right now! Repo is short for repository and it refers
to a related group of files, which might be a codebase for software, materials for
a website, or a group of related files (such as this group of files that offer more
information on how to use Git!). Git is the name of the versioning system,
and GitHub is the name of this distributed, public implementation of Git.

## Background

GitHub has also become a common platform in the digital library community,
used for publishing, sharing and development of resources and tools,
project documentation, and a wide variety of library-oriented projects.
There digital library community has stretched this tool far beyond software
development and built on GitHub's possibilities for open sharing and versioning.  
Here are just a few examples:

* The Association of Research Libraries uses a GitHub repository to share, maintain, and distribute course materials and resources for its Digital Scholarship Institute. https://github.com/tech-at-arl/Digital-Scholarship-Institute
* A group of University of California archivists used GitHub as a platform to collaborate, develop, and share guidelines for processing digital collections. https://github.com/uc-borndigital-ckg/uc-guidelines/tree/master/INTRODUCTION
* The Library Carpentry initiative, which provides hands-on trainings for librarians and others to build skills and confidence in using digital tools, from data management to Git to OpenRefine, develops and posts all of its lessons through a Git repository. These are then published to a display URL using Jekyll and GitHub pages. https://github.com/libcce/lc-lesson-materials
* A group of digital librarians working through a Digital Curation Google Group has been maintaining a library of BagIt profiles to encourage metadata standardization and better understand usage of this common library packaging specification. https://github.com/bagit-profiles/bagit-profiles
* Digital archivists at the Yale University Libraries created, maintain, and publish a list of useful command line combinations for archivists through the Community Resource for Archivists and Librarians Scripting, which is published through Jekyll and GitHub pages. https://github.com/dd388/crals
* The Rockefeller Archive Center uses a Git repository to create, version, manage, and publish its digital preservation policy. https://github.com/RockefellerArchiveCenter/digital-preservation-policy
* Many libraries or library projects, use GitHub to manage public metadata profiles and documentation, through the Digital Library Federation’s Metadata Specs Clearinghouse. https://github.com/DLFMetadataAssessment/MetadataSpecsClearinghouse/
* The LOCKSS initiative uses a GitHub pages space to host its documentation and
guidance for using LOCKSS. https://lockss.github.io/

We will work through the basics of using Git, a widely-used version control tool.
Git, particularly in the open, multiple user "GitHub" or other shared Git platforms
(like GitLab), also supports distributed work on a single project as well as collaboration.

A system schematic of the Git concept might look like this:

![Basic Git schematic image showing working area, staging, and .git directory](https://librarycarpentry.org/lc-git/fig/git-staging-area.svg)

## Basic GitHub Usage

GitHub follows the standard Git workflow, which allows for users to received or copy
large groups of code at once. It supports a versioning workflow that tracks "diffs"
or differences, using hash values to track and display changes. Users working
on a group of files can choose to stage and add to the repo locally, and then  upload to
the collective repository using a common workflow. These very basic actions are covered here.

### Copying or "Pulling" a Repo

You can create a Git repo from an existing group of files with `git init` command.
More often for our purposes, however, we want to pull a copy of the repo, then make
changes locally. These changes might be resubmitted as suggestions for improvements
to the original project, or they might be a modified copy that we want to use for
our own projects.

To copy the repo use this generic command pattern:

```
% git clone {% insert GitHub URL here %}
```

A specific example is as follows:

```
% git clone https://github.com/morskyjezek/digcur/
```

If you have a repo stored locally and want to see if there have been updates,
use the pull command:

```
% git pull
```

If you are in the main directory of the repo, you can use this command without
any further arguments. The current directory is assumed.

### Checking Current Status

If you are working in a repo on your local computer, you can check the status of
the repo to see if there are files that are not updated using the "status"
command:

```
% git status
```

This command will tell you if there are new files to add. If you want to check the
remote repo, always also run a `git pull` too.

### Modifying, Adding, and "Pushing" to a Repo

For most of the purposes of this course, you will not need to upload changes.
A more complex flow is required to suggest changes, but if you make changes and
then want to upload them, the basic sequence is to "add" the files to the repo,
"commit" them (update the diff logs), and then to "push" them to the shared repo.

A basic sequence could be as follows:

```
% git add newfile.txt
```

```
% git commit -m 'adding and/or updating newfile.txt'
```

```
% git push
```

Without any further arguments, the push command will assume the current local
folder is the repo, and it will use the information in the `.git` directory
to route the files to the shared repo.

## Conclusion

This exercise walks through the basics of Git and GitHub, then demonstrates the basic
workflow of copying or "pulling" a repo, and updating or "pushing" to a shared repo.
There are many more advanced things you can do with Git, particularly when it comes
to software or code development. If you are interested in exploring further, see the resources below.

**For the purposes of the course,** the main commands to know are:

* `git clone` to copy the repo
* `git pull` to update the repo; note that this command won't overwrite any files you've added or created

## Useful resources

* GitHub cheat sheet: https://education.github.com/git-cheat-sheet-education.pdf
* GitHub Handbook: https://guides.github.com/introduction/git-handbook/
* Aditya Sridhar, [How to become a Git expert](https://medium.freecodecamp.org/how-to-become-a-git-expert-e7c38bf54826) (Free Code Camp); quick and useful overview of the basic text commands for Git
* Aditya Sridhar, [An Introduction to Git](https://medium.freecodecamp.org/what-is-git-and-how-to-use-it-c341b049ae61) (Free Code Camp)
* [Git Intro from Library Carpentry](https://librarycarpentry.github.io/lc-git/)
* [Git tutorial from Atlassian](https://www.atlassian.com/git/tutorials/setting-up-a-repository)
* [Learn Git Branching](https://learngitbranching.js.org/) - visual, interactive, game-ified approach to learn Git
