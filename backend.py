import requests

API_KEY = "b33fe39ea7e8da944336812f9a3d0636"

def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data

if __name__ == '__main__':
    print(get_data(place="Tokyo", forecast_days=3, kind="Temperatures"))