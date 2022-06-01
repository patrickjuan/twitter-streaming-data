from src.transformer.transform import make_aggregations
import src.logger as logger


def main():
    try:
        logger.setup_logger("TwitterStreamData")
        logger.info("Making aggregations")

        make_aggregations()
    except Exception as err:
        logger.error("Error to make aggregations on data", {"error": err})
        raise err


if __name__ == "__main__":
    main()
