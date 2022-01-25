s = "   fly me   to   the moon  "

cnt = 0
word_list = []
temp_s = ""

for i in s:
    if i == " ":
        if temp_s != "":
            cnt = cnt + 1
            word_list.append(temp_s)
            temp_s = ""
    else:
        temp_s = temp_s + i

if temp_s != "":
    word_list.append(temp_s)
    cnt = cnt + 1

print(len(word_list[cnt-1]))
