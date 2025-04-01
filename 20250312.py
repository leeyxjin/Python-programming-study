print("Hello World")
print("100")
print("%d" % 100)
print("100+100")
print("%d" % (100+100))
print("2+5")
print("%d/%d=%d"%(200,100,200/100))
print("%d점입니다." %100)
print("당신의 학점은 %c입니다." %'B')
print('수학점수:%d 영어점수:%d' %(10,20))
print("%d야." %(2+3))
print('%d야.' %19.6) #이렇게 해도 19까지만 print된다.

a=3
b=1
c=3
print(a+b+c)
print('%d'%c)

print('hi\n')
print("\출력")
print('\\출력')
print("\'안녕\'")
print("\'출력")
print("hi \bi\'m") #???? \b 이거 왜 안됨?

price=100
print(price,'원')
print('%d원' %price)
print(price,'원',sep='') #print는 중간에 무조건 space를 하나씩 넣는다. 단, sep=''를 쓰면 중간의 space를 없앤다.
#sep='/'를 사용하면, 중간에 스페이스 대신 /를 넣는다.

a=1
b=2
c=3
print('%d%d%d'%(a,b,c))
print(a,b,c, sep=', ')

var1=100
var2=3.14
var3='Python'
var4=True

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))

is_raining = False

if is_raining:
    print("우산을 가져가세요!") 
else:
    print("맑은 날이네요!")

a='Lee'+'Yujin' #+는 sapce처리되지 않음
print(a*2)

b= (100+6==106) #같다는 ==로 사용
print(a)

b=(100+6)
print(b==106)


a=int(input('숫자를 입력하세요'))
b=(a%2)

if b==0:
    print('정답입니다!')
else:
    print('메롱')


name=input('name: ')
uni_id=int(input('id number?: '))
print('제 이름은 %s이고, 제 학번은 %d입니다.' %(name, uni_id) )

print('## 택배를 보내기 위한 정보를 입력하세요. ##')
a= input('받는 사람: ')
b= input('주소: ')
c= int(input('무게(g): '))*5 #%c에다가 *5 하면 안 됨! 그냥 문자열 반복 -> 아니면 %(c*5)로 해야 함. 둘 중 택 1

print ('**받는 사람 ==> %s'%a)
print ('**주소 ==> %s'%b)
print ('**배송비 ==> %s원'%(c*5))

print("20250401")