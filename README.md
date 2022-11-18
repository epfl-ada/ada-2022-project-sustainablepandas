# Global to local trends in favorite beer styles: a spatial and temporal analysis linking production and consumption

Github files:
- project_beer_reviews.ipynb: main notebook for the project
- GoogleAPI.ipynb: notebook containing the google API requests to get breweries latitudes and longitudes

## Abstract

Beer is one of the most popular beverages and is consumed worldwide. With this in mind, we are interested to analyze and depict the type of beer consumption across the world, that is, which kind of beers are consumed and preferred in which country. Being provided with the dataset of the beer reviews website Ratebeer, we have access to a huge amount of data about beer ratings from users from everywhere in the world. The goal of the project is to create some interactive spatiotemporal map showing the trends of production and consumption of each country, starting from the earliest reviews available until 2017. It will help us to determine the preference and trend in beer consumption for the analyzed period of time, and we will try to explain the reasons behind it by identifying the main features that people like in beers. Google maps API will be used to localize more precisely the breweries in their respective countries.



## Research questions

1) Which are the most popular beer styles produced and consumed by each country over time? 

2) Are there some trends that can be observed depending on time periods and/or countries? Are these global trends the same as more local trends (inside a country or specific regions)?

3) Why are these beer styles more popular? What are the features that make them more popular?

## Proposed additional datasets

- Google Maps API will give us additional information about breweries locations: latitude and longitude
- Geopandas, which will provide spatial data for the maps production.
- Maps delimitation of Switzerland or other required country by district.
- [Brewer’s Friend Beer recipe](https://www.kaggle.com/datasets/jtrofe/beer-recipes?resource=download) dataframe, which holds the different properties of each style of beer to perform a clustering of beerstyles into wider categories.



## Methods

### Google API

Using google API, we can retrieve the location of the breweries. We already used a simple query to find all of the breweries locations and some mistakes were found. So we still need to find an optimized google API query to minimize the errors while retrieving most of the locations. We will use different queries and try to find which of the queries yield the best results. One idea would be to aggregate the different queries and compare them to find errors and discard the outliers, with a clustering algorithm for example. Eventually, we will show the perfomance of the queries on a ROC curve. We plotted our first API requests below: the second image shows a better query request for retrieving brewery locations in Switzerland than the one on the left.
<p align="center">
  <img src="Images/BadQuery_Swi.PNG" width="405" title="Bad Query">
  <img src="Images/BetterQuery_Swi.PNG" width="380" title="Better Query">
</p>

### Beers clustering into categories

We want to separate our beerstyles into wider categories, to get more distinguishable trends and sharper maps . Brewer’s Friend Beer recipe dataframe will help us to divide the beerstyle into different clusters by providing information about the properties specific to each style of beer.

### Global scale analysis

Google maps API will provide the latitude and longitude of the breweries, with which we will be able to produce different visualization maps with the Geopandas library. The maps that interest us are the following, viewed on a world map:

- Plot a map with breweries density
- Clustering breweries based on their main produced beer style, preferred beer styles
- Style liking evolution per country with evolution over time. Proposed time interval of either 6 months or one year, to be determined exactly
- Map showing the best breweries based on the user rating, changing over time

Here is an example of an interactive map for the favorite beer style per country in Europa until 2017
<p align="center">
  <img src="Images/interactive_Beer_styles.png" width="600" title="Interactive Beer Map">
</p>

### Local scale analysis

Then, maps based on smaller scale regions, such as Switzerland, will be produced to perform more detailed analysis. 
Comparison between two different territories, such as USA and Europa, which probably have different beer consumption habits, can also be processed.


### Features and trends analysis 

The main objective now would be to explain the observed consumption trends. Why are these styles of beer more appreciated globally? We will try to find explanations by performing some algorithms, such as linear regression, to identify the features between palate, taste, aroma, abv or appearance that make a beer more appreciated. Some results of the global and local trends will also be further investigated with graphics.

We will also make a comparison between the production and appreciation of a style of beer in a given country. Importation vs local production: which one receives the best ratings? 


## Proposed timeline

**For the beginning of milestone III (02.12.22):**

- Having the final data provided by google API, with the least amount of errors
- Correcting and adjusting country dataframe

**For the 09.12.22:**

- Clustering the beers into categories
- Final check for data integrity and correctness
- Having created most of the maps
- Choosing a platform to host the story and getting a good grasp on it

**For the 16.12.22:**

- Having all the maps finished
- Having made good progress with the analysis part 

**For the 23.12.22:**
- Finishing the last analyzes and conclude the story.


## Organization within the team

- Noé: Google API, mapping with the retrieved data, analysis part
- Bastien: Mapping beer style and countries, analysis part
- Nicolas: Analysis part
- Baptiste: Google API, beer clustering, analysis part



## Questions for TAs
 
We noted that the API returned quite a few mistakes, as sometiems, it localized breweries far away from their originate location. To correct that, we added the name of the country to the query. However, some breweries in the original csv file have some strange characters. For example: BÃ¤der SÃ¶rfÅ‘zde Ã©s SÃ¶rÃ¶zÅ‘ is a name of a brewery. is there a way to translate those characters to normal characters ? Otherwise we will probably have to discard the breweries with those characters, which would results in a lot of lost data.

