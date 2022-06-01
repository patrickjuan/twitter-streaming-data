import json


def load_json_file(filepath):
    with open(filepath) as f:
        return json.load(f)


def get_config():
    FILTER_SUBJECT = ["formula1", "formula 1", "f1"]
    TOKEN = "YOUR_BEARER_TOKEN_HERE"
    DRIVERS_TEAMS = load_json_file("src/commom/drivers_teams.json")

    return {
        "FILTER_SUBJECT": FILTER_SUBJECT,
        "TOKEN": TOKEN,
        "DRIVERS_TEAMS": DRIVERS_TEAMS,
    }
