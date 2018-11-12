# -*- coding=utf-8 -*-
import os, datetime, re, time, random, logging, traceback
from openpyxl import Workbook
from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException

topic_id = input('请输入话题id号，获取所有答案：')
TOKEN_FILE = 'token.pkl'
client = ZhihuClient()

if os.path.isfile(TOKEN_FILE):
    client.load_token(TOKEN_FILE)
else:
    try:
        client.login('email_or_phone', 'password')
    except NeedCaptchaException:
        with open('a.gif', 'wb') as f:
            f.write(client.get_captcha())
        captcha = input('please input captcha:')
        client.login('email_or_phone', 'password', captcha)
    client.save_token(TOKEN_FILE)

#日志设置
logging.basicConfig(level=logging.ERROR,  
                format='%(asctime)s %(levelname)s %(message)s',  
                datefmt='%Y-%m-%d %H:%M:%S',
                filename='zhi.log',
                filemode='w')

wb = Workbook()
sheet = wb.active
sheet.title = "知乎"
item_name = ['time_now', 'content', 'que_title', 'author', 'gender', 'loc', 'business', 'company', 'job', 'created_time', 'updated_time', 'voteup_count', 'comment_count', 'thanks_count']
for j,title in enumerate(item_name):
    sheet.cell(row=1, column=j+1).value = title

topic = client.topic(int(topic_id))
print(topic.name)
num = 0
for question in topic.unanswered_questions:
    print(question.title)
    num += 1
    for answer in question.answers:
        gender_dict = {'0': '女', '1': '男', '-1': '不详'}
        if answer.author.gender != None:
            gender = gender_dict[str(answer.author.gender)]
        else:
            gender = '不详'
        loc = ''
        if answer.author.locations:
            for location in answer.author.locations:
                loc += location.name
        company = ''
        job = ''
        if answer.author.employments:
            for employment in answer.author.employments:
                if 'company' in employment:
                    company += employment.company.name
                if 'job' in employment:
                    job += employment.job.name
        if answer.author.business:
            business = answer.author.business.name
        else:
            business = ''
        # time.sleep(random.uniform(0.1, 0.3))
        item_data = [datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')]
        try:
            item_data += [re.compile(r'<.*?>', re.S).sub('', answer.content), question.title, answer.author.name, gender, loc, business,
                    company, job, datetime.datetime.fromtimestamp(answer.created_time),
                    datetime.datetime.fromtimestamp(answer.updated_time), answer.voteup_count, answer.comment_count, answer.thanks_count
                    ]
        except:
            logging.error(question.title+'******'+answer.author.name+'\n'+'-'*60+'\n'+traceback.format_exc()+'-'*60+'\n')
        # print(answer.author.name, answer.voteup_count)
        finally:
            sheet.append(item_data)
            # answer.save(question.title)
    if num % 10 == 0:
        wb.save('知乎回答-{}.xlsx'.format('男士护肤'))