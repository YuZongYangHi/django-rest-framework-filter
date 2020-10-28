#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Filter(object):

    def __init__(self, request=None, model=None, extra=None, **kwargs):
        self.extra = extra if extra else {}
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
                        self.parame[new] = v.strip()

            if self.parame.get("deleted"):
                self.parame["deleted"] = False if self.parame["deleted"] == "false" else True
            self.parame = dict(self.extra, **self.parame)

    def filter(self, q=None):
        if self.parame:
            if q:
                self.parame = dict(self.parame, **q)
            queryset = self.model.objects.filter(**self.parame)
            return queryset
        return self.model.objects.all()
