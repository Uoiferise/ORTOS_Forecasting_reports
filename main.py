from get_data import Data
from settings import *


class Report:

    def __init__(self):
        self.__data = Data(FOLDER_PATH)

    @staticmethod
    def create_reports():
        pass


def main():
    reports = Report()
    reports.create_reports()


if __name__ == '__main__':
    main()
