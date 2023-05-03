import matplotlib.pyplot as plt
from copy import deepcopy
msc=1000*86400*36525 #how many ms in a century. I don't think I'm going to use this lmao

#after 1 century, each day is 1 ms longer. 

msd=1000*86400.0 #how many ms in a day
dc=36525*71 #how many days in we'll have gone through when we're done.

dmsd=1.0/36525 #how many ms you gain after a day, because after 36525 days, you've gained 1 ms. 
dmsms=1.0/36525/(1000*86400) #how many ms you gain per ms

days=list(range(0,dc+1))
timegained=[0]
#Alright, we can begin. 
#I'm going to for loop through days. 
for d in days[1:]:
    #Each day, the number of miliseconds in a day increases slightly by dmsd.
    timegained.append(float(deepcopy(msd)))
    msd=msd+deepcopy(dmsd)
    #however, the day is now longer, and dmsd becomes dmsms * the new msd
    dmsd=dmsms*msd
ttgms=sum(timegained)
print("total time gained in ms: ",ttgms)

ttgh=ttgms/3600000
print("total time gained in hours: ",ttgh)
plt.plot(days, timegained)
plt.show()
