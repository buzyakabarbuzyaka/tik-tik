import utils.loggerInitializer  # initializing logger don't delete
import pause
from datetime import datetime, timedelta
import logging
from orm.crud import calc_subscribers
from settings import UPDATE_INTERVAL
from orm.database import SessionLocal

log = logging.getLogger()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == '__main__':
    while True:
        log.info('Start')
        log.info(f'Hello world!!!')
        calc_subscribers(next(get_db()))
        next_start = datetime.now() + timedelta(seconds=UPDATE_INTERVAL)
        log.info(f'Next start: {next_start}')
        log.info('')
        pause.until(next_start)


