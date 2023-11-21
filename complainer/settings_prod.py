from .settings_base import *

# Security
SECRET_KEY = config("SECRET_KEY")
ALLOWED_HOSTS = [".onrender.com"]
CORS_ALLOW_ALL_ORIGINS = True

# Storage
DEFAULT_FILE_STORAGE = "github_storages.backend.BackendStorages"
GITHUB_HANDLE = config("GITHUB_USERNAME")
ACCESS_TOKEN = config("GITHUB_ACCESS_TOKEN")
GITHUB_REPO_NAME = config("GITHUB_REPO_NAME")
MEDIA_BUCKET_NAME = "media"

DEBUG = False

# Database
DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}
}
