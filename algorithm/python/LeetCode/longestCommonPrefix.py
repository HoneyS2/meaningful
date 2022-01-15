strs = ["flower","flow","flight"]

if len(strs) == 0:
    print("")
    exit()

prefix = strs[0]
for str in strs:
    while(str.find(prefix) != 0):
        prefix = prefix[0:len(prefix)-1]
        if len(prefix) == 0:
            print("")
            exit()
print(prefix)
