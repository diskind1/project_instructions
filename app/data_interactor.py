import mysql.connector
import os
from mysql.connector import Error


class DatabaseServise:
  def __init__(self):
      self.connect_db = None
      self.cursor = self.connect_to_db()


  def connect_to_db(self):
      try:
        self.connect_db = mysql.connector.connect(
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            host=os.getenv("DB_HOST"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
          )
        cursor = self.connect_db.cursor()
        return cursor
      except Error as e:
         print("connot conect to db", e)
         

            




# with open("C:Users/menni/OneDrive/Documents/kodcode-file/exercise_idf/project_instructions/sql/init.sql", "r") as file:
#     commands_list = file.read().split(";")
#     for command in commands_list:
#         cur.execute(command)

