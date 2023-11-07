from application import app, db
from flask import request, jsonify
from application.models import FriendsCharacter

def format_character(character):
    return{
        "id":character.id, 
        "name":character.name, "age":character.age, "catch_phrase":character.catch_phrase
    }
##application folder becomes a module
@app.route("/")
def hello_world():
    return "<P>Hello, World!</p>"

@app.route("/characters", methods=['POST'])
def create_character():
    #retrieve the body - req.body
    data = request.json
    #data -> {name:, age:}

    character = FriendsCharacter(data["name"], data["age"], data["catch_phrase"])
    #add the character
    db.session.add(character)

    ##commit
    db.session.commit()
    ## send back a json response
    #jsonify -> turns JSON output into a repose object
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)

# GET route to retrive all the characters

@app.route("/characters")
def get_characters():
    characters = FriendsCharacter.query.all()
    character_list = []
    for character in characters:
        character_list.append(format_character(character))
    return {'characters': character_list }

@app.route("/characters/<id>")
def get_character(id):
    character = FriendsCharacter.query.filter_by(id=id).first()
    print(character)
    return jsonify(id=character.id, name=character.name, age=character.age, catch_phrase=character.catch_phrase)

@app.route("/characters/<id>", methods=["DELETE"])
def delete_character(id):
    character = FriendsCharacter.query.filter_by(id=id).first()
    db.session.delete(character)
    db.session.commit()
    return "character Deleted"

@app.route("/characters/<id>", methods=["PATCH"])
def update_character(id):
    data = request.json
    character = FriendsCharacter.query.filter_by(id=id)
    character.update(dict(name=data['name'], age=data['age'], catch_phrase=data['catch_phrase']))
    db.session.commit()

    updatedCharacter = FriendsCharacter.query.filter_by(id=id).first()

    return jsonify(id=updatedCharacter.id, name=updatedCharacter.name, age=updatedCharacter.age, catch_phrase=updatedCharacter.catch_phrase)