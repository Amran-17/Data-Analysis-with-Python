import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("profit.csv.csv")
data.plot(kind= "line", x="YearsExperience", y="Salary", marker='+')
#data.plot(kind="hist")
#data.plot(kind="line")
plt.show()