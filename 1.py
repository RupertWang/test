db={}

def new_user():
	while True:
		name=input("请输入姓名")
		if name in db:
			print("该姓名已存在，请重新输入！")
		else:
			pwd=input("请输入密码")
			db[name]=pwd
			break

def old_user():
	exit_flag=False
	while True:
		name=input("请输入姓名")
		if name not in db:
			print('姓名不存在，请重新输入')
		else:
			while True:
				pwd=input('请输入密码')
				if db[name]==pwd:
					exit_flag=True
					break
				else:
					print("密码错误！请重新输入")
		if exit_flag==True:
			break
	print('验证成功！')

def main_menu():
	done=False
	while not done:
		chosen=False
		while not chosen:
			try:
				choice=input("请输入选项：N,E,Q")
			except (EOFError,KeyboardInterrupt):
				choice='Q'
			print("您选择了%s" %choice)
			if choice not in 'NEQ':
				print("请重新输入！")
			else:
				chosen= True
		if choice=='N':
			new_user()
		if choice=='E':
			old_user()
		if choice=='Q':
			done=True

if __name__ == '__main__':
	main_menu()

