import os
import requests

def get_weather() -> None:
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("API_KEY is not found in the relevant media.")
        return

    city = "Paris"
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"Weather in {city}: {temp}°C, {condition}")
    except requests.exceptions.RequestException as e:
        print(f"I'll ask for mercy: {e}")
    except KeyError:
        print("The API input is invalid. Check API_KEY or parameters.")

if __name__ == "__main__":
    get_weather()

