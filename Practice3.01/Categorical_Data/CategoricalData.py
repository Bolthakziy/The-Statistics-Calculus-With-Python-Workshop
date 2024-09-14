import pandas as pd
import matplotlib.pyplot as plt


weatherData = {
	"weather" : ["Windy", "Cloudy", "Rainy", "Rainy", "Windy", "Sunny", "Rainy"],
	"temperature" : [23, 27, 18, 16, 22, 30, 17]
		}
weatherEncoding = pd.DataFrame(weatherData)
weatherEncoding["weather_encoded"] = weatherEncoding["weather"].map({"Windy" : 0, "Cloudy" : 1, "Sunny" : 2, "Rainy" : 3})
print(weatherEncoding)
print()
print()

weatherDummy = pd.get_dummies(weatherEncoding["weather"])
print(weatherDummy)
print()
print()

weatherEncoding.value_counts().plot.pie(autopct = "%1.1f%%")
plt.ylabel("")
plt.show()
