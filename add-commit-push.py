import os

print('git status')
os.system('git status')

MESSAGE = input("\nAre you sure that you'd like to commit and push changes?").strip
if MESSAGE == "yes" or "y":
    print('\ngit add -A')
    os.system('git add -A')
    print('\ngit commit -m "update files"')
    os.system('git commit -m "update files"')
    print('\ngit push')
    os.system('git push')

elif MESSAGE == "no":
    exit()