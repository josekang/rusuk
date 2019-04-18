from flask import Flask, render_template, jsonify, request 

app = Flask(__name__)

stores = [
	{
		"name" : "KULIKO TECH INDUSTRIES",
		"items" : [
			{
				"name" : "website",
				"price" : 450000
			}
		]
	},
	{
		"name" : "BLESSED INDUSTRIES",
		"items" : [
			{
				"name" : "Bible Studies",
				"price" : 0.0
			}
		]
	}
]

##home page
@app.route("/")
def home():
	return render_template ("index.html")

##here we are getting all the stores
@app.route("/store", methods = ["GET"])
def get_all_stores():
	return jsonify({"stores" : stores})

##here we are creating a new store and appending it to the existing new stores
@app.route("/store", methods = ["POST"])
def create_store():
	request_data = request.get_json()
	new_store = {
		"name" : request_data["name"],
		"items" : []
	}
	stores.append(new_store)
	return jsonify({"new_store" : new_store})

##here we are getting a store with the specified name
@app.route("/store/<string:name>", methods = ["GET"])
def get_specific_store(name):
	for store in stores:
		if store["name"] == name:
			return jsonify({"store" : store})
	return jsonify({"message : store not found"})

##here we are craeting a new item in the store with the specified name
@app.route("/store/<string:name>/item", methods = ["POST"])
def create_item_in_store(name):
	request_data = request.get_json()
	for store in stores:
		if store["name"] == name:
			new_item = {
				"name" : request_data["name"],
				"price" : request_data["price"]
			}
			store["items"].append(new_item)
			return jsonify({"new_item" : new_item})
	return jsonify({"message : store not found"})

##here we are getting all the items in a specific store
@app.route("/store/<string:name>/item", methods = ["GET"])
def get_item_in_store(name):
	for store in stores:
		if store["name"] == name:
			return jsonify({"items" : store["items"]})
	return jsonify({"message: store not found"})


app.run(port= 5000)