import sys
import os
import subprocess

comm="lsof -n -P -iTCP -sTCP:ESTABLISHED"

try:
    nPort=sys.argv[1]
except IndexError:
    nPort="3001"

proc = subprocess.Popen(comm, shell=True, stdout=subprocess.PIPE)
nOut = []
nCount=[]
while True:
    line = proc.stdout.readline().strip()
    if str(line) == "":
        proc.communicate()
        if proc.returncode == 1:
            print("EMPTY: Nothing to see here")
            sys.exit(1)
        if proc.returncode > 1:
            print("ERROR: Something went wrong with lsof (error should be above)")
            sys.exit(proc.returncode)
        break
    elif line[0:7] != "COMMAND":
        linesplit=line.split()[8].split('->')
        addOn = [linesplit[0].split(':')[0],linesplit[1].split(':')[0],linesplit[1].split(':')[1]]
        if (addOn[2] == nPort) and (addOn not in nOut):
            nOut.append(addOn)
            nCount.append(1)
        elif addOn[2] == nPort:
            nCount[nOut.index(addOn)] = nCount[nOut.index(addOn)] + 1

if len(nOut) == 0:
    print("EMPTY: Nothing to see here at %s" %nPort)
    sys.exit(2)

i=0
print("\nCounting unique established connections for port %s\n" %nPort)
rows=[['Source IP','Destination IP','Connection Count']]
for line in nOut:
    rows.append([line[0],line[1],str(nCount[i])])
    i=i+1

cols = zip(*rows)
col_widths = [ max(len(value) for value in col) for col in cols ]
format = '\t'.join(['%%-%ds' % width for width in col_widths ])
for row in rows:
    print(format % tuple(row))

