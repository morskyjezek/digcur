# Using OpenRefine

## What is OpenRefine?

OpenRefine is 

> a standalone open source desktop application for data cleanup and transformation to other formats. [Wikipedia](https://en.wikipedia.org/wiki/OpenRefine "cited March 7, 2018")

It has become a widely used tool to cleanup, transform, and modify tabular data in bulk. It's capabilities for batch editing and powerful methods and parsing capabilities make it useful for performing metadata transformations and other data wrangling activities that may be required in a digital library environment.

## Example

Input this python code:

```python
from pymarc import MARCReader

with open('loc-marc-tests/BooksAll.2014.part01.marc8', 'rb') as fh:
  reader = MARCReader(fh)
  count = 1
  for record in reader:
    print(record.title())
    count = count + 1
    if count >= 10:
      break
  print('I counted ',count,' Titles')
```

Revised.

* List item 1
* List item 2
* List item 3

### Resources

* [OpenRefine Tutorial in pdf from UMD CASCI Center](https://casci.umd.edu/wp-content/uploads/2013/12/OpenRefine-tutorial-v1.5.pdf), more videos [here](https://casci.umd.edu/research-resource/data-manipulation-tools/openrefine/)
