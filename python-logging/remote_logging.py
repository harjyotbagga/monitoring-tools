import logging

import logging.handlers
logger = logging.getLogger('Synchronous Logging')
http_handler = logging.handlers.HTTPHandler(
    '127.0.0.1:3000',
    '/log',
    method='POST',
)
logger.addHandler(http_handler)

# Log messages:
logger.warning('Hey log a warning')
logger.error("Hey log a error")
