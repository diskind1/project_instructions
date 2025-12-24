import mysql.connector
from data_interactor import DatabaseServise
cur = DatabaseServise()
cur.connect_db
cur.cursor


class Contact:
    def __init__(self, first_name_contact, last_name_contact, phone_number_contact):
        self.id = None
        self.first_name = first_name_contact
        self.last_name = last_name_contact
        self.phone_number = phone_number_contact


    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "phone_number": self.phone_number,
        }



class HandlingContacts:
    def create_contact(contact_info: dict):
        sql = "INSERT INTO Contact (first_name, last_name, phone_number) VALUES (%s, %s, %s)"
        val = (contact_info["first_name"], contact_info["last_name"], contact_info["phone_number"])
        cur.cursor.execute(sql, val)
        return("db has been updated")

    def get_all_contacts():
        sql = "SELECT * FROM Contact"
        cntct = cur.cursor.execute(sql)
        return cntct

    def update_contact(contact_info: dict, id):
        sql = "UPDATE Contact SET first_name = %s, last_name = %s, phone_number = %s WHERE id = %s"
        val = (contact_info["first_name"], contact_info["last_name"], contact_info["phone_number"], id)
        cur.cursor.execute(sql, val)
        return("db has been updated")

    def delete_contact(id):
        sql = "DELETE FROM Contact WHERE id = %s"
        val = (id)
        cur.cursor.execute(sql, val)
        return("db has been updated")


