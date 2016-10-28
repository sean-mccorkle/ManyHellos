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

    def _manyHellos_submit(self, input_params, context=None):
        return self._client._submit_job(
             'ManyHellos.manyHellos', [input_params],
             self._service_ver, context)

    def manyHellos(self, input_params, context=None):
        """
        :param input_params: instance of type "ManyHellosInputParams" (was
           the main service call manyHellos(), now Im not sure what this does
           - initializes, but that should probably be in the constructor?  
           maybe manyHellos_prepare()) -> structure: parameter "hello_msg" of
           String, parameter "time_limit" of Long, parameter "token" of String
        :returns: instance of type "ManyHellosOutputObj"
        """
        job_id = self._manyHellos_submit(input_params, context)
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

    def manyHellos_prepare(self, input_params, context=None):
        """
        :param input_params: instance of type "ManyHellos_prepareInputParams"
           (prepare()) -> structure: parameter "msg" of String, parameter
           "num_jobs" of Long, parameter "workspace" of String
        :returns: instance of type "ManyHellos_tasklist" -> list of type
           "ManyHellos_task" -> structure: parameter "msg" of String,
           parameter "job_number" of Long, parameter "workspace" of String
        """
        return self._client.call_method(
            'ManyHellos.manyHellos_prepare',
            [input_params], self._service_ver, context)

    def _manyHellos_runEach_submit(self, task, context=None):
        return self._client._submit_job(
             'ManyHellos.manyHellos_runEach', [task],
             self._service_ver, context)

    def manyHellos_runEach(self, task, context=None):
        """
        :param task: instance of type "ManyHellos_task" -> structure:
           parameter "msg" of String, parameter "job_number" of Long,
           parameter "workspace" of String
        :returns: instance of type "ManyHellos_runEachResult" (runEach())
        """
        job_id = self._manyHellos_runEach_submit(task, context)
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

    def manyHellos_collect(self, input_params, context=None):
        """
        :param input_params: instance of type "ManyHellos_collectInputParams"
           (collect()) -> structure: parameter "num_jobs" of Long
        :returns: instance of type "ManyHellos_collectResult"
        """
        return self._client.call_method(
            'ManyHellos.manyHellos_collect',
            [input_params], self._service_ver, context)

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

    def _run_narrative_submit(self, said, context=None):
        return self._client._submit_job(
             'ManyHellos.run_narrative', [said],
             self._service_ver, context)

    def run_narrative(self, said, context=None):
        """
        :param said: instance of String
        :returns: instance of String
        """
        job_id = self._run_narrative_submit(said, context)
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
