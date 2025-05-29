from pymongo import MongoClient

# Connect to MongoDB running on localhost at the default port 27017
client = MongoClient("mongodb://localhost:27017/")

# Select your database and collection
db = client['hospital_db']
patient_collection = db['patients']
