from collections import defaultdict

from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Event, Bot
from nonebot.adapters.cqhttp import Message

import pymysql as db


osutest = on_command('osutest')

@osutest.handle()
async def _(bot: Bot, event: Event, state: T_State):
    username = str(event.get_message()).strip()
    if username == "":
        username = str(event.get_user_id())
        try:
            #await osubinding.send("正在连接数据库...")
            conndb = db.Connect(host = '127.0.0.1',
                                port = 3306,
                                user = 'osusql',
                                passwd = 'S3FS4TLkkHXpny3M',
                                db = 'osusql',
                                charset = 'utf8')
            #await osubinding.send("数据库已连接")
        except:
            await osubinding.send("数据库连接失败")
        cur = conndb.cursor()
        sql="""select `Osuid` from `binding` WHERE `QQid`={}
        """.format(str(event.get_user_id()))
        try:
            cur.execute(sql)
            conndb.commit()
            username = str(cur.fetchone())
        except Exception as e:
            await osubinding.send("您好像还没有绑定信息~\n"+str(e))
        cur.close()
        conndb.close()

    
    await osutest.send("玩家 "+username+" 您好❤")
    
   
   
    
osubinding = on_command('osubinding')

@osubinding.handle()
async def _(bot: Bot, event: Event, state: T_State):
    osuid = str(event.get_message()).strip()
    if osuid == "":
        await osubinding.send("这里会写一些绑定的须知")
    else:
        try:
            #await osubinding.send("正在连接数据库...")
            conndb = db.Connect(host = '127.0.0.1',
                                port = 3306,
                                user = 'osusql',
                                passwd = 'S3FS4TLkkHXpny3M',
                                db = 'osusql',
                                charset = 'utf8')
            #await osubinding.send("数据库已连接")
        except:
            await osubinding.send("数据库连接失败")
        cur = conndb.cursor()
        sql="""INSERT INTO `osusql`.`binding` (`QQid`, `Osuid`, `passwd`) 
        VALUES ('{}', '{}', '{}')
        """.format(str(event.get_user_id()),osuid,'0')
        try:
            cur.execute(sql)
            conndb.commit()
            await osubinding.send("绑定信息记录成功\nhttps://osu.ppy.sh/users/"+osuid)
        except Exception as e:
            await osubinding.send("绑定信息记录失败\n"+str(e))
        cur.close()
        conndb.close()