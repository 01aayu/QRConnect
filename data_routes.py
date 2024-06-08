import os
from flask import Blueprint, jsonify, request
from database import mentors_collection, assigned_mentees_collection, mentees_collection, mentees_grade_collection, resources_collection  # Import your MongoDB collections

data_bp = Blueprint('data', __name__)

@data_bp.route('/data', methods=['GET'])
def get_data():
    table = request.args.get('table')
    env = os.environ.get('FLASK_ENV', 'development')

    if env == 'development':
        if table == 'mentors':
            # Perform MongoDB query for students_collection
            data = list(mentors_collection.find())
        elif table == 'assigned_mentees':
            # Perform MongoDB query for mentors_collection
            data = list(assigned_mentees_collection.find())
        elif table == 'mentees':
            # Perform MongoDB query for mentors_collection
            data = list(mentees_collection.find())
        elif table == 'mentees_grade':
            # Perform MongoDB query for mentors_collection
            data = list(mentees_grade_collection.find())
        elif table == 'resources':
            # Perform MongoDB query for mentors_collection
            data = list(resources_collection.find())
        # Add other collections as needed
        else:
            return jsonify({"error": "Collection not found"}), 404
        
        for item in data:
            item['_id'] = str(item['_id'])  # Convert ObjectId to string

        return jsonify(data)
