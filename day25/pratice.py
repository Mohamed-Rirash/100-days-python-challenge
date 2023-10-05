# import csv
# with open("day25/002 weather-data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temp = []
    
#     for row in data:
#         if row[1] != "temp":
#             temp.append( int(row[1]))
#     print(temp)
import pandas as pd
data = pd.read_csv("day25/002 weather-data.csv")
# data_list = data["temp"].tolist()
# avg = sum(data_list)/len(data_list)
# print(avg)
# #in pandas
# print(data["temp"].mean())
# max_temp = data["temp"].max()

# print(data[data.temp == max_temp])

#fine monday row
# select the temp and multiply 9/5 + 32
monday = data[data.day == "Monday"]
temp = monday.temp
temp_fren = (temp*9/5)+32
print(temp_fren)
