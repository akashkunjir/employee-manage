# resources/employee.py
from flask_restful import Resource
from flask import request, jsonify
from models import db, Employee

class EmployeeList(Resource):
    def get(self):
        employees = Employee.query.all()
        employee_list = []
        for employee in employees:
            employee_list.append({
                'id': employee.id,
                'name': employee.name,
                'email': employee.email,
                'department': employee.department,
                'role': employee.role,
                'date_joined': employee.date_joined.isoformat()  # Format datetime
            })
        return jsonify(employee_list)

    def post(self):
        data = request.get_json()
        new_employee = Employee(
            name=data['name'],
            email=data['email'],
            department=data.get('department'),  # Use .get() to avoid KeyError
            role=data.get('role'),
            date_joined=datetime.utcnow()  # Set to current time
        )
        db.session.add(new_employee)
        db.session.commit()
        return jsonify({'message': 'Employee created'}), 201

class EmployeeResource(Resource):
    def get(self, id):
        employee = Employee.query.get_or_404(id)
        return jsonify({
            'id': employee.id,
            'name': employee.name,
            'email': employee.email,
            'department': employee.department,
            'role': employee.role,
            'date_joined': employee.date_joined.isoformat()
        })
    
    def put(self, id):
        employee = Employee.query.get_or_404(id)
        data = request.get_json()
        employee.name = data.get('name', employee.name)
        employee.email = data.get('email', employee.email)
        employee.department = data.get('department', employee.department)
        employee.role = data.get('role', employee.role)
        db.session.commit()
        return jsonify({'message': 'Employee updated'})

    def delete(self, id):
        employee = Employee.query.get_or_404(id)
        db.session.delete(employee)
        db.session.commit()
        return jsonify({'message': 'Employee deleted'})
