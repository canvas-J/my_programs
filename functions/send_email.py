# -*- coding: utf-8 -*-
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.header import Header
from email.utils import formataddr


def email_sender(receiver_list, sender_email, sender_passwd, content):
    try:
        # s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # qq邮箱发
        s = smtplib.SMTP_SSL("smtp.china-norm.com", 465)
        s.login(sender_email, sender_passwd)
        for receiver in receiver_list:
            s.sendmail(sender_email, receiver, content.as_string())
            print('给 ' + receiver + ' 的邮件,发送成功!' + str(datetime.datetime.now()))
        s.quit()
        print("Success!")
    except smtplib.SMTPException as e:
        print("Falied,{}".format(e))

def make_content():
    # HTML 内容(文本+图片)
    contentRoot = MIMEMultipart('related')
    contentRoot['Subject'] = Header('云端程序终止，请连接查看', 'utf-8')
    header = Header(u'云服务停止', 'utf-8')
    header.append('<jingang@china-norm.com>', 'ascii')
    contentRoot['From'] = header
    # contentRoot['From'] = Header(u'云服务停止', 'utf-8')
    # contentRoot['From'] = Header(sender_email, 'utf-8')
    # 文本 内容
    content_text = MIMEText(
        '<html>'
        '<head>'
        '<title>email</title>'
        '<meta http-equiv="Content-Type" content="text/html; charset=utf-8">'
        '<style type="text/css">'
        '.border {'
        'border-top: 1px solid #ebebeb;'
        'margin-left: 65px;'
        'width: 650px;'
        '}'
        '.dm {'
        'margin-top: 20px;'
        '}'
        '</style>'
        '</head>'
        '<body bgcolor="#FFFFFF" leftmargin="0" topmargin="0" marginwidth="0" marginheight="0">'
        '<!-- Save for Web Slices (email.png) -->'
        '<table id="__01" width="750" height="1300" border="0" cellpadding="0" cellspacing="0">'
        '<tr>'
        '<td colspan="3">'
        '<img src="http://www.hotmail.com/upload/email/email_01.gif" width="750" height="1145" alt=""></td>'
        '</tr>'
        '<tr>'
        '<td rowspan="2">'
        '<img src="http://www.hotmail.com/upload/email/email_02.gif" width="53" height="155" alt=""></td>'
        '<td>'
        '<a href="http://www.hotmail.com/cooperation"'
        'onmouseover="window.status="";  return true;"'
        'onmouseout="window.status='';  return true;">'
        '<img src="http://www.hotmail.com/upload/email/email_03.gif" width="640" height="59" border="0" alt=""></a></td>'
        '<td rowspan="2">'
        '<img src="http://www.hotmail.com/upload/email/email_04.gif" width="57" height="155" alt=""></td>'
        '</tr>'
        '<tr>'
        '<td>'
        '<img src="http://www.hotmail.com/upload/email/email_05.gif" width="640" height="96" alt=""></td>'
        '</tr>'
        '</table>'
        '<div class="border">'
        '<table class="dm">'
        '<tbody>'

        '<tr>'
        '<td><b style="font-family:楷体,Times New Roman;font-size:16px">马云</b></td>'
        '<td><p style="font-family:Times New Roman;font-size:16px">阿里巴巴大哥大</p></td>'
        '</tr>'
        '<tr>'
        '<td><b style="font-family:楷体,Times New Roman;font-size:16px">微信</b></td>'
        '<td><p style="font-family:Times New Roman;font-size:16px">1234567</p></td>'
        '</tr>'
        '<tr>'
        '<td><b style="font-family:Times New Roman;font-size:16px">支付宝</b></td>'
        '<td><p style="font-family:Times New Roman;font-size:16px">123456789</p></td>'
        '</tr>'
        '<tr>'
        '<td><b style="font-family:Times New Roman;font-size:16px">Tel</b></td>'
        '<td><p style="font-family:Times New Roman;font-size:16px">123456789</p></td>'
        '</tr>'
        '<tr>'
        '<td><b style="font-family:Times New Roman;font-size:16px">Email</b></td>'
        '<td><p style="font-family:Times New Roman;font-size:16px">mayun@alibaba.com</p></td>'
        '</tr>'
        '<tr>'
        '<td><b style="font-family:Times New Roman;font-size:16px">Addr</b></td>'
        '<td><p style="font-family:楷体,Times New Roman;font-size:16px">杭州萧山区</p></td>'
        '</tr>'

        '</tbody>'
        '</table>'
        '</div>'
        '<!-- End Save for Web Slices -->'
        '</body>'
        '</html>',
        'html',
        'utf-8')
    contentRoot.attach(content_text)

    # 图片内容
    # fp = open('path/to/test_img.jpeg', 'rb')
    # content_image = MIMEImage(fp.read())
    # fp.close()
    # content_image.add_header('Content-ID', 'image_id')
    # contentRoot.attach(content_image)

    return contentRoot


if __name__ == '__main__':
    # 接受邮箱列表
    receiver_list = [
        'livegang@hotmail.com',
        'ja.ga.main@qq.com',
        'vagang@126.com',
        ]
    # 发件人信息
    sender_email = 'jingang@china-norm.com'
    sender_password = '----'
    content = make_content()
    # 发送
    email_sender(receiver_list, sender_email, sender_password, content)
