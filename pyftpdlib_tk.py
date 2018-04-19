# -*- coding:utf-8 -*-  
import os  
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from Tkinter import *

#声名一个tk（你可以把tk理解为一个窗口）
root = Tk()
#这里填写什么，生成窗口的名字就是什么
root.title("ftpserver")

# use----ftp://localhost:2121


#下面为ftpserver主函数
def ftpserver():
    user = var1.get()
    password = var2.get()
    ipaddr = var3.get()
    port = var4.get()
    path = var5.get()

    # Instantiate a dummy authorizer for managing 'virtual' users
    #下面这句声明一个虚拟授权用户
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions and a read-only
    # anonymous user
    #设定登录的账号密码与访问目录
    #设定允许匿名用户登录
    authorizer.add_user(user, password, path, perm='elradfmwMT')
    #authorizer.add_anonymous(os.getcwd())

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready."

    # Specify a masquerade address and the range of ports to use for
    # passive connections.  Decomment in case you're behind a NAT.
    #handler.masquerade_address = '151.25.42.11'
    #handler.passive_ports = range(60000, 65535)

    # Instantiate FTP server class and listen on 0.0.0.0:2121
    address = (ipaddr, port)
    server = FTPServer(address, handler)

    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # start ftp server
    server.serve_forever()


#下面这些是对最开始的时候创建的tk进行行列式填充 label为文本 entry为输入框 
L1 = Label(root,text = 'UserName:').grid(column = 0,row = 0)
var1 = StringVar()
var1.set("admin")
E1 = Entry(root,textvariable = var1, bd = 2).grid(column = 1,row = 0)

L2 = Label(root,text = 'Password:').grid(column = 0,row = 1)
var2 = StringVar()
var2.set("admin")
E2 = Entry(root,textvariable = var2, bd = 2).grid(column = 1,row = 1)

L3 = Label(root,text = 'IP Address:').grid(column = 0,row = 2)
var3 = StringVar()
var3.set("192.168.1.104")
E3 = Entry(root,textvariable = var3, bd = 2).grid(column = 1,row = 2)

L4 = Label(root,text = 'PortNumber:').grid(column = 0,row = 3)
var4 = StringVar()
var4.set("2121")
E4 = Entry(root,textvariable = var4, bd = 2).grid(column = 1,row = 3)

L5 = Label(root,text = 'Path:').grid(column = 0,row = 4)
var5 = StringVar()
var5.set("/home/jingang/app&doc/share_folder")
E5 = Entry(root,textvariable = var5, bd = 2).grid(column = 1,row = 4)

Button1 = Button(root,text = "RunFtpserver",command=ftpserver).grid(column = 1,row = 5)
root.mainloop()