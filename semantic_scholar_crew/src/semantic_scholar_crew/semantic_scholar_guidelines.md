# Basics of Semantic Scholar Python Library



### Basics

Basic usage involves initializing the main class, calling one of its methods to retrieve data, and accessing the response attributes. For example, to get a paper by its ID:



from semanticscholar import SemanticScholar

sch = SemanticScholar()

paper = sch.get\_paper('10.1093/mind/lix.236.433')

print(paper.title)



#### Typed responses:

The library offers typed responses. This simplifies data extraction and enhances code readability. For example, to access the title of a paper:



paper = sch.get\_paper('10.1093/mind/lix.236.433')

print(paper.title)

You can also access the API response in its original JSON format as a dictionary. To retrieve the raw JSON data, use the raw\_data attribute of the response object:



paper = sch.get\_paper('10.1093/mind/lix.236.433')

print(paper.raw\_data)

To explore all available fields in the response, use the keys() method:



paper = sch.get\_paper('10.1093/mind/lix.236.433')

print(paper.keys())

See also



Refer to the SemanticScholar Objects section for details on all available response types and their attributes.



#### Asynchronous requests

The library supports both synchronous and asynchronous versions for its methods, allowing you to choose the approach that best suits your workflow.



You can use the asynchronous version with the AsyncSemanticScholar class:



import asyncio

from semanticscholar import AsyncSemanticScholar



def fetch\_paper():

&nbsp;   async def get\_paper():

&nbsp;       sch = AsyncSemanticScholar()

&nbsp;       return await sch.get\_paper('10.1093/mind/lix.236.433')

&nbsp;   return asyncio.run(get\_paper())



paper = fetch\_paper()



#### Authenticated requests:

If you have an API key, you can pass it as an argument to the main class. This will allow you to make authenticated requests.



from semanticscholar import SemanticScholar

sch = SemanticScholar(api\_key='your\_api\_key\_here')



#### Retry mode:

The library provides an automatic retry mechanism to handle rate-limiting responses from the Semantic Scholar API.



By default, the retry mechanism is enabled (retry=True). When enabled, the library will automatically retry requests up to 10 times if it encounters an HTTP 429 status (Too Many Requests). Each retry attempt waits 30 seconds before trying again.



This feature is especially useful for handling temporary rate limits imposed by the Semantic Scholar API, ensuring your requests are eventually processed without manual intervention. If you prefer to manage retries yourself, you can disable this feature as shown below:



from semanticscholar import SemanticScholar

sch = SemanticScholar(retry=False)



#### Response timeout:

You can set the wait time for a response. By default, requests to the API will wait for 30 seconds until a TimeoutException is raised. To change the default value, specify it during the creation of a SemanticScholar instance:



from semanticscholar import SemanticScholar

sch = SemanticScholar(timeout=5)

Alternatively, you can set the timeout property value:



from semanticscholar import SemanticScholar

sch = SemanticScholar()

sch.timeout = 5



### Paper and Author:

#### Paper:

To access paper data:



from semanticscholar import SemanticScholar

sch = SemanticScholar()

paper = sch.get\_paper('10.1093/mind/lix.236.433')

For details on supported ID types, refer to the official API documentation.



##### Autocomplete suggestions:

Use the autocomplete feature to get suggestions for paper queries. For example:



from semanticscholar import SemanticScholar

sch = SemanticScholar()

suggestions = sch.get\_autocomplete('softw')

The response contains a list of suggestions based on the provided partial query. Each suggestion is represented by an Autocomplete object, which provides minimal information about the papers. Note that these are not full Paper objects with all attributes.



#### Author:

To access author data:



from semanticscholar import SemanticScholar

sch = SemanticScholar()

author = sch.get\_author(2262347)



#### Retrieve multiple items at once:

You can fetch up to 1000 distinct papers or authors in one API call. To do that, provide a list of IDs (array of strings).



Get details for multiple papers:



from semanticscholar import SemanticScholar

sch = SemanticScholar()

list\_of\_paper\_ids = \[

&nbsp;   'CorpusId:470667',

&nbsp;   '10.2139/ssrn.2250500',

&nbsp;   '0f40b1f08821e22e859c6050916cec3667778613'

]

