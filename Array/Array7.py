# find Largest sum contiguous Subarray [V. IMP]

a = [9,-51,-20,-13,-51,40,-21,75,-24,29,-86,5,-38,15,48,-87,-9,42,39,64,47,-63,22,-81,-20,-100,28]
prev_sum = -1
sum_ans = 0

for i in a:
    sum_ans += i
    prev_sum = max(sum_ans,prev_sum)
    if sum_ans < 0:
        sum_ans = 0
print(prev_sum)

