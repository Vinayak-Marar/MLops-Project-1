# from us_visa.logger import logging

# logging.info("This is to test logging file")
#-------------------------------------------------------------------------
# from us_visa.logger import logging
# from us_visa.exception import USvisaException
# import sys


# try:
#     a = 1 + 'Z'
# except Exception as e:
#     logging.info(e)
#     raise USvisaException(e, sys) from e

#----------------------------------------------------------------------------------------
# test DataIngestiion
# from us_visa.entity.artifact_entity import DataIngestionArtifact
# from us_visa.entity.config_entity import DataIngestionConfig
# from us_visa.components.data_ingestion import DataIngestion

# data_ingestion_config = DataIngestionConfig()
# data_ingestion = DataIngestion(data_ingestion_config)
# result = data_ingestion.initiate_data_ingestion()

# print(result)