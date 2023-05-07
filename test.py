import sys 

user_input_list = []
print('Please enter one or more tasks for your AI model in sentence form.')
print('Be as descriptive as possible in explaining the task.')
print('Press Enter after each task. Type "Exit" when you are done entering tasks.')
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    user_input_list.append(line)
print(user_input_list)

