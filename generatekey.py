import time
print 'hi'
'''
1. 
userid : emailid 
uid: last two char
time: mm
time : hh

convert these value in ascii code

### try further : append 000 after every 4 digit 


2. 
	

'''

name=raw_input("enter username:")
id=raw_input("enter id:")
newid=id[-2:]
a=[]
#a.append(newid)
print newid
lt=time.localtime(time.time())
#print "Localtime",localtime
print lt.tm_hour
print lt.tm_min
print"########"
for ch in newid:
 a.append(ord(ch))
 print ord(ch)
print "###################"

#for t in lt.tm_hour:
s = str(lt.tm_hour)
for d in s:
        a.append(ord(d))
	print 'out :', ord(d)


print"########################"
s1=str(lt.tm_min)
for d1 in s1:
  a.append(ord(d1))
  print 'out:',ord(d1)
list1=list(a)
list2=list(a)
f=1
i=0
while i<len(a) and (i+4)<=len(a):
 
 i=i+4
 if f==0:
  k=i+3
 else:
  k=i
 list2.insert(k,'000')
 f=0
#list2[4].replace('\'','')
#print "list2" ,list2
#converting list to string
str2=''.join(str(e) for e in list2)
#print str2
str1=''.join(str(e) for e in list1)
print str1
list3=list(str1)
#print list3 #['1', '2', '1', '9', '7', '4', '9', '5', '1', '5', '3', '4', '9']
i=0
f=1
count=0
b=[]
for l in str1:
 b.append(l)
list4=list(b)
while i<len(list3) and (i+4)<=len(list3):
  i=i+4
  k=i+count
 # list4.insert(k-2,'xa')
  list4.insert(k,'0')
  count=count+1
str3=''.join(str(j) for j in list4)
print str3
#print len(list3)
print "###########################"
####################################DECRYPTION############################################
'''
i=0
while i<len(str3):
 if (i+4)<len(str3):
  print str3[i:i+4]
  i=i+5

 elif (i+1)<len(str3):
  print str3[i+1:len(str3)]
 else:
  print " "
d1=str3[-2:]
print d1
d2=str3[-4:-2]
print d2
'''

