#1
print('Hello, World!')

#2
print('I love python!')

#3
#?

#4
a=int(input())
b=int(input())
print(a+b)

#5
a=int(input())
b=int(input())
print(a,'+',b,'=',a+b)
print(a,'-',b,'=',a-b)
print(a,'*',b,'=',a*b)
print(a,'/',b,'=',a/b)

#6
print('I am a student.\n *\n\t^^Nice to meet you~')

#7
name=input('당신의 이름은? ')
age=input('당신의 나이는? ')
hieght=input('당신의 키는? ')
print('이름은 %s, 나이는 %s살, 키는 %scm입니다.'%(name, age, hieght))

#8
x=int(input())
print(int(x**0.5))
print(x**2)
print(x**3)

#나누기는 float(실수), 몫연산자는 int(정수)
#9-1
#10-1
#11-3
#12-1
#13-1
#14-4
#15-1
#16
x=float(input())
if x>0:
    print('양수입니다.')
elif x<0:
    print('음수입니다.')
else:
    print('0입니다.')
#17
x=int(input())
print('Adult') if x>=18 else print('Teen')
#18
x=int(input())
if x>=90:
    print('A')
elif x>=80:
    print('B')
elif x>=70:
    print('C')
elif x>=60:
    print('D')
else: print('F')
#19
x=int(input())
print('오전') if x<12 else print('오후')
#20
x=list(map(int,input().split()))
print(max(x))
#21
a,b=map(int,input().split())
print('짝수입니다.') if (a+b)%2==0 else print('홀수입니댜.')
#22
x=int(input())
if x%3==0 and x%5==0:
    print('FizzBuzz')
else: print(x)
#23
year=int(input('연도를 입력하세요: '))
if (year%4==0 and year%100!=0) or (year%400==0):
    print('윤년입니다.')
else:
    print('윤년이 아닙니다.')
#24
a,b=map(int,input().split())
c=a-b
if c<0:
    c*=-1
if c>=10:
    print('차이가 10 이상입니다.')
elif c==0:
    print('두 수는 같습니다.')
else: print('차이가 10 미만입니다.')

#25
a,b,c=map(int,input().split())
if a==0 or b==0 or c==0:
    print('0은 포함될 수 없습니다.')
elif a%2==0 and b%2==0 and c%2==0:
    print('모두 짝수입니다.')
elif a%2==1 and b%2==1 and c%2==1:
    print('모두 홀수입니다.')
else: print('홀수와 짝수가 섞여 있습니다.')
