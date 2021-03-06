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
import time


class ManyHellos(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login',
            service_ver=None,
            async_job_check_time_ms=100, async_job_check_time_scale_percent=150, 
            async_job_check_max_time_ms=300000):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = service_ver
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc,
            async_job_check_time_ms=async_job_check_time_ms,
            async_job_check_time_scale_percent=async_job_check_time_scale_percent,
            async_job_check_max_time_ms=async_job_check_max_time_ms)

    def _check_job(self, job_id):
        return self._client._check_job('ManyHellos', job_id)

    def manyHellos(self, input_params, context=None):
        """
        :param input_params: instance of type "ManyHellosInputParams"
           (hello_msg - what to print as the message, time_limit - how long
           the program will run, in seconds, workspace - used to store
           report(s).) -> structure: parameter "hello_msg" of String,
           parameter "num_jobs" of Long, parameter "time_limit" of Long,
           parameter "workspace" of String
        :returns: instance of type "ManyHellos_globalResult" -> structure:
           parameter "output" of String, parameter "jobs" of list of tuple of
           size 2: parameter "job_number" of Long, parameter "message" of
           String
        """
        return self._client.call_method(
            'ManyHellos.manyHellos',
            [input_params], self._service_ver, context)

    def manyHellos_prepare(self, prepare_params, context=None):
        """
        :param prepare_params: instance of type
           "ManyHellos_prepareInputParams" -> structure: parameter
           "global_method" of type "FullMethodQualifier" -> structure:
           parameter "module_name" of String, parameter "method_name" of
           String, parameter "service_ver" of String, parameter
           "global_input_params" of type "ManyHellos_globalInputParams"
           (prepare()) -> structure: parameter "msg" of String, parameter
           "num_jobs" of Long, parameter "workspace" of String
        :returns: instance of type "ManyHellos_prepareSchedule" -> structure:
           parameter "tasks" of list of type "ManyHellos_runEachInput" ->
           structure: parameter "method" of type "FullMethodQualifier" ->
           structure: parameter "module_name" of String, parameter
           "method_name" of String, parameter "service_ver" of String,
           parameter "input_arguments" of tuple of size 1: type
           "ManyHellos_task" -> structure: parameter "msg" of String,
           parameter "job_number" of Long, parameter "workspace" of String,
           parameter "collect_method" of type "FullMethodQualifier" ->
           structure: parameter "module_name" of String, parameter
           "method_name" of String, parameter "service_ver" of String
        """
        return self._client.call_method(
            'ManyHellos.manyHellos_prepare',
            [prepare_params], self._service_ver, context)

    def manyHellos_runEach(self, task, context=None):
        """
        :param task: instance of type "ManyHellos_task" -> structure:
           parameter "msg" of String, parameter "job_number" of Long,
           parameter "workspace" of String
        :returns: instance of type "ManyHellos_runEachResult" (runEach()) ->
           structure: parameter "message" of String
        """
        return self._client.call_method(
            'ManyHellos.manyHellos_runEach',
            [task], self._service_ver, context)

    def manyHellos_collect(self, collect_params, context=None):
        """
        :param collect_params: instance of type
           "ManyHellos_collectInputParams" -> structure: parameter
           "global_params" of type "ManyHellos_globalInputParams" (prepare())
           -> structure: parameter "msg" of String, parameter "num_jobs" of
           Long, parameter "workspace" of String, parameter
           "input_result_pairs" of list of type "ManyHellos_InputResultPair"
           (collect()) -> structure: parameter "input" of type
           "ManyHellos_runEachInput" -> structure: parameter "method" of type
           "FullMethodQualifier" -> structure: parameter "module_name" of
           String, parameter "method_name" of String, parameter "service_ver"
           of String, parameter "input_arguments" of tuple of size 1: type
           "ManyHellos_task" -> structure: parameter "msg" of String,
           parameter "job_number" of Long, parameter "workspace" of String,
           parameter "result" of type "ManyHellos_runEachResult" (runEach())
           -> structure: parameter "message" of String
        :returns: instance of type "ManyHellos_globalResult" -> structure:
           parameter "output" of String, parameter "jobs" of list of tuple of
           size 2: parameter "job_number" of Long, parameter "message" of
           String
        """
        return self._client.call_method(
            'ManyHellos.manyHellos_collect',
            [collect_params], self._service_ver, context)

    def _hi_submit(self, said, context=None):
        return self._client._submit_job(
             'ManyHellos.hi', [said],
             self._service_ver, context)

    def hi(self, said, context=None):
        """
        :param said: instance of String
        :returns: instance of String
        """
        job_id = self._hi_submit(said, context)
        async_job_check_time = self._client.async_job_check_time
        while True:
            time.sleep(async_job_check_time)
            async_job_check_time = (async_job_check_time *
                self._client.async_job_check_time_scale_percent / 100.0)
            if async_job_check_time > self._client.async_job_check_max_time:
                async_job_check_time = self._client.async_job_check_max_time
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def status(self, context=None):
        return self._client.call_method('ManyHellos.status',
                                        [], self._service_ver, context)
