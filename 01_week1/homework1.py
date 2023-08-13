count = input("請輸入數量")
nums = input("請依次輸入數字串，並以空白鍵分隔").split()

newlist = nums[::-1]

ans = ""
for y in range(int(count)):
    ans = ans + str(newlist[y]) + " "
print(ans)