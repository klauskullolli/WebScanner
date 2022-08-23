import sys
import os
sys.path.append(os.path.abspath("."))



import subprocess
import pkg_resources
import logging

logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s", encoding="ufc-8", level=logging.DEBUG)
logger = logging.getLogger()

class Package:

    @staticmethod
    def installPackages(packageList: set) -> bool:
        installedPackages = {pkg.key for pkg in pkg_resources.working_set}
        missing = packageList - installedPackages

        if missing:
            # implement pip as a subprocess:
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])
                logger.info(f"Packages: {missing} are installed successfully")
                return True
            except:
                logger.info(f"Packages: {missing} are not installed successfully")
                return False

        logger.info(f"Packages: {packageList} are already installed")
        return False


    @staticmethod
    def deletePackage(packageName: str) -> bool:
        installedPackages = {pkg.key for pkg in pkg_resources.working_set if pkg.key == packageName}
        if len(installedPackages) == 0:
            logger.warning(f"Package: {packageName} does not exist")
            return False
        else:
            status = os.system(f"pip uninstall f'{packageName} ")
            if status == 0:
                logger.warning(f"Package: {packageName} deleted successfully")
                return True
            else:
                logger.error(f"Package: {packageName} was not deleted successfully")
                return False

    @staticmethod
    def installedPackage() -> set():
        installedPackages = {pkg.key for pkg in pkg_resources.working_set}
        return installedPackages

    @staticmethod
    def isInstalled(packageName: str) -> bool:

        installedPackages = {pkg.key for pkg in pkg_resources.working_set}
        if packageName in installedPackages:
            return True
        else:
            return False
