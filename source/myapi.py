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

# O asterisco (*) antes de um parâmetro em uma função no Python indica que
# esse parâmetro é um parâmetro de palavras-chave (keyword-only argument).
# Isso significa que esse parâmetro só pode ser fornecido na chamada da função
# usando a sintaxe de palavra-chave, e não como um argumento posicional.
# Ex:
    # func(*, a: int, b: int):
    #   pass

    # func(a = 1, b = 2) Ok
    # func(1,2) Erro

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students.keys():
        return {"Error": "Student already exists"}
    
    students[student_id] = student
    return students[student_id]