results = sch.get\_papers(list\_of\_paper\_ids)

Get details for multiple authors:



from semanticscholar import SemanticScholar

sch = SemanticScholar()

list\_of\_author\_ids = \['3234559', '1726629', '1711844']

results = sch.get\_authors(list\_of\_author\_ids)



#### Search by keyword:

To search for papers by keyword:



from semanticscholar import SemanticScholar

sch = SemanticScholar()

results = sch.search\_paper('Computing Machinery and Intelligence')

Warning



From the official documentation: “Because of the subtleties of finding partial phrase matches in different parts of the document, be cautious about interpreting the total field as a count of documents containing any particular word in the query.”



To search for authors by name:



from semanticscholar import SemanticScholar

sch = SemanticScholar()

results = sch.search\_author('Alan M. Turing')



##### Paper Bulk retrieval:

The bulk retrieval method allows fetching up to 1,000 basic paper records per request and up 10,000,000 papers in total. This useful To retrieve a large number of papers, once search\_paper() by default are limited to 1,000 results in total.



from semanticscholar import SemanticScholar

sch = SemanticScholar()

response = sch.search\_paper(query='deep learning', bulk=True)

The query supports advanced syntax for refined searches. For details about query syntax and additional parameters, refer to the official API documentation.



\# Search for papers containing 'deep' or 'learning'

response = sch.search\_paper(query='deep | learning', bulk=True)

Additionally, the sort parameter allows ordering results when using bulk=True. Use the format <field>:<order>, where: - field: Can be paperId, publicationDate, or citationCount. - order: Can be asc (ascending) or desc (descending).



By default, results are sorted by paperId:asc.



\# Retrieve highly-cited papers first

response = sch.search\_paper(query='deep learning', bulk=True, sort='citationCount:desc')



##### Search papers by title:

Retrieve a single paper whose title best matches the given query.



from semanticscholar import SemanticScholar

sch = SemanticScholar()

paper = sch.search\_paper(query='deep learning', match\_title=True)

Note



The match\_title parameter is not compatible with the bulk parameter.



##### Query parameters for search papers:

year: str

Restrict results to a specific publication year or a given range, following the patterns ‘{year}’ or ‘{start}-{end}’. Also you can omit the start or the end. Examples: ‘2000’, ‘1991-2000’, ‘1991-’, ‘-2000’.



results = sch.search\_paper('turing test', year=2000)

publication\_type: list

Restrict results to a given list of publication types. Check official documentation for a list of available publication types.



results = sch.search\_paper('turing test', publication\_type=\['Journal','Conference'])

open\_access\_pdf: bool

Restrict results to papers with open access PDFs. By default, this parameter is set to False.



results = sch.search\_paper('turing test', open\_access\_pdf=True)

venue: list

Restrict results to a given list of venues.



results = sch.search\_paper('turing test', venue=\['ESEM','ICSE','ICSME'])

fields\_of\_study: list

Restrict results to a given list of fields of study. Check official documentation for a list of available fields.



results = sch.search\_paper('turing test', fields\_of\_study=\['Computer Science','Education'])

publication\_date\_or\_year: str

Restrict results to the given range of publication date in the format <start\_date>:<end\_date>, where dates are in the format YYYY-MM-DD, YYYY-MM, or YYYY.



results = sch.search\_paper('turing test', publication\_date\_or\_year='2020-01-01:2021-12-31')

min\_citation\_count: int

Restrict results to papers with at least the given number of citations.



results = sch.search\_paper('turing test', min\_citation\_count=100)



#### Paginated results:

Methods that return large amounts of data in chunks, such as searching for papers or authors, support pagination. These methods retrieve results up to a defined limit per page (default is 100). To access additional pages, you can fetch them individually or iterate through the entire set of results.



For example, iterating over all results for a paper search:



from semanticscholar import SemanticScholar

sch = SemanticScholar()

results = sch.search\_paper('Computing Machinery and Intelligence')

all\_results = \[item for item in results]

Pagination is handled automatically when iterating, retrieving all available items. However, if only the first batch of results is needed, you can access them directly using the items property of the result object, avoiding extra API calls:



results = sch.search\_paper('Computing Machinery and Intelligence')

first\_page = results.items

