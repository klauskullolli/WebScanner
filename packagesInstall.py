import sys
import os
sys.path.append(os.path.abspath("."))

from webServices.package import Package
from webServices.configuration import Configuration


packageSet  = set(Configuration.PACKAGE_LIST)

if __name__ == '__main__':
    Package.installPackages(packageSet)
    pass