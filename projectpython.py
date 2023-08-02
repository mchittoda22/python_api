import requests

API_KEY = "b6907d289e10d714a6e88b30761fae22"
BASE_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly"

def get_weather_data(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data. Please try again.")
        return None

def get_temp(weather_data, target_date):
    for forecast in weather_data["list"]:
        if forecast["dt_txt"].startswith(target_date):
            return forecast["main"]["temp"]
    return None

def get_wind_speed(weather_data, target_date):
    for forecast in weather_data["list"]:
        if forecast["dt_txt"].startswith(target_date):
            return forecast["wind"]["speed"]
    return None

def get_pressure(weather_data, target_date):
    for forecast in weather_data["list"]:
        if forecast["dt_txt"].startswith(target_date):
            return forecast["main"]["pressure"]
    return None

def main():
    city = input("Enter the city name: ")
    weather_data = get_weather_data(city)
    if not weather_data:
        return

    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            temp = get_temp(weather_data, date)
            if temp is not None:
                print(f"Temperature on {date}: {temp}°C")
            else:
                print("Data not available ")

        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed(weather_data, date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")
            else:
                print("Data not available ")

        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure(weather_data, date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")
            else:
                print("Data not available")

        elif choice == "0":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

