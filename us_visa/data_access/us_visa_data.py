from us_visa.configuration.mongo_db_connnection import MongoDBClient
from us_visa.constants import DATABASE_NAME
from us_visa.exception import USvisaException
import pandas as pd
import sys
from typing import Optional
import numpy as np



class USvisaData:
    """
    This class help to export entire mongo db record as pandas dataframe
    """

    def __init__(self):
        try:
            self.mongo_client=MongoDBClient(database_name=DATABASE_NAME)

        except Exception as e:
            raise USvisaException(e, sys)

    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]


            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.tolist():
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"na": np.nan}, inplace=True)

            return df
        
        except Exception as e:
            raise USvisaException(e, sys)
        
if __name__ == "__main__":
    visa_data = USvisaData()
    loop = visa_data.export_collection_as_dataframe("visa_data")

    loop.to_csv("data_from_mongo.csv")