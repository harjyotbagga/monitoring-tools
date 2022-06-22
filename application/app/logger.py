import logging
import logging.handlers
from exporter import HTTP_LOGGING, LOGGING_URL
import os
import json
import sys
import requests
from datetime import datetime
from requests.adapters import HTTPAdapter, Retry

HTTP_LOGGING = (HTTP_LOGGING == "True" or HTTP_LOGGING == "true" or HTTP_LOGGING == "1" or HTTP_LOGGING == True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def post_with_retries(url: str, data: dict, retries: int, backoff: float) -> int:
    retry_adapter = HTTPAdapter(max_retries=Retry(
        total=retries,
        backoff_factor=backoff,
        status_forcelist=[500, 502, 503, 504],
        method_whitelist=frozenset(['POST'])
    ))

    with requests.Session() as session:
        session.mount('http://', retry_adapter)
        session.mount('https://', retry_adapter)

        try:
            response = session.post(url, data=data, headers={'Content-Type': 'application/json'})
        except requests.exceptions.RetryError:
            return 500

        return response.status_code 

class CustomLogHandler(logging.Handler):
    def __init__(self, url, *args, **kwargs):
        super(CustomLogHandler, self).__init__(*args, **kwargs)
        self.url = url
    def emit(self, record):
        log_entry = self.format(record)
        response_code = post_with_retries(self.url, log_entry, retries=3, backoff=1)
        print(response_code)
        return

class ApplicationLogger():
    def __init__(self, logger_name, logging_endpoint, logging_level=logging.INFO):
        self.logger_name = logger_name
        self.logging_level = logging_level
        self.logger = logging.getLogger(logger_name)
        self.formatter = logging.Formatter(json.dumps({
            'pathname': '%(pathname)s',
            'line': '%(lineno)d',
            'logLevel': '%(levelname)s',
            'message': '%(message)s',
            'timestamp': '%(asctime)s',
        }), datefmt='%Y-%m-%d %H:%M:%S')

        customHandler = CustomLogHandler(url=f"{LOGGING_URL}/{logging_endpoint}")
        customHandler.setFormatter(self.formatter)
        customHandler.setLevel(logging_level)
        self.logger.addHandler(customHandler)
        self.logger.setLevel(logging_level)


    def debug(self, message):
        try:
            self.logger.debug(message)
        except Exception as e:
            logger.exception(f"{__name__} Logger Error: {e}")
    def info(self, message):
        try:
            self.logger.info(message)
        except Exception as e:
            logger.exception(f"{__name__} Logger Error: {e}")
    def warning(self, message):
        try:
            self.logger.warning(message)
        except Exception as e:
            logger.exception(f"{__name__} Logger Error: {e}")
    def error(self, message):
        try:
            self.logger.error(message)
        except Exception as e:
            logger.exception(f"{__name__} Logger Error: {e}")
    def critical(self, message):
        try:
            self.logger.critical(message)
        except Exception as e:
            logger.exception(f"{__name__} Logger Error: {e}")

    def __repr__(self) -> str:
        return f"ApplicationLogger: {self.logger_name}"
    def __str__(self) -> str:
        return f"ApplicationLogger({self.logger_name}, {self.logging_level})"