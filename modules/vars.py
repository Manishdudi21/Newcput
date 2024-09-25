import os

API_ID    = os.environ.get("10499690", "")
API_HASH  = os.environ.get("87d0414dc159c10225cac921edde640a", "")
BOT_TOKEN = os.environ.get("7704985946:AAFbmt5-vR18anJr5LnSiQLxbzKet4DEa0o", "") 
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
