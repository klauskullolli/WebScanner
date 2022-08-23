from ctypes import util
import sys
import os
sys.path.append(os.path.abspath("."))

import webServices.utils as util

util.startMitmProxy()