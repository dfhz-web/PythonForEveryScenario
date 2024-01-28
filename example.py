value = "y"
count = 0
# 0 is considered False
while value:
    count += 1
    print(count)
    if(count == 5):
        break
    else:
        value = 0
        continue
      
