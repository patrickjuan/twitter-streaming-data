from src.loader.file_generator import write_csv_from_dict
import os


def test_write_csv_from_dict_should_pass():
    input = {
        "id": "1531806345216802816",
        "text": "McLaren needs to reflect on Monaco F1 strategy.\nFollowing Norris' first stop for intermediate tyres, he made a second for hard-compound slicks but was overtaken by George Russell in the latter instance as the Mercedes driver stopped a lap earlier....\n\nhttps://t.co/HqVf8JAR1Z",
        "mention_driver": ["George Russell", "Lando Norris"],
        "mention_team": ["Mercedes AMG Petronas F1 Team", "McLaren Racing"],
        "mention_country": ["United Kingdom", "United Kingdom"],
    }
    expected_output = True
    output = write_csv_from_dict(input, "test_file.csv")
    assert output == expected_output
    os.remove("test_file.csv")
