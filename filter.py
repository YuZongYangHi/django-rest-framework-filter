#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ops_platform.settings")
django.setup()
from assets import models
from common.utils.custom_response import JsonResponse
from rest_framework import status
from decimal import Decimal, getcontext
from django.forms.models import model_to_dict
from  django.db.models import Q


class Filter(object):

    def __init__(self, request=None, model=None, **kwargs):
        self.request = request
        self.data = []
        self.request = request
        self.model = model
        self.parame = {}
        self.kwargs = kwargs
        if self.request:
            self._init()

    def _init(self):
        if self.request:
            for k, v in self.request.query_params.items():
                for source, new in self.kwargs.items():
                    if source == k:
                        self.parame[new] = v

    def reset(self):
        self.data = [] if self.data else []

    @staticmethod
    def count(**kwargs):
        assert len(kwargs) != 0

        dicts = {}
        data = []
        for field, model in kwargs.items():
            dicts[field] = model.objects.all().count()
        data.append(dicts)
        return data

    def filter(self, tag):
        if self.parame:
            queryset = self.model.objects.filter(**self.parame).order_by('-id')
            return queryset
        return self.model.objects.all().order_by(tag)


if __name__ == '__main__':
    pass
