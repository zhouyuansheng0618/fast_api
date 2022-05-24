"""
!/usr/bin/env python
-*- coding: utf-8 -*-
author： zhouys
email： zhouys618@163.com
datetime： 2022/5/24 23:54 
ide： PyCharm
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from fast.dependencies import CommonQueryParams, get_db
from fast.schemas import (ArticleSchema, CreateArticleSchema,
                                  UpdateArticleSchema)
from fast.services import ArticleService

router = APIRouter()

_service = ArticleService()


@router.get('/articles')
def get(
        session: Session = Depends(get_db),
        commons: CommonQueryParams = Depends()
):
    return _service.get(session, offset=commons.offset, limit=commons.limit)


@router.get('/articles/{pk}')
def get_by_id(
        pk: int,
        session: Session = Depends(get_db)
):
    return _service.get_by_id(session, pk)


@router.post('/articles', response_model=ArticleSchema)
def create(
        obj_in: CreateArticleSchema,
        session: Session = Depends(get_db),
):
    return _service.create(session, obj_in)


@router.patch('/articles/{pk}', response_model=ArticleSchema)
def patch(
        pk: int,
        obj_in: UpdateArticleSchema,
        session: Session = Depends(get_db)
):
    return _service.patch(session, pk, obj_in)


@router.delete('/articles/{pk}')
def delete(
        pk: int,
        session: Session = Depends(get_db)
):
    return _service.delete(session, pk)
