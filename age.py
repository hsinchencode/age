driving = input('有沒有開過車：')
if driving != '有' and driving != '沒有':
        print('只能輸入有或沒有')
        raise SystemExit


age = input('你幾歲：')
age = int(age)

if driving == '有':
	if age >= 18:
		print('你通過測驗了')
	else:
		print('奇怪 你怎麼會有開過車')

elif driving == '沒有':
        if age >= 18:
                print('你可以考駕照了啊')
        else:
                print('過幾年就可以考了')
else:
        print('只能輸入有或沒有')
        
