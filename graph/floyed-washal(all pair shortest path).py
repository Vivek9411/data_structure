# matrix is adjacency matrix 
# -1 denotes no possible edge(inf weight)

def shortest_distance(matrix):
	for i in range(len(matrix)):
		# serach for better path through ith node 
	  #  new_mat = [row[:] for row in matrix]
	    for s in range(len(matrix)):
	    	# s denotes start
	        for e in range(len(matrix)):
	        	# e denotes end
	            if matrix[s][e]==-1:
	                if matrix[s][i] !=-1 and matrix[i][e]!=-1:
	                    matrix[s][e]=matrix[s][i]+matrix[i][e]
                else:
                    if matrix[s][i] !=-1 and matrix[i][e]!=-1:
	                    matrix[s][e] = min(matrix[s][i]+matrix[i][e], matrix[s][e])
    return matrix