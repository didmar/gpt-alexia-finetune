import json
import tiktoken

# MODEL_NAME = 'text-davinci-003'
MODEL_NAME = 'text-curie-001'
MAX_SAMPLES = 1000

TRAINING_PRICE_PER_1K_TOKENS = {
    'text-davinci-003': 0.03,
    'text-curie-001': 0.003,
}
NB_TRAINING_EPOCHS = 4

def num_tokens_from_string(string: str, model_name: str) -> int:
    """
    Returns the number of tokens in a text string.
    """
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

nb_samples = 0
num_tokens = 0

with open('scrapy_spiders/alexia.json', 'r') as f, open('alexia.jsonl', 'w') as g:
    for line in f:
        if line.startswith('{'):
            data = json.loads(line.rstrip().rstrip(','))

            question = data['question']

            for answer in data['answers']:
                if answer['is_best']:
                    completion = answer['answer']
                    break
            else:
                completion = data['answers'][0]['answer']

            sample = {"prompt": f"Question: {question}.\nAnswer: ", "completion": completion}
            g.write(json.dumps(sample)+'\n')
            nb_samples += 1
            num_tokens += num_tokens_from_string(sample['prompt'] + sample['completion'], MODEL_NAME)

            if nb_samples >= MAX_SAMPLES:
                break

print(f'Number of tokens: {num_tokens}\nPrice: ${num_tokens * NB_TRAINING_EPOCHS * TRAINING_PRICE_PER_1K_TOKENS[MODEL_NAME] / 1000:.2f}')
