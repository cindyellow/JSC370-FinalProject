## Acquiring data

Yelp has specified that the datasets are not to be publicly distributed, hence here I have explained the steps to retrieve its data. 

1. Visit [Yelp's Open Dataset](https://www.yelp.com/dataset) and download the relevant files, which will be in a `.tar` compressed file.

2. Extract the respective json files and converting each to csv using Python (code can be found at `JSONtoCSV.py`). Specifically for the reviews file, we only take reviews from the most recent five years (starting at 2017/01/01) and limit data size. 

