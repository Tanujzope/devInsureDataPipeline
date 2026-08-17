from pathlib import Path
import re
import json
from datetime import datetime
import pandas as pd

def get_incoming_files():
    ingestion_folder = Path(__file__).resolve().parent.parent / "data" / "ingestion"

    files = list(ingestion_folder.iterdir())

    return files

def validate_fileName(file_path):
    pattern = r"^claims_\d{8}.csv$"
    return (bool(re.match(pattern, file_path.name)))


def read_configuration():
    configFileFolder = Path(__file__).resolve().parent.parent/ "config" / "control_files"
    configFiles = configFileFolder.iterdir()

    configuration = {}

    for file in configFiles:
        if file.suffix == ".json":
            with file.open("r") as f:
                config_data = json.load(f)

        configuration[file.stem] = config_data

    return configuration


def match_configuration(file, configuration):
    fileName = file.stem
    fileType = fileName.split("_")[0]

    for configName, configData in configuration.items():
        configType = configName.split("_")[0]

        if fileType == configType:
            return configData

    return None


def validate_date(file):
    datePart = file.stem.split("_")[1]

    try:
        datetime.strptime(datePart, '%Y%m%d')
        return True

    except ValueError:
        return False


def validate_extension(file, configData):
    return file.suffix == configData["expected_extension"]

def validate_columns(file, config):
    try:

        df = pd.read_csv(file)

        actual_columns = list(df.columns)
        expected_columns = config['expected_columns']

        return actual_columns == expected_columns

    except pd.errors.EmptyDataError:
        return False

    except pd.errors.ParserError:
        return False

def get_row_count(file):
    df = pd.read_csv(file)
    return len(df)

def move_to_validated(file):
    validatedFolder = Path(__file__).resolve().parent.parent / 'data' / 'validated_files'

    validatedFolder.mkdir(parents= True, exist_ok= True)
    destination =validatedFolder / file.name
    file.rename(destination)

    return destination


def get_validated_files():
    validatedFolder = Path(__file__).resolve().parent.parent / "data" / "validated_files"

    files = list(validatedFolder.iterdir())

    return files
