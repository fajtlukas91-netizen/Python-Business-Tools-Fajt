# Automated Outreach System (Prospector)
# This script generates personalized messages for potential clients.

companies = [
    {"person": "Peter", "company": "Libeň Car Sales", "industry": "automotive"},
    {"person": "Jane", "company": "Tower Flowers", "industry": "flower delivery"},
    {"person": "Mark", "company": "Top Carpenter", "industry": "custom furniture"},
    {"person": "Stephen", "company": "Painters Ltd.", "industry": "house painting"},
    {"person": "Lukas", "company": "Programo", "industry": "web development"}
]

for business in companies:
    # Extracting data from dictionaries into variables
    name = business["person"]
    company_name = business["company"]
    focus = business["industry"]
    
    # Building the personalized message
    greeting = f"Hi {name}, I came across your company, {company_name}."
    offer = f"I am really impressed by your work in {focus} and would love to offer you my automation services."
    
    # Printing the result to the console
    print(greeting)
    print(offer)
    print("Let me know if you are interested in a quick chat about a potential collaboration.")
    print("-" * 50)
