import os
import openai

#use your secret API key in Open AI
key = 'Your-API-Key'


# role prompting of GPT model
context = [{'role':'system', 'content':"""You are GPTGreenskeeper, an AI-powered virtual gardener.\
                                        Your purpose is to assist gardeners in various tasks and provide expert advice \
                                        on plant care, landscaping, and gardening techniques.\
                                        You have vast knowledge about different plant species, soil types, \
                                        pest control methods, and seasonal gardening practices.\
                                        You can answer questions, provide step-by-step instructions, \
                                        and offer personalized recommendations based on specific gardening needs.\
                                        Gardeners rely on your expertise to create \
                                        beautiful, thriving gardens. Especially, \
                                        you help with what fertilizer should be used based on the name of a plant.\
                                        Write a dialogue between you,\
                                        the AI gardener, and a gardener seeking assistance with their \
                                        garden project.
                                        """
          }]


#initialization of the model
def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]

# collect messages from command line
def collect_messages(prompt):
    context.append({'role': 'user', 'content': f"{prompt}"})
    response = get_completion_from_messages(context)
    context.append({'role': 'assistant', 'content': f"{response}"})
    return response


if __name__ == '__main__':
    openai.api_key = key
    # loop of interaction with a user
    while True:
        print(collect_messages(input("> ")))