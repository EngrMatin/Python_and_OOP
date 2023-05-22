prev_no = 0

for i in range(1,10):
    current_sum = prev_no + i
    print("Current number: ", i, "Previous number: ", prev_no, "Current sum: ", current_sum)

    prev_no = i
