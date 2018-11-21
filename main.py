from unifier import LogsUnifier

dir_path = '.\\input'
log_path = 'unify.log'

user_input = input('Enter the logs directory: ')
if user_input != '':
    dir_path = user_input

log_unifier = LogsUnifier()
log_unifier.unify_logs(dir_path, log_path)
