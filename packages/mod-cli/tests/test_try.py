import pytest


def test_cases():
    print(f"{bool('true')}, {bool('false')}")
    pass


def test_logger_level():
    from loguru import logger
    import sys

    logger.info("info log")
    logger.debug("debug log")
    logger.error("err log")

    logger.remove()
    logger.add(sys.stdout, level="INFO")
    logger.info("info log")
    logger.debug("debug log")
    logger.error("err log")


def test_logger2():
    from loguru import logger
    import sys

    logger.remove()
    logger.add(sys.stdout, level="ERROR")
    logger.info("info log")
    logger.debug("debug log")
    logger.error("err log")
