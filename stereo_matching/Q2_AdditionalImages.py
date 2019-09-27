#Q2 - Algorithms
import math
import matplotlib

from PIL import Image
import numpy as np
import matplotlib as plt
import scipy.misc

#FORWARD PASS
from toGrayScaleAdd import getImg

left_image, right_image = getImg()
rows_1, columns_1 = left_image.shape
rows_2, columns_2 = right_image.shape
count = 0

N = len(left_image[0]) #a row of the image
M = len(right_image[0]) #a row of the second image
#will need to be looped later

occlusion_cost = 1
probability_of_detection = 0.9
variance_S = 16
additional_matrix = np.zeros((N,M), dtype=int)
cost_matrix = np.zeros((N,M), dtype=int)
temp_list = list()
disparity_map = np.array((), dtype=int)

#N and M are measurements in the 2 epipolar scanlines, of the 2 images

def build_cost_matrix(N,M, index):
    #Need a for loop for iterating through each epipolar line in the image
    global occlusion_cost
    global cost_matrix
    for i in range(N):#length of the array
        cost_matrix[i][0] = i * occlusion_cost #compare every column with row, image 1 to 2
    for i in range(M):
        cost_matrix[0][i] = i * occlusion_cost #compare every row with column
    for i in range(N):
        for j in range(M):
            cost_matrix[i][j] = get_the_costs(i,j, index)
            additional_matrix[i][j] = populate_matrix(i,j, index)

def get_the_costs(i,j, index):
    #pixels i and j match
    cost_1 = get_cost_1(i, j, index)
    cost_2 = get_cost_2(i, j)
    cost_3 = get_cost_3(i, j)
    minChosen = min(cost_1, cost_2 ,cost_3)
    return minChosen

def populate_matrix(i, j, index):
    cost_1 = get_cost_1(i, j, index)
    cost_2 = get_cost_2(i, j)
    cost_3 = get_cost_3(i, j)
    minChosen = min(cost_1, cost_2, cost_3)
    if minChosen == cost_1:
        return 1
    elif minChosen == cost_2:
        return 2
    elif minChosen == cost_3:
        return 3

def get_cost_1(i,j, index):
    return cost_matrix[i - 1][j - 1] + cost_of_matching_two_features(left_image[index][i],right_image[index][j])  # need to get the value of this and clarify the meaning again
#need something later to loop more than just 0

def get_cost_2(i,j):
    return cost_matrix[i][j - 1] + occlusion_cost

def get_cost_3(i,j):
    return cost_matrix[i - 1][j] + occlusion_cost

def cost_of_matching_two_features(z_1, z_2):
    cost = (1/128)*((abs(z_1 - z_2))**2)
    return cost

def get_disparity_line(N, M):
    i = N - 1
    j = M - 1
    disparity_for_line = [0] * M
    while i > 0 and j > 0:
        value = additional_matrix[i][j]
        if value == 1:
            disparity_for_line[j] = abs(i-j) * 12.75
            i -= 1
            j -= 1
        #i and j match, so need to get the distance between i and j to have disparity
        if value == 2:
            disparity_for_line[j] = abs(i-j) * 12.75
            j -= 1 #j is unmatched
        if value == 3:
            i -= 1 #i is unmatched
    return disparity_for_line

def disparity_map_to_image():
    print("we outcheaaa")
    try:
        with open('disparity_array.txt', 'w') as f:
            for item in disparity_map:
                f.write("%s\n" % item)
        Image.fromarray((disparity_map * 255).astype(np.uint8), mode='L').save('view1_disparity.png')
    except:
        print("Unable to save")

#create_GrayImages()

for value in range(rows_1):
    build_cost_matrix(len(left_image[value]),len(right_image[value]), value)
    temp_list.append(get_disparity_line(N, M))
    length = len(sorted(temp_list, key=len, reverse=True)[0])
    disparity_map = np.array([temp_listi + [0] * (length - len(temp_listi)) for temp_listi in temp_list])
disparity_map_to_image()

