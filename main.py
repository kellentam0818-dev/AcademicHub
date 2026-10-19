from fastapi import FastAPI, Path

app = FastAPI(title="Student Task Management System", version="0.1.0", description="A simple FastAPI application for managing students.")

@app.get("/")
async def home():
    return {"message": "Welcome to Student Task Management System!"}

@app.get("/students/by-name/{student_name}")
async def get_student(student_name: str = Path(min_length=2, max_length=50)):
    return {"student_name": student_name}

@app.get("/students/{student_id}")
async def get_student_by_id(student_id: int = Path(ge=1, le=10000)):
    return {"student_id": student_id, "message": f"Received student ID: {student_id}."}

@app.get("/tasks")
async def get_tasks():
    return {"tasks": []}

