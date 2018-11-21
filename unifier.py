from handlers.filesystem import FileSystemLogHandler
from writers.filesystem import FileSystemLogWriter
from os import listdir, path


class LogsUnifier:

    def unify_logs(self, dir_path, unified_log_path):
        log_writer = FileSystemLogWriter(unified_log_path)
        log_readers = []
        for log_file in listdir(dir_path):
            log_file = path.join(dir_path, log_file)
            log_readers.append(FileSystemLogHandler(log_file))
        while len(log_readers) > 0:
            earliest_log = self.__get_first_log(log_readers)
            log_writer.append_log(earliest_log.current_log)
            earliest_log.get_next_log()
            if earliest_log.finished:
                log_readers.remove(earliest_log)
        log_writer.end_unification()

    def __get_first_log(self, log_readers):
        selected_reader = log_readers[0]
        for reader in log_readers:
            if reader.current_log.timestamp < selected_reader.current_log.timestamp:
                selected_reader = reader
        return selected_reader
