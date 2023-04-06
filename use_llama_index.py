from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader

# documents = SimpleDirectoryReader('code-civil', recursive=True).load_data()
# index = GPTSimpleVectorIndex(documents)  # Total embedding token usage: 361487 tokens
# index.save_to_disk('code-civil.json')

# load from disk
index = GPTSimpleVectorIndex.load_from_disk('code-civil.json')

def query(index, question):
    r = index.query("Un tiers de confiance peut-il faire les démarches pour obtenir un passeport pour un enfant ?")
    print('=====( SOURCES USED )==========\n')
    for source in r.source_nodes:
        print(f'[{source.similarity:.2f}] {source.source_text}\n')
    print('\n=====( ANSWER )================\n')
    print(r.response)

query(index, "Un tiers de confiance peut-il faire les démarches pour obtenir un passeport pour un enfant ?")
# =====( SOURCES USED )==========

# [0.85] Article 374-1----Le tribunal qui statue sur l'établissement d'une filiation peut 
# décider deconfier provisoirement l'enfant à un tiers qui sera chargé de 
# requérirl'organisation de la tutelle.


# =====( ANSWER )================


# Non, un tiers de confiance ne peut pas faire les démarches pour obtenir un passeport 
# pour un enfant. Seul un parent ou un tuteur légal peut faire les démarches pour obtenir 
# un passeport pour un enfant.

# print(index.query("Quels articles expliquent si un tiers de confiance peut-il faire les démarches pour obtenir un passeport pour un enfant ?"))
# ANSWER:
# Les articles 373-4 et suivants expliquent que lorsqu'un enfant est confié à un tiers, 
# la personne à qui l'enfant a été confié peut accomplir tous les actes usuels relatifs 
# à sa surveillance et à son éducation, y compris les démarches pour obtenir un passeport 
# pour l'enfant.