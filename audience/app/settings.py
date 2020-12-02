import logging
from os.path import join, dirname
import yaml

log = logging.getLogger()


def load_yaml(file_path):
    with open(file_path, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
        except Exception as e:
            log.critical(e, exc_info=True)
            raise e
    return data


MAIN_DIR = dirname(__file__)  # /app
CONFIG_PATH = join(MAIN_DIR, 'config.yaml')
FEED_LIST_PATH = join(MAIN_DIR, 'feeds', 'feed_list.yaml')

CONFIG = load_yaml(file_path=CONFIG_PATH)
DB_CONFIG = CONFIG['database']
MAIN_CONFIG = CONFIG['main']
LOGGER_CONFIG = CONFIG['logger']


UPDATE_INTERVAL = MAIN_CONFIG['UPDATE_INTERVAL']


class PostgresConfiguration:
    POSTGRES_PORT = DB_CONFIG['POSTGRES_PORT']
    POSTGRES_DB = DB_CONFIG['POSTGRES_DB']
    POSTGRES_USER = DB_CONFIG['POSTGRES_USER']
    POSTGRES_PASSWORD = DB_CONFIG['POSTGRES_PASSWORD']
    POSTGRES_ADDRESS = DB_CONFIG['POSTGRES_ADDRESS']

    @property
    def postgres_db_path(self):
        return f'postgres://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@' \
               f'{self.POSTGRES_ADDRESS}:' \
               f'{self.POSTGRES_PORT}/{self.POSTGRES_DB}'


if __name__ == "__main__":
    import utils.loggerInitializer
    pc = PostgresConfiguration()
    log.debug(f'db path: {pc.postgres_db_path}')
