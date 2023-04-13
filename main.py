from fastapi import FastAPI 


app = FastAPI()

@app.post("/setHubSpot")
async def setContact():
    return "holita"



@app.post("/syncData")
async def syncData():
    return "holita"