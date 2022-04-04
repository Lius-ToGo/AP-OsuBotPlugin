from collections import defaultdict

from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Event, Bot
from nonebot.adapters.cqhttp import Message

from src.libraries.MySQLConnect import MySQLConnect as MConn
import requests


#=======================================================

osutest = on_command('osutest')

@osutest.handle()
async def _(bot: Bot, event: Event, state: T_State):
    username = str(event.get_message()).strip()
    if username == "":
        username = str(event.get_user_id())
    sql="""select `Osuid` from `binding` WHERE `QQid`={}
        """.format(username)
        
    inf=MConn.executeselect(sql)
    if inf[-1]=='0':
        await osutest.send("难道是服务器寄了吗~\n"+str(inf))
    else:
        await osutest.send("玩家 {} 您好❤" .format(inf[0])) 




osubinding = on_command('osubinding')

@osubinding.handle()
async def _(bot: Bot, event: Event, state: T_State):
    osuid = str(event.get_message()).strip()
    if osuid == "":
        await osubinding.send("这里会写一些绑定的须知")
    else:
        url=reditlist(osuid)
        sql="""INSERT INTO `osusql`.`binding` (`QQid`, `Osuid`, `url`) 
        VALUES ('{}', '{}', '{}')
        """.format(str(event.get_user_id()),osuid,url)
        er=MConn.execute(sql)
        if er != '0':
            await osubinding.send("绑定信息记录成功\n"+url)
        else:
            await osubinding.send("绑定信息记录失败\n"+str(e))


def reditlist(osuid):
    url = "https://osu.ppy.sh/users/"+osuid
    r = requests.get(url,headers={"Content-Type":"application/json"})
    reditList = r.history#地址序列
    return reditList[len(reditList)-1].headers["location"]
    
    
    
osuunbind = on_command('osuunbind')

@osuunbind.handle()
async def _(bot: Bot, event: Event, state: T_State):
    sql = 'DELETE FROM `osusql`.`binding` WHERE `binding`.`QQid` = {}'.format(str(event.get_user_id()))
    er=MConn.execute(sql)
    if er != '0':
        await osuunbind.send("绑定信息删除成功")
    else:
        await osuunbind.send("绑定信息删除失败\n"+str(e))
        
        
        
osuava = on_command('osuava')

@osuava.handle()
async def _(bot: Bot, event: Event, state: T_State):
    QQid = str(event.get_user_id())
    sql="""select `url` from `binding` WHERE `QQid`={}
    """.format(QQid)
    inf=MConn.executeselect(sql)
    if inf[-1]=='0':
        await osuava.finish("难道是服务器寄了吗~\n"+str(inf))
    else:
        osuidnumber=inf[0].split('/')[-1]
        avaurl='https://a.ppy.sh/{0}?{0}.jpeg'.format(osuidnumber)
        message = Message([ MessageSegment(type='image', data={'url':avaurl})])
        await osuava.finish(message)