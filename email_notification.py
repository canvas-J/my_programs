# -*- encoding:utf-8 -*-
from email.header import Header         # 负责构造邮件的模块
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib  # 负责发送邮件的python模块

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = 'xxxxxxxx@163.com'      #发件人地址
password = 'pass'                   #邮箱密码
to_addr = 'xxxxxxxx@qq.com'         #收件人地址
smtp_server = 'smtp.163.com'        #163网易邮箱服务器地址

#设置邮件信息
msg = MIMEText('Python爬虫运行异常，异常信息为遇到HTTP 403', 'plain', 'utf-8')
msg['From'] = _format_addr('一号爬虫 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('一号爬虫运行状态', 'utf-8').encode()

#发送邮件
server = smtplib.SMTP(smtp_server, 25)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
