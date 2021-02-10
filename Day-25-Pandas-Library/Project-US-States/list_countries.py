import pandas

data = pandas.read_csv('50_states.csv')
state_list = data.state
state_x_axis = data.x
state_y_axis = data.y

data_obj = {}
for x in range(len(state_x_axis)):
    data_obj[state_list[x]] = [state_x_axis[x], state_y_axis[x]]