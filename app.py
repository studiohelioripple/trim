from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    # Flask automatically converts dictionaries to JSON
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    print("sigmoid")
    app.run(host="0.0.0.0", debug=True)
