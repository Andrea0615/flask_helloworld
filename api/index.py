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


@app.route('')

@app.route('/about')
def about():
    return 'About'
    
@app.route("/sensor/<int:sensor_id>", methods=["POST"])
def insert_sensor_value(sensor_id):
    value = request.args.get("value", type=float)
    if value is None:
        return jsonify({"error": "Missing 'value' query parameter"}), 400

    try:
        conn = psycopg2.connect( #se conecta a la base de datos
            CONNECTION_STRING
        )
        print("Connection successful!")
        cur = conn.cursor()

        # Insert into sensors table
        cur.execute(
            "INSERT INTO sensors (sensor_id, value) VALUES (%s, %s)",
            (sensor_id, value)
        )
        conn.commit()

        return jsonify({
            "message": "Sensor value inserted successfully",
            "sensor_id": sensor_id,
            "value": value
        }), 201

    except psycopg2.Error as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if 'conn' in locals():
            conn.close()
    
    except Exception as e:
        return f"Failed to connect: {e}"
