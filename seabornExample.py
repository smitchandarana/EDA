import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import csv

sns.set(style="darkgrid")
g=pd.read_csv("All - Form Responses 1.csv")

plot = sns.barplot(x=g["Undergrad Field"], y=g["Year"],
                   hue=g["Nationality"], palette="muted")
plot.set(ylim=(2012,2019))
plt.show()

