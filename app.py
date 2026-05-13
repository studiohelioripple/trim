from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:password@localhost:5432/mydb"

# # MySQL
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:up5FHoQOtbWjN88_F0r=@localhost:3306/bless"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route("/")
def hello_world():
    # Flask automatically converts dictionaries to JSON
    return {"message": "Hello, World!"}

if __name__ == "__main__":
    print("sigmoid Helen")
    app.run(host="0.0.0.0", debug=True)
