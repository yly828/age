driving = input('請問你有沒有開過車？')
if driving != '有' and driving != '沒有':
	print('只能輸入有或沒有')
	raise SystemExit
	
age = input('請問你的年齡？')
age = int(age)
if driving == '有':
	if age >= 18:
		print('恭喜 通過測驗了！')
	else:
		print('奇怪 你怎會開過車！')
elif driving == '沒有':
	if age >= 18:
		print('那你可去考駕照啦')	
	else:
		print('再等等吧')
