# coding=utf-8
import sys, os, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ['DJANGO_SETTINGS_MODULE'] = 'collectBugs.settings'
django.setup()

from base.models import Bugs
import itchat
from itchat.content import *


def console_log(string):
    """输出调试信息"""
    output = open('log.txt','w')
    output.write(str(string))


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def get_text(msg):
    """处理消息"""
    pass

COLLECT_BUGS_BEGIN = False  #开始收集BUG
COLLECT_BUGS_END = False    #收集结束
BUGS = ""  #BUGS
IMGS = ""   #图片
USER = ''   #用户
PROJECT_NAME = '' #项目名称
FLAG_START = '#{'
FLAG_END = '}'

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO], isGroupChat=True)
def download_files(msg):
    """收集图片"""
    if msg['ActualNickName'] == USER:
        global IMGS
        msg.download('static/'+msg.fileName)
        IMGS += msg.fileName+','


@itchat.msg_register(TEXT, isGroupChat=True)
def get_text(msg):
    """收集消息"""
    global COLLECT_BUGS_BEGIN,  COLLECT_BUGS_END, BUGS, USER, IMGS, PROJECT_NAME
    start = msg.Content.startswith
    if start(FLAG_START):
        COLLECT_BUGS_BEGIN = True
        COLLECT_BUGS_END = False
        BUGS = ""
        IMGS = ""
        USER = msg['ActualNickName']
        PROJECT_NAME = msg.User.NickName
        print '开始接收'
    elif COLLECT_BUGS_BEGIN and start(FLAG_END):
        COLLECT_BUGS_END = True
        COLLECT_BUGS_BEGIN = False

    if COLLECT_BUGS_BEGIN and msg['ActualNickName']==USER:
        bug = msg['Content'].replace(FLAG_START,'')
        if bug: BUGS += bug+','
    if COLLECT_BUGS_END:
        COLLECT_BUGS_END = False
        Bugs.objects.create(user=USER, projectName=PROJECT_NAME, content=BUGS, img=IMGS)
        print '接收完成'
        itchat.send(u'@%s\u2005 %s' % (msg['ActualNickName'], u'已接收'),msg['FromUserName'])

itchat.auto_login(hotReload=True)
itchat.run(True)