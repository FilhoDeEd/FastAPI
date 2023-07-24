from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        "name": "John",
        "age": 17,
        "class": "year 12"
    },
    2: {
        "name": "Maria",
        "age": 16,
        "class": "year 11"
    }
}

@app.get("/") #Isso é um endpoint
def index():
    return {"name": "First Data"}

@app.get("/get-student/{student_id}") #Isso é um endpoint com path parameter
def get_student(student_id: int = Path(..., description = "The ID of the student you want to view", gt = 0, le = students.__len__())):
    return students[student_id]
