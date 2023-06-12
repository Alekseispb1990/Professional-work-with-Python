from func import read_csv_file, refactor_data, concat_duplicate, write_csv_file


def main(open_file: str, write_file: str) -> None:
    data_raw = read_csv_file(open_file)
    data_refactor = refactor_data(data_raw)
    data = concat_duplicate(data_refactor)
    write_csv_file(data, write_file)


if __name__ == '__main__':
    main(open_file='phonebook_raw.csv', write_file='phonebook.csv')
