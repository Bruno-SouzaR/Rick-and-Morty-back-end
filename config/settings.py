import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URI = os.getenv("DATABASE_URI")
front_end_url = os.getenv("FRONT_END_URL")
environment = os.getenv("ENVIRONMENT")