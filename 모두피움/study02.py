#01
for i in range(1,11):
    print(i,end='')
#02
x=int(input())
for i in range(1,x+1):
    print(i)
##03
x=int(input())
for i in range(1,x+1,2):
    print(i)
#04
x=int(input())
for i in range(1,10):
    print(f'{x} x {i} = {x*i}')
#05
x=int(input())
y=0
for i in range(1,x+1):
    y+=i
print(f'합: {y}')
##06
for i in range((1,10)):
    print(f'2 * {i} = {2*i}')
##07
x=int(input())
for i in range(1,x):
    if x%i==0:
        print(i)

#08
a,b=map(int,input().split())
for i in range(a,b+1):
    print(i)
#09
for i in range(1,100):
    if i%3==0:
        print(i)
#10
x=int(input())
y=1
for i in range(1,x+1):
    y*=i
print(y)
#11
x=int(input())
for i in range(1,x+1):
    print('*'*i)
?##12
for i in range(1,5):
    print(f'2 * {i} = {2*i} 2 * {i+5} = {2*(i+5)}')
print('2 * 5 = 10')
#13
???
#14
x=int(input())
for i in range(1,x+1):
    print(' '*(x-i),'*'*(2*i-1),sep='')
#15
x=int(input())
for i in range(1,x+1):
    print(' '*(i-1),'*'*(2*(x-i)+1),' '*(i-1),sep='')
for i in range(2,x+1):
    print(' '*(x-i),'*'*(2*i-1),sep='')
#16
for i in range(1,x+1):
    print('*'*i,' '*(2(x-i)-1),'*'*i,sep='')
for i in range(1,x+1):
    print('*'*(x-i),' '*(x-),'*'*(x-i))