# CHANGES.md

## Approach
- Designed a simple **Flask-based URL Shortener** with 3 endpoints:
  - `POST /api/shorten` → Shorten a given URL
  - `GET /<short_code>` → Redirect to the original URL and count clicks
  - `GET /api/stats/<short_code>` → Return analytics (click count, created_at)
- Used **in-memory storage** (Python dictionary) to keep short codes, URLs, and stats.
- Implemented **random 6-character alphanumeric short code** generation.
- Added **URL validation** to ensure valid inputs.
- Added **unit tests** using `pytest` for all core functionalities.

## Implementation Details
- **Routes**: Defined in `app/routes.py` using Flask Blueprints.
- **Storage**: Implemented in `app/storage.py` (in-memory dictionary).
- **Utilities**: 
  - `generate_short_code()` → Generates unique short codes.
  - `validate_url()` → Ensures valid URL format.
- **Testing**:
  - 5 test cases in `tests/test_basic.py` covering shortening, redirection, stats, invalid input, and 404 cases.
  - All tests passing.

## Trade-offs
- **No database**: Chose in-memory storage for simplicity (data resets on restart).
- **No authentication**: Out of scope for this assignment.
- **No custom aliases**: Focused only on required features.

## Future Enhancements
- Add **persistent storage** (SQLite/PostgreSQL).
- Add **rate limiting** & **authentication** for production use.
- Add **custom short code support**.
- Create a **simple frontend** for easier usage.

## AI Usage
- Used **ChatGPT** for structuring project layout, generating boilerplate, and refining test cases.
- Manually reviewed and tested all AI-generated code to ensure correctness.
