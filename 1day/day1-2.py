def check_for_written_numbers(string):
    values = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for word in values:
        if string.startswith(word):
            return True
    return False

def return_written_as_str(string: str):
    values = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for word in values:
        if string.startswith(word):
            match word:
                case "one":   return "1"
                case "two":   return "2"
                case "three": return "3"
                case "four":  return "4"
                case "five":  return "5"
                case "six":   return "6"
                case "seven": return "7"
                case "eight": return "8"
                case "nine":  return "9"
    return ""
            
def get_substring(string, i):
    if i + 4 < len(string):
        return string[i:i+5]
    elif i + 3 < len(string):
        return string[i:i+4]
    elif i + 2 < len(string):
        return string[i:i+3]
    elif i + 1 < len(string):
        return string[i:i+2]
    elif i < len(string):
        return string[i:i+1]
    

def main(strings: list[str]):
    sum = 0
    for string in strings:
        first: str
        last: str

        first_found = False
        # get first digit as string
        for i in range(len(string)):
            substring = get_substring(string, i)

            if not first_found and string[i].isdigit():
                first = string[i]
                first_found = True
            elif not first_found and check_for_written_numbers(substring):
                # its a written number 
                first = return_written_as_str(substring)
                first_found = True

            if first_found and string[i].isdigit():
                last = string[i]
            elif first_found and check_for_written_numbers(substring):
                # its a written number 
                last = return_written_as_str(substring)
        # put them together
        number = first + last
        # sum all values
        sum += int(number)
    print("sum: ", sum)

if __name__ == "__main__":
    f = open("input1.txt", "r")
    main(f.readlines())
    f.close() 
