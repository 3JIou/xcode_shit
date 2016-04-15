#!/usr/bin/python
# -*- coding: utf-8 -*-
from xcode import XCODE_API_MODULE
from dict2xml import dict2xml as to_xml

__title__ = 'xcode_api'
__author__ = 'batman'
__version__ = '0.1'

def azaza():
    # Just for test dict2xml lib
    # Bamboo can't parse json :(( suffer and crying
    test = XCODE_API_MODULE(host='')

    b = test.get_all_bots()
    print to_xml(b, wrap="all", indent="  ")

if __name__ == '__main__':
    azaza()