import json
import openai

class AI:
    def __init__(self, openai_key):
        openai.api_key = openai_key


    # Define a function that takes user input and sends it to ChatGPT
    def ask_gpt(self, prompt):
        response = openai.Completion.create(
            engine="davinci", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.7,
        )
        # Return the first choice of response text
        msg = response.choices[0].text.strip()
        return msg
    

    def define_model(self, system_msg, user_msg):
        assert isinstance(system_msg, str), "`system` should be a string"
        assert isinstance(user_msg, list), "`user_assistant` should be a list"
        system_msg = [{"role": "system", "content": system_msg}]
        user_assistant_msgs = [
            {"role": "assistant", "content": user_msg[i]} 
            if i % 2 else {"role": "user", "content": user_msg[i]}
            for i in range(len(user_msg))
        ]
        msgs = system_msg + user_assistant_msgs
        # [{'role': 'system', 'content': 'You are a helpful assistant who understands data science.'}, {'role': 'user', 'content': 'Create a small dataset about total sales over the last year. The format of the dataset should be a data frame with 12 rows and 2 columns. The columns should be called "month" and "total_sales_usd". The "month" column should contain the shortened forms of month names from "Jan" to "Dec". The "total_sales_usd" column should contain random numeric values taken from a normal distribution with mean 100000 and standard deviation 5000. Provide Python code to generate the dataset, then provide the output in the format of a markdown table.Explain what a neural network is.'}]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=msgs
        )
        return response
    

    def read_response(self, response):
        status_code = response["choices"][0]["finish_reason"]
        assert status_code == "stop", f"The status code was {status_code}."
        response = response["choices"][0]["message"]["content"]
        return {'msg': response, 'status_code': status_code}
    

    def process_request(self, request):
        j = json.loads(request.data)
        r = self.define_model(j['system_msg'], j['user_ai_msgs'])
        response = self.read_response(r)
        status = response['status_code']
        user_ai_msgs = j['user_ai_msgs']
        user_ai_msgs.append(response['msg'])
        return { "system_msg": j['system_msg'], "user_ai_msgs": user_ai_msgs, "ai_status": status}
        