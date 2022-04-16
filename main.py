from flask import Flask, jsonify
import json

app = Flask(__name__)

# employees = [
#     {'first_name': 'Savan',
#      'last_name': 'Disawal',
#      'emp_id': 0},
#     {'first_name': 'Vijay',
#      'last_name': 'Thakur',
#      'emp_id': 1},
#     {'first_name': 'Ajay',
#      'last_name': 'Shah',
#      'emp_id': 2},
# ]

roles = [
    {"role_name": "Admin",
     "role_id": 0},
    {"role_name": "Manager",
     "role_id": 1}
]

# Load external test data from json file
f = open('testdata/employee.json')
emp = json.load(f)


# print(employees)

# root url
@app.route('/')
def index():
    return "RESTful Assignment"


# Display all eployees on web page in JSON format URL: http://127.0.0.1:5000/employees
@app.route('/employees', methods=['GET'])
def getEmployee():
    return jsonify({'employee': emp})


# -----------------------------------------------------------------------------------------------
# Display EMployee by providing emp_id in url e.g., http://127.0.0.1:5000/employee/2
# @app.route('/employees/<int:emp_id>', methods=['GET'])
# def get_employee_id(emp_id):
#     return jsonify({'employee': emp[emp_id]})

# -----------------------------------------------------------------------------------------------

# Create new Employee record on execution curl command and ca be refreshed on web page :
# Curl command: "curl -i -H "Content-Type: Application/json" -X POST http://localhost:5000/employees"
@app.route('/employees', methods=['POST'])
def createEmployee():
    employee = {"first_name": "Narayan",
                "last_name": "Sankara",
                "emp_id": 3}
    emp.append(employee)
    return jsonify({'Created': employee})


# ------------------------------------------------------------------------------------------------
# Bulk Update same role for all records in JSON
# curl -i -H "Content-Type: Application/json" -X POST http://localhost:5000/employees/rolebased
@app.route('/employees/rolebased', methods=['GET','POST'])
def bulkAssociation():
    for s in emp[:]:
        print(s)
        # if s['emp_id'] == id:
        s['role_name'] = 'Manager'
    return jsonify({'Associated': emp})
# -------------------------------------------------------------------------------------------------

# passing User-Role JSON Scenario #5
# mention emp_id in URL, it will update respective role e.g., http://127.0.0.1:5000/employees/2
@app.route('/employees/<int:emp_id>', methods=['GET', 'PUT'])
def association(emp_id):
    emp_role = {
        0: "Manager",
        1: "Admin",
        2: "Finance"
    }
    try:
        for s in emp[:]:
            # print(s)

            if s['emp_id'] == emp_id:
                r = emp_role[emp_id]
                s['role_name'] = r
    except:
        print('Employee ID Not Found')
    return jsonify({'Associated': emp})


# Display all roles on web page in JSON format URL: http://127.0.0.1:5000/roles
@app.route('/roles', methods=['GET'])
def getRoles():
    return jsonify(({'Roles': roles}))


# Display Role by providing ole_id in url e.g., http://127.0.0.1:5000/roles/1
@app.route('/roles/<int:role_id>', methods=['GET'])
def get_role_id(role_id):
    return jsonify({'roles': roles[role_id]})


# Create new roles record on execution curl command and ca be refreshed on web page :
# curl command: "curl -i -H "Content-Type: Application/json" -X POST http://localhost:5000/roles"
@app.route('/roles', methods=['POST'])
def createRole():
    role = {"role_name": "Finance",
            "role_id": 2}
    roles.append(role)
    return jsonify({'Created': role})


if __name__ == "__main__":
    app.run(debug=True)
