n = 9 # Number of images
l = 3 # Number of temporal scales

x = 2
for l in range(l): # Number of temporal scales
    i = 0
    while i < (n//x):
        print('A = ', x*i)
        print('B = ', x*i+x//2)
        print('C = ', x*i+x)
        i += 1
    x *= 2
