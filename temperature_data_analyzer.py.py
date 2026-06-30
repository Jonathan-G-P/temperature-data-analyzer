"""
Temperature Data Analyzer

Reads a CSV file containing temperature measurements,
computes statistics, detects warning and critical events,
generates reports, and plots the data.

Author: Jonathan G. P.
"""

import matplotlib.pyplot as plt
import pandas as pd
import math
data= pd.read_csv("data.CSV")
Sum=0

#region Data
data['Timestamp']= pd.to_datetime(data['Timestamp'])
TemperatureList= data['Temperature'].tolist()
HourList= pd.to_datetime(data['Timestamp']).dt.strftime("%H:%M").tolist()
Sort=data.sort_values(by='Temperature',ignore_index=True)
hour=pd.to_datetime(Sort['Timestamp']).dt.strftime("%H:%M")

Temperature= Sort['Temperature']
TempH= Temperature[len(Sort)-1]
hourH=hour[len(Sort)-1]
TempL= Temperature[0]
hourL=hour[0]
High=Sort.tail(1)
Low=Sort.head(1)
Promedio = round(data["Temperature"].mean(), 3)
for i in range(len(Temperature)):
    Sum+=(Temperature[i]-Promedio) **2
StandDev=round(math.sqrt(Sum/len(Temperature)),3)
#endregion

#region Alarm Report.txt and Stats.txt
Warnings=data[(data['Temperature']>35)&(data['Temperature']<40)]
Warnings=Warnings.reset_index()
Whours=pd.to_datetime(Warnings['Timestamp']).dt.strftime("%H:%M")
Alarm=data[data['Temperature']>40]
Alarm=Alarm.reset_index()
Ahours=pd.to_datetime(Alarm['Timestamp']).dt.strftime("%H:%M")
#endregion

#region Report.txt
with open("Stats.txt","w", encoding="utf-8") as archivo:
    archivo.write("Stats\n")
    archivo.write("Average=")
    archivo.write(str(Promedio))
    archivo.write("°C\n")
    archivo.write("Highest temperature: \n")
    archivo.write(hourH)
    archivo.write("->")
    archivo.write(str(TempH))
    archivo.write("°C\n")
    archivo.write("Lowest temperature: \n")
    archivo.write(hourL)
    archivo.write("->")
    archivo.write(str(TempL))
    archivo.write("°C\n")
    archivo.write("Standard deviation=")
    archivo.write(str(StandDev))
    archivo.write("\n")

with open("Alarm Report.txt","w", encoding="utf-8") as archivo:
    archivo.write("Warning Events\n")
    for i in range(len(Whours)):
        hour=Whours[i]
        temp=str(Warnings.loc[i,'Temperature'])
        archivo.write(hour)
        archivo.write("->")
        archivo.write(temp)
        archivo.write("°C\n")
    archivo.write("Alarm Events\n")
    for i in range(len(Ahours)):
        hour=Ahours[i]
        temp=str(Alarm.loc[i,'Temperature'])
        archivo.write(hour)
        archivo.write("->")
        archivo.write(temp)
        archivo.write("°C\n")
#endregion

#region Graph
plt.figure(figsize=(10, 4))
ax = plt.gca()
ax.axhspan(35, 40, color='yellow', alpha=0.25, label='Warning Zone')
ax.axhspan(40, max(TemperatureList) + 2, color='red', alpha=0.25, label='Critical Zone')
ax.plot(HourList, TemperatureList, color='black', linewidth=1.5)
ax.set_title('Temperatura')
ax.set_ylabel('°C', rotation=0, labelpad=20)
ax.set_xlabel('Hora')
ax.set_ylim(min(TemperatureList) - 1, max(TemperatureList) + 2)
ax.legend()
plt.xticks(rotation=65)
plt.tight_layout()
plt.show()
#endregion