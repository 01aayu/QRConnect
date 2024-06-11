import os
from flask import Blueprint, jsonify, request
from database import mentors_collection, assigned_mentees_collection, mentees_collection, mentees_grades_collection, resources_collection, students_collection  # Import your MongoDB collections

data_bp = Blueprint('data', __name__)

@data_bp.route('/data', methods=['GET'])
def get_data():
    table = request.args.get('table')
    env = os.environ.get('FLASK_ENV', 'development')

    if env == 'development':
        if table == 'mentors':
            data = list(mentors_collection.find())
        elif table == 'assigned_mentees':
            data = list(assigned_mentees_collection.find())
        elif table == 'mentees':
            data = list(mentees_collection.find())
        elif table == 'mentee_grades':
            data = list(mentees_grades_collection.find())
        elif table == 'resources':
            data = list(resources_collection.find())
        elif table == 'students':  # Handle students_collection
            data = list(students_collection.find())
        else:
            return jsonify({"error": "Collection not found"}), 404
        
        for item in data:
            item['_id'] = str(item['_id'])  # Convert ObjectId to string

        return jsonify(data)
