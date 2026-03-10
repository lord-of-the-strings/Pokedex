import requests
from flask import Flask, render_template
app=Flask(__name__)
base_url="https://pokeapi.co/api/v2/"
@app.route('/')
def home():
    url=f"{base_url}/pokemon/pikachu"
    response = requests.get(url)
    if response.status_code == 200:
        return render_template("index.html",pokemon=response.json())
if __name__ == "__main__":
    app.run(debug=True)