from fastapi import APIRouter, Response
import json

from pydantic import BaseModel

from dotenv import load_dotenv
import os

import hubspot
from hubspot.crm.contacts import SimplePublicObjectInput, ApiException


load_dotenv()

router = APIRouter (
    prefix="/hubspot",
    tags=['contacts']
)

class Contact (BaseModel):
    email: str
    firstname: str 
    lastname: str | None = None
    phone: int | None = None
    website: str | None = None

client = hubspot.Client.create(access_token=os.getenv('KEY_HUBSPOT'))

@router.post("/setContact")
async def setContact(contact : Contact):

    try:
        contact = SimplePublicObjectInput(properties= {
            "email" : contact.email,
            "firstname" : contact.firstname,
            "lastname" : contact.lastname,
            "phone" : contact.phone,
            "website" : contact.website
        })

        api_response = client.crm.contacts.basic_api.create(simple_public_object_input=contact)

    except ApiException as e: 
        return str(e)
    
    json_str = json.dumps(api_response, indent=4, default=str)

    return Response(content=json_str, media_type='application/json')

def getContacts():

    try:
        api_response = client.crm.contacts.get_all()
    except ApiException as e:
        return str(e)

    return api_response


