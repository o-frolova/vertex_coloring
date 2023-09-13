import os 

def get_testing_data(path):
    os.chdir(path)
    Testing_data = {}
    Testing_data_amount_info = {}

    for file_ in os.listdir():
        file = open(file_)
        data = []
        while True:
            try:
                line = file.readline()
            except: continue
            if not line:
                break
            else:
                if line.startswith("p "):
                    amount_ver, amount_edge = line[6:-1].split()
                    Testing_data_amount_info[file_] = (int(amount_ver), int(amount_edge))
                if line.startswith("e "):
                    ver_1, ver_2 = line[2:-1].split()
                    data.append((int(ver_1), int(ver_2)))
                
        Testing_data[file_] = data
        file.close
    return Testing_data,Testing_data_amount_info