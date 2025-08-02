# URL Shortener API

A simple URL shortening service built with Flask.

## Features
- Shorten long URLs (`POST /api/shorten`)
- Redirect using short code (`GET /<short_code>`)
- View analytics: clicks, created_at, original URL (`GET /api/stats/<short_code>`)
- In-memory storage (no database)
- Basic input validation
- Unit tests with pytest

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
