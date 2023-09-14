from global_variables import *
import numpy as np
from pyvis.network import Network
import pandas as pd
import time 
import random
import math
import pandas as pd


def get_Adjacency_matrix(amount_ver, data):
    Adjacency_matrix = [0] * amount_ver
    for i in range(amount_ver): 
        Adjacency_matrix[i] = [0] * amount_ver
    for edge in data:
        Adjacency_matrix[edge[0] - 1][edge[1] - 1] = 1
        Adjacency_matrix[edge[1] - 1][edge[0] - 1] = 1
    return Adjacency_matrix

def has_neighours(vert, color_class, Adjacency_matrix):
    flag = False
    for vert_ in color_class:
        if Adjacency_matrix[vert][vert_] == 1:
            flag = True
    return flag


def solver(sorted_keys, Adjacency_matrix):
    color_classes = [[]]
    max_color = 1
    for i, vert in enumerate(sorted_keys):
        current_color = 1
        while has_neighours(int(vert), color_classes[current_color - 1], Adjacency_matrix):
            current_color += 1
            if current_color - 1 >= len(color_classes):
                color_classes.append([])
        if current_color > max_color:
            max_color = current_color

        color_classes[current_color - 1].append(int(vert))
    return max_color, color_classes


def get_degree_vert(Adjacency_matrix):
    degree_vertices = {}

    for num, i in enumerate(Adjacency_matrix):
        count = 0 
        for j in i:
            if j == 1:
                count += 1
        degree_vertices[str(num)] = count
    return degree_vertices

def testing_solution(color_classes, Adjacency_matrix):
        for classter in color_classes:
                for n, vert in enumerate(classter):
                        for n_, vert_2 in enumerate(classter):
                                if Adjacency_matrix[vert][vert_2] == 1:
                                        return 'TEST FAIL'
        return 'TEST PASS'


def get_random(degree_vertices):
    t = sorted(degree_vertices.items(), key=lambda item: item[1])
    result = {}
    stop = t[len(t) - 1][1]

    for j in np.arange(stop + 1):
            for_shuffle = []
            for i in degree_vertices:
                    if degree_vertices[i] == j:
                            for_shuffle.append(i)
            random.shuffle(for_shuffle)
            if len(for_shuffle) != 0:
                    result[str(j)] = for_shuffle

    ready_list = []
    for lis in result:
            ready_list.extend(result[lis])

    ready_list.reverse()
    return ready_list

def save_result(result, name_algorithm):
    data = pd.DataFrame.from_dict(result)
    print(data)
    data = data.T
    data.columns = [ 'AMOUNT_COLORS', 'TIME', 'GROUPS', 'TEST']
    data['OPTIMAL_SOLUTION'] = OPTIMAL_SOLUTION
    data['SOLVED'] = data['AMOUNT_COLORS'] <= data['OPTIMAL_SOLUTION']

    data.to_excel('path' + name_algorithm)