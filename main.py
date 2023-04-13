from fastapi import FastAPI
import uvicorn

from routers import hubspot,clickup


app = FastAPI()

app.include_router(hubspot.router)
app.include_router(clickup.router)

if __name__ == '__main__':
    uvicorn.run('main:app')
