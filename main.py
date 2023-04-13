from fastapi import FastAPI 


app = FastAPI()

@app.post("/setHubSpot")
def setContact():
    return "hola"


@app.post("syncData")
def syncData():
    return "buenas"