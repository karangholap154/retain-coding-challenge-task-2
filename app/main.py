from flask import Flask, jsonify
from app.routes import url_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(url_routes)

    # Health check routes
    @app.route('/')
    def health_check():
        return jsonify({
            "status": "healthy",
            "service": "URL Shortener API"
        })

    @app.route('/api/health')
    def api_health():
        return jsonify({
            "status": "ok",
            "message": "URL Shortener API is running"
        })

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
