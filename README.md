1. 
clone repository in local system

2. 
create virtual environment

3. 
Install supportig libraries

fastapi==0.68.1
uvicorn==0.15.0
pydantic==1.9.0
pytest==6.2.5

4.
Start uvicorn server
     ey_assignment_updated> uvicorn main:app --reload

5. 
http://127.0.0.1:8000/addition/


Example
--Request Body---

{
  "batchid": "string",
  "payload": [
    [
      1,2
    ],
    [
      3,4
    ]

  ]
}

---Resposne Body---

{
  "batchid": "string",
  "response": [
    3,
    7
  ],
  "status": "complete",
  "started_at": "2024-05-28T17:40:06.016997",
  "completed_at": "2024-05-28T17:40:08.156768"
} 



