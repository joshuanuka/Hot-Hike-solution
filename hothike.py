days=input()                                                     #the number of days
if days.isdigit() and int(days) in range(3,51):                  #input within range
    forecast=input()
    temps=forecast.split()
    if len(temps)==int(days):                                    #makes sure the temperatures are the same as the number of days
        for n in temps:
            if n.isdigit() and int(n) in range(-20,41):          
                bestday=[]
                for t in range(len(temps)-2):                     #since the first day will always need two days after it
                    startday=temps[t]
                    if int(temps[t])<0 and int(temps[t+2])<0:     #differentiates negative temps from positive temps
                         bestday.append(min(temps[t],temps[t+2])) #checks only the minimum of the hiking days
                    else:
                        bestday.append(max(temps[t],temps[t+2]))

negativedays=[]
for j in range(len(bestday)):
    if int(bestday[j])<0:
        negativedays.append(bestday[j])
if negativedays==[]:                                            #if there were no negative temperatures
    d=bestday.index(min(bestday))        
    t=(min(bestday))                                            #max. temp
    print(int(d+1),int(t))
else:
    d=bestday.index(max(negativedays))
    t=(max(negativedays))                                       #max.temp
    print(int(d+1),int(t))

