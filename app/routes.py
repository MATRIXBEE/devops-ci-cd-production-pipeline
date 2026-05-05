from flask import Blueprint, jsonify

api = Blueprint("api", __name__)


@api.get("/")
def root():
    return "Service is running", 200


@api.get("/health")
def health():
    return jsonify({"status": "ok"}), 200
