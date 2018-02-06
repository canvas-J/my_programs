import re
import tkinter
import tkinter.messagebox

# 设置主窗口和显示文本框
root = tkinter.Tk()
root.geometry('300x270+400+100')				# 设置窗口位置和大小
root.resizable(False,False)						# 不允许改变大小
root.title('简易计算器-biu哩个biu')				# 设置窗口标题

# 放置并设置显示文本框,设为只读
contentVar = tkinter.StringVar(root,'')
contentEntry = tkinter.Entry(root,textvariable=contentVar)
contentEntry['state'] = 'readonly'
contentEntry.place(x=10,y=10,width=280,height=20)

# 编写各个按钮的处理方法
def buttonClick(btn):
	content = contentVar.get()
	if content.startswith('.'):					# 以小数点开头,加个0
		content = '0' + content
	if btn in '0123456789':
		content += btn
	elif btn == '.':
		lastPart = re.split(r'\+|-|\*|/]', content)[-1]
		if '.' in lastPart:
			tkinter.messagebox.showerror('错误','小数点太多了')
			return
		else:
			content += btn
	elif btn == 'C':
		content = ''
	elif btn == '=':
		try:
			content = str(eval(content))			# 运算求值
		except:
			tkinter.messagebox.showerror('错误','表达式错误')
			return
	elif btn in operators:
		if content.endswith(operators):
			tkinter.messagebox.showerror('错误','不允许存在连续运算符')
			return
		content += btn
	elif btn == 'Sqrt':
		n = content.split('.')
		if all(map(lambda x: x.isdigit(),n)):
			content = eval(content)**0.5
		else:
			tkinter.messagebox.showerror('错误','表达式错误')
			return
	contentVar.set(content)

# 创建按钮并链接方法
btnClear = tkinter.Button(root,text='Clear',command=lambda:buttonClick('C'))			# 清除按钮
btnClear.place(x=40,y=40,width=80,height=20)
btnCompute = tkinter.Button(root,text='=',command=lambda:buttonClick('='))				# 计算按钮
btnCompute.place(x=170,y=40,width=80,height=20)

digits = list('0123456789.') + ['Sqrt']								# 放置按钮
index = 0
for row in range(4):
	for col in range(3):
		d = digits[index]
		index += 1
		btnDigit = tkinter.Button(root,text=d,command=lambda x=d:buttonClick(x))
		btnDigit.place(x=20+col*70,y=80+row*50,width=50,height=20)

operators = ('+','-','*','/','**','//')								# 放置运算符按钮
for index,operator in enumerate(operators):
	btnOperator = tkinter.Button(root,text=operator,command=lambda x=operator:buttonClick(x))
	btnOperator.place(x=230,y=80+index*30,width=50,height=20)

# 主循环
root.mainloop()