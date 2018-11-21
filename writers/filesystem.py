from .base import BaseLogWriter

class FileSystemLogWriter(BaseLogWriter):

    def __init__(self, log_path):
        self.file_handle = open(log_path, 'w')

    def append_log(self, log):
        self.file_handle.write(log.raw)

    def end_unification(self):
        self.file_handle.close()
