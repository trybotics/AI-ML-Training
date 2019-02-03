import math 

def classifyAPoint(points,p,k=3): 
	
	distance=[] 
	for group in points: 
		for feature in points[group]: 

			#calculate the euclidean distance of p from training points 
			euclidean_distance = math.sqrt((feature[0]-p[0])**2 +(feature[1]-p[1])**2) 

			# Add a touple of form (distance,group) in the distance list 
			distance.append((euclidean_distance,group)) 

	# sort the distance list in ascending order 
	# and select first k distances 
	distance = sorted(distance)[:k] 

	freq1 = 0 #frequency of group 0 
	freq2 = 0 #frequency og group 1 

	for d in distance: 
		if d[1] == 0: 
			freq1 += 1
		elif d[1] == 1: 
			freq2 += 1

	return 0 if freq1>freq2 else 1

# driver function 
def main(): 

	# Dictionary of training points having two keys - 0 and 1 
	# key 0 have points belong to class 0 
	# key 1 have points belong to class 1 

	points = {0:[(1,12),(2,5),(3,6),(3,10),(3.5,8),(2,11),(2,9),(1,7)], 
			1:[(5,3),(3,2),(1.5,9),(7,2),(6,1),(3.8,1),(5.6,4),(4,2),(2,5)]} 

	# testing point p(x,y) 
	p = (3.5,5) 

	# Number of neighbours 
	k = 3

	print("The value classified to unknown point is: {}".format(classifyAPoint(points,p,k))) 

if __name__ == '__main__': 
	main() 
	
