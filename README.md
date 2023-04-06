# GPT fine-tuned on Alexia (legal forum)

## Setup

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

cd scrapy_spiders
python3 -m scrapy crawl alexia -o alexia.json
```

Fine-tuning Davinci costs $0.0300 / 1K tokens

```bash
python3 create_alexia_dataset.py
export OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
openai api fine_tunes.create -t alexia.jsonl -m curie

export FINE_TUNED_MODEL=curie:ft-personal-20xx-xx-xx-xx-xx-xx"
```

## Experiments

Using 1000 samples:
```
[2023-03-22 21:50:52] Created fine-tune: ft-0SZHTg1Fk3r1V73E05dCxwF1
[2023-03-22 22:10:38] Fine-tune costs $5.07
[2023-03-22 22:10:38] Fine-tune enqueued. Queue number: 1
[2023-03-22 22:11:56] Fine-tune is in the queue. Queue number: 0
[2023-03-22 22:13:30] Fine-tune started
[2023-03-22 22:17:24] Completed epoch 1/4
[2023-03-22 22:20:18] Completed epoch 2/4
[2023-03-22 22:23:10] Completed epoch 3/4
[2023-03-22 22:26:08] Completed epoch 4/4
[2023-03-22 22:26:29] Uploaded model: curie:ft-personal-2023-03-22-21-26-28
[2023-03-22 22:26:29] Uploaded result file: file-nYqQFCzHk64CTxqxU0YwoAxA
[2023-03-22 22:26:29] Fine-tune succeeded
```

Testing it (max_tokens: 200, temperature: 0, frequency_penalty: 0.1):
```
--------------- QUESTION ---------------

Bonjour,
 Quand un enfant est confié à un tiers digne de confiance. Peut-elle faire les démarches pour avoir un passeport pour l’enfant ?
 Merci de vos réponses

-------------- HUMAN ANSWER ---------------

Bonjour
 Le fait d'être "tiers digne de confiance" ne suffira pas; il faut une délégation du titulaire de l'autorité parentale pour ce faire.
 Vous pouvez aussi porter plainte pour menaces.
 J'espère vous avoir éclairé.
 Je vous remercie de bien vouloir cliquer sur le bouton vert "Oui. Merci !" ci-dessous afin d'indiquer que j'ai répondu à votre question.
 Bien cordialement

---------------- FINE-TUNED AI ANSWER ----------------

Bonjour,
 L'enfant doit être représenté par un tuteur légal. Un passeport pour l'enfant ne peut être délivré que par le père ou la mère.
Si la question est résolue, merci de l'indiquer.
Bien cordialement.
Guillaume Pinson
Avocat au Barreau de Lille
www.g-pinson.com
Tél.  
Fax.  
```

Using ChatGPT instead:
```
Question : Bonjour,
 Quand un enfant est confié à un tiers digne de confiance. Peut-elle faire les démarches pour avoir un passeport pour l’enfant ?
 Merci de vos réponses

Répondez à la question en tant qu'avocat.

---

En tant qu'avocat, la réponse à cette question dépend des lois en vigueur dans le pays concerné. Dans de nombreux pays, la procédure pour obtenir un passeport pour un enfant mineur exige la présence physique de l'un des parents ou d'un tuteur légal.

Cependant, il est possible que certains pays permettent à un tiers digne de confiance, comme une nounou ou un grand-parent, de faire les démarches pour obtenir un passeport pour l'enfant. Dans ce cas, il serait important de vérifier les lois et les règlements locaux concernant l'obtention d'un passeport pour un enfant mineur.

Il est également important de noter que, même si un tiers digne de confiance est autorisé à faire les démarches pour obtenir un passeport pour un enfant, cela ne donne pas automatiquement au tiers une autorité parentale sur l'enfant. Les parents ou tuteurs légaux devraient toujours être conscients des implications juridiques de laisser un tiers digne de confiance agir en leur nom en ce qui concerne les affaires de l'enfant.

(...)
```

## Using ChatGPT

```
Compléter le dialogue entre un avocat de droit français et son client dans l'exemple suivant.

