# student information management
from read_write import *
from add_info import *
from update_info import *
from remove_info import *

def choose_option():
    while True:
        try:
            option = int(input("""
            Choose one of the following options:
            1. Add
            2. Update
            3. Display list of all students
            4. Display list of students which have final grade >= 75
            5. Display list of students which have final grade < 75
            6. Remove
            7. Quit

            => Your choice: """))
            if 1 <= option <= 7:
                return option
                break
            else:
                print("You only have 7 options. Try again!!!\n")
        except ValueError:
            print("Invalid input. Try again!!!\n")

def try_again(text):
    choice = input(text).upper().strip()
    if choice == "Y" or choice == "YES":
        return True
    else:
        return False

if __name__ == '__main__':
    fi = "data.txt"
    fo = "data.txt"
    data = read_data(fi).split("\n")
    while True:
        option = choose_option()
        if option == 1:
            while True:
                data.append(add_info(data))
                if try_again("Do you want to add more student information? (Y/N): ") == False:
                    print("DONE!!!")
                    break
        elif option == 2:
            while True:
                print_data(data, "all")
                index = choose_SN(data, "Which serial number do you want to update?: ")
                choice = choose_correct_info()
                if choice == 1:
                    correct_data = input("Correct name: \t")
                    data[index - 1] = correct_info(data, index - 1, choice, correct_data)
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
                if try_again("Do you want to update more? (Y/N): ") == False:
                    print("DONE!!!\n")
                    break
        elif option == 3:
            print_data(data, "all")
        elif option == 4:
            print_data(data, ">= 75")
        elif option == 5:
            print_data(data, "< 75")
        elif option == 6:
            while True:
                if data == [""] or data == "" or data == []:
                    print("\nNo student information. You have to add first\n")
                    break
                else:
                    print_data(data, "all")
                    STT = choose_SN(data, "Which serial number that you want to remove?: ")
                    data = remove_info(STT, data)
                    data = generate_STT(data)
                if try_again("Do you want to remove something else? (Y/N): ") == False:
                    print("DONE!!!\n")
                    break
        else:
            print("Bye! See you next time!!!")
            exit()
        if try_again("Do you want to exit STUDENT INFORMATION MANAGEMENT program? (Y/N): ") == True:
            print("\nDone. Please check detail in 'data.txt'")
            break
    header = "{:^5}|{:^20}|{:^10}|{:^20}|{:^10}|{:^10}\n"
    write_data(header.format("S/N", "FULL NAME", "GENDER", "CITY", "THEORY", "PRACTICE"), fo, "w")
    for element in data:
        temp = element.split("|")
        if temp == [""]:
            continue
        else:
            info = "{:^5}|{:^20}|{:^10}|{:^20}|{:^10}|{:^10}\n"
            write_data(info.format(temp[0], temp[1], temp[2], temp[3], temp[4], temp[5]), fo, "a")