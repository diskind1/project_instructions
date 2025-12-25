from fastapi import FastAPI
from pathlib import Path
from Contact import HandlingContacts
from fastapi import APIRouter
router = APIRouter()


con = HandlingContacts()

app = FastAPI()

@router.get("/contacts")
def list_contacts():
    get_list = con.get_all_contacts()
    return get_list
    
@router.post("/contacts")
def create_contacts(payload: dict):
    con.create_contact(payload)

@router.put("/contacts/{id}")
def create_many(payload: list[dict], id):
    con.update_contact(payload,id)

@router.delete("/contacts/{id}")
def delete_contacts(id):
    con.delete_contact(id)
