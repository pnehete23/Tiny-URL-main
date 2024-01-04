import os

# Database Configuration
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///default.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Admin Credentials for URL Shortening Service
ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'default_admin')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'default_password')
