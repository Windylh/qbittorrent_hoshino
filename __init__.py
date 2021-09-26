# -*- coding: utf-8 -*-
import json
import asyncio
import re
from typing import Optional
from nonebot import CommandSession

from hoshino import Service, priv
from .qbClient import qbClient

sv = Service('qbittorrent', enable_on_default=False, manage_priv=priv.SUPERUSER)

qbit = qbClient('http://ip:8080/', 'admin', 'password') # web ui配置
categorys = ['anime', 'movies', 'others', None] # 分类名称

mission = qbit.mission_list()

@sv.on_command('qblink')
async def _(session: CommandSession):
    _ = session.current_arg_text.strip().split(' ')
    if len(_) == 2:
        category, link = _[0], _[1]
    elif len(_) == 1:
        link = _[0]
        category = None
    else:
        return await session.send(f'格式错误')
    if not re.match("^(magnet:\?xt=urn:btih:)[0-9a-fA-F]{40}.*", link):
        return await session.send(f'链接格式错误')
    if category not in categorys:
        return await session.send(f'类型格式错误')
    msg = qbit.link_download(link, category)
    if msg:
        return await session.send(msg)
    return await session.send(f'添加链接下载成功')
    


@sv.on_command('qbfile')
async def _(session: CommandSession):
    _ = session.current_arg_text.strip().split(' ')
    if len(_) == 2:
        category, link = _[0], _[1]
    elif len(_) == 1:
        link = _[0]
        category = None
    else:
        return await session.send(f'格式错误')
    if category not in categorys:
        return await session.send(f'类型格式错误')
    msg = qbit.link_download(link, category)
    if msg:
        return await session.send(msg)
    return await session.send(f'添加链接下载成功')


@sv.on_command('qblist')
async def _(session: CommandSession):
    mission_list = qbit.mission_list()
    msg = ""
    for mission in mission_list:
        msg += "\n"+ ",".join(list(mission.values()))
    await session.send(f'hash,名称,分类,进度,状态{msg}')
