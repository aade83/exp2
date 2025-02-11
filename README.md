# Related Services Search Project

This project allows you to search for services based on input text. It uses a natural language processing (NLP) approach to match keywords from the input and return related services. The system also returns **parent services** when a **child service** is found, and **child services** when a **parent service** is searched.

# Features

- **Search for related services** based on user input.
- Automatically include **parent services** when searching for child services (level 2 or level 3).
- Automatically include **child services** when searching for parent services (level 1).

# Requirements

To run this project, you need:

- Python 3.x
- `spaCy` library
- `en_core_web_sm` spaCy model
- `JSON` data file with services

# Install Dependencies:

1. **Install the required Python dependencies:**

```bash
pip install spacy
```
2.**Download the spaCy model:**
```bash
python -m spacy download en_core_web_sm
```

# Usage
Please make sure you have the **services.json** file with the necessary service data in the same directory as the script.

**Run the script:**
```
python your_script_name.py
```
The script will take an input search query and return a list of related services, including their parent and child services where applicable.

**Example Input:**
```
"AGRICULTURAL PRODUCT MARKETING"
```
**Example Output:**
```
Related Services:
- AGRICULTURAL PRODUCT MARKETING
- AGRICULTURE AND ENVIRONMENTAL SUSTAINABILITY
```
# Contributing
Feel free to fork this project and create a pull request with your improvements.

# License
This project is licensed under the MIT License
