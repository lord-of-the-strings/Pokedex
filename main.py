import requests
from flask import Flask, render_template, request
app=Flask(__name__)
base_url="https://pokeapi.co/api/v2"
@app.route('/')
def home():
    pokemon=None
    name = request.args.get('pokemon_name', '').lower().strip()
    if name:
        response = requests.get(f"{base_url}/pokemon/{name}")
        if response.status_code == 200:
            pokemon = response.json()
    return render_template("index.html", pokemon=pokemon)
if __name__ == "__main__":
    app.run(debug=False)