# Gathering Data with an API

## What is an API?

An [API](https://en.wikipedia.org/wiki/Application_programming_interface) is an "Application Programming Interface," which is basically a protocol that defines how data may be output, requested, and interchanged between different systems. So for example, if you want to get a bunch of information out of a library catalog, you can follow a set of standard request rules to get that data and pull it into your system or program. If a library provides a publicly available API, it can make its data more open, or help to automate the process of requesting and receiving data.

## Some Examples

Do you, for example, use an app to tell when the next bus will arrive or find out if the Metro is delayed? It's likely that you are using an app that was designed by an organization that has access to the data provided by DC Metro and presents it in a different form or integrates it into a newsfeed. For example, [Is Metro on Fire?](https://ismetroonfire.com/) pulls its data from the WMATA API, [MetroHero](https://dcmetrohero.com/apis).

Increasingly, libraries and archives are using web services like APIs in order to provide access to the data in their catalogs. For example, the National Archives allows users to make requests and receive responses in structured formats. The Library of Congress and OCLC WorldCat also provide API endpoints for users to interact with their catalog data.

* Here is how the National Archives describes and presents its catalog API: https://github.com/usnationalarchives/Catalog-API
* WorldCat, maintained by OCLC provides interactive capabilities for authenticated users: https://www.oclc.org/developer/develop/web-services/worldcat-search-api.en.html (there is also an "explorer" tool for developing queries)
* Documentation for BibIt: https://www.oclc.org/developer/news/2016/bibit-a-simple-cataloging-application.en.html

These examples use a [REST API framework](https://en.wikipedia.org/wiki/Representational_state_transfer), which means that data can be requested in a specified format using an HTTP protocol. Thus, we can construct requests to the API using an HTML GET request. Let's take a closer look at how to form such a request.

## Forming URL Queries

Let's take the Library of Congress web service as an example. You can find their website at https://loc.gov/, and you will notice that if you enter a query in the search box at the top, the base URL will change. If you enter a query for "kittens," for example, you would note that the request generates the following URL:

```http
https://www.loc.gov/search/?in=&q=kittens&new=true&st=
```

* Library of Congress API Documentation: https://libraryofcongress.github.io/data-exploration/index.html


### Credits and Resources

* See [these slides](https://osf.io/csbrz/) from [@Liblaura](https://twitter.com/liblaura).
* See [this tutorial](https://programminghistorian.org/lessons/downloading-multiple-records-using-query-strings) on constructing and parsing multiple URLs with Python.
