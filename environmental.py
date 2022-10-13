from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

pressure = sense.get_pressure()
temp = sense.get_temperature()
humidity = sense.get_humidity()

pressure = round(pressure, 1)
temp = round(temp, 1)
humidity = round(humidity, 1)

environmental = "temperature: " + str(temp) + "humidity: " + str(humidity) + "pressure: " + str(pressure)

sense.show_message(environmental)
