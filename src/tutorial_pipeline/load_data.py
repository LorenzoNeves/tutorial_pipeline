import os
import pandas as pd
from sqlalchemy import create_engine

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_engine():
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT', '5432')
    name = os.getenv('DB_NAME')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')

    url = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}'
    return create_engine(url)


def load_weather_data(table_name: str, df: pd.DataFrame) -> None:
    logging.info(f"Carregando {len(df)} linha(s) na tabela '{table_name}'...")

    engine = get_engine()
    df.to_sql(table_name, engine, if_exists='append', index=False)

    logging.info(f"Dados carregados com sucesso na tabela '{table_name}'")
