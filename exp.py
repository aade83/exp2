import json
import spacy


nlp = spacy.load("en_core_web_sm")


with open("services.json", "r") as file:
    services = json.load(file)


def fetch_related_services(input_text):
    doc = nlp(input_text)
    
  
    keywords = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    
    related_services = []
    parent_services = set()  
    child_services = set()   
    
   
    for service in services:
        
        if any(keyword.lower() in service["name"].lower() for keyword in keywords):
            related_services.append(service["name"])

           
            if service["level"] == 2 or service["level"] == 3:
                parent_service_id = service["parentService"]
                
                
                parent_service = next((s for s in services if s["_id"] == parent_service_id), None)
                if parent_service and parent_service["name"] not in related_services:
                    related_services.append(parent_service["name"])
                    parent_services.add(parent_service["_id"])
            
           
            if service["level"] == 1:
                for child_service in services:
                    if child_service["parentService"] == service["_id"]:
                        if child_service["name"] not in related_services:
                            related_services.append(child_service["name"])
                        child_services.add(child_service["_id"])

    return related_services


input_text = "entertainment"


related_services = fetch_related_services(input_text)


if related_services:
    print("Related Services:")
    for service in related_services:
        print(f"- {service}")
else:
    print("No related services found.")
