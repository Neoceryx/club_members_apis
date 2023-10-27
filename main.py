from fastapi import FastAPI
import uvicorn

# customs apis
app = FastAPI()

@app.get("/")
async def hello_world():
    return {"response":"Hello world"}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)