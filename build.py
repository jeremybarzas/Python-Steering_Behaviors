import os
import sys

if (len(sys.argv) > 1):
    build_target = sys.argv[1]
else:
    build_target = raw_input('name of python file to build, with extension -> ')

if (not build_target.__contains__('.py')):
    build_target += '.py'

original_file = open('build_app.py', 'r')

my_file = original_file.readlines()
original_file.close()

for i in range(0, len(my_file)):
    if(my_file[i].__contains__('target =')):
        my_file[i] = 'target = "{0}"\n'.format(build_target)

newFile = open('build_app.py', 'w+')
for line in my_file:
    newFile.write(line)
newFile.close()

os.system('python build_app.py py2exe')