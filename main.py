from fastapi import FastAPI
from db import engine,Base
from routes import user_routes

app = FastAPI()
app.include_router(user_routes.router)
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}