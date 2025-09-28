from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def read_root():
    return ("Hola FastAPI")

@app.get("/mensaje")
async def read_message():
    return {"message": "Hola MUNDO"}  