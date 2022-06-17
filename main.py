import re
pattern_1 = r".*2[2-4]/Mar/2009:[0-2][1-3]:[4-5][5-6]:[2-4][3-9].*\"GET.*\"[4-4][0-9][0-9]"
input_file = open("access.log.txt", mode='r')
my_log_file = input_file.read()
result = re.findall(pattern_1 , my_log_file)
print(result)
print(len(result))

