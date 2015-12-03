#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Robin Yang'

import goslate

gs = goslate.Goslate()
print gs.translate('你快乐么？', 'en', 'zh-CN')
