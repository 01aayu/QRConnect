from pymongo import MongoClient

# MongoDB connection
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['mentor-mentee']

# MongoDB collections
# students_collection = db['students']
mentors_collection = db['mentors']
assigned_mentees_collection = db['assigned_mentees']
mentees_collection = db['mentees']
mentees_grades_collection = db['mentees_grades']
resources_collection = db['resources']

