"""
!/usr/bin/env python
-*- coding: utf-8 -*-
author： zhouys
email： zhouys618@163.com
datetime： 2022/5/24 23:55 
ide： PyCharm
"""
from fastapi import APIRouter, FastAPI

from fast import views


def router_v1():
    router = APIRouter()
    router.include_router(views.router, tags=['Article'])
    return router


def init_routers(app: FastAPI):
    app.include_router(router_v1(), prefix='/api/v1', tags=['v1'])
