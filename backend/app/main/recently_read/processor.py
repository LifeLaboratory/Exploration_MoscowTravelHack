from main.base.provider import Provider


class Processor:
    @staticmethod
    def get_recently_read():
        recently_read = Provider('main/sql').exec_by_file('recently_read.sql')
        return recently_read
