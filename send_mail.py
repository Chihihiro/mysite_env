import os
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite_env.settings'

if __name__ == '__main__':

    subject, from_email, to = '来自632207812@qq.com的测试邮件', '632207812@qq.com', '632207812@qq.com'
    text_content = '欢迎访问，这里是中午吃啥的站点'
    html_content = '<p>欢迎访问<a href="http://www.liujiangblog.com" target=blank>www.liujiangblog.com</a>，这里是中午吃啥</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

    # send_mail(
    #     '来自632207812@qq.com的测试邮件',#邮件标题
    #     '欢迎访问，这里是中午吃啥的站点',#邮件正文
    #     '632207812@qq.com',#发件人
    #     ['632207812@qq.com'],#收件人列表5
    # )