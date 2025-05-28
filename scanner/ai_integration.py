from openai import OpenAI
import os

def get_api_key():
    # get the API key from a file
    with open("api_key.txt", "r") as f:
        api_key = f.read().strip()
    return api_key


API_KEY = get_api_key()
client = OpenAI(api_key=API_KEY)

def get_gender_for_name(name: str) -> str:
    print("name:"+ name)    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.2,
        max_tokens=1,
        seed=4216516354,
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "Du bist ein System für die einschätzung von Geschlechtern. Du bekommst einen Namen und gibst mir das Geschlecht zurück. M für männlich, W für weiblich und X für unbekannt oder unsicher."
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Laura"
                    }
                ]
            },
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": "W"
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Christian"
                    }
                ]
            },
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": "M"
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Toni"
                    }
                ]
            },
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": "X"
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": name
                    }
                ]
            }
        ],
    )
    gender = response.choices[0].message.content
    print(gender)
    if gender != "M" and gender != "W":
        gender = "D"
    if gender == "M":
        return "Männlich"
    if gender == "W":
        return "Weiblich"
    if gender == "D":
        return "Divers"
    return gender

