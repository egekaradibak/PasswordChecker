f = open("passwordData.txt", "r")
passwords = f.readlines()
nOfRightP = 0
WantedIndexes = []
def find(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            WantedIndexes.append(i)
for line in passwords:
    s = line
   
    length = len(s)
    if s[1] == '-':
        min = int(s[0])
        if s[3].isspace() == True :
            max = int(s[2])
            c = s[4]
            password = s[7:length]
        else:
            max = int(s[2:4])
            c= s[5]
            password = s[8: length]
    else :
        min = int(s[:2])
        if s[4].isspace() == True:
            max = int(s[3])
            c= s[5]
            password = s[8: length]
        else:
            max = int(s[3:5])
            c= s[6]
            password = s[9: length]
    for i, ltr in enumerate(password):
        if ltr == c:
            #if i == min+1 or i == max+1:
                #nOfRightP = nOfRightP+1
            WantedIndexes.append(i+1)
   
    if min in WantedIndexes and max not in WantedIndexes:
        nOfRightP = nOfRightP+1
        WantedIndexes.clear()
    if max in WantedIndexes and min not in WantedIndexes:
        nOfRightP = nOfRightP+1
        WantedIndexes.clear()
    WantedIndexes.clear()
          
print(nOfRightP)