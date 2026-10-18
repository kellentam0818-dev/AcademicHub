from fastapi import FastAPI

app = FastAPI(title="Student Task Management System", version="0.1.0", description="A simple FastAPI application for managing students.")

@app.get("/")
async def home():
    return {"message": "Welcome to Student Task Management System!"}

@app.get("/student/{student_name}")
async def get_student(student_name: str):
    return {"student_name": student_name}
