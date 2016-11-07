# -*- coding: utf-8 -*-
#BEGIN_HEADER

from pprint import pprint 
from biokbase.njs_wrapper.client import NarrativeJobService as NJS
from biokbase.workspace.client import Workspace
import time
import json

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
    VERSION = "0.0.3"
    GIT_URL = "https://github.com/sean-mccorkle/ManyHellos"
    GIT_COMMIT_HASH = "ad06b26fe125da9ebac51dcca6f49c582de39cb3"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.main_message = ""
        self.number_of_jobs = 0
        self.time_limit = 24 * 3600  # sec 
        self.config = config
        
        #END_CONSTRUCTOR
        pass


    def manyHellos(self, ctx, input_params):
        """
        :param input_params: instance of type "ManyHellosInputParams" (was
           the main service call manyHellos(), now Im not sure what this does
           - initializes, but that should probably be in the constructor?  
           maybe manyHellos_prepare()) -> structure: parameter "hello_msg" of
           String, parameter "time_limit" of Long
        :returns: instance of type "ManyHellos_globalResult" -> structure:
           parameter "output" of String
        """
        # ctx is the context object
        # return variables are: returnVal
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
        returnVal = {'output': output_obj}
        print( "this is manyHellos(), signing off!  Bye!" )
        #END manyHellos

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method manyHellos return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def manyHellos_prepare(self, ctx, prepare_params):
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
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN manyHellos_prepare
        input_params = prepare_params['global_input_params']
        global_method = prepare_params['global_method']
        print( "this is manyHellos_prepare..." )
        print( "num_jobs is ", input_params["num_jobs"] )
        self.num_jobs = int(input_params["num_jobs"]);

        tasks = []
        for i in range( self.num_jobs ):
            input_params = {'msg': input_params['msg'], 
                            'job_number': i , 
                            'workspace' : input_params['workspace']}
            each_method = global_method.copy()
            each_method['method_name'] = global_method['method_name'] + "_runEach"
            task = {'method': each_method, 'input_arguments': [input_params]}
            tasks.append( task )

        collect_method = global_method.copy()
        collect_method['method_name'] = global_method['method_name'] + "_collect"
        returnVal = {'tasks': tasks, 'collect_method': collect_method}
        pprint( ["exiting manyHellos_prepare, tasks is", returnVal] )
        #END manyHellos_prepare

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method manyHellos_prepare return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def manyHellos_runEach(self, ctx, task):
        """
        :param task: instance of type "ManyHellos_task" -> structure:
           parameter "msg" of String, parameter "job_number" of Long,
           parameter "workspace" of String
        :returns: instance of type "ManyHellos_runEachResult" (runEach()) ->
           structure: parameter "message" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN manyHellos_runEach
        print( "this is manyHellos_runEach..." )
        pprint( [ "task is ", task] )

        res = "{0}: {1}".format(task['job_number'], task['msg'])

        ws_client=Workspace(url=self.config['workspace-url'], token=ctx['token'])
        res_obj= ws_client.save_objects(
                            {"workspace":task['workspace'],
                             "objects": [{
                                            'type':'KBaseReport.Report',
                                            "data":{'objects_created':[], 'text_message': res },
                                            "name":"{0}_{1}.rpt".format(task['msg'],task['job_number']),
                                            "meta" : {}
                                        }]
                            })
        res = json.dumps( res_obj )

        print( "exiting manyHellos_runEach(), res is", res )
        returnVal = {'message': res}
        #END manyHellos_runEach

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method manyHellos_runEach return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

    def manyHellos_collect(self, ctx, collect_params):
        """
        :param collect_params: instance of type
           "ManyHellos_collectInputParams" -> structure: parameter
           "global_params" of type "ManyHellos_globalInputParams" (prepare())
           -> structure: parameter "msg" of String, parameter "num_jobs" of
           Long, parameter "workspace" of String, parameter
           "input_result_pairs" of list of type "ManyHellos_InputResultPair"
           (execution_time - execution time in milliseconds (may be not set
           by KBParallel).) -> structure: parameter "input" of type
           "ManyHellos_runEachInput" -> structure: parameter "method" of type
           "FullMethodQualifier" -> structure: parameter "module_name" of
           String, parameter "method_name" of String, parameter "service_ver"
           of String, parameter "input_arguments" of tuple of size 1: type
           "ManyHellos_task" -> structure: parameter "msg" of String,
           parameter "job_number" of Long, parameter "workspace" of String,
           parameter "result" of type "ManyHellos_runEachResult" (runEach())
           -> structure: parameter "message" of String, parameter
           "execution_time" of Long
        :returns: instance of type "ManyHellos_globalResult" -> structure:
           parameter "output" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN manyHellos_collect

        print( "this is manyHellos_collect..." )
        input_params = collect_params['global_params']
        print( "num_jobs is ", input_params["num_jobs"] )

        res = "default manyHellos_collect() result"

        print( "exiting manyHellos_collect, res is", res )
        returnVal = {'output': res}
        #END manyHellos_collect

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method manyHellos_collect return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]

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
