import time

sblue = 0
sred = 0
tpassed = 0
for x in range(0,12):
    nscore = input("Use rt or bt for a takedown. Use s to start and stop time")

    if nscore == "rt":
        sred += 2
    if nscore == "bt":
        sblue += 2

    print("red score " + str(sred))
    print("blue score " + str(sblue))

    
