def main(strings: list[str]):
    sum = 0
    for string in strings:
        first: str
        last: str

        first_found = False
        # get first digit as string
        for i in range(len(string)):
            if string[i].isdigit() and not first_found:
                first = string[i]
                first_found = True
            if first_found and string[i].isdigit():
                last = string[i]

        # put them together
        number = first + last
        # sum all values
        sum += int(number)
    print(sum)

if __name__ == "__main__":
    f = open("input1.txt", "r")
    main(f.readlines())
    f.close() 
