from fastapi import FastAPI
import models
from database import engine
from routers import users, activities, progress

# Create tables if not exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Kido API", version="1.0")

# Include Routers
app.include_router(users.router)
app.include_router(activities.router)
app.include_router(progress.router)

@app.get("/")
def root():
    return {"message": "Welcome to Kido API"}
