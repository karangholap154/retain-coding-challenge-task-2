import pytest
from app.main import create_app

# Fixture to create a fresh test client for each test
@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Health check test (already provided)
def test_health_check(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    assert data['service'] == 'URL Shortener API'

# Shorten URL test
def test_shorten_url(client):
    response = client.post("/api/shorten", json={"url": "https://example.com"})
    assert response.status_code == 201
    data = response.get_json()
    assert "short_code" in data
    assert "short_url" in data

# Invalid URL test
def test_invalid_url(client):
    response = client.post("/api/shorten", json={"url": "invalid-url"})
    assert response.status_code == 400

# Redirect and stats test
def test_redirect_and_stats(client):
    # Create short URL
    response = client.post("/api/shorten", json={"url": "https://example.com"})
    short_code = response.get_json()["short_code"]

    # Check stats (clicks = 0)
    response = client.get(f"/api/stats/{short_code}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["clicks"] == 0

    # Simulate redirect
    client.get(f"/{short_code}")

    # Check stats again (clicks should increase)
    response = client.get(f"/api/stats/{short_code}")
    data = response.get_json()
    assert data["clicks"] == 1

# Stats for non-existent short code
def test_stats_not_found(client):
    response = client.get("/api/stats/unknown")
    assert response.status_code == 404
