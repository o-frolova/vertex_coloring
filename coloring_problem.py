from reading_files import *
from functions import *
from global_variables import *
from standart_greedy import *
from greedy_with_vertex_degree_sort import * 
from  greedy_with_vertex_degree_sort_and_randomize import *
from greedy_randomize import *




if __name__ == '__main__':

    Testing_data, Testing_data_amount_info = get_testing_data(PATH)
    print('1')
    save_result(standart_greedy_heuristics(Testing_data, Testing_data_amount_info), 'standart_greedy_heuristics.xlsx')
    print('2')
    save_result(greedy_with_vertex_degree_sort(Testing_data, Testing_data_amount_info), 'greedy_with_vertex_degree_sort.xlsx')
    print('3')
    save_result(greedy_with_vertex_degree_sort_and_randomize(Testing_data, Testing_data_amount_info), 'greedy_with_vertex_degree_sort_and_randomize.xlsx')
    print('4')
    save_result(greedy_randomize(Testing_data, Testing_data_amount_info), 'greedy_randomize.xlsx')
