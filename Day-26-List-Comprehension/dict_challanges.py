# I have to create a dictionary that takes each word in the given sentence and calculates the number
# of letters in each word.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_to_list = sentence.split(' ')
length_count_sentence = {key: len(key) for key in sentence_to_list}
print(length_count_sentence)