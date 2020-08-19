scores = []
people = []
maxscore = 0
minscore = 100
max2=0
min2=0
total = 0
for i in range (2):
    n = int(input("What's your score:"))
    p = str(input ("What's your name:"))
    scores.append(n)
    people.append(p)
    
    if n > maxscore:
        maxscore = (n)
        max2= p
    if n < minscore:
        minscore = n
        min2= p
    total = total + n 
    
s = total/len(scores)
print ("The total score is:", total)
print ("The average is:", s)
print ("The highest score is:", maxscore,"Your name:", max2)
print ("THe lowest score is:", minscore,"Your name:", min2)
    