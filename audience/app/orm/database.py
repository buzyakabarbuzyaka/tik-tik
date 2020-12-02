import logging
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from settings import PostgresConfiguration


log = logging.getLogger()

pg = PostgresConfiguration()
url = pg.postgres_db_path

if not database_exists(url):
    log.info(f"Creating {pg.POSTGRES_DB}")
    create_database(url)

try:
    engine = create_engine(url)
except Exception as e:
    logging.exception("While connecting to db exception occurred:")
    raise e

metadata = MetaData(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base(metadata=metadata)

if __name__ == '__main__':
    from utils.loggerInitializer import initialize_logger
    # initialize_logger(file_output=False)
    log.debug(pg.postgres_db_path)
