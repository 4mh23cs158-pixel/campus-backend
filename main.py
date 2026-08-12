from fastapi import FastAPI
from db import engine,Base
from routes import admin_routes, ai_routes, analytics_routes, department_routes, user_routes
from routes import complaint_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",

        # Production frontend
    "https://campus-ai-frontend-six.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_routes.router)
app.include_router(complaint_routes.router)
app.include_router(department_routes.router)
app.include_router(admin_routes.router)
app.include_router(ai_routes.router)
app.include_router(analytics_routes.router)
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}