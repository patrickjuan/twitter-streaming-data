from aws_lambda_powertools import Logger

logger = Logger()

_metadata = {}


def setup_logger(handler=""):
    logger.structure_logs({})
    clear_metadata()
    if handler:
        add_metadata("handler", handler)


def clear_metadata():
    global _metadata
    _metadata = {}


def add_metadata(k, v):
    global _metadata
    _metadata[k] = v


def error(message, extra_info={}):
    logger.error(
        {"message": message, "extraInfo": {**extra_info}, "metadata": {**_metadata}}
    )


def info(message, extra_info={}):
    logger.info(
        {"message": message, "extraInfo": {**extra_info}, "metadata": {**_metadata}}
    )


def warn(message, extra_info={}):
    logger.warning(
        {"message": message, "extraInfo": {**extra_info}, "metadata": {**_metadata}}
    )
