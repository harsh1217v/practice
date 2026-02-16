s = "Harsh Dongare"
print((len(s)))
print(len(s)//2)
print("________________________________________________")
###positive index###
print(s[6:9])#Don
print(s[3:10])#sh Dong  
print(s[4:0:-1])
print(s[3:10])
print(s[0:6])
print("________________________________________________")
###negative index###
print(s[-2:-5:-1])
print(s[-8:-13:-1])
print(s[-7:-10:-1])
print(s[-12:len(s)-1])
print(s[-5:-8:-1])
print("________________________________________________")
###positive and negative index###   
print(s[6:-13:-1])
print(s[3:-2:1])
print(s[6:-9:-1])
print(s[1:-1:1])
print(s[4:-6:1])
print("______________________________________________")
###negative and positive index###
print(s[-2:6:-1])
print(s[-8:3:-1])
print(s[-7:1:-1])
print(s[-12:3:1])
print(s[-1:6:-1])
print('______________________________________________')
###positive index with step###
print(s[0:len(s):2])
print(s[6:len(s):3])
print(s[ : :4])
print(s[-1:-9:-5])
print("______________________________________________")
###negative index with step###
print(s[-1:-6:-2])
print(s[-1:-13:-5])
print(s[-7:-2:5])
print(s[-5:-8:-1])