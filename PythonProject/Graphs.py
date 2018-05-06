import numpy as np
import matplotlib.pyplot as plt
 
# data to plot
# n_groups = 5
# mi_time = (20, 180, 350, 690, 1350)
# greedy_time = (20, 175, 190, 210, 250)

#mi_time .02 .18, .35, .69, 1.35
#greedy_time .02, .175, .19, .21, .25

#mi mult 20, 180 350, 690, 1350 
#greed mult 20, 175, 190, 210, 250
 
# create plot
# fig, ax = plt.subplots()
# index = np.arange(n_groups)
# bar_width = 0.25
# opacity = 0.8
 
# rects1 = plt.bar(index, mi_time, bar_width,
#                  alpha=opacity,
#                  color='b',
#                  label='Mixed Integer')
 
# rects2 = plt.bar(index + bar_width, greedy_time, bar_width,
#                  alpha=opacity,
#                  color='g',
#                  label='Greedy')
 
# plt.xlabel('Targets')
# plt.ylabel('Time (seconds)')
# plt.title('Time to Complete Given Targets')
# plt.xticks(index + bar_width, ('2', '3', '4', '5', '6'))
# plt.legend()
 
# plt.tight_layout()
# plt.show()


# n_groups = 5
# mi_outcome = (42, 34, 29.8, 26.1, 23.1)
# greedy_outcome = (41.5, 33.6, 29.2, 25.7, 22.8)
# default_outcome = (32, 26.8, 23.6, 21, 18.1)

# #mi_time .02 .18, .35, .69, 1.35
# #greedy_time .02, .175, .19, .21, .25

# #mi mult 20, 180 350, 690, 1350 
# #greed mult 20, 175, 190, 210, 250
 
# # create plot
# fig, ax = plt.subplots()
# index = np.arange(n_groups)
# bar_width = 0.25
# opacity = 0.8
 
# rects1 = plt.bar(index, mi_outcome, bar_width,
#                  alpha=opacity,
#                  color='b',
#                  label='Mixed Integer')
 
# rects2 = plt.bar(index + bar_width, greedy_outcome, bar_width,
#                  alpha=opacity,
#                  color='g',
#                  label='Greedy')

# rects3 = plt.bar(index + bar_width + bar_width, default_outcome, bar_width,
#                  alpha=opacity,
#                  color='r',
#                  label='Default')
 
# plt.xlabel('Targets')
# plt.ylabel('Defender Score')
# plt.title('Average Outcome Given Targets')
# plt.xticks(index + bar_width, ('2', '3', '4', '5', '6'))
# plt.legend()
 
# plt.tight_layout()
# plt.show()



# n_groups = 4
# mi_time = (10, 40, 210, 880)
# greedy_time = (10, 55, 220, 590)

# # mi_time .01 .18, .35, .69, 1.35
# # greedy_time .02, .175, .19, .21, .25

# # mi mult 20, 180 350, 690, 1350 
# # greed mult 20, 175, 190, 210, 250
 
# #create plot
# fig, ax = plt.subplots()
# index = np.arange(n_groups)
# bar_width = 0.25
# opacity = 0.8
 
# rects1 = plt.bar(index, mi_time, bar_width,
#                  alpha=opacity,
#                  color='b',
#                  label='Mixed Integer')
 
# rects2 = plt.bar(index + bar_width, greedy_time, bar_width,
#                  alpha=opacity,
#                  color='g',
#                  label='Greedy')
 
# plt.xlabel('Grid Size')
# plt.ylabel('Time (seconds)')
# plt.title('Time to Complete Grid Size')
# plt.xticks(index + bar_width, ('3x3', '6x6', '9x9', '12x12'))
# plt.legend()
 
# plt.tight_layout()
# plt.show()



# n_groups = 4
# mi_outcome = (24.5, 40, 58, 74.1)
# greedy_outcome = (24.5, 39.9, 57.9, 73.8)
# default_outcome = (14.4, 30.2, 49, 64.1)

# #mi_time .02 .18, .35, .69, 1.35
# #greedy_time .02, .175, .19, .21, .25

# #mi mult 20, 180 350, 690, 1350 
# #greed mult 20, 175, 190, 210, 250
 
# # create plot
# fig, ax = plt.subplots()
# index = np.arange(n_groups)
# bar_width = 0.25
# opacity = 0.8
 
# rects1 = plt.bar(index, mi_outcome, bar_width,
#                  alpha=opacity,
#                  color='b',
#                  label='Mixed Integer')
 
# rects2 = plt.bar(index + bar_width, greedy_outcome, bar_width,
#                  alpha=opacity,
#                  color='g',
#                  label='Greedy')

# rects3 = plt.bar(index + bar_width + bar_width, default_outcome, bar_width,
#                  alpha=opacity,
#                  color='r',
#                  label='Default')
 
