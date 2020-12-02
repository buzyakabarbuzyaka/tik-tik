from sqlalchemy.orm import Session

from orm import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.Channels).filter(models.Channels.id == user_id).first()


def get_user_by_telegram_id(db: Session, channel_name: str):
    return db.query(models.Channels).filter(models.Channels.channel_name == channel_name).first()
