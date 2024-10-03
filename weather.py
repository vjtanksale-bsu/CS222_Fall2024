import json
import ssl
from urllib.request import urlopen

def main():
    url = "https://api.weather.gov/alerts/active?area=TX"
    context = ssl._create_unverified_context()
    response = urlopen(url, context=context)
    weatherData = json.loads(response.read())
    print(len(weatherData["features"]))
    for event in weatherData["features"]:
        print(event["properties"]["headline"])

main()