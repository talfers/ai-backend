import sys 
from log_cli import logging

logger = logging.getLogger('terminal.py')

class Terminal:
    def __init__(self):
        pass


    def read_system_msg(self):
        user_input_str = ''
        logger.info('*** Please enter the purpose for your AI model in sentence form. ***')
        logger.info('*** EX: You are a helpful assistant who understands data science. ***')
        for line in sys.stdin:
            user_input_str = f'{user_input_str} {line[:-1]}'
            user_input = input('*** Are you finished entering the purpose of this AI model? (y/n) ***')
            if user_input.lower() == 'y':
                break
        return user_input_str
    

    def read_tasks(self, i):
        user_input_str = ''
        logger.info('*** Please enter one or more tasks for your AI model in sentence form. ***')
        logger.info('*** Be as descriptive as possible in explaining the task. ***')
        logger.info('*** Press Enter after each task. ***')
        for line in sys.stdin:
            user_input_str = f'{user_input_str} {line[:-1]}'
            user_input = input('*** Are you finished entering tasks for this AI model? (y/n) ***')
            if user_input.lower() == 'y':
                break
        if i == 0:
            return [user_input_str]
        else:
            return user_input_str