for _ in range(5):
    print('* * * * * * * * * *')

for i in range(6):
    print('*'*(5-i))

for i in range(31):
    if i%3==0 and i!=0:
        print(i)

x=0
for i in range(11):
    x+=i
print(x)

x=0
for i in range(1,11,1):
    x+=i
print(x)

#예시5
x=int(input('2 이상의 숫자를 입력해주세요: '))
y=1 #이거 중요
for i in range(x):
    y*=i+1
print(y)

x=int(input('2 이상의 숫자를 입력해주세요: '))
y=1 #이거 중요
for i in range(1,x+1,1):
    y*=i
print(y)

x=0
for i in range(1001,2001,2):
    x+=i
print(x)

#구구단
x=int(input('구구단 몇 단을 계산할까요?'))
for i in range(1,10):
    print(f'{x} x {i} = {x*i}')

for i in range(2,10):
    for j in range(1,10):
        print(f'{i} x {j} = {i*j}')
    print()

i=1
while i<6:
    print('*'*10)
    i+=1

for i in range(3) :
    print("안녕하세요. 어서 오세요. QR 체크 부탁드립니다.\n")
    break

x = 0
for i in range(1,11,1):
    x+=i
    if x>40:
        break
print("1에서 10까지의 합에서 최초로 40을 넘는 숫자는 = %d\n" %i)

i=1
x=0
while i<11:
    x+=i
    if x>40: break
    i+=1
print("1에서 10까지의 합에서 최초로 40을 넘는 숫자는 = %d\n" %i)

#예시9
x=0
for i in range(100):
    x+=i+1
print(x)

#예시10
y=0

for i in range(1,31):
    if 30%i==0 and 75%i==0:
        y=i
print(y)

x=1
y=0
while x<31:
    if 30%x==0 and 75%x==0:
        y=x
    x+=1
print(y)

x=int(input())
y=1
for i in range(1,x+1):
    y*=i
print(y)

x=0
for i in range(10):
    if (i+1)%2==0:
        x+=i+1
print(x)

#최대공약수
x=0
for i in range(1,31):
    if 30%i==0 and 75%i==0:
        x=i
print(x)

x=1
while x<31:
    if 30%x==0 and 75%x==0:
        y=x
    x+=1
print(y)

#최소공배수
a,b=map(int,input().split())
c=[]
x=1
y=1
z=1
while x<=a:
    if a%x==0:
        c.append(int(x))
    x+=1
while y<=b:
    if b%y==0:
        c.append(int(y))
for i in set(c):
    z*=i
print(z)