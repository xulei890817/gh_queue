#!/usr/bin/env python

# encoding: utf-8

'''
 * Create File d_error
 * Created by leixu on 2018/9/27
 * IDE PyCharm
'''


class NoValueError(Exception):
    def __str__(self):
        return "queue is empty,no value get!"


class GetValueTimeOutError(Exception):
    def __str__(self):
        return "get value timeout!"
