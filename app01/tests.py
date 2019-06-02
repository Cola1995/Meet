from django.test import TestCase

# Create your tests here.

l = [1,2,2,4,5]
for j in range(1):
    flag = False
    for i in l:
        if i == 2:
            flag = True
            break

    if flag:
        print("找得2")
    else:
        print("未找到哦")

