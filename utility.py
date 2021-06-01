import os
import json

class Utility:
    def __init__(self, _base_path:str='/content/drive/MyDrive/CSE547_Final_Project/ml-100k'):
        """Init the utility class

        Keyword arguments
        base_path -- The directory where files are located. 
        """

        if not os.path.isdir(_base_path):
            raise OSError(f'{_base_path} is not a directory')
        
        self.base_path = _base_path

        self.training_file = 'ratings_train.csv'
        self.test_file = 'ratings_train.csv'
        self.validation_file = 'ratings_validation.csv'

        self.user_to_idx_file = "user_to_idx.json"
        self.movie_to_idx_file = "movie_to_idx.json"

        self.k_anonymized_postfix = '_anonymized.csv'
        self.k_anonymized_map_postfix = '_anonymized_idx_to_kanon_idx.json'
    
    def get_training_data_path(self, base_path=""):
        """Get path to training file

        Keyword arguments
        base_path -- The directory where files are located. 
        """
        if not base_path:
            base_path = self.base_path
        
        if not os.path.isdir(base_path):
            raise OSError(f'{base_path} is not a directory')
        
        file_path = os.path.join(base_path, self.training_file)
        if not os.path.exists(file_path):
            raise OSError(f'{file_path} is not a directory')
        
        return file_path

    def get_test_data_path(self, base_path=""):
        """Get path to test file

        Keyword arguments
        base_path -- The directory where files are located. 
        """
        if not base_path:
            base_path = self.base_path
        
        if not os.path.isdir(base_path):
            raise OSError(f'{base_path} is not a directory')
        
        file_path = os.path.join(base_path, self.test_file)
        if not os.path.exists(file_path):
            raise OSError(f'{file_path} is not a directory')

        return file_path
    
    def get_validation_data_path(self, base_path=""):
        """Get path to validation file

        Keyword arguments
        base_path -- The directory where files are located. 
        """
        if not base_path:
            base_path = self.base_path
        
        if not os.path.isdir(base_path):
            raise OSError(f'{base_path} is not a directory')
        
        file_path = os.path.join(base_path, self.validation_file)
        if not os.path.exists(file_path):
            raise OSError(f'{file_path} is not a directory')

        return file_path
    
    def get_train_data_user_map_path(self, base_path=""):
        """Get path to user id to train index file map

        Keyword arguments
        base_path -- The directory where files are located. 
        """
        if not base_path:
            base_path = self.base_path
        
        if not os.path.isdir(base_path):
            raise OSError(f'{base_path} is not a directory')
        
        file_path = os.path.join(base_path, self.user_to_idx_file)
        if not os.path.exists(file_path):
            raise OSError(f'{file_path} is not a directory')

        return file_path
    
    def get_train_data_movie_map_path(self, base_path=""):
        """Get path to movie id to train index file map

        Keyword arguments
        base_path -- The directory where files are located. 
        """
        if not base_path:
            base_path = self.base_path
        
        if not os.path.isdir(base_path):
            raise OSError(f'{base_path} is not a directory')
        
        file_path = os.path.join(base_path, self.movie_to_idx_file)
        if not os.path.exists(file_path):
            raise OSError(f'{file_path} is not a directory')

        return file_path

    def get_k_anonymized_data_path(self, k, base_path=""):
        """Get path to k-anonymzied file

        Keyword arguments
        k -- 
        base_path -- The directory where files are located. 
        """
        if not base_path:
            base_path = self.base_path
        
        if not os.path.isdir(base_path):
            raise OSError(f'{base_path} is not a directory')
        
        k_file_name = str(k) + self.k_anonymized_postfix

        file_path = os.path.join(base_path, k_file_name)
        if not os.path.exists(file_path):
            raise OSError(f'{file_path} is not a directory')

        return file_path
    
    def get_k_anonymized_map_path(self, k, base_path=""):
        """Get path to k-anonymzied map. 
        {k}_anonymized_idx_to_kanon_idx.json --> the mapping from user index 
        (row in the ratings_train.csv) to the row index in the 
        corresponding {k}_anonymized.csv file

        Keyword arguments
        k -- 
        base_path -- The directory where files are located. 
        """
        if not base_path:
            base_path = self.base_path
        
        if not os.path.isdir(base_path):
            raise OSError(f'{base_path} is not a directory')
        
        k_file_name = str(k) + self.k_anonymized_map_postfix
        
        file_path = os.path.join(base_path, k_file_name)
        if not os.path.exists(file_path):
            raise OSError(f'{file_path} is not a directory')

        return file_path
    
    def get_closest_k_cluster_to_user_id(self, user_id:int, k:int, base_path=""):
        id_to_idx_path = self.get_train_data_user_map_path(base_path)
        idx_to_kidx_path = self.get_k_anonymized_map_path(k, base_path)

        with open(id_to_idx_path) as json_file:
            id_to_idx_dict = json.load(json_file)
        
        with open(idx_to_kidx_path) as json_file:
            idx_to_kidx_path_dict = json.load(json_file)
        
        user_id = str(user_id)
        
        # Easy case - We have trained on this user before
        # Just need to lookup, to see what cluster they belong to
        if user_id in id_to_idx_dict.keys() and\
           str(id_to_idx_dict[user_id]) in idx_to_kidx_path_dict.keys():            
            return idx_to_kidx_path_dict[str(id_to_idx_dict[user_id])]
        else:
            print(f'{user_id} not found in training data!')

u = Utility()
# print(u.get_training_data_path())
# print(u.get_train_data_user_map_path())
# print(u.get_train_data_movie_map_path())
# print(u.get_test_data_path())
# print(u.get_validation_data_path())
# print(u.get_k_anonymized_data_path(2))
# print(u.get_k_anonymized_map_path(3))

import pandas as pd
df = pd.read_csv(u.get_test_data_path())
# df = pd.read_csv(u.get_validation_data_path())

user_ids = df.userId.unique()
for user_id in user_ids:
    print(u.get_closest_k_cluster_to_user_id(user_id, 2))