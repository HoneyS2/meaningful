flowerbed = [1,0,0,0,1]
n = int(input())

for key, value in enumerate(flowerbed):
    if key == 0:
        if value == 0:
            if key+1 == len(flowerbed):
                if flowerbed[len(flowerbed)-1] == 0:
                    if n >= 1:
                        flowerbed[key] = 1
                        n = n-1
            else:
                if flowerbed[key+1] == 0:
                    if n >= 1:
                        flowerbed[key] = 1
                        n = n-1
    else:
        if value == 0:
            if key+1 == len(flowerbed):
                if flowerbed[key-1] == 0 and flowerbed[len(flowerbed)-1] == 0:
                    flowerbed[key] = 1
                    n = n-1
            else:
                if flowerbed[key-1] == 0 and flowerbed[key+1] == 0:
                    flowerbed[key] = 1
                    n = n-1

if n >= 1:
    print(False)
else:
    print(True)
