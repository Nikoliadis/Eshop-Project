from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import db, User
from itsdangerous import URLSafeTimedSerializer
import re, smtplib

main = Blueprint('main', __name__)

from flask import current_app

def get_serializer():
    return URLSafeTimedSerializer(current_app.config['SECRET_KEY'])


def send_verification_email(user_email):
    s = get_serializer()
    token = s.dumps(user_email, salt='email-confirm')
    link = url_for('main.verify_email', token=token, _external=True)
    print(f"📧 Verification link: {link}")


def is_password_valid(password):
    if len(password) < 8:
        return False
    if not re.match(r"^[A-Za-z0-9!@#$%^&*()_+=\-{}\[\]:;\"'<>?/|\\~`]+$", password):
        return False
    if '.' in password or ',' in password:
        return False
    return True

@main.route("/")
def home():
    user = None
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
    return render_template("index.html", user=user)

@main.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        if User.query.filter_by(email=email).first():
            flash("❌ Αυτό το email είναι ήδη καταχωρημένο. Παρακαλώ συνδεθείτε.")
            return redirect(url_for("main.login"))

        if not is_password_valid(password):
            flash("❌ Ο κωδικός πρέπει να έχει τουλάχιστον 8 χαρακτήρες, χωρίς τελείες/κόμματα και μόνο γράμματα ή σύμβολα.")
            return redirect(url_for("main.register"))

        hashed_password = generate_password_hash(password)
        user = User(name=username, email=email, password=hashed_password, is_admin=False, is_verified=False, verification_token='pending')
        db.session.add(user)
        db.session.commit()

        send_verification_email(email)
        flash("✅ Εγγραφή επιτυχής! Παρακαλώ ελέγξτε το email σας για επιβεβαίωση.")
        return redirect(url_for("main.login"))

    return render_template("register.html")


@main.route("/verify/<token>")
def verify_email(token):
    try:
        s = get_serializer()
        email = s.loads(token, salt='email-confirm', max_age=3600)
    except:
        flash("❌ Verification link expired or invalid.")
        return redirect(url_for("main.login"))

    user = User.query.filter_by(email=email).first()
    if user:
        user.is_verified = True
        db.session.commit()
        flash("✅ Email verified. You can now log in.")
    return redirect(url_for("main.login"))

@main.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        
        if not user or not check_password_hash(user.password, password):
            flash("❌ Το email ή ο κωδικός είναι λάθος.", "danger")
            return redirect(url_for("main.login"))
        
        if user and check_password_hash(user.password, password):
            if not user.is_verified:
                flash("Email not verified.")
                return redirect(url_for("main.login"))

            session['user_id'] = user.id
            session['is_admin'] = user.is_admin
            return redirect(url_for("main.home"))
        else:
            flash("Invalid credentials.")
    return render_template("login.html")


@main.route("/logout")
def logout():
    session.pop('user_id', None)
    session.pop('is_admin', None)
    flash("Logged out.")
    return redirect(url_for("main.home"))

@main.route("/admin")
def admin_panel():
    if not session.get('is_admin'):
        flash("Access denied.")
        return redirect(url_for("main.home"))
    return render_template("admin_panel.html") 


@main.route('/account')
def account():
    if 'user_id' not in session:
        flash("You need to log in to access your account.")
        return redirect(url_for('main.login'))
    
    user = User.query.get(session['user_id'])
    return render_template("account.html", user=user)

@main.route('/contact')
def contact():
    return render_template('contact.html')

@main.route('/about')
def about():
    return render_template('about.html')
