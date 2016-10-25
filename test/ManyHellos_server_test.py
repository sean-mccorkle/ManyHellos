# -*- coding: utf-8 -*-
import unittest
import os  # noqa: F401
import json  # noqa: F401
import time
import requests

from os import environ
try:
    from ConfigParser import ConfigParser  # py2
except:
    from configparser import ConfigParser  # py3

from pprint import pprint  # noqa: F401

from biokbase.workspace.client import Workspace as workspaceService
from ManyHellos.ManyHellosImpl import ManyHellos
from ManyHellos.ManyHellosServer import MethodContext

from biokbase.njs_wrapper.client import NarrativeJobService as NJS

class ManyHellosTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = environ.get('KB_AUTH_TOKEN', None)
        user_id = requests.post(
            'https://kbase.us/services/authorization/Sessions/Login',
            data='token={}&fields=user_id'.format(token)).json()['user_id']
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'ManyHellos',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        config_file = environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('ManyHellos'):
            cls.cfg[nameval[0]] = nameval[1]
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = workspaceService(cls.wsURL, token=token)
        cls.serviceImpl = ManyHellos(cls.cfg)

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    def getWsClient(self):
        return self.__class__.wsClient

    def getWsName(self):
        if hasattr(self.__class__, 'wsName'):
            return self.__class__.wsName
        suffix = int(time.time() * 1000)
        wsName = "test_ManyHellos_" + str(suffix)
        ret = self.getWsClient().create_workspace({'workspace': wsName})  # noqa
        self.__class__.wsName = wsName
        return wsName

    def getImpl(self):
        return self.__class__.serviceImpl

    def getContext(self):
        return self.__class__.ctx

    # NOTE: According to Python unittest naming rules test method names should start from 'test'. # noqa
    #def test_your_method(self):
        # Prepare test objects in workspace if needed using
        # self.getWsClient().save_objects({'workspace': self.getWsName(),
        #                                  'objects': []})
        #
        # Run your method by
        # ret = self.getImpl().your_method(self.getContext(), parameters...)
        #
        # Check returned data with
        # self.assertEqual(ret[...], ...) or other unittest methods
        #pass

    def test_NJS_connect( self ):
        print( "about to test NJS connect" )
        tok = os.environ.get('KB_AUTH_TOKEN')
        print( "tok is ", tok )
        w = NJS( url="https://ci.kbase.us/services/njs_wrapper", token=tok )
        pprint( w )
        v = w.ver()
        pprint( v )
        s = w.status()
        pprint( s )
        l = w.list_config()
        pprint( l )


    def test_manyHellos(self):
        # Prepare test objects in workspace if needed using
        # self.getWsClient().save_objects({'workspace': self.getWsName(),
        #                                  'objects': []})
        #
        # Run your method by
        print( "in test_manyHellos() about to run...")
        input_params = { 'hello_msg': "Hai",
                         'num_jobs': 3,
                         'time_limit':  5000000,
                         'njs_wrapper_url': "https://ci.kbase.us/services/njs_wrapper",
                         'token': os.environ.get('KB_AUTH_TOKEN')
                       }

        ctx = self.getContext()
        # NOTE - this is not right - should call a constructor that is used for further methods
        #ret = self.getImpl().manyHellos( self.getContext(), input_params )
        print( "about to construct..." )
        mh = ManyHellos( None )
        pprint( mh )
        ret = mh.manyHellos( ctx, input_params )
        print( ret )

        tasks_ret = mh.manyHellos_prepare( ctx, { 'num_jobs': input_params["num_jobs"] } );
        print( "back in test_manyHellos")
        tasks = tasks_ret[0]
        pprint( tasks )

        for task in tasks:
            pprint( ["   launching task", task]  )
            r1 = mh.manyHellos_runEach( ctx, task )
            pprint( r1 )

        r2 = mh.manyHellos_collect( ctx, { 'num_jobs': input_params["num_jobs"] } );
        pprint( r2 )

        #
        # Check returned data with
        # self.assertEqual(ret[...], ...) or other unittest methods
        print( "exiting test_manyHellos()")

