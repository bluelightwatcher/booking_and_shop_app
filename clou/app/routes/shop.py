from flask import Blueprint, request, render_template

# Define a Blueprint instead of using `app.route`
shop_bp = Blueprint("shop", __name__)

@shop_bp.route("/lecloudore/api/boutique")
def boutique():
    return render_template("boutique.html")
