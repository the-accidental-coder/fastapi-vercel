from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI on Vercel 🚀"}


@app.get("/users")
def home():
    data = [
        { "id": 1, "name": "Somnath" },
        { "id": 2, "name": "Rahul" }
    ]
    return data