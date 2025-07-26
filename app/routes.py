from flask import Blueprint,Flask, render_template, request

main = Blueprint('main', __name__)


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/services")
def services():
    return "<h2>Services Page</h2>"

@app.route("/contact")
def contact():
    return "<h2>Contact Page</h2>"

@app.route("/login", methods=["GET", "POST"])
def login():
    if app.debug:
        print("Login route hit")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # Προσωρινός έλεγχος
        print(f"Username: {username}, Password: {password}")
        return "<h3>Login attempted (check terminal for values)</h3>"

    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        print(f"REGISTER DATA -> Username: {username}, Email: {email}, Password: {password}")
        return "<h3>Registration submitted. Check terminal.</h3>"

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
