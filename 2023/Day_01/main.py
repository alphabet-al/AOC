def number_in_string(line):
    # list to store index position and value of first number
    # and index position and value of last number
    temp = []
    
    for char in line:
        if ord(char) >= 49 and ord(char) <= 57:
            temp.append(char)
            break

    for char in reversed(line):
        if ord(char) >= 49 and ord(char) <= 57:
            temp.append(char)
            break

    return temp

def word_to_numbers(line):
    wtn = {"one" : "o1e", 
        "two" : "t2o",
        "three" : "t3e",
        "four" : "f4r",
        "five" : "f5e",
        "six" : "s6x",
        "seven" : "s7n",
        "eight" : "e8t",
        "nine" : "n9e"
        }
    
    spelled_digit = False

    for key in wtn:
        if key in line:
            spelled_digit = True
        
    while spelled_digit:
        lowest_index = float('inf')

        for key in wtn:
            index = line.find(key)
            if index < lowest_index and index != -1:
                lowest_index = index
                lowest_index_and_value = (index, key)
            
        if lowest_index == float('inf'):
            return line

        lowest_spelled_number = lowest_index_and_value[1]

        line = line.replace(lowest_spelled_number, wtn[lowest_spelled_number])

        for key in wtn:
            if key in line:
                spelled_digit = True
                break
            else:
                spelled_digit = False
    return line     



if __name__ == "__main__":
    path = r'C:\AOC\2023\Day_01\data.txt'
    values = []

    with open(path, 'r') as file:
        data = file.read().splitlines()
 
    for line in data:
        new_line = word_to_numbers(line)
        numbers = number_in_string(new_line)
        values.append(int(numbers[0]+ numbers[1]))

    print(sum(values))

    
