import os


class Config:
    APP_NAME = "devops-ci-cd-service"
    ENV = os.getenv("FLASK_ENV", "production")
