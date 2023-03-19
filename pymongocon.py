import pymongo
import os


# Provide the mongodb localhost url to connect python to mongodb.
def fun(d):
  client = pymongo.MongoClient(os.environ['pymongo'])

  # Database Name
  dataBase = client["venky"]

  # Collection  Name
  collection = dataBase["jovian website"]

  # Insert above records in the collection
  collection.insert_one(d)


