# Using OpenRefine

## What is OpenRefine?

OpenRefine is

> a standalone open source desktop application for data cleanup and transformation to other formats. [Wikipedia](https://en.wikipedia.org/wiki/OpenRefine "cited March 7, 2018")

It has become a widely used tool to cleanup, transform, and modify tabular (and other types of) data in bulk. Its capabilities for batch editing and powerful methods and parsing capabilities make it useful for performing metadata transformations and other data wrangling activities that may be undertaken by digital stewards in a digital library environment.

## Setup

You will need to install OpenRefine, which can be downloaded at http://openrefine.org/download.html. The below information was written using OpenRefine 2.7.

### Installation

When you download the Windows version, you will have a zip, and Mac/Linux will get a dmg. To run, extract (zip) the files in a location where you will run the file from, or open (dmg) and follow instructions. To run the program:

* On Windows: Navigate to the folder where you’ve installed OpenRefine and double-click ’openrefine.exe’ or ‘refine.bat’ (for either)
* On Mac: Navigate to where you installed OpenRefine and click the OpenRefine icon
* On Linux: Navigate to the folder where you’ve installed OpenRefine in a terminal window and type ‘./refine’

The program runs within a web browser. A browser window may automatically open, but if it does not, you can access the program by opening the address http://127.0.0.1:3333 in a browser window.

To follow along the basics below, you can use the JSON data that we gathered in the API exercise [linked here](../assets/loc-101-kittens.json).

## Basic Operations

Let's walk through some of the basic operations that you can undertake with OpenRefine.

### Import data

First, let's import the data. When OpenRefine opens, you will see a sidebar at the left with the options "Create Project," "Open Project," "Import Project," and "Language Settings." *Select* the "Create Project" option. In the nested window, select the option to Get data from ... "This Computer." Click the "Choose Files" button, select the JSON file of 101 kittens, and click "Next >>".

### Filters and facets

### Edit and Transform

#### Simple Split & Join cells

#### GREL for more complex operations

#### Clustering

### Exporting data



## Another Example

Let's take a look at how we might use OpenRefine to gather, view, and modify some data about
grants from a funder in the cultural heritage sector. The National Endowment for the
Humanities has put up information about its awarded funds on [data.gov](http://data.gov/),
which can be accessed here. For the purposes of this example, let's take a look at the file with
information about the 1960s at https://catalog.data.gov/dataset/neh-grant-data-1966-1969-flattened. Note: this is a "flattened" version of the data, which does not include nested subfields; multiple values are separated by semi-colon, instead
of being separated into multiple subfields. You should receive the data in XML format.

### Basic editing: Split and Join

## Resources

* [OpenRefine Tutorial in pdf from UMD CASCI Center](https://casci.umd.edu/wp-content/uploads/2013/12/OpenRefine-tutorial-v1.5.pdf), more videos [here](https://casci.umd.edu/research-resource/data-manipulation-tools/openrefine/)
* [GREL reference](https://github.com/OpenRefine/OpenRefine/wiki/General-Refine-Expression-Language)
* [OpenRefine Recipes](https://github.com/OpenRefine/OpenRefine/wiki/Recipes) (examples for performing common operations, like removing rows, transforming data with GREL examples, etc)
* Thomas Padilla, "Getting Started with OpenRefine" at http://thomaspadilla.org/dataprep/
* [Library Carpentry OpenRefine tutorial](http://data-lessons.github.io/library-openrefine/)
