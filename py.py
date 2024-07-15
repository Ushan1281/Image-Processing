### Basic python code to GIT REPO

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as patches
import numpy as np
from PIL import Image
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")


#Road Input Parameters to setup the graphic
street_name = "Scott Street"
l_sidewalk = 8   #feet
r_sidewalk = 8   #feet
road_width = 40   #feet
# l_parklane = 8   #feet
l_drivelane = 11  #feet
# r_parklane = 8   #feet
r_drivelane = 11  #feet


#Folder for the images
image_folder = 'C:/Users/DELL/Documents/New py/images/'
image_bld1_path = image_folder + 'building1.png'
image_bld2_path = image_folder + 'building2.png'
image_tree_path = image_folder + 'tree.png'
image_car_path = image_folder + 'car.png'
image_pedestrian_path = image_folder + 'pedestrian.png'

#Setup dimensions of the plot in feet
building_base = 7 # feet.  Assume each building image occupies 10 feet of the extent
total_width = road_width + l_sidewalk + r_sidewalk + (2*building_base)   #additional 20 feet is added for the building, each of 10 feet width
total_height = 50  #feet fixed for now
total_subsurface = 30 # feet fixed for now
total_abovesurface = total_height - total_subsurface  #20 feet 
l_sidewalk_s = -l_sidewalk - (road_width/2)
r_sidewalk_s = (road_width/2)

adj_fig_width = 20 * total_height/total_width

# Update the plot to include a roadway, two sidewalks and two buildings
fig, ax = plt.subplots(figsize=(20, adj_fig_width))

# Create rectangles for four road layers - surface, subbase, base and subgrade
road_surface = plt.Rectangle((-road_width/2, 0), road_width, -0.5, color='gray')  #0.5 feet of road_surface
subbase = plt.Rectangle((-road_width/2, -0.5), road_width, -0.5, color='dimgray')
base = plt.Rectangle((-road_width/2, -1.0), road_width, -2.0, color='#5E2C04')


# For subgrade, create a custom colormap for the gradient from saddlebrown to tan
cmap = mcolors.LinearSegmentedColormap.from_list("custom_gradient", ["tan", "white"])
# Create a vertical gradient
gradient = np.linspace(0, 1, 100)
gradient = np.vstack((gradient, gradient)).T
# Add the gradient to the rectangle representing subgrade
# subgrade = plt.Rectangle((-total_width/2, -3.0), total_width, -30, color='tan' )
ax.imshow(gradient, extent=(-total_width/2, total_width/2, -30, -3), aspect='auto', cmap=cmap)

#Add sidewalk, center lane and left/right drive lanes
sidewalk_left = plt.Rectangle((l_sidewalk_s - building_base, -3.0), l_sidewalk+building_base, 3.8, color='silver')
sidewalk_right = plt.Rectangle((r_sidewalk_s, -3.0), r_sidewalk+building_base, 3.8, color='silver')
center_line1 = plt.Rectangle((-0.2,0),0.2,0.1,color='yellow')
center_line2 = plt.Rectangle((0.2,0),0.2,0.1,color='yellow')
l_drive_lane = plt.Rectangle((-l_drivelane,0),0.2,0.1,color='white')
r_drive_lane = plt.Rectangle((r_drivelane,0),0.2,0.1,color='white')

# Add elements to the plot
ax.add_patch(road_surface)
ax.add_patch(subbase)
ax.add_patch(base)
ax.add_patch(sidewalk_left)
ax.add_patch(sidewalk_right)
ax.add_patch(center_line1)
ax.add_patch(center_line2)
ax.add_patch(l_drive_lane)
ax.add_patch(r_drive_lane)


# Set limits, aspect ratio, and labels
ax.text(0, 10, street_name, color='black', fontsize=16, ha='center', va='center')  #street name label
ax.set_xlim(-total_width/2, total_width/2)
ax.set_ylim(-total_subsurface, total_abovesurface)
ax.set_aspect('equal')
ax.set_title('Street Cross-Section View - For Illustration Purposes Only, Not to Scale')
ax.set_xlabel('Distance (feet)')
ax.set_ylabel('Depth/Height (feet)')


#Add background images for making the graph more realistic
# Load an image of Building 1, convert to NP array and define extent 
image_bld1 = Image.open(image_bld1_path)
image_bld1_array = np.array(image_bld1)
image_bld1_extent = [l_sidewalk_s - building_base, l_sidewalk_s, 0.8, 15]