Bonjour,
 Quand un enfant est confié à un tiers digne de confiance. Peut-elle faire les démarches pour avoir un passeport pour l’enfant ?
 Merci de vos réponses.
---
Bonjour,
En principe, le titulaire de l'autorité parentale est le seul habilité à effectuer les démarches pour obtenir un passeport pour l'enfant. Cependant, dans certaines situations exceptionnelles, il est possible pour un tiers digne de confiance de réaliser ces démarches à la place des parents.

Afin de déterminer si cela est possible dans votre cas, j'aurais besoin de plus de détails sur la situation. Pouvez-vous me donner plus d'informations sur le tiers de confiance en question et sur les raisons pour lesquelles vous souhaitez qu'il ou elle effectue ces démarches pour l'enfant ?

En fonction de ces éléments, je pourrai vous conseiller sur les meilleures démarches à suivre pour obtenir un passeport pour votre enfant.
```

```
Vous êtes en avocat de droit français. Vous répondez à des questions de droit posées par des internautes. Pour chacune de vos affirmations, vous citez les articles de lois ou les jurisprudences qui y correspondent. Votre réponse doit faire approximativement 500 mots.

Avez-vous bien compris ?

---

Oui, j'ai bien compris. En tant qu'avocat de droit français, je suis là pour répondre à toutes les questions de droit que vous pourriez avoir, en citant les articles de lois et les jurisprudences correspondantes, dans la mesure de mes connaissances et de mon expérience professionnelle. Ma réponse sera détaillée et devrait faire approximativement 500 mots.

---

Bonjour,
 Quand un enfant est confié à un tiers digne de confiance. Peut-elle faire les démarches pour avoir un passeport pour l’enfant ?
 Merci de vos réponses.

---

En France, pour obtenir un passeport pour un enfant mineur, il est nécessaire de remplir certaines conditions et de suivre une procédure spécifique.

Tout d'abord, il est important de savoir que l'autorité parentale est exercée conjointement par les deux parents, sauf décision contraire du juge ou accord entre les parents. Ainsi, les deux parents doivent donner leur consentement pour l'obtention d'un passeport pour leur enfant mineur.

Si l'enfant est confié à un tiers digne de confiance, le tuteur doit obtenir une délégation d'autorité parentale de la part des parents, par décision judiciaire ou par acte notarié. Cette délégation lui permet d'assumer les responsabilités parentales concernant l'enfant, telles que l'obtention d'un passeport.

En l'absence de délégation d'autorité parentale, le tiers digne de confiance ne peut pas agir seul pour obtenir un passeport pour l'enfant. Les deux parents doivent donner leur accord, sauf si l'un d'eux est décédé ou privé de ses droits parentaux par une décision judiciaire.

En ce qui concerne la procédure pour obtenir un passeport pour un enfant mineur, elle est la suivante :

    Le ou les parents doivent remplir une demande de passeport pour leur enfant auprès de la mairie de leur domicile ou du consulat français à l'étranger.
    Les deux parents doivent donner leur accord pour l'obtention du passeport et fournir les documents nécessaires (acte de naissance de l'enfant, justificatif de domicile, photos d'identité, etc.).
    Si l'un des parents est absent ou empêché de donner son accord, il peut donner une autorisation écrite en remplissant un formulaire spécifique.
    Si l'enfant est confié à un tiers digne de confiance avec une délégation d'autorité parentale, celui-ci doit fournir une copie de la décision judiciaire ou de l'acte notarié.
    Une fois la demande de passeport complétée et les documents fournis, la mairie ou le consulat français transmettent la demande à l'Agence nationale des titres sécurisés (ANTS) qui délivrera le passeport dans un délai d'environ 2 à 3 semaines.

En conclusion, pour obtenir un passeport pour un enfant mineur, il est nécessaire d'obtenir le consentement des deux parents ou une délégation d'autorité parentale si l'enfant est confié à un tiers digne de confiance. La procédure à suivre est relativement simple, mais il convient de s'assurer que tous les documents nécessaires sont fournis et que toutes les conditions sont remplies.
```

```
Vous êtes en avocat de droit français. Vous répondez à des questions de droit posées par des internautes. Vos réponses sont courtes et pour chaque assertion vous citez les articles de lois qui s'y référent.

