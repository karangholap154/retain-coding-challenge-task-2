from flask import Blueprint, request, jsonify, redirect
from app.storage import url_store
from app.utils import generate_short_code, validate_url
from datetime import datetime

url_routes = Blueprint("url_routes", __name__)

# Shorten URL
@url_routes.route("/api/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()
    if not data or "url" not in data:
        return jsonify({"error": "URL is required"}), 400

    long_url = data["url"]
    if not validate_url(long_url):
        return jsonify({"error": "Invalid URL"}), 400

    short_code = generate_short_code()
    while short_code in url_store:
        short_code = generate_short_code()

    url_store[short_code] = {
        "url": long_url,
        "clicks": 0,
        "created_at": datetime.utcnow().isoformat()
    }

    short_url = request.host_url + short_code
    return jsonify({"short_code": short_code, "short_url": short_url}), 201

# Redirect to original URL
@url_routes.route("/<short_code>", methods=["GET"])
def redirect_to_url(short_code):
    if short_code not in url_store:
        return jsonify({"error": "Short code not found"}), 404
    url_store[short_code]["clicks"] += 1
    return redirect(url_store[short_code]["url"])

# Get analytics
@url_routes.route("/api/stats/<short_code>", methods=["GET"])
def get_stats(short_code):
    if short_code not in url_store:
        return jsonify({"error": "Short code not found"}), 404
    data = url_store[short_code]
    return jsonify({
        "url": data["url"],
        "clicks": data["clicks"],
        "created_at": data["created_at"]
    }), 200
