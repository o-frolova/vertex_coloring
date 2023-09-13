from functions import *
def greedy_with_vertex_degree_sort(Testing_data, Testing_data_amount_info):
    TOTAL_INFO = {}
    for file in Testing_data:
            try:
                    data = Testing_data[file]
                    data_info = Testing_data_amount_info[file]
                    Adjacency_matrix = get_Adjacency_matrix(data_info[0], data)
                    degree_vertices = get_degree_vert(Adjacency_matrix)
                    sorted_keys = sorted(degree_vertices, key=degree_vertices.get)
                    sorted_keys.reverse()

                    time_start = time.time()
                    max_color, color_classes = solver(sorted_keys, Adjacency_matrix)
                    time_end = time.time()
                    
                    test = testing_solution(color_classes, Adjacency_matrix)

                    TOTAL_INFO[file] = (max_color, (time_end - time_start),  color_classes, test)
            except:
                    continue
                
    return TOTAL_INFO
