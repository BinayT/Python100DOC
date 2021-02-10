import pandas

# def space_del(data):
#     return data[:-1]
#
#
# with open('weather_data.csv', mode="r") as data:
#     initial_data_list = []
#     for x in data.readlines():
#         initial_data_list.append(x)
#
#     data_header = initial_data_list[0].split(',')
#     data_header[-1] = space_del(data_header[-1])
#     initial_data_list[0] = data_header
#
#     finished_data_list = []
#     for x in range(1, len(initial_data_list)):
#         seperated_data = initial_data_list[x].split(',')
#         seperated_data[-1] = space_del(seperated_data[-1])
#         individual_obj = {}
#         for y in range(len(initial_data_list[0])):
#             individual_obj[data_header[y]] = seperated_data[y]
#         finished_data_list.append(individual_obj)
#     print(finished_data_list)

# import csv
#
# with open('weather_data.csv', mode="r") as data_file:
#     data = csv.reader(data_file)
#     lista = []
#     for row in data:
#         if row[1] != 'temp':
#             lista.append(int(row[1]))
#     print(lista)

# data = pandas.read_csv('weather_data.csv')
# print(data[data.temp == data.temp.max()])
# list_temp = data['temp'].to_list()
# sum_of_temps = 0
#
# for x in list_temp:
#     sum_of_temps += x
#
# print(round(sum_of_temps/len(list_temp), 2))

# print(data[data.day == 'Monday'].temp*(9/5)+32)

# data_dict = {
#     'students': ['Student1', 'Student2', 'Student3'],
#     'scores': [8, 6, 2]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv('students_dict.csv')

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
data_gray = data[data['Primary Fur Color'] == 'Gray']
data_black = data[data['Primary Fur Color'] == 'Black']
data_cinnamon = data[data['Primary Fur Color'] == 'Cinnamon']

list_data_colors = {'Fur Color': ['grey', 'black', 'red'], 'Count': [len(data_gray), len(data_black),
                                                                     len(data_cinnamon)]}

data_conversion = pandas.DataFrame(list_data_colors)
print(data_conversion)
data_conversion.to_csv('squirrels_color.csv')
