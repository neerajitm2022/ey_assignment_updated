Implimentation Descriprion

1. Setting up FastAPI project with Pydantic models for request and response validation:
First, install FastAPI and Pydantic:

 2. Implementing addition logic with multiprocessing:
Utilize Python's multiprocessing module to perform addition on input lists of integers concurrently.

3. Writing unit tests:
Write unit tests to cover edge cases and scenarios for both the FastAPI endpoint and the addition logic. used unittest framework.

4. Organizing project structure in MVC format:
Create directories for models, views, and controllers.
Pydantic models in the models directory,
FastAPI endpoint logic in the controllers directory
i didnt create any function in views

5.
"app/" contains the main application code.
"app/controllers/" holds the endpoint logic.
"app/models/" contains Pydantic models.
"app/views/" can have additional views if needed.
"app/main.py" serves as the entry point for running the FastAPI app.
"tests/" contains unit tests for both the endpoint and the addition logic.


-------------Stup and Endpoint testing----------
1. clone repository in local system

2. create virtual environment

3. Install supportig libraries
fastapi==0.68.1
uvicorn==0.15.0
pydantic==1.9.0
pytest==6.2.5

4.Start uvicorn server
     ey_assignment_updated> uvicorn main:app --reload
5. go to end point http://127.0.0.1:8000/addition/

Example
--Request Body---
{
  "batchid": "string",
  "payload": [
    [1,2],[3,4]
  ]
}

---Resposne Body---
{
  "batchid": "string",
  "response": [3,7],
  "status": "complete",
  "started_at": "2024-05-28T17:40:06.016997",
  "completed_at": "2024-05-28T17:40:08.156768"
} 



