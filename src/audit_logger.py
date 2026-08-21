import csv
from pathlib import Path
from datetime import datetime

def archilog_ingestion():

    projectFolder = Path(__file__).resolve().parent.parent
    logsFolder = projectFolder / "logs"
    logsFolder.mkdir(exist_ok=True, parents=True)

    currentDate = datetime.now().strftime("%Y%m%d")
    logFile = logsFolder / f"ingestion_log_{currentDate}.csv"

    with open(logFile, "a", newline="") as file:
        writer = csv.writer(file)
        if logFile.stat().st_size == 0:
            writer.writerow([
                "logdate",
                "stage",
                "status",
                "message"
            ])

            writer.writerow([
                datetime.now().strftime("%Y-%M-%D %H:%M:%S"),
                "ingestion",
                "success",
                "file validation and ingestion completed successfully"
            ])
    print("Ingestion Log created successfully")

def log_preprocess():
    projectFolder = Path(__file__).resolve().parent.parent
    logsFolder = projectFolder / "logs"
    logsFolder.mkdir(exist_ok=True, parents=True)
    currentDate = datetime.now().strftime("%Y%m%d")

    logFile = logsFolder / f"preprocessig_log_{currentDate}.csv"

    with open(logFile, "a", newline="") as file:
        writer = csv.writer(file)

        if logFile.stat().st_size == 0:

            writer.writerow([
                "logdate",
                "stage",
                "status",
                "message"
            ])

            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "preprocess",
                "success",
                "Data preprocessing completed successfully"
            ])
    print("Preprocess log created successfully")

def log_retention():
    projectFolder = Path(__file__).resolve().parent.parent
    logsFolder = projectFolder / "logs"
    logsFolder.mkdir(parents=True, exist_ok=True)
    currentDate = datetime.now().strftime("%Y%m%d")

    logFile = logsFolder / f"retention_log_{currentDate}.csv"

    with open(logFile, "a", newline= "") as file:
        writer = csv.writer(file)

        if logFile.stat().st_size == 0:
            writer.writerow([
                "logdate",
                "stage",
                "status",
                "message"
            ])

            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Retention",
                "Success",
                "Semantic Files Archived Successfully"
            ])
    print("Retention Log Creted Successfully")

