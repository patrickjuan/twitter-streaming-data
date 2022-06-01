import tweepy
import json
import src.logger as logger
from src.transformer.transform import identify_mentions
from src.loader.file_generator import write_csv_from_dict


class StreamData(tweepy.StreamingClient):
    def on_data(self, raw_data):
        try:
            _raw_data = json.loads(raw_data)
            write_csv_from_dict(_raw_data["data"], "raw_data.csv")

            data_identified = identify_mentions(_raw_data["data"])
            write_csv_from_dict(data_identified, "data_identified.csv")

        except Exception as err:
            logger.error(
                "Failed to stream data", {"error": err, "data": data_identified}
            )
            raise err
