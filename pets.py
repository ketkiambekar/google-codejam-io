n_test_cases = int(input())
output = []

for t in range(n_test_cases):
    n_pets = int(input())
    sizes = sorted(list(map(int, input().split())))
    base = 0
    treats= 1
    
    for i in range(1, len(sizes)):
        if sizes[i-1] < sizes[i]:
            base +=1
        treats += base + 1

    output.append("Case #{}: {}".format((t+1), treats))

    
#print output
for o in output:
    print(o)
        


    

        


    