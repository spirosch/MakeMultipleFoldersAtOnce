import os

i = 0
# change the number 101 to any number you want and add 1
for i in range(0, 101):
    # specify your path and at the end write the name you want for your folder
    # plus the i inside the strings to add the current number of the loop statement
    path = fr'C:\Users\spirosch\Desktop\New folder/Day {i}'
    os.mkdir(path)

    # so when you execute this, with your current path, it will create 100 folders Day 1, Day 2 .... Day 100

