n_testcases=int(input())
output = []
        
for t in range(n_testcases):
    n_blocks=int(input())
    n_letters = list(map(int, input().split()))
    main_str=""
    
    #loop for creating string in each block
    for i in range(n_blocks):
        block_str=""
        start=ord('A')
       
        #loop for building string
        for k in range(n_letters[i]):
            start+=1
            block_str+=chr(start)
        
            #Reverse str if block is even
            if i % 2!=0:
                block_str=block_str[::-1]
            
        main_str+=block_str
    
    output.append("Case #{}: {}".format((t+1), "A"+main_str))    
        


    
#print output
for o in output:
    print(o)
        


    