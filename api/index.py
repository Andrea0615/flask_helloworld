from flask import Flask
import psycopg2 #conectarse a posgres ccon sql en pyhton
from dotenv import load_dotenv# leer las variables de ambiente
import os #leer las variables de ambiente
# Load environment variables from .env
load_dotenv()

# Fetch variables
CONNECTION_STRING= os.getenv("CONNECTION_STRING")

"""USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")"""


app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'
    
@app.route('/sensor')
def sensor():
    # Connect to the database
    try:
        connection = psycopg2.connect( #se conecta a la base de datos
            CONNECTION_STRING
        )
        print("Connection successful!")
        
        # Create a cursor to execute SQL queries
        cursor = connection.cursor() #cursor al objeto que se encarga de leer los datos (tablas, sqls etc)
        
        # Example query
        cursor.execute("select * from sensores;") #select: es la sql que se quiere ejecutar
        result = cursor.fetchone()
        print("Current Time:", result)
    
        # Close the cursor and connection
        cursor.close()
        connection.close()
        print("Connection closed.")
        return f"Current Time:, {result}"
    
    except Exception as e:
        return f"Failed to connect: {e}"
