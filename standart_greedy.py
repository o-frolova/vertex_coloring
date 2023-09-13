from functions import *

def standart_greedy_heuristics(Testing_data, Testing_data_amount_info):
    TOTAL_INFO = {}
    for file in Testing_data:
            try:
                    data = Testing_data[file]
                    data_info = Testing_data_amount_info[file]
                    Adjacency_matrix = get_Adjacency_matrix(data_info[0], data)

                    time_start = time.time()
                    color_classes = [[]]
                    max_color = 1
                    for i, vert in enumerate(Adjacency_matrix):
                        current_color = 1
                        while has_neighours(i, color_classes[current_color - 1], Adjacency_matrix):
                            current_color += 1
                            if current_color - 1 >= len(color_classes):
                                color_classes.append([])
                        if current_color > max_color:
                            max_color = current_color

                        color_classes[current_color - 1].append(i)
                    time_end = time.time()
                    
                    test = testing_solution(color_classes, Adjacency_matrix)

                    TOTAL_INFO[file] = (max_color, (time_end - time_start),  color_classes, test)
            except:
                continue
            
    return TOTAL_INFO

