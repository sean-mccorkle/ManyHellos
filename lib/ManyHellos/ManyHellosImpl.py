# -*- coding: utf-8 -*-
#BEGIN_HEADER

from pprint import pprint 
from biokbase.njs_wrapper.client import NarrativeJobService as NJS

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
    GIT_URL = "https://github.com/sean-mccorkle/ManyHellos"
    GIT_COMMIT_HASH = "472e30894078e653d42819b301e6edf674259f58"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        main_message = ""
        number_of_jobs = 0
        time_limit = 0
        #END_CONSTRUCTOR
        pass


    def manyHellos(self, ctx, input_params):
        """
        :param input_params: instance of type "ManyHellosInputParams" (was
           the main service call manyHellos(), now Im not sure what this does
           - initializes, but that should probably be in the constructor?  
           maybe manyHellos_prepare()) -> structure: parameter "hello_msg" of
           String, parameter "time_limit" of Long, parameter
           "njs_wrapper_url" of String, parameter "token" of String
        :returns: instance of type "ManyHellosOutputObj"
        """
        # ctx is the context object
        # return variables are: output_obj
        #BEGIN manyHellos
        print( "Hi this is manyHellos()!" )
        print( "hello_mesg is ", input_params["hello_msg"] )
        print( "time_limit is ", input_params["time_limit"] )
        print( "njs_wrapper_url is ", input_params["njs_wrapper_url"] )
        print( "token is ", input_params["token"] )

        self.main_message = input_params["hello_msg"]
        self.time_limit = input_params["time_limit"]
        self.njs_wrapper_url = input_params["njs_wrapper_url"]
        self.token = input_params["token"]

        output_obj = "manyHellos() default return string"

        print( "this is manyHellos(), signing off!  Bye!" )
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
        :returns: instance of type "ManyHellos_tasklist" -> list of type
           "ManyHellos_task" -> structure: parameter "job_number" of Long
        """
        # ctx is the context object
        # return variables are: tasks
        #BEGIN manyHellos_prepare

        print( "this is manyHellos_prepare..." )
        print( "num_jobs is ", input_params["num_jobs"] )
        self.num_jobs = input_params["num_jobs"];

        tasks = []
        for i in range( self.num_jobs ):
            tasks.append( { 'job_number': i } )

        pprint( ["exiting manyHellos_prepare, tasks is", tasks] )

        #END manyHellos_prepare

        # At some point might do deeper type checking...
        if not isinstance(tasks, list):
            raise ValueError('Method manyHellos_prepare return value ' +
                             'tasks is not type list as required.')
        # return the results
        return [tasks]

    def manyHellos_runEach(self, ctx, task):
        """
        :param task: instance of type "ManyHellos_task" -> structure:
           parameter "job_number" of Long
        :returns: instance of type "ManyHellos_runEachResult" (runEach())
        """
        # ctx is the context object
        # return variables are: res
        #BEGIN manyHellos_runEach
        print( "this is manyHellos_runEach..." )
        pprint( [ "task is ", task] )

        res = "default manyHellos_runEach() result"

        print( "exiting manyHellos_runEach(), res is", res )
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

        print( "this is manyHellos_collect..." )
        print( "num_jobs is ", input_params["num_jobs"] )

        res = "default manyHellos_collect() result"

        print( "exiting manyHellos_collect, res is", res )

        #END manyHellos_collect

        # At some point might do deeper type checking...
        if not isinstance(res, basestring):
            raise ValueError('Method manyHellos_collect return value ' +
                             'res is not type basestring as required.')
        # return the results
        return [res]

    def hi(self, ctx, said):
        """
        :param said: instance of String
        :returns: instance of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN hi
        returnVal = "Hi~~"
        #END hi

        # At some point might do deeper type checking...
        if not isinstance(returnVal, basestring):
            raise ValueError('Method hi return value ' +
                             'returnVal is not type basestring as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
