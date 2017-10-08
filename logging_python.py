
#from oslo_log import fixture
#from oslo_log import log as logging

import logging

LOG = logging.getLogger(__name__)

# Define a default handler at INFO logging level
logging.basicConfig(level=logging.INFO)

LOG.info("Python Standard Logging")
LOG.warning("Python Standard Logging")
LOG.error("Python Standard Logging")

