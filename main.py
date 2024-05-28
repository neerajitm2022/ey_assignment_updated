from fastapi import FastAPI
from app.controllers.addition_controller import router
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='logs/app.log',
    filemode='a'
)

app = FastAPI()

app.include_router(router)