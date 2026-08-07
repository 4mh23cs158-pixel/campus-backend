from fastapi import FastAPI
from db import engine,Base
from routes import admin_routes, department_routes, user_routes
from routes import complaint_routes

app = FastAPI()
app.include_router(user_routes.router)
app.include_router(complaint_routes.router)
app.include_router(department_routes.router)
app.include_router(admin_routes.router)
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}