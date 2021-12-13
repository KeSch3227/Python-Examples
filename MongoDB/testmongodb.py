from pymongo import MongoClient
from loguru import  logger 

client = MongoClient("mongodb://localhost:27017")
db=client.admin
serverStatusResult=db.command("serverStatus")
logger.debug(serverStatusResult)