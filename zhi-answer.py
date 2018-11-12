# -*- coding=utf-8 -*-
import os, datetime, re
from openpyxl import Workbook
from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException

question_id = input('请输入问题id号，获取所有答案：')
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

question = client.question(int(question_id))
print(question.title)
wb = Workbook()
sheet = wb.active
sheet.title = "知乎"
item_name = ['time_now', 'content', 'author', 'gender', 'loc', 'business', 'company', 'job', 'created_time', 'updated_time', 'voteup_count', 'comment_count', 'thanks_count']
for j,title in enumerate(item_name):
    sheet.cell(row=1, column=j+1).value = title

for answer in question.answers:
    item_data = [datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')]
    # item_data.append([answer.author.name, answer.can_comment.status, answer.comment_count, answer.comment_permission, answer.content,
    #         answer.created_time, answer.excerpt, answer.is_copyable, answer.is_mine, answer.question, answer.suggest_edit.reason,
    #         answer.thanks_count, answer.updated_time, answer.voteup_count, answer.collections, answer.comments, answer.voters
    #         ])
    gender_dict = {'0': '女', '1': '男', '-1': '不详'}
    loc = ''
    for location in answer.author.locations:
        loc += location.name
    company = ''
    job = ''
    for employment in answer.author.employments:
        if 'company' in employment:
            company += employment.company.name
        if 'job' in employment:
            job += employment.job.name
    item_data += [re.compile(r'<.*?>', re.S).sub('', answer.content), answer.author.name, gender_dict[answer.author.gender],
            loc, answer.author.business.name, company, job, datetime.datetime.fromtimestamp(answer.created_time),
            datetime.datetime.fromtimestamp(answer.updated_time), answer.voteup_count, answer.comment_count, answer.thanks_count
            ]
    print(answer.author.name, answer.voteup_count)
    sheet.append(item_data)
    # answer.save(question.title)
wb.save('知乎回答-{}.xlsx'.format('dota2'))