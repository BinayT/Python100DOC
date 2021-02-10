def space_del(data):
    return data[:-1]


with open('weather_data.csv', mode="r") as data:
    initial_data_list = []
    for x in data.readlines():
        initial_data_list.append(x)

    data_header = initial_data_list[0].split(',')
    data_header[-1] = space_del(data_header[-1])
    initial_data_list[0] = data_header

    finished_data_list = []
    for x in range(1, len(initial_data_list)):
        seperated_data = initial_data_list[x].split(',')
        seperated_data[-1] = space_del(seperated_data[-1])
        individual_obj = {}
        for y in range(len(initial_data_list[0])):
            individual_obj[data_header[y]] = seperated_data[y]
        finished_data_list.append(individual_obj)

    print(finished_data_list)