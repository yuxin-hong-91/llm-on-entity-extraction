def find_max(num_list):
    max_num = num_list[0]
    for num in num_list:
        if num > max_num:
            max_num = num
    return max_num

import openai
import os
def chat_completion(user_msg):
    openai.api_key = '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'
    start_chat_log = '''Human: 你好，你今天过的怎么样
    AI: 不错，我今天有什么可以帮你的吗？
    '''
    prompt = f'{start_chat_log}Human: {user_msg}\nAI:'
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )
    story = response['choices'][0]['text']
    return story
print(chat_completion('第一性原理是什么'))


def get_answer(user_msg):
    if len(user_msg) != 0:
        return chat_completion(user_msg)
    else:
        return "Please enter a valid question"
