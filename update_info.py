from add_info import print_data, choose_gender, input_score
from read_write import *

def choose_SN(data, text):
    while True:
        try:
            SN = int(input(text))
            for element in data:
                if int(element.split("|")[0].strip()) == SN:
                    return SN
                    break
            else:
                print("Invalid Serial Number. Try again!!!\n")
        except ValueError:
            print("Invalid Serial Number. Try again!!!\n")

def choose_correct_info():
    while True:
        try:
            choice = int(input("""
            Which information that you want to correct?:
            1. Full Name
            2. Gender
            3. City
            4. Grade of Theory
            5. Grade of Practice
            
            => Your choice: """))
            if 1 <= choice <= 5:
                return choice
                break
            else:
                print("Invalid input. Try again!!!\n")
        except ValueError:
            print("Invalid input. Try again!!!\n")

def correct_info(data, index, choice, correct_data):
    temp_list = data[index].split("|")
    temp_list[choice] = correct_data
    data[index] = "|".join(temp_list)
    return data[index]

if __name__ == '__main__':
    fi = "data.txt"
    data = read_data(fi).split("\n")
    print_data(data, "all")
    index = choose_SN(data, "Which serial number do you want to update?: ")
    choice = choose_correct_info()
    if choice == 1:
        correct_data = input("Correct name: \t")
        data[index-1] = correct_info(data, index - 1, choice, correct_data)
    elif choice == 2:
        print("Correct Gender: \n")
        correct_data = choose_gender()
        data[index - 1] = correct_info(data, index - 1, choice, correct_data)
    elif choice == 3:
        correct_data = input("Correct City: \t")
        data[index - 1] = correct_info(data, index - 1, choice, correct_data)
    elif choice == 4:
        print("Correct Score: \n")
        correct_data = input_score()
        data[index - 1] = correct_info(data, index - 1, choice, str(correct_data))
    else:
        print("Correct Score: \n")
        correct_data = input_score()
        data[index - 1] = correct_info(data, index - 1, choice, str(correct_data))
    print_data(data, "all")