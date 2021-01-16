from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from dotenv import load_dotenv
from sqlalchemy.sql.expression import func

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:pwd@localhost/hwa"
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    height = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email = email
        self.height = height


@app.route("/")
def root():
    return render_template("index.html")


@app.route("/sucess", methods=["POST"])
def success():
    if request.method == "POST":
        email, height = request.form.values()

        # check if user already exists
        if db.session.query(Data).filter(Data.email == email).count() == 0:
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            avg = db.session.query(func.avg(Data.height)).scalar()
            avg = round(avg, 1)
            count = db.session.query(Data.height).count()
            send_email(email, height, avg, count)
            return render_template("success.html")

    return render_template("index.html", text="This email already submitted a height!")


@app.route("/average", methods=["GET"])
def average():
    return "stub"


if __name__ == "__main__":
    app.run(debug=True)