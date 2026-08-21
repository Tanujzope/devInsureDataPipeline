import zipfile
from pathlib import Path
from datetime import datetime

def archive_file():
    project_folder = Path(__file__).resolve().parent.parent

    semantic_folder = project_folder / "data" / "semantic"
    archive_folder = project_folder / "data" / "retention" / "archive"

    archive_folder.mkdir(exist_ok=True, parents=True)
    current_date = datetime.now().strftime("%Y%m%d")
    archive_file = archive_folder / f"archive_{current_date}.zip"

    semantic_files = list(semantic_folder.glob("*"))

    with zipfile.ZipFile(archive_file, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for file in semantic_files:
            if file.is_file():
                zip_file.write(file, arcname=file.name)



    print("Semantic files archived successfully")
    print("Archive created:", archive_file)