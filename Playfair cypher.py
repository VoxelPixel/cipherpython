
# coding: utf-8

# In[ ]:


key_text=input('Enter key text : ')
key_text=key_text.upper()
key_text_list=list(key_text)
left_alphabets=[]
for i in range(65,91):
    left_alphabets.append(chr(i))
for i in range(65,91):
    if(chr(i)=='J'):
        left_alphabets.remove('J')
    for j in key_text:
        if(chr(i)==j):
            left_alphabets.remove(chr(i))

for i in left_alphabets:
    key_text_list.append(i)

    
# def to_matrix(l, n):
#     return [l[i:i+n] for i in range(0, len(l), n)]

# to_matrix(key_text_list,5)

import numpy as np
a=np.array(key_text_list).reshape(5,5)
a.tolist()


plain_text=str(input("Enter the plain text : "))
print("Press 1 for encription Press 2 for decription")
inn=int(input())
if(inn==1):
    val='Encription'
else:
    val='Decription'
plain_text=plain_text.upper()
if(len(plain_text)%2!=0):
    final_plain_text=plain_text+'Z'
else:
    final_plain_text=plain_text
    
final_plain_text=list(final_plain_text)
for i in range(len(final_plain_text)):
    if(final_plain_text[i]=='J'):
        
        final_plain_text[i]='I'
        

final_plain_text="".join(final_plain_text)



encrypted_list=[]
for i in range(0,len(final_plain_text),2):
    check=0
    #checking for horizontally
    for j in range(0,5):
        ll=[]
        c=0
        for z in range(0,5):
            if(final_plain_text[i]==a[j][z]):
                ll.append(a[j][(z+1)%5])
                c+=1
            elif(final_plain_text[i+1]==a[j][z]):
                ll.append(a[j][(z+1)%5])
                c+=1
        if(c==2):
            encrypted_list.append(ll)
            check=1
            break
        else:
            ll.clear()
            continue
    
    #checking for vertically
    for j in range(0,5):
        vr=[]
        c=0
        for z in range(0,5):
            if(final_plain_text[i]==a[z][j]):
                vr.append(a[(z+1)%5][j])
                c+=1
            elif(final_plain_text[i+1]==a[z][j]):
                vr.append(a[(z+1)%5][j])
                c+=1
        if(c==2):
            encrypted_list.append(vr)
            check=2

            break
        else:
            vr.clear()
            continue
    #checking for rectangle 
    c1=0
    for j in range(0,5):
        
        for z in range(0,5):
            if(final_plain_text[i]==a[j][z]):
                i1=j
                j1=z
                c1+=1
            elif(final_plain_text[i+1]==a[j][z]):
                i2=j
                j2=z
                c1+=1
        
        if(c1==2 and check==0):
            encrypted_list.append([a[i1,j2],a[i2,j1]])
            break


aa=np.array(encrypted_list)

aa=aa.reshape(len(final_plain_text),)
aa="".join(aa)
aa

