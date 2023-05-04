words = []
w = 0
for x in range(0,6):
     w += 1
     y = input("Please enter word " + str(w) + ": ")
     words.append(y)
     

StanzaList = [[0,1,2,3,4,5],
[5,0,4,1,3,2],
[2,5,3,0,1,4],
[4,2,1,5,0,3],
[3,4,0,2,5,1],
[1,3,5,4,2,0]]

envoiEnd = [1,3,2]
envoiMiddle =[5, 0, 4]

for row in StanzaList:
    for i in row:
        print(words[i])
    print("\n")

for middle,end in zip(envoiMiddle, envoiEnd):
        print(words[middle], words[end])
  