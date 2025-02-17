from flask import Blueprint, request, render_template

# Define a Blueprint instead of using `app.route`
main_bp = Blueprint("main", __name__, url_prefix="/lecloudore")

@main_bp.route("/")
def main():
    return render_template("accueil.html")

@main_bp.route("/restauration")
def restauration():
    return render_template("restauration.html")

@main_bp.route("/tenture")
def tenture():
    return render_template("tenture.html")

@main_bp.route("/contact.html")
def contact():
    return render_template("contact.html")
