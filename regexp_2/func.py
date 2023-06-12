import csv
import re


def read_csv_file(open_file: str) -> list:
    with open(open_file) as f:
        contacts_raw = [dict(i) for i in csv.DictReader(f)]
    return contacts_raw


def change_name(contact: dict) -> list:
    name = f"{contact['lastname']} {contact['firstname']} {contact['surname']}".split()
    while len(name) != 3:
        name.append('')
    return name


def change_phone(phone: str) -> str:
    pattern = r'(?:\+7|8)?[\s-]?\(?(\d{3})\)?[\s-]?(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})(?:\s\(?(доб\.)\s(\d+)\)?)?'
    repl = r'+7(\1)\2-\3-\4 \5\6'
    return re.sub(pattern=pattern, repl=repl, string=phone).strip()


def refactor_data(data_raw: list[dict]) -> list[dict]:
    for contact in data_raw:
        contact['lastname'], contact['firstname'], contact['surname'] = change_name(contact)
        contact['phone'] = change_phone(contact['phone'])
    return data_raw


def concat_duplicate(data_refactor: list[dict]) -> list[dict]:
    data_copy = data_refactor.copy()
    for i, el in enumerate(data_copy, 1):
        duplicate = list(filter(lambda x: el['lastname'] == x['lastname'] and el['firstname'] == x['firstname'],
                                data_copy[i:]))
        if duplicate:
            data_refactor.remove(duplicate[0])
            for k, v in el.items():
                if not el[k]:
                    el[k] = duplicate[0][k]
    return data_refactor


def write_csv_file(data: list[dict], write_file: str) -> None:
    with open(write_file, 'w') as f:
        fieldnames = ['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
