class  WeatherSystem:
    def __init__(self, city) -> None:
        self.temperature = None
        self.weather = None
        self.city = city
        self.weather_list = dict()
    
    def query(self, weather_list, tmp_units = 'celsius'):
        self.weather_list = weather_list
        if not self.city not in weather_list:
            self.temperature = self.weather_list[self.city]['temperature']
            self.weather = self.weather_list[self.city]['weather']
        else:
            return False
        if not self.weather_list[self.city]['temperature units'] != tmp_units:
            return self.temperature, self.weather
        else:
            if tmp_units == 'celsius':
                return self.fahrenheit_to_celsius(), self.weather
            elif tmp_units == 'fahrenheit':
                return self.celsius_to_fahrenheit(), self.weather
    
    def set_city(self, city):
        self.city = city

    def celsius_to_fahrenheit(self):
        return (self.temperature * 9/5) + 32

    def fahrenheit_to_celsius(self):
        return (self.temperature - 32) * 5 / 9