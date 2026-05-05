import logging
from flask import Flask

from app.routes import api


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    configure_logging(app)
    app.register_blueprint(api)

    app.logger.info("Flask application initialized")
    return app


def configure_logging(app: Flask) -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    )
    app.logger.setLevel(logging.INFO)
