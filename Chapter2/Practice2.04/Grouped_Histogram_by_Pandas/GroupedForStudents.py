import pandas as pd
import matplotlib.pyplot as plt


studentsData = pd.DataFrame({
		"name" : ["Alexander", "Laura", "Daniel", "David", "Nikolas", "Karen", "Alma"],
		"gender" : ["male", "female", "male", "male", "male", "female", "female"],
		"class" : ["Math", "Math", "Science", "Ethics", "Ethics", "Science", "Ethics"],
		"GPA" : [92, 94, 95, 93, 91, 93, 98],
		"classnumbers" : [3, 5, 3, 4, 5, 4, 3]
		})
studentsData["GPA"].plot.hist()
plt.show()
