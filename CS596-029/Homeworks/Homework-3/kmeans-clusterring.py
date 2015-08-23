# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import texttable
import scipy


data_points = [
    {'id':'ID=1', 'data' : [76,180], 'cluster': 1}, 
    {'id':'ID=2', 'data' : [73,200], 'cluster': 2}, 
    {'id':'ID=3', 'data' : [62,150], 'cluster': 0}, 
    {'id':'ID=4', 'data' : [60,140], 'cluster': 0}, 
#    {'id':'ID=1', 'data' : [66,170], 'cluster': 1}, 
#    {'id':'ID=2', 'data' : [73,210], 'cluster': 2}, 
#    {'id':'ID=3', 'data' : [72,165], 'cluster': 0}, 
#    {'id':'ID=4', 'data' : [70,180], 'cluster': 0}, 
#    {'id':'ID=5', 'data' : [74,185], 'cluster': 0}, 
#    {'id':'ID=6', 'data' : [68,155], 'cluster': 0}, 
#    {'id':'ID=7', 'data' : [65,150], 'cluster': 0}, 
#    {'id':'ID=8', 'data' : [64,120], 'cluster': 0}, 
#    {'id':'ID=9', 'data' : [63,125], 'cluster': 0}, 
#    {'id':'ID=10', 'data' : [67,140], 'cluster': 0}
]

seeds = [
    [66,170], [73,210]
]
epoch = 1
CLUSTERING_CHANGED = True



def generate_headers():
    header_row = []
    header_row.append("") #first column is empty
    for dp in data_points: #generate header title
        header_row.append(dp['id'])
    return header_row

def kmeans_clusterings_2d():
    print "\nEPOCH {0}".format(epoch)
    print "Seed 1: {0} ∈ C1".format(seeds[0])
    print "Seed 2: {0} ∈ C2".format(seeds[1])
    print "Distance between 2 seeds to each element:"
    
    distance_matrix = []
    for i in range(0, len(seeds)):
        
        # Add Header
        if i==0:
            distance_matrix.append(generate_headers())
    
        #Add Content
        row = []
        for j in range (0, len(data_points)):        
            #Add 1st Column Title
            if j==0: 
                row.append("Seed-{0}".format(i+1))
            #Add Content
            d = scipy.spatial.distance.euclidean(seeds[i], data_points[j]['data'])
            row.append("{:.2f}".format(d))
        distance_matrix.append(row)
    if CLUSTERING_CHANGED == generate_result(distance_matrix):
        global epoch
        epoch += 1
        kmeans_clusterings_2d()
    
def generate_result(distance_matrix):
    cluster_result_row = []
    cluster_result_row.append("Cluster")
    c1_sum = [0,0]
    c1_count = 0
    c2_sum = [0,0]
    c2_count = 0
    clustering_changed = False
    for j in range (1, len(data_points) + 1):
        if float(distance_matrix[1][j]) <= float(distance_matrix[2][j]):
            cluster_result_row.append("C1")
            c1_sum[0] += data_points[j-1]['data'][0]
            c1_sum[1] += data_points[j-1]['data'][1]
            c1_count += 1
            
            if data_points[j-1]['cluster'] != 1:
                clustering_changed = True
                data_points[j-1]['cluster'] = 1
        else:
            cluster_result_row.append("C2")
            c2_sum[0] += data_points[j-1]['data'][0]
            c2_sum[1] += data_points[j-1]['data'][1]
            c2_count += 1
            
            if data_points[j-1]['cluster'] != 2:
                clustering_changed = True
                data_points[j-1]['cluster'] = 2
                
    distance_matrix.append(cluster_result_row)
#    print distance_matrix
    
    c1_centroid = [float(c1_sum[0])/c1_count, float(c1_sum[1])/c1_count]
    c2_centroid = [float(c2_sum[0])/c2_count, float(c2_sum[1])/c2_count]
    
    distance_table = texttable.Texttable()
    distance_table.set_precision(1)
#    distance_table.set_cols_width([7,4,4,4,4,4,4,4,4,4,5])
    distance_table.set_cols_width([7,4,4,4,4])
    distance_table.add_rows(distance_matrix) 
    distance_table.set_cols_align(["l", "r","r","r","r"])
#    distance_table.set_cols_align(["l", "r","r","r","r","r","r","r","r","r","r"])
    print distance_table.draw()
    
    #Update seeds
    global seeds
    seeds = [
    c1_centroid, c2_centroid
    ]
    print "–> Base on above result of new clusterings, new seeds (mean) are computed: {0}, and {1}\n".format(c1_centroid, c2_centroid)
    return clustering_changed

kmeans_clusterings_2d()

#for s in seeds:
    
    
    