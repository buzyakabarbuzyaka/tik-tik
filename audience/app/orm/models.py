from sqlalchemy import Column, Integer, String

from orm.database import Base, engine


class Channels(Base):
    __tablename__ = "channels"

    id = Column(Integer, primary_key=True)
    channel_name = Column(String, index=True, nullable=False)
    boobs = Column(Integer, nullable=False)
    subscribers = Column(Integer, nullable=False)


Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
