"""
!/usr/bin/env python
-*- coding: utf-8 -*-
author： zhouys
email： zhouys618@163.com
datetime： 2022/5/24 23:55 
ide： PyCharm
"""
from typing import Callable

from fastapi import FastAPI, Request, Response

from fast.db import SessionFactory


async def db_session_middleware(request: Request, call_next: Callable) -> Response:
    response = Response('Internal server error', status_code=500)
    try:
        request.state.db = SessionFactory()
        response = await call_next(request)
    finally:
        request.state.db.close()

    return response


def init_middleware(app: FastAPI) -> None:
    app.middleware('http')(db_session_middleware)
