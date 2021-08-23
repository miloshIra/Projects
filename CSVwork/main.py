# import pandas
# #"""WORKING IN PANDAS .. NOT CSV SO MUCH"""
#
# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperature = []
# #     print(data)
# #     for row in data:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# #     print(temperature)
#
# data = pandas.read_csv("weather_data.csv")
# #     print(data["temp"])
# # data_dict = data.to_dict()
# #
# # temp_list = data["temp"].to_list()
# # print(len(temp_list))
# # print(temp_list)
# #
# # print(data["temp"].max())
# #
# # # Get Data in Column
# #
# # print(data["day"])
# # print(data.day)
#
# # Get Data in Rows! << Kinda harder ...
#
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(int(monday.temp) * 9/5 + 32)
#
# # Create DataFrame from Scratch
#
# date_dict = {
#     "students": ["Amy", "James", "Ira"],
#     "scores" : [77, 21, 22]
# }
#
# date = pandas.DataFrame(date_dict)
# print(date)
#
# date.to_csv("new_data.csv")
#
#
#

import pandas

sq_data = pandas.read_csv("Squirrel_Data.csv")

grey_squirrels_count = len(sq_data[sq_data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(sq_data[sq_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(sq_data[sq_data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(black_squirrels_count)
print(red_squirrels_count)

data_dict = {
    "Fur color" : ["Gray,", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Sq_count.csv")