import uvicorn
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from orm import crud, schemas
from orm.database import SessionLocal


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/channels/", response_model=List[schemas.Channel])
def read_channels(db: Session = Depends(get_db)):
    users = crud.get_channels(db=db)
    return users


@app.get("/channels/{channel_name}", response_model=schemas.Channel)
def read_channel(channel_name: str, db: Session = Depends(get_db)):
    db_user = crud.get_channel_by_name(db=db, channel_name=channel_name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/video/{channel_name}", response_model=schemas.Channel)
def add_channel(channel_name: str, new_boobs: int, db: Session = Depends(get_db)):
    db_user = crud.get_channel_by_name(db=db, channel_name=channel_name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.add_video(db=db, channel_name=channel_name, new_boobs=new_boobs)


@app.post("/new/{channel_name}", response_model=schemas.Channel)
def new_channel(channel_name: str, db: Session = Depends(get_db)):
    db_user = crud.get_channel_by_name(db=db, channel_name=channel_name)
    if db_user is not None:
        raise HTTPException(status_code=404, detail="User exists")
    db_user = crud.make_channel(db=db, channel_name=channel_name)

    return db_user


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
