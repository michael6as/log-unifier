class LogObject:

    def __init__(self, raw_log):
        self.raw = raw_log
        self.timestamp = self.__find_timestamp(raw_log)

    def __find_timestamp(self, log):
        open_index = log.find('<')
        closing_index = log.find('>')
        if open_index != -1 and closing_index != -1:
            return float(log[open_index + 1:closing_index])
