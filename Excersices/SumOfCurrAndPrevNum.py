print("Printing current and previous number and their sum in a range(10)")
for i in range(10):
    prev = i-1
    if prev < 0:
        prev = 0
        print('Current Number {} Previous Number  {}  Sum:  {}'.format(i, prev, i + prev))
    else:
        print('Current Number {} Previous Number  {}  Sum:  {}'.format(i,prev, i + prev ))