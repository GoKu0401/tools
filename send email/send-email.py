from smtplib import SMTP_SSL        # 加密传输服务协议
from email.header import Header     # 添加主题内容
from email.mime.text import MIMEText   # 用于创建邮件的模块


def send_email(to_addr):
    # 1. 选择一个邮箱作为发送工具
    smtp_server = 'smtp.qq.com'   # 邮箱服务器
    from_addr = ''   # 发送者邮箱
    password = ''   # smtp 授权码 (需要到邮箱里面开启smtp服务，再生产授权码)

    # 创建一封邮件
    text = ''
    email = MIMEText(text, 'plain', 'utf-8')
    email['Subject'] = Header('')    # 邮件主题
    email['From'] = Header(from_addr)  # 设置发送人
    email['To'] = Header(to_addr)   # 设置接收人

    # 3 发送邮件
    smtp = SMTP_SSL(smtp_server)
    smtp.login(from_addr, password)
    smtp.sendmail(from_addr, to_addr, email.as_string())
    smtp.quit()


if __name__ == '__main__':
    to_addr = ''
    send_email(to_addr)
