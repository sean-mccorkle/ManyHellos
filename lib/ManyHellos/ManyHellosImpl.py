# -*- coding: utf-8 -*-
#BEGIN_HEADER
#END_HEADER


class ManyHellos:
    '''
    Module Name:
    ManyHellos

    Module Description:
    This is a single-language prototype for parallel subjob execution.  All this
does is run several "hello world" programs.
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/sean-mccorkle/ManyHellos.git"
    GIT_COMMIT_HASH = "b50816e9b2bb933a040909ddbb594c0db5b6ff53"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        #END_CONSTRUCTOR
        pass


    def manyHellos(self, ctx, input_params):
        """
        :param input_params: instance of type "ManyHellosInputParams" (Main
           service call:  manyHellos()) -> structure: parameter "hello_msg"
           of String, parameter "num_jobs" of Long, parameter "time_limit" of
           Long
        :returns: instance of type "ManyHellosOutputObj"
        """
        # ctx is the context object
        # return variables are: output_obj
        #BEGIN manyHellos
        #END manyHellos

        # At some point might do deeper type checking...
        if not isinstance(output_obj, basestring):
            raise ValueError('Method manyHellos return value ' +
                             'output_obj is not type basestring as required.')
        # return the results
        return [output_obj]

    def manyHellos_prepare(self, ctx, input_params):
        """
        :param input_params: instance of type "ManyHellos_prepareInputParams"
           (prepare()) -> structure: parameter "num_jobs" of Long
        :returns: instance of type "ManyHellos_prepareResult"
        """
        # ctx is the context object
        # return variables are: res
        #BEGIN manyHellos_prepare
        #END manyHellos_prepare

        # At some point might do deeper type checking...
        if not isinstance(res, basestring):
            raise ValueError('Method manyHellos_prepare return value ' +
                             'res is not type basestring as required.')
        # return the results
        return [res]

    def manyHellos_runEach(self, ctx, input_params):
        """
        :param input_params: instance of type "ManyHellos_runEachInputParams"
           (runEach()) -> structure: parameter "job_number" of Long
        :returns: instance of type "ManyHellos_runEachResult"
        """
        # ctx is the context object
        # return variables are: res
        #BEGIN manyHellos_runEach
        #END manyHellos_runEach

        # At some point might do deeper type checking...
        if not isinstance(res, basestring):
            raise ValueError('Method manyHellos_runEach return value ' +
                             'res is not type basestring as required.')
        # return the results
        return [res]

    def manyHellos_collect(self, ctx, input_params):
        """
        :param input_params: instance of type "ManyHellos_collectInputParams"
           (collect()) -> structure: parameter "num_jobs" of Long
        :returns: instance of type "ManyHellos_collectResult"
        """
        # ctx is the context object
        # return variables are: res
        #BEGIN manyHellos_collect
        #END manyHellos_collect

        # At some point might do deeper type checking...
        if not isinstance(res, basestring):
            raise ValueError('Method manyHellos_collect return value ' +
                             'res is not type basestring as required.')
        # return the results
        return [res]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
