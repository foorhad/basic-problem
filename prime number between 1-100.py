n1=1
n2=100
print('Print prime number between', n1 , 'and', n2, 'are: ')

for num in range(n1, n2+1):
    if num>1:
        for i in range(2, num):
            if num%i==0:
                break
        else:
            print(num)