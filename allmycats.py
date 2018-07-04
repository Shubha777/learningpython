num = list(range(0, 17))
catNames = []
r=0
while True:
    r = r+1
    print('Enter the name of your cat numbered  ' + str(num[r]) + ' ( or enter nothing to stop.):')
    name = input()
    if name == '':
        r=0
        break
    if r==16:
        print('Maximum limit of input has bee achieved. You must not have any more cats')
        r=0
        break
    catNames = catNames + [name]
    continue
print('The name of the cats are:')
for name in catNames:
    r=r+1
    print('  ' + name+' . And its number is '+ str(num[r]))
