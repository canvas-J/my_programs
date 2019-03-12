# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText

def send_email(link, item_name):
    _user = "jingang@china-norm.com"
    _pwd = "----"
    _to = "livegang@hotmail.com"

    mail_msg = """
    <p> Batman , 你想买的"""+item_name+"""已找到符合价位的那一个,已经加入购物车,赶紧去看看...</p>
    <p><a href=""" + link + """>这是链接</a></p>"""

    msg = MIMEText(mail_msg, 'html', 'utf-8')

    msg["Subject"] = "igxe 扫到货了!"
    msg["From"] = _user
    msg["To"] = _to

    try:
        s = smtplib.SMTP_SSL("hwsmtp.qiye.163.com", 994)
        s.login(_user, _pwd)
        s.sendmail(_user, _to, msg.as_string())
        s.quit()
        print("Success!")
    except smtplib.SMTPException as e:
        print("Falied,{}".format(e))


if __name__ == '__main__':
    send_email('www.baidu.com','www')