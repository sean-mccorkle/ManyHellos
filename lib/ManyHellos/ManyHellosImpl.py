# -*- coding: utf-8 -*-
#BEGIN_HEADER

from pprint import pprint 
from biokbase.njs_wrapper.client import NarrativeJobService as NJS
from biokbase.workspace.client import Workspace
import time
import json
import os

from KBParallel.KBParallelClient import KBParallel
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
    GIT_COMMIT_HASH = "07149cb1fcb259e3f978fc64b517b657bf48501b"

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
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN manyHellos
        print( "Hi this is manyHellos()!" )
        print( "hello_mesg is ", input_params["hello_msg"] )
        print( "time_limit is ", input_params["time_limit"] )
        print( "num_jobs is ", input_params["num_jobs"] )
        print( "workspace is ", input_params["workspace"] )

        kbp = KBParallel(os.environ['SDK_CALLBACK_URL'], token=ctx['token'])
        returnVal = kbp.run({'module_name': 'ManyHellos',
                             'method_name': 'manyHellos',
                             'service_ver': 'dev',
                             'is_local': 1,
                             'global_params': {'msg': input_params["hello_msg"],
                                               'num_jobs': input_params["num_jobs"],
                                               'workspace': input_params["workspace"]},
                             'time_limit': input_params["time_limit"]})
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
        global_input_params = prepare_params['global_input_params']
        global_method = prepare_params['global_method']
        print( "this is manyHellos_prepare..." )
        print( "num_jobs is ", global_input_params["num_jobs"] )
        num_jobs = int(global_input_params["num_jobs"])

        tasks = []
        each_method = global_method.copy()
        each_method['method_name'] = global_method['method_name'] + "_runEach"
        for i in range( num_jobs ):
            each_input_params = {'msg': global_input_params['msg'], 
                            'job_number': i , 
                            'workspace' : global_input_params['workspace']}
            task = {'method': each_method, 'input_arguments': [each_input_params]}
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
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN manyHellos_collect

        print( "this is manyHellos_collect..." )
        input_params = collect_params['global_params']
        print( "num_jobs is ", input_params["num_jobs"] )

        res = "default manyHellos_collect() result"

        job_pairs = collect_params['input_result_pairs']
        jobs = [tuple(job_pairs[job_id]['input']['input_arguments']['job_number'], 
                      job_pairs[job_id]['result']['message']) for job_id in job_pairs]
        returnVal = {'output': res, 'jobs': jobs}
        print( "exiting manyHellos_collect, returnVal is", returnVal )
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
