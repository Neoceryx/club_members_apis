from fastapi import FastAPI
import uvicorn

# To import customs apis
from routes.members import member_rute
from db.models import Base, User
from db.database import engine, SessionLocal
from sqlalchemy.orm import Session

# to create the models on the DB
Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

app = FastAPI()
app.include_router(member_rute)


@app.get("/")
async def hello_world():
    return {"response":"Hello world"}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)