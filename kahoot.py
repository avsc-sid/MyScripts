import requests

id = input("Enter id\n>>> ")

kahoot_url = f"https://kahoot.it/rest/challenges/{id}/answers"

data = requests.get(kahoot_url).json()

def edwf(i):
    choices = i["question"]["choices"]
    for j in choices:
        if j["correct"] == True:
            return j["answer"]

for i in data["answers"]:
    correct = edwf(i)
    with open('words.txt', 'a') as f:
        f.write(correct + "\n")