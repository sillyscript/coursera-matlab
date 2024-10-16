#1. As of early 2018, Usain Bolt holds the world record in the men's 100-meter dash. It is 9.58 seconds. 
#   What was his average speed in km/h?  Assign the result to a variable called hundred.

#2. Kenyan Eliud Kipchoge set a new world record for men of 2:01:39 on September 16, 2018. 
#   Assign his average speed in km/h to the variable marathon. The marathon distance is 42.195 kilometers.

distance_1 = 100
time_1 = 9.58
speed_in_metre_per_second = distance_1/time_1
hundred = (18/5)*speed_in_metre_per_second
disp(hundred)

#time converted to seconds then again hours by dividing 3600
marathon = 42.195/(7299/3600)
disp(marathon)
