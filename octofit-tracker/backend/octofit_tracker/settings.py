import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB connection
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit',
        'CLIENT': {
            'host': os.getenv('MONGODB_URI'),
        },
    }
}

# Enable CORS
INSTALLED_APPS = [
    # ...existing apps...
    'corsheaders',
    'octofit_tracker',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # ...existing middleware...
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS',
]
CORS_ALLOW_HEADERS = [
    '*',
]

# Allow all hosts
ALLOWED_HOSTS = ['*']
