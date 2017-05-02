# encoding=utf-8
import sys, os, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ['DJANGO_SETTINGS_MODULE'] = 'collectBugs.settings'
django.setup()

from base.models import Bugs
import itchat
from itchat.content import *


CONTENT = {}
START = 'BUG:'
END = ':END'


@itchat.msg_register([TEXT, PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def receive(msg):
    """接收信息"""
    user = msg.ActualNickName

    if user in CONTENT:
        if msg.Type == 'Text':
            content = msg.text if msg.text != END else ''
        elif msg.Type == 'Picture':
            content = "img:" + msg.fileName
            msg.download('static/'+msg.fileName)
        CONTENT[user].append(content)

    if msg.Type == TEXT:
        if msg.text.startswith(START):
            CONTENT[user] = []
        elif msg.text.endswith(END) and user in CONTENT:
            bugs = ','.join(CONTENT[user])
            Bugs.objects.create(user=user, projectName=msg.User.NickName, content=bugs)
            del CONTENT[user]


itchat.auto_login(hotReload=True)
itchat.run(True)