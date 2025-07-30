from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from app.models import db, User

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/services")
def services():
    return "<h2>Services Page</h2>"

@main.route("/contact")
def contact():
    return render_template("contact.html")

@main.route("/about")
def about():
    return render_template("about.html")

from werkzeug.security import check_password_hash

@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            print("✅ Login successful:", user.name)
            return f"<h3>Welcome back, {user.name}!</h3>"
        else:
            print("❌ Invalid login attempt")
            return "<h3>Invalid email or password</h3>"

    return render_template("login.html")


    return render_template("login.html")

@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        print(f"REGISTER DATA -> Username: {username}, Email: {email}, Password: {password}")

        hashed_password = generate_password_hash(password)
        new_user = User(name=username, email=email, password=hashed_password)

        try:
            db.session.add(new_user)
            db.session.commit()
            print("✅ User saved to DB.")
        except Exception as e:
            print("❌ DB Error:", e)

        return "<h3>Registration submitted. Check terminal.</h3>"

    return render_template("register.html")
