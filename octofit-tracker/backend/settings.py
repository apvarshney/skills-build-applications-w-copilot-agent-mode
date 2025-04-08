import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB connection string
MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI is not set in the environment variables.")

# Example usage: Print the connection string (remove in production)
print(f"MongoDB URI: {MONGODB_URI}")

INSTALLED_APPS = [
    # ...existing apps...
    'octofit',
]
