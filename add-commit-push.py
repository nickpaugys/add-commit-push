import os
import sys

commitCommand = '\ngit commit -m "update files"'
if len(sys.argv) == 3:
    if sys.argv[1] == '-m':
        # if there are 3 arguments and the second one is -m, use the third as a commit message
        commitCommand = '\ngit commit -m "' + sys.argv[2] + '"'

print('git status')
os.system('git status')

force = False
for x in range(len(sys.argv)):
    print(x)
    if sys.argv[x] == '-f':
        print('force = True')
        force = True

def addcommitpush():
    print('\ngit add -A')
    os.system('git add -A')
    print(commitCommand)
    os.system(commitCommand)
    print('\ngit push')
    os.system('git push')


if force == False:
    MESSAGE = input("\nAre you sure that you'd like to commit and push changes? ").strip().lower()
    if MESSAGE == "yes" or "y":
        addcommitpush()
    if MESSAGE == "no":
        quit()        

elif force == True:
    addcommitpush()