from flask import Blueprint, request, render_template, jsonify, flash, session
from app.model.user import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from app.model.user import User

# Define a Blueprint instead of using `app.route`
auth_bp = Blueprint("auth", __name__)


def record_exists(model, field, value):
    """
    Check if a record exists in the database for any given model, field, and value.

    :param model: SQLAlchemy model class (e.g., User)
    :param field: Column name as a string (e.g., "email")
    :param value: Value to check (e.g., "test@example.com")
    :return: True if the record exists, False otherwise
    """
    if not hasattr(model, field):  # Ensure the field exists in the model
        raise AttributeError(f"{model.__name__} has no column '{field}'")

    return model.query.filter(getattr(model, field) == value).first() is not None

@auth_bp.route("/lecloudore/api/register", methods=["POST"])
def register():
    email = request.form.get("email").strip().lower()
    first_name = request.form.get("fname").strip()
    last_name = request.form.get("lname").strip()
    password = request.form.get("password")

    # Validate input using static methods
    email = User.email_check(email)
    first_name = User.first_name_check(first_name)
    last_name = User.last_name_check(last_name)

    # Check if user already exists in the database
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"error": "Email already exists"}), 400

    # Hash the password
    hashed_password = generate_password_hash(password)

    # Create the User object (only after all checks pass)
    new_user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password_hash=hashed_password
    )
    
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201

@auth_bp.route("/lecloudore/api/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Query the database for the user
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password_hash, password):
            # Store user ID in session
            session["user_id"] = user.id
            flash("Login successful!", "success")
            return render_template("accueil.html") 
        else:
            flash("Invalid email or password", "danger")

    return render_template("login.html")
