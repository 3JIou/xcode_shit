#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import logging
import sys

logging.basicConfig(level=logging.DEBUG)

__author__ = 'batman'


def get_pycurl(url, request_type=None, data=None):
    """
    Executes a query on xcode server with requested parameters
    :param url: as string. Full URL for request
    :param request_type: as string. Type of request
    :param data: as string. Body for POST and PATCH request
    :return: as list (or int in case of status_code). Result of request
    """
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
        """
        Initial module of class
        :param kwargs: as list. Some parameters for initialization
        """
        self.host = kwargs['host']

    def get_all_bots(self):
        """
        GET request for getting all bots from xcode server
        :return: as list or int. Result of request
        """
        try:
            result = get_pycurl('https://' + self.host + ':20343/api/bots')
        except Exception as err_mgs:
            print err_mgs
            sys.exit(1)
        return result.json()[u'results'] if result.ok else result.status_code

    def post_duplicate_bot(self, bot_id, body):
        """
        POST request for duplicate bot with some changes
        :param bot_id: as string. Bot for duplicate
        :param body: as string. Some body with changes (like json)
        :return: as list or int. Result of request
        """
        try:
            result = get_pycurl('https://' + self.host + ':20343/api/bots/' + bot_id + '/duplicate',
                                request_type='POST', data=body)
        except Exception as err_msg:
            print err_msg
            sys.exit(1)
        return result.json()[u'results'] if result.ok else result.status_code

    def patch_update_bot(self, bot_id, body):
        """
        PATCH request for update single bot.
        :param bot_id: as string. Bot for updating
        :param body: as string. Some body with change (like json)
        :return: as list or int. Result of request
        """
        try:
            result = get_pycurl('https://' + self.host + ':20343/api/bots' + bot_id, request_type='PATCH',
                                data=body)
        except Exception as err_msg:
            print err_msg
            sys.exit(1)
        return result.json()[u'results'] if result.ok else result.status_code

    def delete_bot(self, bot_id):
        """
        DELETE request for remove single bot
        :param bot_id: as string. Bot for delete
        :return: as list or int. Result of request
        """
        try:
            result = get_pycurl('https://' + self.host + ':20343/api/bots/' + bot_id, request_type='DELETE')
            return result
        except Exception as err_msg:
            print err_msg
            sys.exit(1)

    def post_create_integration(self, bot_id, body):
        """
        POST request for create integration
        :param bot_id: as string. Bot on which to will be created integration
        :param body: as string. Some body with integration model (like json)
        :return: as list or int. Result of request
        """
        try:
            result = get_pycurl('https://' + self.host + ':20343/api/bots/' + bot_id + '/integrations',
                                request_type='POST', data=body)
        except Exception as err_msg:
            print err_msg
            sys.exit(1)
        return result.json()[u'results'] if result.ok else result.status_code

    def get_retrieving_integration(self, integration_id):
        """
        GET request for retrieving single integration
        :param integration_id: as string. Integration id
        :return: as list or int. Result of request
        """
        try:
            result = get_pycurl('https://' + self.host + ':20343/api/integrations/' + integration_id)
        except Exception as err_msg:
            print err_msg
            sys.exit(1)
        return result.json()[u'results'] if result.ok else result.status_code

    def delete_integration(self, integration_id):
        """
        DELETE request for remove single integration
        :param integration_id: as string. Integration id
        :return: as list or int. Result of request
        """
        try:
            result = get_pycurl('https://' + self.host + ':20343/api/integrations/' + integration_id,
                                request_type='DELETE')
        except Exception as err_msg:
            print err_msg
            sys.exit(1)
        return result.json()[u'results'] if result.ok else result.status_code

    def post_canceling_integration(self, integration_id):
        """
        POST request for canceling single integration
        :param integration_id: as string. Integration id
        :return: as list or int. Result of request
        """
        try:
            result = get_pycurl('https://' + self.host + ':20343/api/integrations/' + integration_id + '/cancel',
                                request_type='POST')
        except Exception as err_msg:
            print err_msg
            sys.exit(1)
        return result.json()[u'results'] if result.ok else result.status_code

    def get_filtering_integration_for_current_bot(self, bot_id, integration_filter, type_integration_filter):
        """
        GET request for filtering all integrations of single bot
        :param bot_id: as string. Bot id
        :param integration_filter: as string. May be content {filter,last,number,from,next,prev,count,summary_only}
                                   parameters.
                                   For more examples and details look at: https://goo.gl/x6rKV5
        :param type_integration_filter: as string. There are two filter options: non_fatal and with_build_results.
                                        non_fatal: Integrations with a result of type succeeded, test-failures,
                                                   build-errors, warnings, analyzer-warnings or build-failed.
                                        with_build_results: Integrations containing build summary information.
        :return: as list or int. Result of request
        """
        try:
            result = get_pycurl(
                'https://' + self.host + ':20343/api/bots/' + bot_id + '/integrations?' + integration_filter + '=' +
                type_integration_filter)
        except Exception as err_msg:
            print err_msg
            sys.exit(1)
        return result.json()[u'results'] if result.ok else result.status_code

    def get_filtering_integration_for_all_bots(self, integration_filter, type_integration_filter):
        """
        GET request for filtering all integrations of all bots
        :param integration_filter: as string. May be content {filter,last,number,from,next,prev,count,summary_only}
                                   parameters.
                                   For more examples and details look at: https://goo.gl/x6rKV5
        :param type_integration_filter: as string. There are two filter options: non_fatal and with_build_results.
                                        non_fatal: Integrations with a result of type succeeded, test-failures,
                                                   build-errors, warnings, analyzer-warnings or build-failed.
                                        with_build_results: Integrations containing build summary information.
        :return: as list or int. Result of request
        """
        try:
            result = get_pycurl(
                'https://' + self.host + ':20343/api/bots/integrations?' + integration_filter + '=' +
                type_integration_filter)
        except Exception as err_msg:
            print err_msg
            sys.exit(1)
        return result.json()[u'results'] if result.ok else result.status_code

    def get_retrieving_files_for_integration(self, integration_id):
        """
        GET request for retrieving files of single integration
        :param integration_id: as string. Integration id
        :return: as list or int. Result of request
        """
        try:
            result = get_pycurl('https://' + self.host + ':20343/api/integrations/' + integration_id + '/files')
        except Exception as err_msg:
            print err_msg
            sys.exit(1)
        return result.json()[u'results'] if result.ok else result.status_code

    def get_assets(self, path):
        """
        GET request for getting all assets at the specified path
        :param path: as string. Path for getting assets
        :return: as list or int. Result of request
        """
        try:
            result = get_pycurl('https://' + self.host + ':20343/api/assets/' + path)
        except Exception as err_msg:
            print err_msg
            sys.exit(1)
        if result.ok:
            result_list = {
                'content': result.content,
                'url': result.url,
                'links': result.links,
            }
            return result_list
        else:
            return result.status_code


if __name__ == '__main__':
    test = XCODE_API_MODULE(host='')
