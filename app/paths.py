from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
APP_DIR = ROOT_DIR / "app"

STATIC_DIR = APP_DIR / "static"
TEMPLATES_DIR = APP_DIR / "templates"
MEDIA_DIR = ROOT_DIR / "media"
PROFILE_PICS_DIR = MEDIA_DIR / "profile_pics"