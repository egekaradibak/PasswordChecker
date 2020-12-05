f = open("passwordData.txt", "r")
passwords = f.readlines()
nOfRightP = 0
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
    number = password.count(c)
    if number >= min and number <= max:
        nOfRightP = nOfRightP+1
        
print(nOfRightP)




    
   
    