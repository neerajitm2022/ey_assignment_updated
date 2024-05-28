from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime
from multiprocessing import Pool
from ..models.models import AdditionRequest, AdditionResponse
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

def perform_addition(numbers: List[int]) -> int:
    return sum(numbers)


@router.post("/addition/")
async def addition(request: AdditionRequest):
    try:
        start_time = datetime.now().isoformat()
        with Pool() as pool:
            results = pool.map(perform_addition, request.payload)

        end_time = datetime.now().isoformat()
        response_data = {
            "batchid": request.batchid,
            "response": results,
            "status": "complete",
            "started_at": start_time,
            "completed_at": end_time
        }
        logger.info(f"Addition request processed successfully. Batch ID: {request.batchid}")
        return AdditionResponse(**response_data)

    except Exception as e:
        logger.info(f"Error while Addition request . Batch ID: {request.batchid}")
        raise HTTPException(status_code=500, detail=str(e))