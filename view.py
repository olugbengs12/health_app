from pymongo import MongoClient
 
# Connect to MongoDB
mongo_uri = 'mongodb+srv://hafisayeni:40hyUfg8n6bod5pT@healthcare.yeweczc.mongodb.net/?retryWrites=true&w=majority&appName=healthcare'
client = MongoClient(mongo_uri)
db = client.survey_db
collection = db.users
 
# Retrieve all documents
users = collection.find()
 
# Print the documents
for user in users:
    print(user)