To fetch the next page of results, use the next\_page() method. This method appends the next batch of items to the current list, as shown in the example below:



results = sch.search\_paper('Computing Machinery and Intelligence')

results.next\_page()

first\_two\_pages = results.items



### Recommended papers:

To get recommended papers for a given paper:



from semanticscholar import SemanticScholar

sch = SemanticScholar()

results = sch.get\_recommended\_papers('10.2139/ssrn.2250500')

To get recommended papers based on a list of positive and negative paper examples:



from semanticscholar import SemanticScholar

sch = SemanticScholar()

positive\_paper\_ids = \['10.1145/3544585.3544600']

negative\_paper\_ids = \['10.1145/301250.301271']

results = sch.get\_recommended\_papers\_from\_lists(positive\_paper\_ids, negative\_paper\_ids)

You can also omit the list of negative paper IDs; in which case, the API will return recommended papers based on the list of positive paper IDs only. 



# Semantic Scholar Class

class semanticscholar.SemanticScholar.SemanticScholar(timeout: int = 30, api\_key: str | None = None, api\_url: str | None = None, debug: bool = False, retry: bool = True)

Main class to retrieve data from Semantic Scholar Graph API synchronously.



Parameters:

timeout (float) – (optional) an exception is raised if the server has not issued a response for timeout seconds.



api\_key (str) – (optional) private API key.



api\_url (str) – (optional) custom API url.



debug (bool) – (optional) enable debug mode.



retry (bool) – enable retry mode.



get\_author(author\_id: str, fields: list | None = None) → Author

Author lookup



Calls:

GET /graph/v1/author/{author\_id}



Parameters:

author\_id (str) – S2AuthorId.



Returns:

author data



Return type:

semanticscholar.Author.Author



Raises:

ObjectNotFoundException: if Author ID not found.



get\_author\_papers(author\_id: str, fields: list | None = None, limit: int = 100) → PaginatedResults

Get details about a author’s papers



Calls:

POST /graph/v1/paper/{author\_id}/papers



Parameters:

paper\_id (str) –



S2PaperId, CorpusId, DOI, ArXivId, MAG, ACL, PMID, PMCID, or URL from:



semanticscholar.org



arxiv.org



aclweb.org



acm.org



biorxiv.org



fields (list) – (optional) list of the fields to be returned.



limit (int) – (optional) maximum number of results to return (must be <= 1000).



get\_authors(author\_ids: List\[str], fields: list | None = None, return\_not\_found: bool = False) → List\[Author] | Tuple\[List\[Author], List\[str]]

Get details for multiple authors at once



Calls:

POST /graph/v1/author/batch



Parameters:

author\_ids (str) – list of S2AuthorId (must be <= 1000).



Returns:

author data, and optionally list of IDs not found.



Return type:

List of semanticscholar.Author.Author or Tuple \[List of semanticscholar.Author.Author, List of str]



Raises:

BadQueryParametersException: if no author was found.



get\_autocomplete(query: str) → List\[Autocomplete]

Get autocomplete suggestions for a paper query.



Calls:

GET /graph/v1/paper/autocomplete?query={query}



Parameters:

query (str) – query to get autocomplete suggestions for.



Returns:

list of autocomplete suggestions.



Return type:

List of semanticscholar.Autocomplete.Autocomplete



get\_available\_releases() → List\[str]

Gets all available dataset releases.



Calls:

GET /datasets/v1/release/



Returns:

list of available release ids.



Return type:

List of str



get\_dataset\_diffs(dataset\_name: str, start\_release\_id: str, end\_release\_id: str) → DatasetDiff

Get incremental diffs for a dataset between two releases.



Calls:

GET /datasets/v1/diffs/{start\_release\_id}/to/ {end\_release\_id}/{dataset\_name}



Parameters:

dataset\_name (str) – Name of the dataset.



start\_release\_id (str) – ID of the release currently held by the client.



end\_release\_id (str) – ID of the release the client wishes to update to, or ‘latest’ for the most recent release.



Returns:

information containing dataset, start\_release, end\_release, and list of diffs.



Return type:

semanticscholar.DatasetDiff.DatasetDiff



get\_dataset\_download\_links(release\_id: str, dataset\_name: str) → Dataset

