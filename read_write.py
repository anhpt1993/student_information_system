def read_data(file_name):
    try:
        with open(file_name) as file:
            temp = file.readline()
            data = file.read()
    except FileNotFoundError:
        print("That file was not found :(")
        data = None
    file.close()
    return data

def write_data(data, file_name, method):
    with open(file_name, method) as file:
        file.write(data)

if __name__ == '__main__':
    try:
        with open("data.txt") as file:
            data1 = file.readline()
            data = file.read()
    except FileNotFoundError:
        print("That file was not found :(")
        data = None
    file.close()
    #print(data1)
    print(data)