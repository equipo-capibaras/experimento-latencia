import os
import google.cloud.logging

def setup_cloud_logging():
    if os.getenv('ENABLE_CLOUD_LOGGING') == '1':
        client = google.cloud.logging.Client()
        handler = google.cloud.logging.handlers.StructuredLogHandler()
        google.cloud.logging_v2.handlers.setup_logging(handler)
