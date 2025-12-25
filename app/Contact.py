import mysql.connector
from data_interactor import DatabaseServise


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


class Contact_DA:

    @staticmethod
    def create_contact(contact_info: dict):
        conn = DatabaseServise.get_connection()
        sql = "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)"
        val = (
            contact_info["first_name"],
            contact_info["last_name"],
            contact_info["phone_number"],
        )
        conn.cursor().execute(sql, val)
        return "db has been updated"

    @staticmethod
    def get_all_contacts():
        conn = DatabaseServise.get_connection()
        sql = "SELECT * FROM contacts"

        cursor = conn.cursor()
        cursor.execute(sql)
        contacts = cursor.fetchall()
        return contacts

    @staticmethod
    def update_contact(contact_info: dict, id):
        conn = DatabaseServise.get_connection()
        sql = "UPDATE contacts SET first_name = %s, last_name = %s, phone_number = %s WHERE id = %s"
        val = (
            contact_info["first_name"],
            contact_info["last_name"],
            contact_info["phone_number"],
            id,
        )
        conn.cursor().execute(sql, val)
        return "db has been updated"

    @staticmethod
    def delete_contact(id):
        conn = DatabaseServise.get_connection()
        sql = "DELETE FROM contacts WHERE id = %s"
        val = id
        conn.cursor().execute(sql, val)
        return "db has been updated"