# Load an image of Building 2, convert to NP array and define extent 
image_bld2 = Image.open(image_bld2_path)
image_bld2_array = np.array(image_bld2)
image_bld2_extent = [r_sidewalk_s + r_sidewalk,r_sidewalk_s + r_sidewalk+ building_base, 0.8, 20]

# Load an image of Car, convert to NP array and define extent 
image_car = Image.open(image_car_path)
image_car_array = np.array(image_car)
image_car_extent = [(-road_width/2), (-road_width/2)+8, 0, 5]

# Load an image of Tree, convert to NP array and define extent 
image_tree = Image.open(image_tree_path)
image_tree_array = np.array(image_tree)
image_tree_extent = [(road_width/2) + 1, (road_width/2)+5, 0.8, 8]

# Load an image of Pedestrian, convert to NP array and define extent 
image_pedestrian = Image.open(image_pedestrian_path)
image_pedestrian_array = np.array(image_pedestrian)
image_pedestrian_extent = [(-road_width/2) - 6, (-road_width/2) - 0, 0.1, 7]

# Plot the image in the background at the specified location
ax.imshow(image_bld1_array, aspect='auto', extent=image_bld1_extent, zorder=1)
ax.imshow(image_bld2_array, aspect='auto', extent=image_bld2_extent, zorder=1)
ax.imshow(image_car_array, aspect='auto', extent=image_car_extent, zorder=1)
ax.imshow(image_tree_array, aspect='auto', extent=image_tree_extent, zorder=1)
ax.imshow(image_pedestrian_array, aspect='auto', extent=image_pedestrian_extent, zorder=1)


#Function to draw a utility with defined parameters
def draw_utility(ax,  u_width, u_height,u_shape, u_label, u_cx, u_cy,  u_color, ul_width):   
    if u_shape == "Circle":
       utility = plt.Circle((u_cx, u_cy+(u_height/2)), u_width/2, color=u_color, linewidth=ul_width, fill=False)
       # Adding the utility and label 
       ax.add_patch(utility)
       ax.text(u_cx, u_cy - 1.5, str(u_width) + "-feet " + u_label, color=u_color, fontsize=11, ha='center', va='center')
    elif u_shape == "Oval" or u_shape == "Egg":
       # utility = plt.Ellipse((u_cx, u_cy+(u_height/2)), u_width, u_height, angle =0, color=u_color, linewidth=ul_width, fill=False)
       utility = patches.Ellipse((u_cx, u_cy+(u_height/2)), u_width, u_height, edgecolor=u_color, facecolor='none', label=u_label, linewidth=ul_width)
       # Adding the utility and label 
       ax.add_patch(utility)
       ax.text(u_cx, u_cy - 1.5, str(u_width) + ' x ' + str(u_height) + "-feet " + u_label, color=u_color, fontsize=11, ha='center', va='center')

#Add utilities of different types/size by calling function and specific inputs

# 0.5-feet circular gas pipe, at -4 feet depth and -12 feet offset from centerline
draw_utility (ax,  0.5, 0.5,"Circle", "\n gas pipe", -12, -4,  'red', 1)

# 5-feet circular sewer pipe, at -12 feet depth and -7 feet offset from centerline
# draw_utility (ax,  5, 5,"Circle", "\n sewer pipe", -7, -12,  'saddlebrown', 3)

# 3x4.5-feet Egg-shape sewer pipe, at -12 feet depth and -7 feet offset from centerline
draw_utility (ax,  3, 4.5,"Egg", "\n sewer pipe", -7, -12,  'saddlebrown', 3)

# 24-inch circular sewer pipe, at -6 feet depth and 4 feet offset from centerline
draw_utility (ax,  24/12, 24/12,"Circle", "\n water pipe", 4, -6,  'blue', 2)

# Proposed 12-feet circular sewer pipe, at -18 feet depth and 7 feet offset from centerline
draw_utility (ax,  9, 9,"Circle", "\n new sewer pipe", 12, -12,  'black', 5)
# filename = f'C:/Users/DELL/Documents/New py/Static/road_cross_section_{timestamp}.png'
filename = f'C:/Users/DELL/Documents/New py/Static/road_cross_section.png'
# output_image_path = 'C:/Users/DELL/Documents/New py/Static/road_cross_section.png'
# fig.savefig(output_image_path)
plt.savefig(filename)
# plt.show()
