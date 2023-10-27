from fastapi import FastAPI, Depends
import uvicorn

# To import customs apis
from routes.members import member_rute
from db.models import Base, User
from db.database import engine, SessionLocal
from sqlalchemy.orm import Session
from schemas.member_sh import member_schema

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
async def hello_world(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@app.post("/")
async def new_user(new_user: member_schema, db: Session = Depends(get_db)):
    user = User()
    user.name = new_user.name
    user.email = new_user.email
    user.nickname = new_user.nickname

    # save it on DB
    db.add(user)
    db.commit()
    db.refresh(user)
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)