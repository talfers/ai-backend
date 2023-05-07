from log import logging
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
tasks2 = 'Using the dataset you just created, write code to calculate the mean of the `total_sales_usd` column. Also include the result of the calculation.'

try:    
    # TEST REQUEST #1
    try:
        r = ai.define_model(system_msg, tasks)
        print("ORIGINAL TASKS", tasks)
    except Exception as e: 
        logger.error(e)
    finally:
        response = ai.read_response(r)
        status_code = response['status_code']
        tasks.append(response['msg'])
        print("*** RETURN DATA #1 ***", { "system_msg": system_msg, "user_ai_msgs": tasks })

    # TEST REQUEST #2
    try:
        tasks.append(tasks2)
        r = ai.define_model(system_msg, tasks)
    except Exception as e: 
        logger.error(e)
    finally:
        response = ai.read_response(r)
        status_code = response['status_code']
        msg2 = response['msg']
        tasks.append(msg2)
        print("*** RETURN DATA #2 ***", { "system_msg": system_msg, "user_ai_msgs": tasks })


except Exception as e:
    exit_code = 1
    logger.error(f'Error in main app. Error: {str(e)}')


exit(exit_code)