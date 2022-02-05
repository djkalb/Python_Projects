import datetime

#UTC-05:00 -- NEW YORK

#UTC_08:00 -- Portland

#UTC 0000 -- London
description = """
The Portland-based company you work for just opened two new branches. One is in New York City, the other in 
London. They need a very simple program to find out if the branches are open or closed. The hours 
of both branches are 9:00 a.m.-5:00 p.m. in their own time zone.



Create a script that will find out the current times in the Portland HQ and NYC and London branches. Then, 
compare that time with each branch's hours to see if they are open or closed.

Print out to the screen the three branches and whether they are open or closed.

"""

def isOpen():
    #prints whether an office is open based on UTC 
    time = datetime.datetime.now()
    utc = time.utcnow()
    hour = utc.hour
    dictUTC = { 'London': 0, 'New York': 5, 'Portland': 8}

    #handles conversions below 0 and above 24 for time zone conversions with utc
    def rollover(time, offset):
        if time - offset < 0:
            return (time - offset) * -1
        elif time - offset > 24:
            return (time - offset - 24)
        else:
            return time - offset
         
    for item in dictUTC:
        if 8 < (rollover(hour, dictUTC[item])) < 18:
            print('The office in {} is currently open'.format(item))
        else:
            print('The office in {} is currently closed.'.format(item))
      
isOpen()
    

