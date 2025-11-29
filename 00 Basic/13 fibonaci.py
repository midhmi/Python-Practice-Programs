olist=[]
nlist=[]
b=0
while True:
    ele=input('Enter or exit')
    if ele=='exit':
        break
    olist.append(ele)
for i in olist:
    if i not in nlist:
        nlist.append(i)
print(nlist)

