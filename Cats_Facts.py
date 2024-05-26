#ziskani faktu z API
import requests
response = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=10&status=verified')
data = response.json()

# vyber textovych dat
for item in data:
    facts = item["text"]
    print(facts)

# vytvoreni seznamu faktu
list_of_facts = []
for i in data:
    fact = i["text"]
    list_of_facts.append(str(fact))
    print(list_of_facts)
  
# vytvoreni souboru a ocislovani
with open('kocici_facta.json', mode='w', encoding='utf-8') as output_file:
    for index, value in enumerate(list_of_facts,1):
         print("{}. {}".format(index, value), file=output_file) 
         
# dotaz jeste jednou s vyjimkou na timeout """
url = "https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=10&status=verified"
try:
    response = requests.get(url, timeout=3)
    data = response.json()
    for item in data:
        facts = item["text"]
    list_of_facts = []
    for i in data:
        fact = i["text"]
        list_of_facts.append(str(fact))
        print(list_of_facts)
    with open('kocici_facta.json', mode='a', encoding='utf-8') as output_file:
        for index, value in enumerate(list_of_facts,11):
            print("{}. {}".format(index, value), file=output_file)
except Exception as Err: 
    print(f"Musis byt trpelivejsi:{Err}")
 


        

