import requests
import json

def fetch_weather_data(city_name):
    api_url = "https://api.open-meteo.com/v1/forecast?latitude=30.0444&longitude=31.2357&current_weather=true"

    print(f"[*] Connecting to Weather API...")
    
    try:
        response = requests.get(api_url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            current_weather = data.get("current_weather", {})
            
            print("\n[+] Data Fetched & Processed Successfully!")
            print("-" * 30)
            print(f"Temperature : {current_weather.get('temperature')} °C")
            print(f"Wind Speed  : {current_weather.get('windspeed')} km/h")
            print(f"Wind Direction: {current_weather.get('winddirection')}°")
            print(f"Time        : {current_weather.get('time')}")
            print("-" * 30)
            
            return current_weather
        else:
            print(f"[-] Error: Received status code {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"[-] Connection Error: {e}")
        return None

if __name__ == "__main__":
    print("=== Python API Integration Utility ===")
    fetch_weather_data("Cairo")
