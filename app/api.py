from Contact import Contact_DA
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


@router.get("/contacts")
def list_contacts():
    get_list = Contact_DA.get_all_contacts()
    return get_list


class ContectBody(BaseModel):
    first_name: str
    last_name: str
    phone_number: str



@router.post("/contacts")
def create_contacts(payload: ContectBody):
    post_list = Contact_DA.create_contact(payload)
    return post_list


@router.put("/contacts/{id}")
def update_contact(payload: ContectBody, id):
    Contact_DA.update_contact(payload, id)
    return "Done"


@router.delete("/contacts/{id}")
def delete_contacts(id):
    Contact_DA.delete_contact(id)
    return "Done"
