import mysql.connector
import os
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()


class DatabaseServise:

    connection = None

    @staticmethod
    def connect_to_db():
        try:
            connection = mysql.connector.connect(
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                host=os.getenv("DB_HOST"),
                password=os.getenv("DB_PASSWORD"),
                port=os.getenv("DB_PORT"),
            )
            DatabaseServise.connection = connection
            return DatabaseServise.connection
        except Error as e:
            print("connot conect to db", e)

    @staticmethod  
    def get_connection():
        if DatabaseServise.connection and DatabaseServise.connection.is_connected():
            return DatabaseServise.connection
        DatabaseServise.connection = DatabaseServise.connect_to_db()
        return DatabaseServise.connection
        

# with open("C:Users/menni/OneDrive/Documents/kodcode-file/exercise_idf/project_instructions/sql/init.sql", "r") as file:
#     commands_list = file.read().split(";")
#     for command in commands_list:
#         cur.execute(command)
