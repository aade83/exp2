import json
import spacy


nlp = spacy.load("en_core_web_sm")


json_data = '''
[
  {
    "_id": "5d244676d4b798333898a6a0",
    "name": "AGRICULTURE AND ENVIRONMENTAL SUSTAINABILITY",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Agriculture%20and%20Environmental%20Sustainability.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "1f5ab32dcd28334c98e1b650",
    "name": "AGRICULTURE AND FARMING CONSULTING",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Agriculture%20and%20Farming%20Consulting.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "cf799a13451043a1dda75fe0",
    "name": "ARTS AND CREATIVE INDUSTRY CONSULTING",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Arts%20and%20Creative%20Industry%20Consulting.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "83165dec27050a924c1e8c8b",
    "name": "ASTROLOGY AND SPIRITUAL CONSULTATION",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Astrology%20and%20Spiritual%20Consultation.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "a61f4f397a560df2e1015ce4",
    "name": "BUSINESS AND STARTUP CONSULTATION",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Business%20and%20Startup%20Consultation.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "7c7a331e223c3d46a266b9a1",
    "name": "CYBERSECURITY CONSULTATION",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Cybersecurity%20Consultation.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "b23241f6eff29e5fbb0f5279",
    "name": "E-COMMERCE AND RETAIL STRATEGY",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/E-commerce%20and%20Retail%20Strategy.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "88d37639e7224ac79ba5db48",
    "name": "EDUCATION AND CAREER COUNSELING",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Education%20and%20Career%20Counseling.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "713ddfbc75861383dc5296f2",
    "name": "EVENT PLANNING AND MANAGEMENT",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Event%20Planning%20and%20Management.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "85af571fa3feae60efc5f511",
    "name": "FAN TALK",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Fan%20Talk.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "42ae9c2606d8f130ee3655e4",
    "name": "FINANCIAL AND INVESTMENT CONSULTATION",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Financial%20and%20Investment%20Consultation.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "fa3fd16a802e790ed5d8eee3",
    "name": "FITNESS AND PERSONAL TRAINING CONSULTATION",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Fitness%20and%20Personal%20Training%20Consultation.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "82eddf076aba4dade708b157",
    "name": "HOME IMPROVEMENT AND REAL ESTATE ADVISORY",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Home%20Improvement%20and%20Real%20Estate%20Advisory.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "762ade794a28713f0afb34cb",
    "name": "HUMAN RESOURCES CONSULTATION",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Human%20Resources%20Consultation.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "39f85c0347723f4512b7d1c8",
    "name": "INSURANCE AND RISK MANAGEMENT CONSULTING",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Insurance%20and%20Risk%20Management%20Consulting.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "a304a8a41ba21036e8587c62",
    "name": "LEADERSHIP AND EXECUTIVE COACHING",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Leadership%20and%20Executive%20Coaching.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "fcefe208e9cf68accb5601f9",
    "name": "LEGAL",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Legal.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "69eb0235f952a6e5b260538a",
    "name": "LIFE COACHING AND PERSONAL DEVELOPMENT",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Life%20Coaching%20and%20Personal%20Development.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "f0263c12016a9cb3855dda8f",
    "name": "MARKETING AND ADVERTISING CONSULTATION",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Marketing%20and%20Advertising%20Consultation.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "7398ef50594b4c40e09063c8",
    "name": "NON-PROFIT AND SOCIAL ENTERPRISE CONSULTING",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Non-Profit%20and%20Social%20Enterprise%20Consulting.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "f3356fa0e2a598b8e5edcb9f",
    "name": "PET CARE AND VETERINARY CONSULTING",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Pet%20Care%20and%20Veterinary%20Consulting.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "fd1c8a30da81f099daedf3d1",
    "name": "PRODUCT MANAGEMENT AND DEVELOPMENT",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Product%20Management%20and%20Development.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "4b829976b47dcdbddb815e70",
    "name": "PUBLIC RELATIONS AND CORPORATE COMMUNICATION",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Public%20Relations%20and%20Corporate%20Communication.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "daa938e91584e430a5b6622d",
    "name": "PUBLIC SECTOR AND GOVERNMENT CONSULTING",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Public%20Sector%20and%20Government%20Consulting.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "485419d8d8677c0bc7030bf4",
    "name": "REAL ESTATE CONSULTATION",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Real%20Estate%20Consultation.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "7577bdb139c5191ecebf154e",
    "name": "SOCIAL MEDIA AND INFLUENCER MARKETING CONSULTATION",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Social%20Media%20and%20Influencer%20Marketing%20Consultation.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "060d8fbdd450e93a86c2736e",
    "name": "SUSTAINABILITY AND ENVIRONMENTAL CONSULTING",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Sustainability%20and%20Environmental%20Consulting.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "2155ba45fc780b642c8e49a5",
    "name": "TAX CONSULTATION",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Tax%20Consultation.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "ff78553de6e4f2ce93f8473a",
    "name": "TECHNOLOGY AND IT CONSULTATION",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Technology%20and%20IT%20Consultation.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "42466e5ada68eb59789e973c",
    "name": "TRAVEL AND HOSPITALITY CONSULTATION",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Travel%20and%20Hospitality%20Consultation.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "9fab053b6e450fec26040daa",
    "name": "WRITING AND CONTENT CREATION",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Writing%20and%20Content%20Creation.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "5763e7ac28622586854af9aa",
    "name": "WRITING AND LANGUAGE SERVICES",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Writing%20and%20Language%20Services.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  },
  {
    "_id": "c187b7297473c43503f623d5",
    "name": "YOGA AND WELLNESS CONSULTATION",
    "icon": "https://expertabackend.s3.ap-south-1.amazonaws.com/services/icons/Yoga%20and%20Wellness%20Consultation.svg",
    "level": 1,
    "parentService": null,
    "info": "This is a sample service description."
  }
]
'''


services = json.loads(json_data)

def fetch_related_services(input_text):
    
    doc = nlp(input_text)
    
   
    keywords = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    

    related_services = []
    for service in services:
        if any(keyword.lower() in service["name"].lower() for keyword in keywords):
            related_services.append(service["name"])
    
    return related_services


input_text = "technology"
related_services = fetch_related_services(input_text)


if related_services:
    print("Related Services:")
    for service in related_services:
        print(f"- {service}")
else:
    print("No related services found.")