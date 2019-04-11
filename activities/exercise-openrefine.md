# Using OpenRefine

## What is OpenRefine?

OpenRefine is

> a standalone open source desktop application for data cleanup
> and transformation to other formats.
> [Wikipedia](https://en.wikipedia.org/wiki/OpenRefine "cited March 7, 2018")

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

Let's bring the data into OpenRefine. For this exercise, you can try two ways to do this.

1. When OpenRefine opens, you will see a sidebar at the left with the options "Create Project," "Open Project," "Import Project," and "Language Settings." *Select* the "Create Project" option. In the nested window, select the option to Get data from ... "This Computer." Click the "Choose Files" button, select the JSON file of 101 kittens, and click "Next >>".

2. You might also try to import the data directly from the API using an HTTP request. To do this, select the "Web Addresses (URLs)" option in the Get data from column. In the input box, enter the following URL: `https://www.loc.gov/photos/?fa=online-format:image&q=kittens&c=101&fo=json` (the one designed in the API activity). When you click "Next >>" you should see the option to select the level of the file that you want OpenRefine to see as the "record" (akin to a row in a spreadsheet). In this case, you want to scan the JSON for the "record" element level. When you mouse over this level, you should see the section corresponding to an item in the catalog is highlighted. When you click, you should see a preview of the first few records that would be created. When this looks correct, click through to open the project.

Now, we are ready to work on the data. For the activities described below, use the "Row" view.

One of the things that makes OpenRefine useful is its capacity to use complex rules and apply them over a large range of values.
In other words, it is a powerful batch editing tool that can help you to get, cleanup, and augment data. You might use it, say, to check metadata for inconsistencies or make changes to many values based on strict rules. We will take a look at the basic tools for filtering, editing, and transforming data.

### Filters and facets
Filters and facets help to display or hide particular subsets of data according to specific criteria. For example, you can use a basic filter to remove rows that have a blank first cell. Click on the arrow to the left of the column name, select `[?]` and click [blank]. Let's "Undo" this action for now, because there is information in the hidden rows that we want.

Facets allow you to get an aggregate view of all the values in a given range, and if desired, to make batch edits on this information. *For example, if we want to take a look at the subject terms,*

### Edit and Transform
*OpenRefine also provides powerful options to edit cells and transform their data in bulk, or batch editing options.*

#### Transform to Titlecase
Let's take a look at a few simple ways to do this. Look for the column titled `_ - contributor - contributor`. You might notice that everything is lowercase. Click on the arrow next to the column title, choose "Edit cells >" then "Common transforms >" and then "To titlecase." Now, most of the words, which were all lowercase before, will appear to be names with an initial capital.

#### Simple Joins & Splits
*Join together subjects with ";" separator.*

#### GREL for more complex operations
*Change ISO date to YYYYMMDD or MM/DD/YYYY*

### Exporting data
*Export to `csv`.*


## Another Example

Let's take a look at how we might use OpenRefine to gather, view, and modify some data about
grants from a funder in the cultural heritage sector. The National Endowment for the
Humanities has put up information about its awarded funds on [data.gov](http://data.gov/),
which can be accessed here. For the purposes of this example, let's take a look at the file with
information about the 1960s at https://catalog.data.gov/dataset/neh-grant-data-1966-1969-flattened. Note: this is a "flattened" version of the data, which does not include nested subfields; multiple values are separated by semi-colon, instead
of being separated into multiple subfields. You should receive the data in XML format. (Even though this is "flattened," the same data is in the file; you could, in fact, probably recreate the nested version using cell splits.)

### Clustering
*Try on programs column.*

## Reflection Activities

1. Practice pulling in data from at least two sources. For example, pull in the XML data from data.gov discussed
above. Also, try pulling JSON information from the loc.gov API, try a search that we haven't done in class. 
1. For the next activities, use the "frog" dataset from the assets folder [here](../assets/FW06166-frogs-track-info-no-location.csv). The data is a CSV file. 
  * Practice splits on the species column (some contain multiple values). What character is used to separate the data? 
  * Practice a text facet on the collector column. What are the names of the collectors? 
  * Practice a join on the dates and times. How would you join these columns together into one "date-time" column? Provide the GREL expression you develop. 

## Resources

* [OpenRefine Tutorial in pdf from UMD CASCI Center](https://casci.umd.edu/wp-content/uploads/2013/12/OpenRefine-tutorial-v1.5.pdf), more videos [here](https://casci.umd.edu/research-resource/data-manipulation-tools/openrefine/)
* [GREL reference](https://github.com/OpenRefine/OpenRefine/wiki/General-Refine-Expression-Language)
* [OpenRefine Recipes](https://github.com/OpenRefine/OpenRefine/wiki/Recipes) (examples for performing common operations, like removing rows, transforming data with GREL examples, etc)
* Sarah Weeks and Elissah Becknell, "Using OpenRefine" ([ALA ALCTS Webinar](http://www.ala.org/alcts/confevents/upcoming/webinar/091813))
* Michael J. Carroll, "Metadata Cleanup Made Easy with OpenRefine," [web resources on PA Digital](https://padigital.org/2017/10/31/metadata-cleanup-made-easy-with-openrefine/) (October 2017)
* Thomas Padilla, "Getting Started with OpenRefine" at http://thomaspadilla.org/dataprep/
* [Library Carpentry OpenRefine tutorial](http://data-lessons.github.io/library-openrefine/)
