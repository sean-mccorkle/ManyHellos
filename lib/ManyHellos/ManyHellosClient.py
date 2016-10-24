# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class ManyHellos(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def manyHellos(self, input_params, context=None):
        """
        :param input_params: instance of type "ManyHellosInputParams" (Main
           service call:  manyHellos()) -> structure: parameter "hello_msg"
           of String, parameter "num_jobs" of Long, parameter "time_limit" of
           Long
        :returns: instance of type "ManyHellosOutputObj"
        """
        return self._client.call_method(
            'ManyHellos.manyHellos',
            [input_params], self._service_ver, context)

    def manyHellos_prepare(self, input_params, context=None):
        """
        :param input_params: instance of type "ManyHellos_prepareInputParams"
           (prepare()) -> structure: parameter "num_jobs" of Long
        :returns: instance of type "ManyHellos_prepareResult"
        """
        return self._client.call_method(
            'ManyHellos.manyHellos_prepare',
            [input_params], self._service_ver, context)

    def manyHellos_runEach(self, input_params, context=None):
        """
        :param input_params: instance of type "ManyHellos_runEachInputParams"
           (runEach()) -> structure: parameter "job_number" of Long
        :returns: instance of type "ManyHellos_runEachResult"
        """
        return self._client.call_method(
            'ManyHellos.manyHellos_runEach',
            [input_params], self._service_ver, context)

    def manyHellos_collect(self, input_params, context=None):
        """
        :param input_params: instance of type "ManyHellos_collectInputParams"
           (collect()) -> structure: parameter "num_jobs" of Long
        :returns: instance of type "ManyHellos_collectResult"
        """
        return self._client.call_method(
            'ManyHellos.manyHellos_collect',
            [input_params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('ManyHellos.status',
                                        [], self._service_ver, context)
