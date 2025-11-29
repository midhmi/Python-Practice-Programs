# Unique list
samp_list = [2,2, 3,4,4 ,5,6]
new_list=[]
for x in samp_list:
     if x not in new_list:  
        new_list.append(x) #my wrong method new_list = x+ new_list
print(new_list)