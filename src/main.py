from ingestion_manager import(
get_incoming_files, validate_fileName, read_configuration,
match_configuration, validate_date,
validate_extension, validate_columns,
get_row_count, move_to_validated, get_validated_files
)
from preprocessing_engine import (
preprocessed_file
)
from transformation_engine import (
build_curated_data
)

files = get_incoming_files()



# for file in files:
#     print(file)
#     print(validate_fileName(file))

configuration = read_configuration()
# print(configuration.keys())

for file in files:
    config = match_configuration(file, configuration)

    if config is None:
        print(f'{file.name} ---> No Matching Configuration')
        continue

    validDate = validate_date(file)
    validExtension = validate_extension(file, config)

    if validDate and validExtension:
        validColumn = validate_columns(file, config)

        if validColumn:
            print(f"{file.name} -> VALID")
            validatedFile = move_to_validated(file)

            preprocessed_file(validatedFile)

        else:
            print(f"{file.name} -> INVALID")
    else:
        print(f"{file.name} -> INVALID")


validatedFiles = get_validated_files()

for file in validatedFiles:
    preprocessed_file(file)
    #print(f"{file.name} ----> Processing Completed")


build_curated_data()