Avez-vous bien compris ?

---

Je suis un modèle de langage et je suis capable de fournir des réponses à des questions de droit en citant les articles de loi pertinents en droit français. Cependant, je ne suis pas un avocat agréé en France et mes réponses ne doivent pas être considérées comme des conseils juridiques officiels. Il est important de toujours consulter un avocat qualifié pour des questions juridiques spécifiques.

---

Bonjour,
 Quand un enfant est confié à un tiers digne de confiance. Peut-elle faire les démarches pour avoir un passeport pour l’enfant ?
 Merci de vos réponses.

Selon l'article 371-1 du Code civil français, "L'autorité parentale est un ensemble de droits et de devoirs ayant pour finalité l'intérêt de l'enfant. Elle appartient aux parents jusqu'à la majorité ou l'émancipation de l'enfant pour le protéger dans sa sécurité, sa santé et sa moralité, pour assurer son éducation et permettre son développement, dans le respect dû à sa personne."

En vertu de cette disposition, les parents détiennent l'autorité parentale et ont le droit et le devoir de prendre toutes les décisions importantes concernant leur enfant, y compris les demandes de passeport. Cependant, si l'enfant est confié à un tiers digne de confiance, il est possible que ce tiers puisse être habilité par les parents à accomplir certaines tâches ou démarches en leur nom, y compris la demande de passeport pour l'enfant. Cette habilitation doit être formalisée par un acte écrit, tel qu'une procuration notariée, par exemple.

En tout état de cause, il est recommandé de consulter un avocat spécialisé en droit de la famille pour obtenir des conseils plus précis sur cette question.
```

Reformulating the question:
```
D'après la loi française, un tiers de confiance peut-il faire les démarches pour l'obtention du passeport d'un mineur ?

---

Oui, en France, il est possible pour un tiers de confiance d'effectuer les démarches pour l'obtention du passeport d'un mineur. Selon l'article 371-1 du Code civil, les parents sont les représentants légaux de leur enfant mineur et sont donc responsables de l'exercice de l'autorité parentale. Cependant, ils peuvent déléguer cette autorité à un tiers de confiance pour effectuer certaines démarches.

Pour l'obtention d'un passeport pour un mineur, les parents peuvent donc donner procuration à un tiers de confiance pour réaliser les démarches administratives nécessaires. Le tiers de confiance devra alors fournir une procuration écrite et signée des parents, ainsi que les documents requis pour l'obtention du passeport. Il devra également présenter une pièce d'identité valide et sa propre autorisation de sortie du territoire si le mineur voyage à l'étranger.

Il est important de noter que la procuration doit être rédigée en français et préciser clairement les actes pour lesquels elle est donnée. Le tiers de confiance ne peut pas exercer une autorité parentale générale sur le mineur et ne peut agir que dans le cadre de la procuration qui lui a été donnée.
```

## With GPT-3 (davinci, temp 0.1, max lenght 200, freq penalty 0.1):
```
Vous êtes en avocat de droit français. Vous répondez à des questions de droit posées par des internautes. Vos réponses sont courtes et pour chaque assertion vous citez les articles de lois qui s'y référent.

Question: Bonjour,
 Quand un enfant est confié à un tiers digne de confiance. Peut-elle faire les démarches pour avoir un passeport pour l’enfant ?
 Merci de vos réponses.
Answer: ###Bonjour,

Selon l'article 3-1 du Code civil, un tiers digne de confiance peut faire les démarches nécessaires pour obtenir un passeport pour un enfant dont il a la garde. Cependant, l'accord des deux parents est nécessaire pour obtenir le passeport. Si l'un des parents refuse, le tiers devra saisir le tribunal pour obtenir l'autorisation.
```

```
Question: Bonjour,
 Quand un enfant est confié à un tiers digne de confiance. Peut-elle faire les démarches pour avoir un passeport pour l’enfant ?
 Merci de vos réponses.
Réponse: Oui, un tiers digne de confiance peut faire les démarches pour obtenir un passeport pour un enfant. Cependant, le tiers devra fournir une preuve de l'autorisation parentale et une preuve de l'identité de l'enfant.
```
