#Author: Omar Darwish
#Assignment Title: Program 27
#Assignment Description: LAX DataSet
#Date Created: 11/27/2023

import pandas as pd
import matplotlib.pyplot as plt

file_name = input("Enter the CSV file name: ")
df = pd.read_csv(file_name)

average_delays = df['Delayed'].mean()
average_cancellations = df['Cancelled'].mean()
print(f"Average delays: {average_delays:.2f}")
print(f"Average cancellations: {average_cancellations:.2f}")

plt.figure(figsize = (10,6))
plt.plot(df['Month'], df['Delayed'], label = ['Delays'], marker = 'o')
plt.plot(df['Month'], df['Cancelled'], label = ['Cancellations'], marker = 'x')

plt.xlabel("Months", fontsize = 10)
plt.ylabel("Number of flights", fontsize = 10)
plt.title("Flight status at LAX", fontsize = 14)
plt.legend()

plt.savefig('output_fig.png')
plt.show()