Get download links for a specific dataset in a release.



Calls:

GET /datasets/v1/release/{release\_id}/dataset/{dataset\_name}



Parameters:

release\_id (str) – Release identifier (e.g., ‘2023-12-01’).



dataset\_name (str) – Name of the dataset.



Returns:

dataset information including download links.



Return type:

semanticscholar.Dataset.Dataset



get\_paper(paper\_id: str, fields: list | None = None) → Paper

Paper lookup



Calls:

GET /graph/v1/paper/{paper\_id}



Parameters:

paper\_id (str) –



S2PaperId, CorpusId, DOI, ArXivId, MAG, ACL, PMID, PMCID, or URL from:



semanticscholar.org



arxiv.org



aclweb.org



acm.org



biorxiv.org



fields (list) – (optional) list of the fields to be returned.



Returns:

paper data



Return type:

semanticscholar.Paper.Paper



Raises:

ObjectNotFoundException: if Paper ID not found.



get\_paper\_authors(paper\_id: str, fields: list | None = None, limit: int = 100) → PaginatedResults

Get details about a paper’s authors



Calls:

POST /graph/v1/paper/{paper\_id}/authors



Parameters:

paper\_id (str) –



S2PaperId, CorpusId, DOI, ArXivId, MAG, ACL, PMID, PMCID, or URL from:



semanticscholar.org



arxiv.org



aclweb.org



acm.org



biorxiv.org



fields (list) – (optional) list of the fields to be returned.



limit (int) – (optional) maximum number of results to return (must be <= 1000).



get\_paper\_citations(paper\_id: str, fields: list | None = None, limit: int = 100) → PaginatedResults

Get details about a paper’s citations



Calls:

POST /graph/v1/paper/{paper\_id}/citations



Parameters:

paper\_id (str) –



S2PaperId, CorpusId, DOI, ArXivId, MAG, ACL, PMID, PMCID, or URL from:



semanticscholar.org



arxiv.org



aclweb.org



acm.org



biorxiv.org



fields (list) – (optional) list of the fields to be returned.



limit (int) – (optional) maximum number of results to return (must be <= 1000).



get\_paper\_references(paper\_id: str, fields: list | None = None, limit: int = 100) → PaginatedResults

Get details about a paper’s references



Calls:

POST /graph/v1/paper/{paper\_id}/references



Parameters:

paper\_id (str) –



S2PaperId, CorpusId, DOI, ArXivId, MAG, ACL, PMID, PMCID, or URL from:



semanticscholar.org



arxiv.org



aclweb.org



acm.org



biorxiv.org



fields (list) – (optional) list of the fields to be returned.



limit (int) – (optional) maximum number of results to return (must be <= 1000).



get\_papers(paper\_ids: List\[str], fields: list | None = None, return\_not\_found: bool = False) → List\[Paper] | Tuple\[List\[Paper], List\[str]]

Get details for multiple papers at once



Calls:

POST /graph/v1/paper/batch



Parameters:

paper\_ids (str) –



list of IDs (must be <= 500) - S2PaperId, CorpusId, DOI, ArXivId, MAG, ACL, PMID, PMCID, or URL from:



semanticscholar.org



arxiv.org



aclweb.org



acm.org



biorxiv.org



fields (list) – (optional) list of the fields to be returned.



return\_not\_found (bool) – (optional) flag to include not found IDs in the return, except for IDs in URL:<url> format.



Returns:

papers data, and optionally list of IDs not found.



Return type:

List of semanticscholar.Paper.Paper or Tuple \[List of semanticscholar.Paper.Paper, List of str]



Raises:

BadQueryParametersException: if no paper was found.



get\_recommended\_papers(paper\_id: str, fields: list | None = None, limit: int = 100, pool\_from: Literal\['recent', 'all-cs'] = 'recent') → List\[Paper]

Get recommended papers for a single positive example.



Calls:

GET /recommendations/v1/papers/forpaper/{paper\_id}



Parameters:

paper\_id (str) –



S2PaperId, CorpusId, DOI, ArXivId, MAG, ACL, PMID, PMCID, or URL from:



semanticscholar.org



arxiv.org



aclweb.org



acm.org



biorxiv.org



