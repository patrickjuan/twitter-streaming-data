import pandas as pd
import src.logger as logger
from src.commom.config import get_config

config = get_config()


def make_aggregations() -> None:
    try:
        raw_data = pd.read_csv("raw_data.csv")
        raw_data.columns = ["id", "text"]
        raw_data.to_csv("raw_data_2.csv", index=False)

        data_identified = pd.read_csv("data_identified.csv")
        data_identified.columns = [
            "id",
            "text",
            "mention_driver",
            "mention_team",
            "mention_country",
        ]

        aggregated_by_driver = data_identified.groupby(["mention_driver"]).agg(
            {
                "text": "count",
            }
        )

        aggregated_by_driver.to_csv("aggregated_drivers.csv")

        aggregated_by_team_and_driver = data_identified.groupby(
            ["mention_team", "mention_driver"]
        ).agg(
            {
                "text": "count",
            }
        )
        aggregated_by_team_and_driver.to_csv("aggregated_teams_and_drivers.csv")

        aggregated_by_country = data_identified.groupby(["mention_country"]).agg(
            {
                "text": "count",
            }
        )
        aggregated_by_country.to_csv("aggregated_country.csv")
        logger.info("data created")
    except Exception as err:
        logger.error("Failed to transform data", {"error": err})


def identify_mentions(raw_data: dict) -> dict:
    try:
        raw_data["mention_driver"] = []
        raw_data["mention_team"] = []
        raw_data["mention_country"] = []

        drivers_teams = config["DRIVERS_TEAMS"]

        for driver in drivers_teams:
            possible_mentions = drivers_teams[driver]["possible_mentions"]
            for p in possible_mentions:
                if p.lower() in raw_data["text"].lower():
                    raw_data["mention_driver"].append(driver)
                    raw_data["mention_team"].append(drivers_teams[driver]["team"])
                    raw_data["mention_country"].append(drivers_teams[driver]["country"])

        if len(raw_data["mention_driver"]) == 0:
            raw_data["mention_driver"] = ""
        if len(raw_data["mention_team"]) == 0:
            raw_data["mention_team"] = ""
        if len(raw_data["mention_country"]) == 0:
            raw_data["mention_country"] = ""

        return raw_data
    except Exception as err:
        logger.error(
            "Failed to identify drivers and team names",
            {"error": err, "raw_data": raw_data},
        )
        raise err
