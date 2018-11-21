from .base import BaseLogHandler
from logfile import LogObject


class FileSystemLogHandler(BaseLogHandler):

    def __init__(self, file_path):
        self.file_handler = open(file_path, 'r')
        self.current_log = ''
        self.finished = False
        self.get_next_log()

    def get_next_log(self):
        next_line = self.file_handler.readline()
        if next_line == '':
            self.finished = True
            self.file_handler.close()
        self.current_log = LogObject(next_line)
