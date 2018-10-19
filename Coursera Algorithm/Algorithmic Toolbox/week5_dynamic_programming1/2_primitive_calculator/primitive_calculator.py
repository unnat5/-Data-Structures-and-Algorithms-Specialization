# Uses python3
import sys
import math

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def primitiveCalculator(numbers,operations = [1,2,3]):
    cal_table = [0]*(numbers+1)
    for number in range(2,numbers+1):
        minOperations = math.inf
        for operation in operations:
            if number%operation==0:
                if operation==1:
                    temp_minOperations = cal_table[number-operation]+1
                    #hist_result.append(number-operation)
                else:
                    temp_minOperations = cal_table[number//operation]+1
                    
                if temp_minOperations<minOperations:
                    minOperations = temp_minOperations
                    cal_table[number]=temp_minOperations
                    
    temp = numbers
    ls=[temp]
    yo1 = (math.inf,math.inf)
    yo2 = (math.inf,math.inf)
    yo3 = (math.inf,math.inf)
    while temp!= 1:
        if temp%operations[2]==0:
            yo3 = cal_table[temp//operations[2]]
            yo3 = (yo3,temp//operations[2])
        if temp%operations[1]==0:
            yo2 = cal_table[temp//operations[1]]
            yo2 = (yo2,temp//operations[1])
        yo1 = cal_table[temp-operations[0]]
        yo1 = (yo1,temp-operations[0])
        final_yo = min(yo1,yo2,yo3)
        temp = final_yo[1]
        ls.append(final_yo[1])
            
            
    return cal_table[-1],ls[::-1]

if __name__ == "__main__":

    input = sys.stdin.readline()
    n = int(input)
    min_operation,sequence = primitiveCalculator(n)
    print(min_operation)
    print(*sequence) 
    # sequence = list(optimal_sequence(n))
    # print(len(sequence) - 1)
    # for x in sequence:
    #     print(x, end=' ')

