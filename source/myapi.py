import uvicorn
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "year": "year 12"
    },
    2: {
        "name": "Maria",
        "age": 16,
        "year": "year 11"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

#Essa classe que permite atualizar um studant (Nem todos os campos precisam ser atualizados)
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get("/") # Isso é um endpoint
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}") # Isso é um endpoint com path parameter
def get_student(student_id: int = Path(..., description = "The ID of the student you want to view", gt = 0, le = 50)):
    return students[student_id]

@app.get("/get-by-name")
def get_student(*, name: str = None, test: int):  # A typing permite você explicite parâmetros opcionais
    for student_id in students.keys():
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students.keys():
        return {"Error": "Student already exists"}
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students.keys():
        return {"Error": "Student does not exist"}
    if student.name != None:
        students[student_id]["name"] = student.name
    if student.age != None:
        students[student_id]["age"] = student.age
    if student.year != None:
        students[student_id]["year"] = student.year
    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students.keys():
        return {"Error": "Student does not exist"}
    del students[student_id]
    return {"Message": "Student deleted successfully"}

uvicorn.run(app)