# I have to create a dictionary that takes each word in the given sentence and calculates the number
# of letters in each word.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_to_list = sentence.split(' ')
length_count_sentence = {key: len(key) for key in sentence_to_list}

# I am going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in
# degrees Celsius and converts it into degrees Fahrenheit.

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {key: (value*9/5)+32 for key, value in weather_c.items()}

# weather_f = {key: ((value * 9/5)+32) for (key, value) in weather_c.items()}

print(weather_f)