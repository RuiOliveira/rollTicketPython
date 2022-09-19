class Ticket:
    # Input values
    input = input("Enter a valid ticket number:\n")

    if not input.isdecimal():
        print("Input ticket does not contains only number!")
        quit()

    if len(input) != 6:
        print("Input ticket should have length of six!")
        quit()

    lstString = list(input)

    #split array and compare two pieces
    intList = list(map(int, lstString))
    length = len(intList)

    middle_index = length // 2

    first_half = intList[:middle_index]
    second_half = intList[middle_index:]

    #sort and compare arrays
    first_half.sort()
    second_half.sort()

    if first_half != second_half:
        print("The first three digits are not the same of last three digits!")
        quit()

    #calculate sum
    sum = 0
    for value in first_half:
        sum += value

    print("Your ticket id is: " + str(sum))