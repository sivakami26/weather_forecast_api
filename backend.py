import requests
API_KEY = "6354b8ff60e34032eee6e83137ce6e30"

def get_data(place, forcast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"][:8*forcast_days]
    return filtered_data


if __name__ == "__main__":
    print(get_data("abc", 3))