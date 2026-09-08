import requests
import json
from pathlib import Path

import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')


#a gnt só consegue receber esses dados se o status code dessa requisição for igual a 200
def extract_weather_data(url:str) -> list:
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        logging.error(f"Erro de requisição: {data}")
        raise RuntimeError(f"Erro de requisição (status {response.status_code}): {data}")

    if not data:
        logging.warning("Nenhum dado retornado")

    output_path = Path(__file__).resolve().parent.parent.parent / 'data' / 'weather_data.json' #nome do arquivo que eu vou salvar pra essa api
    output_dir = output_path.parent #parent é o python, ele vai olhar pro caminho e vai ver que a gnt ta uma pasta acima
    output_dir.mkdir(parents = True, exist_ok = True)

    with open(output_path, 'w') as f:
        json.dump(data, f, indent = 4)

    logging.info(f"Arquivo salvo em {output_path}")
    return data

# extract_weather_data(url) chamando a função p ver se ta ok, e ta ok/// ETL, fizemos a Extração, falta a transformação e Load(carga)

