import tarfile
import pandas as pd
import numpy as np

# The file at tar.getnames()[3] is the yelp_reviews dataset 
with tarfile.open('yelp_dataset.tar', 'r:gz') as tar:
  csv_path = tar.getnames()[3]
  b_pandas = []
  r_dtypes = {"review_id": np.dtype.str , 
              "user_id": np.dtype.str , 
              "business_id": np.dtype.str,
              "stars": np.int32,
              "date": np.dtype.str
            }
  reader = pd.read_json(tar.extractfile(csv_path), orient="records", encoding = "utf-8", 
                        lines=True, dtype=r_dtypes, chunksize=1000)
          
  for chunk in reader:
    reduced_chunk = chunk.drop(columns=['review_id', 'user_id'])\
                              .query("`date` >= '2017-01-01'")
    b_pandas.append(reduced_chunk)
      
  b_pandas = pd.concat(b_pandas, ignore_index=True)    
  b_pandas.to_csv("Reviews.csv")