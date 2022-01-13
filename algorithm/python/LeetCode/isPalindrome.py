x = 121
str_x = str(x)
str_len = len(str_x)

if x < 0:
    print(False)

str_y = ""
for i in reversed(range(0, str_len)):
    str_y = str_y + str_x[i] 

print(int(str_x) == int(str_y))
