import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "Cartier WAF"
    VERSION = "1.0.0"
    DEBUG = os.getenv("DEBUG", "True") == "True"

    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))

    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "cartier")

    MODEL_PATH = os.getenv("MODEL_PATH", "backend/model/model.pkl")

    CONFIDENCE_THRESHOLD_BLOCK = float(os.getenv("CONFIDENCE_THRESHOLD_BLOCK", 0.90))
    CONFIDENCE_THRESHOLD_ALERT = float(os.getenv("CONFIDENCE_THRESHOLD_ALERT", 0.70))


settings = Settings()
