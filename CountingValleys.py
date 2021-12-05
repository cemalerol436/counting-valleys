# in the code "path" describes a hiker's path by using U (up) and D (down).

path = "UDDDUDUUUDDUDUU"

total = 0
i = 0
valleys = 0

# recognising U and D

while i<len(path):

    if path[i]== "D":
        total= total-1
    elif path[i]== "U":
        total= total+1
    i += 1

    # A loop to eliminate valleys form mountains.

    if total==0 and path[i-1]=="U":
        valleys = valleys+1

# a valley means hiker goes down from the sea level and climbs back to the sea level.

print(valleys)
