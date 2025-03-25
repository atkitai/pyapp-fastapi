from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Running"}

@app.get("/check")
def read_check():
    return {"message": "Checking"}


    

