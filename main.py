from fastapi import FastAPI, Depends
import uvicorn

from sentry_sdk import capture_exception
import sentry_sdk

# To import customs apis
from routes.members import member_rute
from routes.charges import charge_rute
from db.database import engine, Base

sentry_sdk.init(
    dsn="https://f3acb52326ccebaaccbefdcdcaea0472@o203672.ingest.sentry.io/4506168974901248",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
    enable_tracing=True,  # Enable performance monitoring
)

# to create the models on the DB
Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(member_rute)
app.include_router(charge_rute)

@app.get("/sentry-debug")
async def trigger_error():
    division_by_zero = 1 / 0

@app.get("/sentry-manually-debug")
async def capture_manually_error():
    try:
        division_by_zero = 1 / 0
    except Exception as e:
        capture_exception(e)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)