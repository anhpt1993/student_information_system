from read_write import *

def choose_gender():
    while True:
        try:
            number = int(input("""
            Choose one of the following:
            1. Male
            2. Female
            3. Fluid

            Your choice: """))

            if 1 <= number <= 3:
                if number == 1:
                    gender = "Male"
                elif number == 2:
                    gender = "Female"
                else:
                    gender = "Fluid"
                return gender
                break
            else:
                print("Invalid input. Try again!!!\n")
        except ValueError:
            print("Invalid input. Try again!!!\n")


def input_score():
    while True:
        try:
            score = int(input("\tInput score (0-100): "))
            if 0 <= score <= 100:
                return score
                break
            else:
                print("Invalid input. Try again!!!\n")
        except ValueError:
            print("Invalid input. Try again!!!\n")

def generate_SN(data):
    if data == [""]:
        result = 1
    else:
        if data[-1] != "":
            STT = data[-1].split('|')
            result = int(STT[0].strip()) + 1
        else:
            STT = data[-2].split('|')
            result = int(STT[0].strip()) + 1
    return result

def add_info(data):
    my_str = None
    serial = generate_SN(data)
    print("+) Serial Number: ", serial)
    name = input("+) Name: ")
    print("+) Gender: ")
    gender = choose_gender()
    city = input("+) City: ")
    print("+) Theory: ", end = "\n")
    theory = input_score()
    print("+) Practice: ", end = "\n")
    practice = input_score()
    my_str = str(serial) + "|" + name + "|" + gender + "|" + city + "|" + str(theory) + "|" + str(practice)
    return my_str

def print_data(data, condition):
    header = "{:^5}|{:^20}|{:^10}|{:^20}|{:^10}|{:^10}"
    print(header.format("S/N", "FULL NAME", "GENDER", "CITY", "THEORY", "PRACTICE"))
    if data == [] or data == [""] or data == None:
        print("Nil")
    else:
        for element in data:
            temp = element.split("|")
            if temp == [""]:
                continue
            else:
                info = "{:^5}|{:^20}|{:^10}|{:^20}|{:^10}|{:^10}"
                if condition == "all":
                    print(info.format(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5]))
                elif condition == ">= 75":
                    if (int(temp[4]) + int(temp[5])) // 2 >= 75:
                        print(info.format(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5]))
                elif condition == "< 75":
                    if (int(temp[4]) + int(temp[5])) // 2 < 75:
                        print(info.format(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5]))
                else:
                    print("Nil")
            
if __name__ == "__main__":
    fi = "data.txt"
    fo = "data.txt"
    data = read_data(fi).split("\n")
    option = choose_option()
    if option == 1:
        data.append(add_info(data))
    print_data(data, "all")