from dotenv import load_dotenv
import os

load_dotenv()

SERVER = os.getenv("SERVER")
DATABASE = os.getenv("DATABASE")
DATABASE2=os.getenv('DATABASE2')
DRIVER = os.getenv("DRIVER")

masterengine = f"mssql+pyodbc://{SERVER}/{DATABASE}?driver={DRIVER}&trusted_connection=yes"
Amazonengine = f"mssql+pyodbc://{SERVER}/{DATABASE2}?driver={DRIVER}&trusted_connection=yes"
