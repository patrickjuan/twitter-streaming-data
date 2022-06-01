import tweepy
from src.extractor import StreamData
from src.commom.config import get_config
import src.logger as logger


config = get_config()


def main():
    try:
        logger.setup_logger("TwitterStreamData")
        logger.info("Streaming data from Twitter")

        streamer = StreamData(config["TOKEN"])

        for subject in config["FILTER_SUBJECT"]:
            streamer.add_rules(tweepy.StreamRule(subject))
        logger.add_metadata("filters_applied", config["FILTER_SUBJECT"])

        streamer.filter()

    except Exception as err:
        logger.error("Error to stream data from Twitter API", {"error": err})
        raise err


if __name__ == "__main__":
    main()
