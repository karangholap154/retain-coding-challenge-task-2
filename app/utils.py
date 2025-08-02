import random
import string
from urllib.parse import urlparse

# Generate a random 6-character alphanumeric code
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Validate URL format
def validate_url(url):
    try:
        parsed = urlparse(url)
        return all([parsed.scheme in ("http", "https"), parsed.netloc])
    except:
        return False
