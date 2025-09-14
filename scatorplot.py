# # draw a scatorplot in matplotlib

# import matplotlib.pyplot as plt

# # data to plot
# # score of two teams


# team1score =[12,34,4,56,67,78,45,34,23]
# team2score =[3,56,34,78,99,77,66,55,44]


# # set the score range for scator plot

# teamscorerange=[4,8,12,16,20,25,27,29]


# #plot a scator plot using the pyplot.scator method()

# plt.scatter(team1score, teamscorerange, color='r')
# plt.scatter(team2score, teamscorerange, color='b')

# #set the labels
# plt.xlabel("team-score")
# plt.ylabel("score-range")


# #plot the title
# plt.title("Score of two teams")

# #show the figure
# plt.show()



import matplotlib.pyplot as plt

match_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
team1_score = [12, 34, 4, 56, 67, 78, 45, 34, 23]

# Check if sizes match
if len(match_number) == len(team1_score):
    plt.scatter(match_number, team1_score, color='blue', label='Team 1 Score')
    plt.xlabel("Match Number")
    plt.ylabel("Score")
    plt.title("Team 1 Score Over Matches")
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("Error: X and Y data must be the same length.")
