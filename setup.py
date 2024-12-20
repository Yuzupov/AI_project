import openai, json
from datasets import load dataset
from openai import OpenAI

with open('apikey.txt', 'r') as file:
    OPENAI_API_KEY = file.read().strip() 

DEFAULT_SYSTEM_PROMPT = "You are an expert on scrum. You are a helpful and kind Scrum assistant."

# formats the dataset into the specific format needed for the JSONL file
def create_dataset(question, answer):
    return {
            "messages": [
                {"role": "system", "content": DEFAULT_SYSTEM_PROMPT},
                {"role": "user", "content": question},
                {"role": "assistant", "content": answer},
            ]
    }

# dataset used to train the model
dataset = load_dataset("nalmeida/agile_dataset_fusionado")

# formats the dataset from huggingface into JSONL format for OpenAI training
with open("data.jsonl", "w") as f:
    for example in dataset['train']:
        question = example['input']
        answer = example['text']
        f.write(json.dumps(create_dataset(question, answer)) + "\n")

client = OpenAI(api_key=OPENAI_API_KEY)

# Creates the file from which to fine-tune the model on
with open("data.jsonl", "rb") as f:
    response = client.files.create(file=f, purpose='fine-tune')
    print(response)

# Enters your file id here for training the model
fileId = response["id"]

# Train the model, can take a while
response = client.fine_tuning.jobs.create(
    training_file=fileId,
    model='gpt-3.5-turbo'
)
