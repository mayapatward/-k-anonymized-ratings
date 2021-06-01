# -k-anonymized-ratings
Final project for CSE 547 - Mining Large Datasets


## Data Schema

In the ml-100k folder:

1. ratings_train.csv --> The training data 
2. ratings_test.csv --> The test data 
3. ratings_validation.csv --> The validation data
4. user_to_idx.json --> Mapping from user id to the user index (row in the ratings_train.csv)
5. {k}_anonymized.csv --> k-anonymized files (without PCA applied)
6. {k}_anonymized_idx_to_kanon_idx.json --> the mapping from user index (row in the ratings_train.csv) to the row index in the corresponding {k}_anonymized.csv file

# Contact
For information about this project contact:

- {} @ uw.edu