# plt.xlabel('Grid Size')
# plt.ylabel('Defender Score')
# plt.title('Average Outcome Given Grid Size')
# plt.xticks(index + bar_width, ('3x3', '6x6', '9x9', '12x12'))
# plt.legend()
 
# plt.tight_layout()
# plt.show()



#data to plot
# n_groups = 3
# mi_time = (49, 42, 72)
# greedy_time = (38, 63, 89)

# # mi_time .02 .18, .35, .69, 1.35
# # greedy_time .02, .175, .19, .21, .25

# # mi mult 20, 180 350, 690, 1350 
# # greed mult 20, 175, 190, 210, 250
 
# #create plot
# fig, ax = plt.subplots()
# index = np.arange(n_groups)
# bar_width = 0.25
# opacity = 0.8
 
# rects1 = plt.bar(index, mi_time, bar_width,
#                  alpha=opacity,
#                  color='b',
#                  label='Mixed Integer')
 
# rects2 = plt.bar(index + bar_width, greedy_time, bar_width,
#                  alpha=opacity,
#                  color='g',
#                  label='Greedy')
 
# plt.xlabel('Barriers')
# plt.ylabel('Time (seconds)')
# plt.title('Time to Complete Given Barriers')
# plt.xticks(index + bar_width, ('1', '2', '3'))
# plt.legend()
 
# plt.tight_layout()
# plt.show()





# n_groups = 3
# mi_time = (34.9, 42, 47.5)
# greedy_time = (34.5, 41.5, 46.5)
# default_time = (32.1, 32.2, 32.5)

# # mi_time .02 .18, .35, .69, 1.35
# # greedy_time .02, .175, .19, .21, .25

# # mi mult 20, 180 350, 690, 1350 
# # greed mult 20, 175, 190, 210, 250
 
# #create plot
# fig, ax = plt.subplots()
# index = np.arange(n_groups)
# bar_width = 0.25
# opacity = 0.8
 
# rects1 = plt.bar(index, mi_time, bar_width,
#                  alpha=opacity,
#                  color='b',
#                  label='Mixed Integer')
 
# rects2 = plt.bar(index + bar_width, greedy_time, bar_width,
#                  alpha=opacity,
#                  color='g',
#                  label='Greedy')

 
# rects3 = plt.bar(index + bar_width + bar_width, default_time, bar_width,
#                  alpha=opacity,
#                  color='r',
#                  label='Default')
 
# plt.xlabel('Barriers')
# plt.ylabel('Defender Score')
# plt.title('Average Outcome Given Barriers')
# plt.xticks(index + bar_width, ('1', '2', '3'))
# plt.legend()
 
# plt.tight_layout()
# plt.show()


# n_groups = 3
# mi_time = (34.9, 43, 73)
# greedy_time = (34.5, 42.7, 61)
# default_time = (32.1, 32.2, 32.2)

# # mi_time .02 .18, .35, .69, 1.35
# # greedy_time .02, .175, .19, .21, .25

# # mi mult 20, 180 350, 690, 1350 
# # greed mult 20, 175, 190, 210, 250
 
# #create plot
# fig, ax = plt.subplots()
# index = np.arange(n_groups)
# bar_width = 0.25
# opacity = 0.8
 
# rects1 = plt.bar(index, mi_time, bar_width,
#                  alpha=opacity,
#                  color='b',
#                  label='Mixed Integer')
 
# rects2 = plt.bar(index + bar_width, greedy_time, bar_width,
#                  alpha=opacity,
#                  color='g',
#                  label='Greedy')

 
# rects3 = plt.bar(index + bar_width + bar_width, default_time, bar_width,
#                  alpha=opacity,
#                  color='r',
#                  label='Default')
 
# plt.xlabel('Barrier Penalty')
# plt.ylabel('Defender Score')
# plt.title('Average Outcome Given Barrier Penalty')
# plt.xticks(index + bar_width, ('2', '10', '50'))
# plt.legend()
 
# plt.tight_layout()
# plt.show()




n_groups = 1
mi_time = (34.9)
greedy_time = (34.5)
default_time = (32.1)

# mi_time .02 .18, .35, .69, 1.35
# greedy_time .02, .175, .19, .21, .25

# mi mult 20, 180 350, 690, 1350 
# greed mult 20, 175, 190, 210, 250
 
#create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.8
 
rects1 = plt.bar(index, mi_time, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Mixed Integer')
 
rects2 = plt.bar(index + bar_width, greedy_time, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Greedy')

 
rects3 = plt.bar(index + bar_width + bar_width, default_time, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Default')
 
plt.xlabel('Barrier Penalty')
plt.ylabel('Defender Score')
plt.title('Average Outcome Given Barrier Penalty')
plt.xticks(index + bar_width, ('Stationary', '10', '50'))
plt.legend()
 
plt.tight_layout()
plt.show()