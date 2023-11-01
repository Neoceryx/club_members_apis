from fastapi import FastAPI, Depends
import uvicorn

# To import customs apis
from routes.members import member_rute
from db.database import engine, Base

# to create the models on the DB
Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(member_rute)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)