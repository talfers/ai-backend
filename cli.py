from log_cli import logging
from config import Config
from terminal import Terminal
from ai import AI

logger = logging.getLogger('app.py')

config = Config()
terminal = Terminal()
ai = AI(config.openai_key)

exit_code = 0

system_msg = 'You are a helpful assistant who understands data science.'
tasks = [
    'Create a small dataset about total sales over the last year. The format of the dataset should be a data frame with 12 rows and 2 columns. The columns should be called "month" and "total_sales_usd". The "month" column should contain the shortened forms of month names from "Jan" to "Dec". The "total_sales_usd" column should contain random numeric values taken from a normal distribution with mean 100000 and standard deviation 5000. Provide Python code to generate the dataset, then provide the output in the format of a markdown table.'
]
tasks2 = [
    'Using the dataset you just created, write code to calculate the mean of the `total_sales_usd` column. Also include the result of the calculation.'
]

try:
    i = 0
    system_msg = terminal.read_system_msg()
    tasks = terminal.read_tasks(i)

    while True:
        try:
            r = ai.define_model(system_msg, tasks)
        except Exception as e: 
            logger.error(e)
        finally:
            i+=1
            response = ai.read_response(r)
            status_code = response['status_code']
            tasks.append(response['msg'])
            logger.info(response['msg'])
            user_input = input("Are you finished interacting with this AI model? (y/n)")
            if user_input.lower() == 'y':
                logger.info("Goodbye!")
                break
            new_tasks = terminal.read_tasks(i)
            tasks.append(new_tasks)


except Exception as e:
    exit_code = 1
    logger.error(f'Error in main app. Error: {str(e)}')


exit(exit_code)