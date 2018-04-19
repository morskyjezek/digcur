# Packaging Data (SIP Preparation)

## What is packaging?

OAIS describes packaging information as

> that information which, either actually or logically, binds,
identifies and relates the Content Information and PDI. (2-7)

Whereas descriptive information provides useful tags or text for discovering digital information,
the packaging information structures the information used for preservation (such as
fixity checksums, unique identifiers, provenance, etc) and the "content" (the digital bitstream
or content intended for preservation).

To bring information into a digital preservation environment that follows the general
models and functions outlined by the OAIS, the information needs to be formed into a
submission information package (SIP). If this information is large-scale and an archive
hopes to manage it, then consistently structured incoming information makes it more likely
that a system of rules can be used to manage the archival storage consistently and
reliably. For example, the University of North Texas defines their information packages according to
this [prospectus](https://www.library.unt.edu/sites/default/files/documents/digital-libraries-uploads/Appendix_M_UNT_Libraries_OAIS_Information_Package_Specification.pdf). Examples of the information assets that make up
information packages that are ingested and stored for the National Digital Newspaper Program,
which provides the data for the historic newspaper database [Chronicling America](https://chroniclingamerica.loc.gov/), are [described here](http://www.loc.gov/ndnp/guidelines/examples.html).
Some disciplines develop their own tools or standard protocols, and other digital repositories
use tools to prepare information, such as Bagger and Data Accessioner.

## Setup

You will need to install Bagger, a Java application that supports the creation of digital packages that conform to the BagIt specification.
You can find the current version of Bagger at https://github.com/LibraryOfCongress/bagger/releases.

## Bagger

Some digital preservation organizations use the BagIt library to package data for
transmission between entities and for preparation to place information into long-term
storage.

### Description

Bagger is a packaging tool used by many digital libraries to assemble, document,
transfer, and verify digital content. The Bagger program puts selected content
into a "bag" that conforms to the [BagIt specification](https://tools.ietf.org/html/draft-kunze-bagit-14),
which contains a basic description (bag-info.txt), a checksum manifest,
and data payload. The general concept is that the package is "self describing" (the description
acts like a "tag" on a physical bag naming the contents) and verifiable (using the
checksum manifest).

This format has been adopted in many settings. Various digital libraries, including the
[California Digital Library](https://www.cdlib.org/cdlinfo/2008/07/02/bagit-transferring-digital-content/),
[Digital Preservation Network](https://docs.google.com/document/d/1JqKMFn9KfeIMAAEdOGQr6LZPqNWx8Qubi12uoUXi2QU/edit),
and others, have adopted the specification as a generalized format
for submission and transfer of information (a SIP). Moreover, various tools, like
[Exactly](https://www.weareavp.com/products/exactly/) have been developed that use the BagIt standard.

### Assembling files

Put information into a structure that lets you store it in a coherent way. For example,
it may be sufficient to have all files in one folder. Perhaps you have a series of images in both
high-resolution preservation files and lower-resolution access derivatives.
Other cases may suggest a hierarchical structure of folders. For example,
you may want a series of folders and subfolders that correspond to the chapters of a
book or other smaller semantic units; or perhaps large groupings demand deeper and
more nested hierarchies (eg, a [pairtree](https://confluence.ucop.edu/display/Curation/PairTree) structure).

Once you have the files organized as you wish to store them, you are ready to use
Bagger to generate the baginfo.txt file and requisite data integrity checksums.
You will use the

### Create a Bagger Profile

Bagger uses a JSON file to configure the information that


### Resources
See these additional resources for more detailed information:
* M. Phillips, ["What do we put in our BagIt bag-info.txt files?"](https://vphill.com/journal/post/4142/) (2015).
