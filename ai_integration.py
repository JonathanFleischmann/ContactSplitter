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
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.2,
        max_tokens=1,
        seed=42,
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
    if gender != "M" and gender != "W":
        gender = "D"
    return gender


def get_age_for_name(name: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.2,
        seed=42,
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "Du bist ein System für die einschätzung vom Alter. Du bekommst einen Namen und sollst ein Alter schätzen. Gib dafür den Grund deiner Einschätzung, sowie das geschätzte Alter zurück. Beispiel für den Namen Prof. Dr. Markus Plümicke: 'Grund: Basierend auf dem Titel schätze ich das Alter auf 50 Jahre. Alter: 50'"
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Horst Lichter"
                    }
                ]
            },
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": "Grund: Basierend auf dem eher älter wirkenden Vornamen schätze ich das Alter auf 60 Jahre. Alter: 60"
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Prof. Dr. Olaf Herden"
                    }
                ]
            },
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": "Grund: Der Titel von Professor und Doktor, sowie der Vorname Olaf lassen auf eine eher ältere Person schätzen. Alter: 51"
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Laura Schleicher"
                    }
                ]
            },
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": "Grund: Der Vorname Laura deutet auf eine junge Erwachsene hin. Alter: 22"
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
    output = response.choices[0].message.content
    age = output.split("Alter: ")[1]
    return age

