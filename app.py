# app.py
from flask import Flask
from flask_restful import Api
from db import db  # Import db from db.py
from resources.employee import EmployeeResource, EmployeeList

app = Flask(__name__)
app.config.from_object('instance.config.Config')

# Initialize the database
db.init_app(app)

api = Api(app)

# Root route
@app.route('/')
def index():
    return "Welcome to the Employee Management API! Visit /api/employees/ to see the available endpoints."

# Registering the resources
api.add_resource(EmployeeList, '/api/employees/')
api.add_resource(EmployeeResource, '/api/employees/<int:id>/')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)
