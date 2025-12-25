from Contact import HandlingContacts
from fastapi import APIRouter


router = APIRouter()


@router.get("/contacts")
def list_contacts():
    get_list = HandlingContacts.get_all_contacts()
    return get_list


@router.post("/contacts")
def create_contacts(payload: dict):
    post_list = HandlingContacts.create_contact(payload)
    return post_list


@router.put("/contacts/{id}")
def create_many(payload: list[dict], id):
    HandlingContacts.update_contact(payload, id)
    return "Done"


@router.delete("/contacts/{id}")
def delete_contacts(id):
    HandlingContacts.delete_contact(id)
    return "Done"
