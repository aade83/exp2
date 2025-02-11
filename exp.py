import json
import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Load services data from services.json
with open("services.json", "r") as file:
    services = json.load(file)

# Function to fetch related services, including child services for parent services and vice versa
def fetch_related_services(input_text):
    doc = nlp(input_text)
    
    # Extract keywords from input text
    keywords = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    
    related_services = []
    parent_services = set()  # To store parent services and avoid duplicates
    child_services = set()   # To store child services for parents found
    
    # Iterate through the services to find matches based on input
    for service in services:
        # Check if service name matches any keyword
        if any(keyword.lower() in service["name"].lower() for keyword in keywords):
            related_services.append(service["name"])

            # If the service is level 2 or 3, include its parent service if it exists
            if service["level"] == 2 or service["level"] == 3:
                parent_service_id = service["parentService"]
                
                # Find the parent service based on the parentService ID
                parent_service = next((s for s in services if s["_id"] == parent_service_id), None)
                if parent_service and parent_service["name"] not in related_services:
                    related_services.append(parent_service["name"])
                    parent_services.add(parent_service["_id"])
            
            # If the service is a parent (level 1), include its child services
            if service["level"] == 1:
                for child_service in services:
                    if child_service["parentService"] == service["_id"]:
                        if child_service["name"] not in related_services:
                            related_services.append(child_service["name"])
                        child_services.add(child_service["_id"])

    return related_services

# Input text for service search
input_text = "AGRICULTURAL PRODUCT MARKETING"

# Fetch related services
related_services = fetch_related_services(input_text)

# Display the results
if related_services:
    print("Related Services:")
    for service in related_services:
        print(f"- {service}")
else:
    print("No related services found.")
