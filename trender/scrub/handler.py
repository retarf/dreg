import datetime


class DataSerializer:

    @staticmethod
    def string_to_date(string, string_format):
        return datetime.datetime.strptime(string, string_format)

    @staticmethod
    def string_to_intiger(string):
        return int(string.replace(' ', ''))
