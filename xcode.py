#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import logging
import sys

logging.basicConfig(level=logging.DEBUG)

__author__ = 'batman'


def get_pycurl(url, request_type=None, data=None):
    headers = {"Content-Type": "application/json"}
    if request_type is None or request_type == 'GET':
        result = requests.get(url=url, headers=headers, verify=False)
        return result
    elif request_type == 'POST' and data is not None:
        result = requests.post(url=url, headers=headers, verify=False, data=data)
        return result
    elif request_type == 'POST' and data is None:
        result = requests.post(url=url, headers=headers, verify=False)
        return result
    elif request_type == 'PATCH' and data is not None:
        result = requests.patch(url=url, headers=headers, verify=False, data=data)
        return result
    elif request_type == 'DELETE':
        result = requests.delete(url=url, headers=headers, verify=False)
        return result.status_code
    else:
        print 'Some shit happened!'
        sys.exit(1)


class XCODE_API_MODULE(object):
    def __init__(self, **kwargs):
        self.host = kwargs['host']

    def get_all_bots(self):
        try:
            result = get_pycurl('https://' + self.host + ':20343/api/bots')
        except Exception as err_mgs:
            print err_mgs
            sys.exit(1)
        return result if result is dict else result.status_code

    def post_duplicate_bot(self, bot_id, body):
        try:
            result = get_pycurl('https://' + self.host + ':20343/api/bots/' + bot_id + '/duplicate',
                                request_type='POST', data=body)
        except Exception as err_msg:
            print err_msg
            sys.exit(1)
        return result if result is dict else result.status_code

    def patch_update_bot(self, bot_id, body):
        try:
            result = get_pycurl('https://' + self.host + ':20343/api/bots' + bot_id, request_type='PATCH',
                                data=body)
        except Exception as err_msg:
            print err_msg
            sys.exit(1)
        return result if result is dict else result.status_code

    def delete_bot(self, bot_id):
        try:
            result = get_pycurl('https://' + self.host + ':20343/api/bots/' + bot_id, request_type='DELETE')
            return result
        except Exception as err_msg:
            print err_msg
            sys.exit(1)

    def post_create_integration(self, bot_id, body):
        try:
            result = get_pycurl('https://' + self.host + ':20343/api/bots/' + bot_id + '/integrations',
                                request_type='POST', data=body)
        except Exception as err_msg:
            print err_msg
            sys.exit(1)
        return result if result is dict else result.status_code

    def get_retrieving_integration(self, integration_id):
        try:
            result = get_pycurl('https://' + self.host + ':20343/api/integrations/' + integration_id)
        except Exception as err_msg:
            print err_msg
            sys.exit(1)
        return result if result is dict else result.status_code

    def delete_integration(self, integration_id):
        try:
            result = get_pycurl('https://' + self.host + ':20343/api/integrations/' + integration_id,
                                request_type='DELETE')
        except Exception as err_msg:
            print err_msg
            sys.exit(1)
        return result if result is dict else result.status_code

    def post_canceling_integration(self, integration_id):
        try:
            result = get_pycurl('https://' + self.host + ':20343/api/integrations/' + integration_id + '/cancel',
                                request_type='POST')
        except Exception as err_msg:
            print err_msg
            sys.exit(1)
        return result if result is dict else result.status_code

    def get_filtering_integration_for_current_bot(self, bot_id, integration_filter, type_integration_filter):
        try:
            result = get_pycurl(
                'https://' + self.host + ':20343/api/bots/' + bot_id + '/integrations?' + integration_filter + '=' +
                type_integration_filter)
        except Exception as err_msg:
            print err_msg
            sys.exit(1)
        return result if result is dict else result.status_code

    def get_filtering_integration_for_all_bots(self, integration_filter, type_integration_filter):
        try:
            result = get_pycurl(
                'https://' + self.host + ':20343/api/bots/integrations?' + integration_filter + '=' +
                type_integration_filter)
        except Exception as err_msg:
            print err_msg
            sys.exit(1)
        return result if result is dict else result.status_code

    def get_retrieving_files_for_integration(self, integration_id):
        try:
            result = get_pycurl('https://' + self.host + ':20343/api/integrations/' + integration_id + '/files')
        except Exception as err_msg:
            print err_msg
            sys.exit(1)
        return result if result is dict else result.status_code

    def get_assets(self, path):
        try:
            result = get_pycurl('https://' + self.host + ':20343/api/assets/' + path)
        except Exception as err_msg:
            print err_msg
            sys.exit(1)
        if result.ok:
            result_dict = {
                'content': result.content,
                'url': result.url,
                'links': result.links,
            }
            return result_dict
        else:
            return result.status_code


if __name__ == '__main__':
    f = XCODE_API_MODULE(host='10.10.253.3')
    a = f.get_assets(path='079960823be25a5a83d868a21c00eea9-ios_bot/15/Screenshot_220FAFD9-EBFC-4BFE-84D4-10618997F9D1.jpg')
    print a
