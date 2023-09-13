from functions import *

def greedy_randomize(Testing_data,Testing_data_amount_info ):
    TOTAL_INFO = {}
    for file in Testing_data:
            best_color = math.inf
            try:
                    for l in np.arange(5000):
                            data = Testing_data[file]
                            data_info = Testing_data_amount_info[file]
                            Adjacency_matrix = get_Adjacency_matrix(data_info[0], data)
                        
                            time_start = time.time()
                            list_vert = list((np.arange(len(Adjacency_matrix))))
                            color_classes = [[]]
                            max_color = 1
                            while (len(list_vert) != 0):
                                    current_color = 1
                                    vert = random.choice(list_vert)
                                    list_vert.remove(vert)
                                    while has_neighours(vert, color_classes[current_color - 1], Adjacency_matrix):
                                            current_color += 1
                                            if current_color - 1 >= len(color_classes):
                                                    color_classes.append([])
                                    if current_color > max_color:
                                            max_color = current_color

                                    color_classes[current_color - 1].append(vert)
                            time_end = time.time()
                            
                            test = testing_solution(color_classes, Adjacency_matrix)
                            if max_color < best_color:
                                    best_color = max_color
                                    TOTAL_INFO[file] = (max_color, (time_end - time_start),  color_classes, test)
                            l +=1
            except:
                    continue
    return TOTAL_INFO