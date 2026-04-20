# WebScraper

## Project implementation steps

### Stage 1-3

1. Provide url of the product's opinions page
1. Send request to provided url 
1. Fetch product name 
1. Fetch all opinions from the webpage
1. Parse opinions to extract required data
1. Check if there is a next page with opinions
1. Repeat steps 4-6 for all pages with opinions about product
1. Save acquired opinions

## Project inputs

### Product codes

- https://www.ceneo.pl/135965172#tab=reviews
- https://www.ceneo.pl/183327747#tab=reviews_new
- https://www.ceneo.pl/173381730#tab=reviews
- https://www.ceneo.pl/23398168#tab=reviews
- https://www.ceneo.pl/52624415#tab=reviews

### Opinion structure
|component|name|selector|
|---|---|---|
|opinion ID|opinion_id|[data-entry-id]|
|opinion’s author|author|span.user-post__author-name|
|author’s recommendation|recommendation|span.user-post__author-recomendation|
|score expressed in number of stars|score|span.user-post__score-count|
|opinion’s content|content|div.user-post__text|
|list of product advantages|pros|div.review-feature__item--positive|
|list of product disadvantages|cons|div.review-feature__item--negative|
|how many users think that opinion was helpful|helpful|button.vote-yes > span|
|how many users think that opinion was unhelpful|unhelpful|.vote-no > span|
|publishing date|publish_date|.user-post__published > time:nth-child(1)[datetime]|
|purchase date|purchase_date|.user-post__published time:last-of-type[datetime]|




#### venv environment activate 
``` source venv/Scripts/activate  ```