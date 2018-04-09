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

To understand how to structure a call to the API, you might think of the URL in two parts: first, an "endpoint" URL, then following question mark, a series of queries that specify values for given variables. For example, you may notice that the query string `kittens` appears following `q=`. Thus, it seems that the server is responding to our search and assigning the search request to a variable `q`. So you might think of the URL as a request containing a few variables, represented here with the following variables on new lines to draw attention to them:

```http
https://www.loc.gov/search/
?in=
&q=kittens
&new=true
&st=
```

We might, therefore, think of this as a series of variable assignments encoded in the URL. Notice that some of the variables are blank. In this case, these are optional variables and they need not be included in every request. The most important thing to note is the `q` variable, since it contains the most critical information: our desired query. This pattern of using a URL to pass in variables with an HTTP request is quite common, and although in many cases where you see this it is up to you to guess or infer what each variable is and what it might do, a well-maintained API should offer some explanation of what you can ask for. In this case, the Library of Congress makes information about URL requests available through short documentation at
https://libraryofcongress.github.io/data-exploration/index.html. The documentation tells us that although the default form of requests is HTML, resopnses can also be requested in JSON using the `fo` variable. Thus, if we wanted to get the a list of the items related to "kittens" in Library's catalog in a structured data form, we could make a request as follows:

```http
https://www.loc.gov/search?q=kittens&fo=json
```

As you become more familiar with the URL request formats, you can continue to add variables to better focus requests. For example, if you wanted to find only items that digitized photographs, you can add in multiple `fa` parameters; the number of results per set, likewise, can be changed using the `c` variable. More complex requests might be constructed as follows:

```http
https://www.loc.gov/search?q=kittens&fo=json&fa=online-format:image|original-format:photo,+print,+drawing&c=101
```

Appending the `/{format}/?` subdirectory to the original endpoint, you can simplify the query as follows:

```http
https://www.loc.gov/photos/?fa=online-format:image&q=kittens&c=101&fo=json
```

If you save the response as a file, you can open it in a text editor or browser to view the JSON structure. You may note that it contains much more information than just the results: it has data that is used to construct the page, such as the breadcrumb, the pagination of each page, and the list of search facets.

## Automating the Data Retrieval with Python  

Let's write a program that will query the API endpoint and write the results into a JSON file and/or CSV. 

### Credits and Resources

* See [these slides](https://osf.io/csbrz/) from [@Liblaura](https://twitter.com/liblaura).
* See [this tutorial](https://programminghistorian.org/lessons/downloading-multiple-records-using-query-strings) on constructing and parsing multiple URLs with Python.
