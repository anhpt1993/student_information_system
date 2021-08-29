# student information management
def read_data(file_name):
    try:
        with open(file_name, "r") as file:
            data = file.read()
    except FileNotFoundError:
        print("That file was not found :(")
        data = None
    file.close()
    return data

def write_data(data, file_name, method):
    with open(file_name, method) as file:
        file.write(data)

def choose_option():
    while True:
        try:
            option = int(input("""
            Choose one of the following options:
            1. Add
            2. Update
            3. List of all students
            4. List of students which have final grade >= 75
            5. List of students which have final grade < 75
            6. Remove

            => Your choice: """))
            if 1 <= option <= 3:
                return option
                break
            else:
                print("You only have 3 options. Try again!!!\n")
        except ValueError:
            print("Invalid input. Try again!!!\n")

def generate_SN(data):
    pass

def choose_gender():
    while True:
        try:
            gender = int(input("""
            Choose one of the following:
            1. Male
            2. Female
            3. Fluid
            
            Your choice: """))

            if 1 <= gender <= 3:
                return gender
                break
            else:
                print("Invalid input. Try again!!!\n")
        except ValueError:
            print("Invalid input. Try again!!!\n")

def input_score():
    while True:
        try:
            score = int(input("Input score (0-100): "))
            if 0 <= score <= 100:
                return score
                break
            else:
                print("Invalid input. Try again!!!\n")
        except ValueError:
            print("Invalid input. Try again!!!\n")


def add_info():
    pass

if __name__ == '__main__':
    data = read_data("input.txt").split("\n")
    option = choose_option()
    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 5:
        pass
    else:
        pass
    write_data(data, "output.txt", "w")


