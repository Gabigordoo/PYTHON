import json
from typing import Any
from flask import Flask, jsonify
from dataclasses import dataclass
from random import randint
from pathlib import Path

app = Flask(__name__)

@dataclass
class People: 
    weight: float 
    height: float

class Profile(People):
    def __init__(self, weight: float , height: float, age: int, name: str, email: str):
        super().__init__(weight, height)
        self.age: int = int(age)
        self.name: str = str(name.strip())
        self.email: str = str(email.strip())
        self.weight: float = float(weight)
        self.height: float = float(height)


def create_list(peoples: list[dict[str, Any]] ) -> list[dict[str, Any]]:
    def validate_peoples(peoples):
        valid_peoples: list = []
        for people in peoples:
            match people:
                case {"age": age, "name": name} if age >= 18 and len(people["name"]) > 3 :
                    valid_peoples.append(people["name"])
        return valid_peoples
    valid_peoples = validate_peoples(peoples)      
    return [{"age": people["age"] *2, "name": people["name"], "email": people["email"], "height": people["height"], "weight": people["weight"]} for people in peoples if people["name"] in valid_peoples]      

def create_list_peoples() -> list [list[dict[str, Any]]]:
    def open_json() -> list[dict[str, Any]]:
        with open(Path(__file__).parent / "users.json", "r", encoding="utf-8") as f:
            return json.load(f)    
    list_peoples: list[dict] = open_json()
    return create_list([Profile(randint(0,90), user_data["age"], randint(0,100), user_data["name"], user_data["email"]).__dict__ for user_data in list_peoples[0].values()])

@app.route('/users_list', methods=["GET"])
def method_name():
    try:
        return jsonify(create_list_peoples())
    except Exception as e:
        return jsonify("Request error")
    
if __name__ == "__main__":
    app.run(debug=True, port=5600, host="0.0.0.0")    

            