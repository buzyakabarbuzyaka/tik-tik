from sqlalchemy.orm import Session
from orm import models, schemas


def get_channels(db: Session):
    return db.query(models.Channels).all()


def get_channel_by_name(db: Session, channel_name: str):
    return db.query(models.Channels).filter(models.Channels.channel_name == channel_name).first()


def add_video(db: Session, channel_name: str, new_boobs: int):
    db_channel = get_channel_by_name(db=db, channel_name=channel_name)
    db_channel.boobs += new_boobs
    db.add(db_channel)
    db.commit()
    db.refresh(db_channel)
    return db_channel


def calc_subscribers(db: Session):
    channel_list = db.query(models.Channels).all()
    for channel in channel_list:
        channel.subscribers += channel.boobs*10
        from pprint import pprint
        pprint(channel.__dict__)
        db.add(channel)

    db.commit()


def make_channel(db: Session, channel: schemas.Channel):
    data = channel.dict()
    tmp_channel = db.query(models.Channels).filter_by(id=channel.id).first()
    if tmp_channel:
        for key, value in data.items():
            setattr(tmp_channel, key, value)
        db.add(tmp_channel)
        db.commit()
        pass
    else:
        new_channel = models.Channels(**data)
        db.add_all(new_channel)
        db.commit()
        print("New channel")


if __name__ == '__main__':
    from orm.database import SessionLocal

    def get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()

    # data = {
    #     "id": 1,
    #     "channel_name": "Стас_A0",
    #     "boobs": 1,
    # }
    #
    # a4 = schemas.Channel.parse_obj(data)
    # from pprint import pprint
    # pprint(a4.__dict__)
    # make_channel(next(get_db()), channel=a4)

    calc_subscribers(next(get_db()))
