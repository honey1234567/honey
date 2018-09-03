import re
str3="489705551049"#1219075650150
str2="489705551049"
if str2.isupper() or str2.islower() or str2.isdigit():
    print "valid"
    '''
if re.match(r"[a-zA-Z0-9]",str2):
    print "valid"
'''
s=""
i=0
while i<len(str3):
    if (i+4)<len(str3):
        print str2[i:i+4]
        s+=str2[i:i+4]
        i=i+5
    if (i+1)<len(str3) and (i+4)>len(str3):
        l=len(str3)
        print str2[i:l]
        s+=str2[i:l]
        break
print "s",s
s2=s[-2:]
s1=s[-4:-2]
h1=s[-6:-4]
h2=s[-8:-6]
d_h2=""
d_id2=""
d_id1=""

'''
if not(h1>=1 and h1<=9):
  
    d_h2=chr(int(h2))
'''
#print s1===last 2 character
d_m1=chr(int(s2))
d_m2=chr(int(s1))
d_h=chr(int(h1))
#print d_m1
#print d_m2
l1=s[ :2]
l2=s[ :3]
l3=s[2:4]
l4=s[2:5]
l5=s[3:5]
l6=s[3:6]
print "l3",l3
print "l2",l2
print l3
print l4
print "l1",l1
if (l1>='97' and l1<='99')or(l1>='65' and l1<='90')or(l1>='48' and l1<='57'):
    print "2"
    d_id1+=chr(int(l1))
    
    if (l3>='48' and l3<='57')or(l3>='65' and l3<='90')or(l3>='97' and l3<='99'):
        print "3"
        d_id2+=chr(int(l3))
    else:
        d_id2+=chr(int(l4))    
else:
    print "f" 
    d_id1+=chr(int(l2))
 
    if (l5>='48' and l5<='57')or(l5>='65' and l5<='90')or(l5>='97' and l5<='99'):
        d_id2+=chr(int(l5))
    else:
        d_id2+=chr(int(l6))    
print  d_id1+d_id2+d_h2+d_h+d_m1+d_m2
