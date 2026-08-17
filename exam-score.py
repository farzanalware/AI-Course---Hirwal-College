import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Histogram 
data = np.random.normal(70,10,1000)
plt.hist(data, bins = 30 , edgecolor="Red",
alpha=0.7, color="#306998")
plt.title("Exams Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.axvline(data.mean(), color ="Red",
            linestyle="--", lable ="Mean")
plt.legend()
plt.show()


