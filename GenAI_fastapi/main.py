from fastapi import FastAPI
from services.user import router as user_router
from services.admin import router as admin_router

app = FastAPI()

# Register routers
# app.include_router(data_router, prefix="/iot", tags=["IoT Data"])

app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(admin_router, prefix="/admin", tags=["Admin"])

@app.get("/")
def read_root():
    return {"message": "Static Chatbot"}