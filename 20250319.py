#Review
print('hello', end='')
print('I\'m tony')

print(1,3,5,7,sep='+',end='=')
print(1+3+5+7)

math = 92
science = 87
english = 94
print('수학,과학,영어 점수는 각각 %d,%d,%d 입니다' %(math,science,english))
print("%s score: %d" %('math',math))
print("%s score: %d" %('sceicne', science))
print("%s score: %d" %('englsih', english))

###int 말고 float..?
math=input()
python=input()
mean_score= (int(math)+int(python))*0.5
print('수학 점수는 %s, 파이썬 점수는 %s입니다.'%(math, python))
print('그리고 평균 점수는 %f점 입니다.'%mean_score)

a=1
b=2
c=a+b
print(c)

a=5
print(c)


#Class
n1=5
n2=3


sum=n1+n2
quo=n1//n2
rem=n1%n2
square=n1**n2 #^는 or 판단연산자이다.

print('두 수의 합은 %d이지~'%sum)
print('n1을 n2로 나눈 몫은 %d, 나머지는 %d이지~'%(quo,rem))
print('n1의 n2승은 %d이지~'%square)

pi=3.14159265
r=float(input('원의 반지름은? : '))
length=2*pi*r
area=pi*(r**2)

print('원의 둘레는 %f, 넓이는 %f 입니다.'%(length, area))


#복합대입연산자
a=20

a+=3 #a+3한 걸 다시 a에 넣는다.
print(a)
a-=3 #윗윗줄에서 변경된 a에 -3한 걸 다시 a에 넣는다.
print(a)
a/=3
print(a)
a//=3
print(a)
a%=3
print(a)
a**=3
print(a)


a=10
print('a=', a)
a*=3+2
print('a=',a)

#FTTFT TFFT

print(10==100)
print(13!=23)
print(41<92)
print(52>60)
print(22<=22)

print('가방'!='사랑')
print('가방'<'사랑')
print('가자'>'가차')
print('abc'<='abd')

#TFTTTF
a=5
print(a>1)
print(a<1)
print(a>=5)
print(a<=5)
print(a==5)
print(a!=5)

num=float(input())
k=(num>100)and(num<100)
print(k)

r=(num==99) or (num>=200)
print(r)
print(not(r))

a=5
b=10

print(a>1 and b<10, a>1 or b<10)
