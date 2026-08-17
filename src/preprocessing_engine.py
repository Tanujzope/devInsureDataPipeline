import pandas as pd
from pathlib import Path
from datetime import datetime

def preprocessed_file(file):
    dfFile = pd.read_csv(file)

    dfFile.drop_duplicates()

    #print(f"{file.name} -> DUPLICATES REMOVED -> {len(dfFile)} rows remaining")

    dfFile["ingestion_time"] = datetime.now()
    #print(f"{file.name} -> INGESTION_DATE ADDED -> {dfFile['ingestion_time'].iloc[0]}")

    fileDate = file.stem.split("_")[1]

    dfFile['fileDate'] = pd.to_datetime(fileDate, format= "%Y%m%d")
    #print(f"{file.name} -> FILE_DATE ADDED -> {dfFile['fileDate'].iloc[0].date()}")

    preProcessedFile = Path(__file__).resolve().parent.parent / "data" / "preprocessed"
    preProcessedFile.mkdir(parents=True, exist_ok=True)

    outputFile = preProcessedFile / f"{file.stem}.parquet"

    dfFile.to_parquet(outputFile, index=False)

    #print(f"{file.name} -> PREPROCESSING PASSED -> {outputFile.name}")

    return outputFile