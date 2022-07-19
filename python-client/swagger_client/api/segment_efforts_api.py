# coding: utf-8

"""
    Strava API v3

    The [Swagger Playground](https://developers.strava.com/playground) is the easiest way to familiarize yourself with the Strava API by submitting HTTP requests and observing the responses before you write any client code. It will show what a response will look like with different endpoints depending on the authorization scope you receive from your athletes. To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. Please note, we only support Swagger 2.0. There is a known issue where you can only select one scope at a time. For more information, please check the section “client code” at https://developers.strava.com/docs.  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SegmentEffortsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_efforts_by_segment_id(self, segment_id, **kwargs):  # noqa: E501
        """List Segment Efforts  # noqa: E501

        Returns a set of the authenticated athlete's segment efforts for a given segment.  Requires subscription.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_efforts_by_segment_id(segment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int segment_id: The identifier of the segment. (required)
        :param datetime start_date_local: ISO 8601 formatted date time.
        :param datetime end_date_local: ISO 8601 formatted date time.
        :param int per_page: Number of items per page. Defaults to 30.
        :return: list[DetailedSegmentEffort]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_efforts_by_segment_id_with_http_info(segment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_efforts_by_segment_id_with_http_info(segment_id, **kwargs)  # noqa: E501
            return data

    def get_efforts_by_segment_id_with_http_info(self, segment_id, **kwargs):  # noqa: E501
        """List Segment Efforts  # noqa: E501

        Returns a set of the authenticated athlete's segment efforts for a given segment.  Requires subscription.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_efforts_by_segment_id_with_http_info(segment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int segment_id: The identifier of the segment. (required)
        :param datetime start_date_local: ISO 8601 formatted date time.
        :param datetime end_date_local: ISO 8601 formatted date time.
        :param int per_page: Number of items per page. Defaults to 30.
        :return: list[DetailedSegmentEffort]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['segment_id', 'start_date_local', 'end_date_local', 'per_page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_efforts_by_segment_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'segment_id' is set
        if self.api_client.client_side_validation and ('segment_id' not in params or
                                                       params['segment_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `segment_id` when calling `get_efforts_by_segment_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'segment_id' in params:
            query_params.append(('segment_id', params['segment_id']))  # noqa: E501
        if 'start_date_local' in params:
            query_params.append(('start_date_local', params['start_date_local']))  # noqa: E501
        if 'end_date_local' in params:
            query_params.append(('end_date_local', params['end_date_local']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('per_page', params['per_page']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['strava_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/segment_efforts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[DetailedSegmentEffort]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_segment_effort_by_id(self, id, **kwargs):  # noqa: E501
        """Get Segment Effort  # noqa: E501

        Returns a segment effort from an activity that is owned by the authenticated athlete. Requires subscription.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_segment_effort_by_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The identifier of the segment effort. (required)
        :return: DetailedSegmentEffort
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_segment_effort_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_segment_effort_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_segment_effort_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get Segment Effort  # noqa: E501

        Returns a segment effort from an activity that is owned by the authenticated athlete. Requires subscription.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_segment_effort_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The identifier of the segment effort. (required)
        :return: DetailedSegmentEffort
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_segment_effort_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_segment_effort_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['strava_oauth']  # noqa: E501

        return self.api_client.call_api(
            '/segment_efforts/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DetailedSegmentEffort',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
