import json
import spacy

nlp = spacy.load("en_core_web_sm")

with open("services.json", "r") as file:
    services = json.load(file)

def fetch_related_services(input_text):
   
    doc = nlp(input_text)
    
   
    keywords = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    
   
    related_services = []
    for service in services:
        if any(keyword.lower() in service["name"].lower() for keyword in keywords):
            related_services.append(service["name"])
    
    return related_services


input_text = "startup"
related_services = fetch_related_services(input_text)


if related_services:
    print("Related Services:")
    for service in related_services:
        print(f"- {service}")
else:
    print("No related services found.")