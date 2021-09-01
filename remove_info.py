from read_write import read_data
from add_info import print_data
from update_info import choose_SN, correct_info

def remove_info(STT, data):
    for element in data:
        if element.split("|")[0].strip() == str(STT):
            data.pop(STT-1)
    return data

def generate_STT(data):
    STT = 0
    for i in range(len(data)):
        if data[i] == "":
            continue
        else:
            STT += 1
            data[i] = correct_info(data, i, 0, str(STT))
    return data

if __name__ == '__main__':
    fi = "data.txt"
    data = read_data(fi).split("\n")
    if data == [""]:
        print("No student information. Please add first")
    else:
        print_data(data, "all")
        STT = choose_SN(data, "Which serial number that you want to remove?: ")
        #print(STT)
        data = remove_info(STT, data)
        data = generate_STT(data)
    print_data(data, "all")

    