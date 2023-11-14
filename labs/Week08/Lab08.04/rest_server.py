from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path="", static_folder='staticpages')

customers = [
    {"id":1, "firstName":"Joe", "surname":"Bloggs", "creditLimit":1000},
    {"id":2, "firstName":"Jane", "surname":"Doe", "creditLimit":9500},
    {"id":3, "firstName":"Elaine", "surname":"Tynan", "creditLimit":1000000}
]
nextId = 4

@app.route('/')
def index():
    return "Hello"

# Command to run in curl:
# curl http://127.0.0.1:5000/customers
@app.route('/customers')
def getAll():
    return jsonify(customers)

# Find by ID
# Command to create in curl:
# curl http://127.0.0.1:5000/customers/1
@app.route('/customers/<int:id>')
def findById(id):
    foundCustomers = list(filter(lambda t: t["id"]==id, customers))
    #print(foundCustomers)
    if len(foundCustomers) == 0:
        return jsonify({}), 204
    
    return jsonify(foundCustomers[0])

# Create
# Command to run in curl:
# curl -X POST -H  "content-type:application/json"-d "{\"firstName\":\"Some name\", \"surname\":\"Some surname\", \"creditLimit\":9.99}" http://127.0.0.1:5000/customers
@app.route('/customers', methods=['POST'])
def create():
    global nextId

    if not request.json: # if no json request
        abort(400)

    customer = {"id":nextId, "firstName":request.json["firstName"], "surname": request.json["surname"], "creditLimit": request.json["creditLimit"]}
    customers.append(customer)
    nextId += 1
    return jsonify(customer)

# Update by ID
# This will also update this in the array
# Command to update in curl:
#  curl -X PUT -H "content-type:application/json" -d "{\"firstName\":\"New title\", \"creditLimit\":2.34}" http://127.0.0.1:5000/customers/1
@app.route('/customers/<int:id>', methods=['PUT'])
def update(id):
    foundCustomers = list(filter(lambda t: t["id"]==id, customers))
    #print(foundCustomers)
    if len(foundCustomers) == 0:
        return jsonify({}), 404
    currentCustomer = foundCustomers[0]

    if 'firstName' in request.json:
        currentCustomer['firstName'] = request.json['firstName']
    if 'surname' in request.json:
        currentCustomer['surname'] = request.json['surname']
    if 'creditLimit' in request.json:
        currentCustomer['creditLimit'] = request.json['creditLimit']
    
    return jsonify(currentCustomer)

# Delete by ID
# Command to delete in curl:
# curl -X DELETE http://127.0.0.1:5000/customers/1
@app.route('/customers/<int:id>', methods=['DELETE'])
def delete(id):
    foundCustomers = list(filter(lambda t: t["id"]==id, customers))
    #print(foundCustomers)
    if len(foundCustomers) == 0:
        return jsonify({}), 404
    
    customers.remove(foundCustomers[0])

    return jsonify({"done": "True"})

if __name__ == '__main__':
    app.run(debug=True)

# ectivate the virtual environment before runing in curl
# .\venv\Scripts\activate.bat

# Deactivate virtual environment at end:
# .\venv\Scripts\activate.bat