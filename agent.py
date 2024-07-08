from openai import OpenAI

openai = OpenAI(api_key="[INSERT API KEY HERE")


def agent(prompt, sending):
    messages = [
                    {"role": "system", "content": f"You are a general chat bot"},
                    {"role": "system", "content": f"""you are just regular chatGPT"""},
                ]
    for send in sending:
        messages.append(send)
    print(messages)
    completion = openai.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=messages
            )
    return completion.choices[0].message.content
