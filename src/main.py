from ingestion_manager import(
get_incoming_files, validate_fileName, read_configuration,
match_configuration, validate_date,
validate_extension, validate_columns,
get_row_count, move_to_validated
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
            move_to_validated(file)
        else:
            print(f"{file.name} -> INVALID")
    else:
        print(f"{file.name} -> INVALID")

