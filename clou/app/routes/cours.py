from flask import Blueprint, request, render_template

# Define a Blueprint instead of using `app.route`
cours_bp = Blueprint("cours", __name__)

@cours_bp.route("/lecloudore/api/cours")
def cours():
    return render_template("cours/cours.html")
