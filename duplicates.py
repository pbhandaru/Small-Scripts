#!/usr/bin/python
import os
import sys
import commands

##############

sizes = {}
files = []
dir = ''
md5 = {}

try:
    dir = sys.argv[1]
except:
        print 'You need to give the name of the directory as an argument to the Script'
        print 'Exiting with exit status 5'
        sys.exit(5)

try:
    if os.path.isdir(dir):
	 os.chdir(dir)
	 print dir, 'is a directory and accessible'
except:
    print 'Directory ', dir, ' is not accessible'
    print 'Exiting the script with exit status 10'
    sys.exit(10)

for file in os.listdir(os.getcwd()):
    if os.path.isfile(file):
	size = os.path.getsize(file)
        sizes.setdefault(size,[]).append(file)

#for key, value in sizes.iteritems():
#    print key, '=> ', value

for ks, vs in sizes.iteritems():
    files = vs
    if len(vs) == 1:
        continue

    for f in files:
        output = commands.getoutput('/sbin/md5' ' %s' % f)
        md5sum = output.split()[-1]
        md5.setdefault(md5sum, []).append(f)


    for km, vm in md5.iteritems():
        same = vm
        if len(vm) == 1:
            continue
        print ks, km
        for f in same:
            print f


#print md5
