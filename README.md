# 🌤️ Python Weather & Data Insights API Tool

A robust Python utility script that connects to external RESTful APIs, fetches real-time data, processes JSON payloads, and extracts actionable insights.

---

### 🚀 Features:
* **API Integration:** Connects seamlessly to public REST APIs using the `requests` library.
* **JSON Processing:** Parses complex nested JSON responses and extracts key data fields.
* **Error Handling:** Implements robust status code validation and exception handling for failed requests.

---

### 🛠️ Built With:
* **Python 3.x** (`requests`, `json`)

---

### 💻 The Code:
```python
import requests
import json

def fetch_weather_data(city_name):
    api_url = "[https://api.open-meteo.com/v1/forecast?latitude=30.0444&longitude=31.2357&current_weather=true](https://api.open-meteo.com/v1/forecast?latitude=30.0444&longitude=31.2357&current_weather=true)"

    print(f"[*] Connecting to Weather API for Cairo...")
    
    try:
        response = requests.get(api_url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            current_weather = data.get("current_weather", {})
            
            print("\n[+] Data Fetched Successfully!")
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
💻 How to run:
Clone the repository:

Bash
git clone [https://github.com/moh21042002-tech/python-weather-api-tool.git](https://github.com/moh21042002-tech/python-weather-api-tool.git)
Install dependencies:

Bash
pip install requests
Run the script:

Bash
python main.py

if __name__ == "__main__":
    print("=== Python API Integration Utility ===")
    fetch_weather_data("Cairo")
