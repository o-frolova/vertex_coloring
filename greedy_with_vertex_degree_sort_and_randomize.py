from functions import *

def greedy_with_vertex_degree_sort_and_randomize(Testing_data, Testing_data_amount_info):
    TOTAL_INFO = {}
    for file in Testing_data:
            best_color = math.inf
            try:
                for l in np.arange(5000):
                        data = Testing_data[file]
                        data_info = Testing_data_amount_info[file]
                        Adjacency_matrix = get_Adjacency_matrix(data_info[0], data)
                        degree_vertices = get_degree_vert(Adjacency_matrix)
                        ready_list = get_random(degree_vertices)

                        time_start = time.time()
                        max_color, color_classes = solver(ready_list, Adjacency_matrix)
                        time_end = time.time()
                        
                        test = testing_solution(color_classes, Adjacency_matrix)
                        if max_color < best_color:
                                best_color = max_color
                                TOTAL_INFO[file] = (max_color, (time_end - time_start),  color_classes, test)
                        l += 1
            except:
                continue
    return TOTAL_INFO

