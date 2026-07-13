import psycopg2
import os


# DATABASE CONNECTION

def get_connection():

    connection = psycopg2.connect(

        host=os.getenv("DB_HOST"),

        database=os.getenv("DB_NAME"),

        user=os.getenv("DB_USER"),

        password=os.getenv("DB_PASSWORD"),

        port=os.getenv("DB_PORT")

    )

    return connection

# CREATE DATABASE TABLE

def create_table():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute("""

        CREATE TABLE IF NOT EXISTS calculations (

            id SERIAL PRIMARY KEY,

            username VARCHAR(100) NOT NULL,

            shape VARCHAR(50) NOT NULL,

            dimension1 FLOAT,

            dimension2 FLOAT,

            area FLOAT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        );

    """)


    connection.commit()


    cursor.close()

    connection.close()