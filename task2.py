import requests
import matplotlib.pyplot as plt
from datetime import datetime

# === CONFIGURATION ===
API_KEY = 'ba682315dffd45c4975124145253107'   
CITY = 'Chennai'                
DAYS = 5

# === API REQUEST ===
url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={CITY}&days={DAYS}"
response = requests.get(url)
data = response.json()

# === PARSE WEATHER DATA ===
dates = []
temps = []

for day in data['forecast']['forecastday']:
    date_str = day['date']                         # e.g., "2025-08-01"
    avg_temp = day['day']['avgtemp_c']             # Average temperature in °C

    date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    dates.append(date_obj)
    temps.append(avg_temp)

# === PLOT THE DATA ===
plt.figure(figsize=(10, 5))
plt.plot(dates, temps, marker='o', linestyle='-', color='blue')

plt.title(f'{DAYS}-Day Temperature Trend in {CITY}')
plt.xlabel('Date')
plt.ylabel('Average Temperature (°C)')
plt.grid(True)
plt.tight_layout()
plt.show()
