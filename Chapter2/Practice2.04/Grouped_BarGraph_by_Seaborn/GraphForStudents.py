import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


studentsData = pd.DataFrame({
		"name" : ["Alexander", "Laura", "Daniel", "David", "Nikolas", "Karen", "Alma"],
		"gender" : ["male", "female", "male", "male", "male", "female", "female"],
		"class" : ["Math", "Math", "Science", "Ethics", "Ethics", "Science", "Ethics"],
		"GPA" : [92, 94, 95, 93, 91, 93, 98],
		"classnumbers" : [3, 5, 3, 4, 5, 4, 3]
		})
sns.catplot(x = "class", y = "GPA", hue = "gender", kind = "bar", data = studentsData)
plt.show()