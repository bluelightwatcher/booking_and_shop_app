from app.routes.cours import cours_bp
from app.routes.main import main_bp
from app.routes.shop import shop_bp
from app.routes.auth import auth_bp


def registerblueprint(app):
    app.register_blueprint(cours_bp)
    app.register_blueprint(shop_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
