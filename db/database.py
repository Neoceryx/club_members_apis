from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DATABASE_URL = "postgresql://postgres:1234@localhost:5432/ClubMembers"
DATABASE_URL = "postgresql://clubmembers_gevw_user:D7iqJOgToWvkt7VBuYFwyopEcCmrISAO@dpg-cm16u58cmk4c73d6b2vg-a.oregon-postgres.render.com/clubmembers_gevw"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# return BD Session
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()  # close DB connection