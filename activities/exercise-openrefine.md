# Using OpenRefine

## What is OpenRefine?

OpenRefine is

> a standalone open source desktop application for data cleanup and transformation to other formats. [Wikipedia](https://en.wikipedia.org/wiki/OpenRefine "cited March 7, 2018")

It has become a widely used tool to cleanup, transform, and modify tabular (and other types of) data in bulk. Its capabilities for batch editing and powerful methods and parsing capabilities make it useful for performing metadata transformations and other data wrangling activities that may be undertaken by digital stewards in a digital library environment.

## Basic Operations

### Import data

### Filters and facets

### Editing and Transformations:

#### Simple Split & Join cells

#### GREL for more complex operations

#### Clustering

### Exporting data



## Example

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
