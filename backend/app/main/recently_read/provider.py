from main.recently_read.processor import Processor


class Provider:
    @staticmethod
    def get_recently_read():
        return Processor.get_recently_read()