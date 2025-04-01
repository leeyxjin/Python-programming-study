password='data'
answer=input('비밀번호를 입력해주세요: ')

if(answer==password): print('correct')


num=int(input('숫자 하나 입력해주세요: '))
print('짝수') if(num%2==0) else print('홀수')


math=83
science=90
if (math>=80 and science>=80): print('합격') #math and science >=80 -> 이런 건 안됨
if (math<=85 or science<=85): print('탈락')

#pass -> 수업 듣기
num=int(input('숫자 입력: '))
if(num%5==0 and num%7== 0):
    print('35의 배수')

#?같으면 어떡해
if(math>science):
    print('math')
else:
    print('science')


num=int(input('숫자 입력: '))
if(num%2==0 and num>10):
    print('x')
else:
    print('o')


year=int(input('연도를 입력하세요: '))
if (year%4==0 and year%100!=0) or (year%400==0):
    print('%d년은 윤년입니다.'%year)
else:
    print('%d년은 윤년이 아닙니다.'%year)


x=int(input('숫자를 입력 ==> '))
if x>100:
    if x<1000:
        print('100보다 크고 1000보다 작군요')
    else:
        print('1000보다 크군요.')
else:
    print('100보다 작군요.')


print("A", end='')
print('학점입니다.')

x=int(input('주문 금액을 입력해주세요 : '))

if x>=50000:
    print('배달비 무료')
elif x>=30000:
    print(x*0.05,'원',sep='')
elif x>=10000:
    print(x*0.1,'원',sep='')
else:
    print('배달 불가')


######
x=int(input('주문 금액을 입력해주세요 : '))
y=0 #초기값 설정

if x>=50000:
    y=0
elif x>=30000:
    y=x*0.05
elif x>=10000:
    y=x*0.1
else:
    print('배달 불가')
print('배달비는 ',y,'원입니다.', sep='')


y=float(input('자동차 속도를 입력해주세요 (km/h)'))
if y>100:
    print('위험! 면허 정지 조치가 필요합니다.')
elif y>80:
    print('과속입니다! 벌금이 부과됩니다.')
elif y>50:
    print('속도를 줄이세요!')
else:
    print('정상 속도입니다.')


z=int(input('1부터 100 사이의 숫자를 입력하세요: '))
if z<42:
    print('더 큰 숫자를 입력하세요!')
elif z>42:
    print('더 작은 숫자를 입력하세요!')
else:
    print('정답입니다! 축하합니다!')



a=input()
a+='!'
print(a)

a=5
if 10%a==0 and 15%a==0:
    print('정답')


x=input()
y=int(input())
h,m=map(int,x.split())

h+=y//60
m+=y%60

if m>=60:
    h+=m//60
    m%=60
if h>24:
    h-=24
print(h,m)