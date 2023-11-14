from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path="", static_folder='staticpages')

books = [
    {"id":1, "Title":"Title1", "Author":"Author1", "Price":1.11},
    {"id":2, "Title":"Title2", "Author":"Author2", "Price":2.22},
    {"id":3, "Title":"Title3", "Author":"Author3", "Price":3.33}
]
nextId = 4

@app.route('/')
def index():
    return "Hello"

@app.route('/books')
def getAll():
    return jsonify(books)

# Find by ID
@app.route('/books/<int:id>')
def findById(id):
    foundBooks = list(filter(lambda t: t["id"]==id, books))
    #print(foundBooks)
    if len(foundBooks) == 0:
        return jsonify({}), 204
    
    return jsonify(foundBooks[0])

# Create
# Command to create in curl:
# curl -X POST -H  "content-type:application/json"-d "{\"Title\":\"Some title\", \"Author\":\"Some Author\", \"Price\":9.99}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
    global nextId

    if not request.json: # if no json request
        abort(400)

    book = {"id":nextId, "Title":request.json["Title"], "Author": request.json["Author"], "Price": request.json["Price"]}
    books.append(book)
    nextId += 1
    return jsonify(book)

# Update by ID
# This will also update this in the array
# Command to update in curl:
#  curl -X PUT -H "content-type:application/json" -d "{\"Title\":\"New title\", \"Price\":2.34}" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    foundBooks = list(filter(lambda t: t["id"]==id, books))
    #print(foundBooks)
    if len(foundBooks) == 0:
        return jsonify({}), 404
    currentBook = foundBooks[0]
    if 'Title' in request.json:
        currentBook['Title'] = request.json['Title']
    if 'Author' in request.json:
        currentBook['Author'] = request.json['Author']
    if 'Price' in request.json:
        currentBook['Price'] = request.json['Price']
    
    return jsonify(currentBook)

# Delete by ID
# Command to delete in curl:
# curl -X DELETE http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    foundBooks = list(filter(lambda t: t["id"]==id, books))
    #print(foundBooks)
    if len(foundBooks) == 0:
        return jsonify({}), 404
    
    books.remove(foundBooks[0])

    return jsonify({"done": "True"})

if __name__ == '__main__':
    app.run(debug=True)