fields (list) – (optional) list of the fields to be returned.



limit (int) – (optional) maximum number of recommendations to return (must be <= 500).



pool\_from (str) – (optional) which pool of papers to recommend from. Must be either “recent” or “all-cs”.



Returns:

list of recommendations.



Return type:

List of semanticscholar.Paper.Paper



get\_recommended\_papers\_from\_lists(positive\_paper\_ids: List\[str], negative\_paper\_ids: List\[str] | None = None, fields: list | None = None, limit: int = 100) → List\[Paper]

Get recommended papers for lists of positive and negative examples.



Calls:

POST /recommendations/v1/papers/



Parameters:

positive\_paper\_ids (list) – list of paper IDs that the returned papers should be related to.



negative\_paper\_ids (list) – (optional) list of paper IDs that the returned papers should not be related to.



fields (list) – (optional) list of the fields to be returned.



limit (int) – (optional) maximum number of recommendations to return (must be <= 500).



Returns:

list of recommendations.



Return type:

List of semanticscholar.Paper.Paper



get\_release(release\_id: str) → Release

Get a specific release.



Calls:

GET /datasets/v1/release/{release\_id}



Parameters:

release\_id (str) – Release identifier (e.g., ‘2023-12-01’).



Returns:

release information including datasets.



Return type:

semanticscholar.Release.Release



search\_author(query: str, fields: list | None = None, limit: int = 100) → PaginatedResults

Search for authors by name



Calls:

GET /graph/v1/author/search



Parameters:

query (str) – plain-text search query string.



fields (list) – (optional) list of the fields to be returned.



limit (int) – (optional) maximum number of results to return (must be <= 1000).



Returns:

query results.



Return type:

semanticscholar.PaginatedResults.PaginatedResults



search\_paper(query: str, year: str | None = None, publication\_types: list | None = None, open\_access\_pdf: bool | None = None, venue: list | None = None, fields\_of\_study: list | None = None, fields: list | None = None, publication\_date\_or\_year: str | None = None, min\_citation\_count: int | None = None, limit: int = 100, bulk: bool = False, sort: str | None = None, match\_title: bool = False) → PaginatedResults | Paper

Search for papers by keyword. Performs a search query based on the S2 search relevance algorithm, or a bulk retrieval of basic paper data without search relevance (if bulk=True). Paper relevance search is the default behavior and returns up to 1,000 results. Bulk retrieval instead returns up to 10,000,000 results (1,000 in each page).



Calls:

GET /graph/v1/paper/search



Calls:

GET /graph/v1/paper/search/bulk



Parameters:

query (str) – plain-text search query string.



year (str) – (optional) restrict results to the given range of publication year.



publication\_type (list) – (optional) restrict results to the given publication type list.



open\_access\_pdf (bool) – (optional) restrict results to papers with public PDFs.



venue (list) – (optional) restrict results to the given venue list.



fields\_of\_study (list) – (optional) restrict results to given field-of-study list, using the s2FieldsOfStudy paper field.



fields (list) – (optional) list of the fields to be returned.



publication\_date\_or\_year (str) – (optional) restrict results to the given range of publication date in the format <start\_date>:<end\_date>, where dates are in the format YYYY-MM-DD, YYYY-MM, or YYYY.



min\_citation\_count (int) – (optional) restrict results to papers with at least the given number of citations.



limit (int) – (optional) maximum number of results to return (must be <= 100).



bulk (bool) – (optional) bulk retrieval of basic paper data without search relevance (ignores the limit parameter if True and returns up to 1,000 results in each page).



sort (str) – (optional) sorts results (only if bulk=True) using <field>:<order> format, where “field” is either paperId, publicationDate, or citationCount, and “order” is asc (ascending) or desc (descending).



match\_title (bool) – (optional) retrieve a single paper whose title best matches the given query.



Returns:

query results.



Return type:

semanticscholar.PaginatedResults.PaginatedResults or semanticscholar.Paper.Paper



property debug: bool

Enable/disable debug mode.



Type:

bool



Deprecated since version 0.8.4: Use Python’s standard logging in DEBUG level instead.



property retry: bool

Enable/disable retry mode.



Type:

bool



property timeout: int

Timeout for server response in seconds.



Type:

int

