from pprint import pprint
from fastapi import APIRouter

import requests

from dotenv import load_dotenv
import os

from routers.hubspot import *

load_dotenv()

router = APIRouter (
    prefix="/clickup",
    tags=['sync']
)

@router.post("/syncData")
def syncData():

    contacts = getContacts()

    for contact in contacts:

        if 'estado_clickup' not in contact.properties:
            setTask(contact.properties)
        else:
            if contact.properties.estado_clickup == (None or ''):
                setTask(contact.properties)
   
    return listTask()

def listTask ():
    list_id = os.getenv('LIST_CLICKUP') 
    url = "https://api.clickup.com/api/v2/list/" + list_id + "/task"

    headers = {
    "Content-Type": "application/json",
    "Authorization": os.getenv('KEY_CLICKUP') 
    }

    try :
       api_response = requests.get(url, headers=headers)
    except :
        return "ocurrio un erroir"

    data = api_response.json()
    return data


def setTask(data):

    list_id = os.getenv('LIST_CLICKUP') 
    url = "https://api.clickup.com/api/v2/list/" + list_id + "/task"

    query = {
    "custom_task_ids": "true",
    "team_id": "123"
    }

    payload = {
    "name": "Contacto %s" %(data['firstname']),
    "description": " se creo el contacto de %s %s \n Email %s" %(data['firstname'],data['lastname'],data['email']),
    "tags": [
        "Prueba tecnica"
    ],
    "notify_all": True,
    "check_required_custom_fields": None,
    }

    headers = {
    "Content-Type": "application/json",
    "Authorization": os.getenv('KEY_CLICKUP') 
    }

    response = requests.post(url, json=payload, headers=headers, params=query)

    data = response.json()
    print(data)
