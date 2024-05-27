from fastapi import FastAPI
from app.controllers.addition_controller import router

app = FastAPI()

app.include_router(router)