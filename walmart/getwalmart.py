import boto3
import pandas as pd

class Walmart:
    
    def __init__(self, bucket = 'jmah-public-data'):
        self.bucket = bucket
        self.s3 = boto3.resource('s3')
        
    def get_all_filenames(self, prefix = 'walmart/'):
    
        prefix_objs = self.s3.Bucket(self.bucket).objects.filter(Prefix=prefix)
        for obj in prefix_objs:
            print(obj.key.split('/')[1])
            
    def get_csv(self, key):

        assert isinstance(key, (str)), 'Key must be a string datatype'
        
        key_name = 'walmart/' + key
        
        df = pd.read_csv(self.s3.Object(bucket_name = self.bucket, key = key_name).get()['Body'])
        
        return df 

