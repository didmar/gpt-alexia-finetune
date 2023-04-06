import openai
import os

FINE_TUNED_MODEL = os.environ['FINE_TUNED_MODEL']

COMPLETION_SETTINGS = {
    # Max number of tokens (words) to generate
    'max_tokens': 200,

    # Lower temperature means less random, between 0 and 2
    # With 1, it starts to hallucinate
    'temperature': 0.0,

    # An alternative to sampling with temperature
    # top_p: 1,

    # Positive values penalize new tokens based on whether they appear in the text so far, 
    # increasing the model's likelihood to talk about new topics.
    # Number between -2.0 and 2.0.
    # Reasonable values for the penalty coefficients are around 0.1 to 1 
    'presence_penalty': 0.0,

    # Positive values penalize new tokens based on their existing frequency in the text so far, 
    # decreasing the model's likelihood to repeat the same line verbatim.
    # Number between -2.0 and 2.0. 
    'frequency_penalty': 0.1,
}

sample = {
    "url": "https://www.alexia.fr/questions/385307/tiers-digne-de-confiance-passeport.htm",
    "question": "Bonjour,\n Quand un enfant est confi\u00e9 \u00e0 un tiers digne de confiance. "
                "Peut-elle faire les d\u00e9marches pour avoir un passeport pour l\u2019enfant ?\n "
                "Merci de vos r\u00e9ponses\r",
    "answers": [
        {
            "avocat_name": "Maitre Philippe DE CAUNES",
            "answer": "Bonjour\n Le fait d'\u00eatre \"tiers digne de confiance\" ne suffira pas; "
                      "il faut une d\u00e9l\u00e9gation du titulaire de l'autorit\u00e9 parentale pour ce faire.\n "
                      "Vous pouvez aussi porter plainte pour menaces.\n "
                      "J'esp\u00e8re vous avoir \u00e9clair\u00e9.\n "
                      "Je vous remercie de bien vouloir cliquer sur le bouton vert \"Oui. Merci !\" ci-dessous afin d'indiquer que j'ai r\u00e9pondu \u00e0 votre question.\n "
                      "Bien cordialement",
            "is_best": True
        }
    ]
}
prompt = f"""Answer the question as truthfully as possible, and if you're unsure of the answer, say "Désolé, je ne sais pas".
Question: {sample['question']}.\n
Answer:"""

print('--------------- QUESTION ---------------\n')
print(sample['question'])
print('\n-------------- HUMAN ANSWER ---------------\n')
print(sample['answers'][0]['answer'])

# print('\n---------------- BASE AI ANSWER ----------------\n')
# resultBase = openai.Completion.create(
#     prompt=prompt,
#     model='curie',
#     **COMPLETION_SETTINGS)
# print(resultBase['choices'][0]['text'])

print('\n---------------- FINE-TUNED AI ANSWER ----------------\n')
resultFinedTune = openai.Completion.create(
    prompt=prompt,
    model=FINE_TUNED_MODEL,
    **COMPLETION_SETTINGS)
print(resultFinedTune['choices'][0]['text'])
