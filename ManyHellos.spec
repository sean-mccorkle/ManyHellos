/*
A KBase module: ManyHellos
*/

/*
This is a single-language prototype for parallel subjob execution.  All this
does is run several "hello world" programs.
*/

module ManyHellos {
    /*
        Insert your typespec information here.
    */

    /* 
       was the main service call manyHellos(), now Im not sure what this does - initializes, but that
       should probably be in the constructor?   maybe manyHellos_prepare()
    */

    typedef structure {
        string  hello_msg;
        int     time_limit;
        string  token;
    } ManyHellosInputParams;

    typedef string ManyHellosOutputObj;

    async funcdef  manyHellos( ManyHellosInputParams input_params) returns ( ManyHellosOutputObj output_obj ) authentication required;

    /* prepare() */

    typedef structure {
        string  msg;
        int     num_jobs;
        string  workspace;
    } ManyHellos_prepareInputParams;

    typedef  structure {
        string msg;
        int  job_number;
        string  workspace;
    } ManyHellos_task;

    typedef  list<ManyHellos_task>  ManyHellos_tasklist;

    funcdef  manyHellos_prepare( ManyHellos_prepareInputParams input_params ) returns ( ManyHellos_tasklist tasks ) authentication required;

    /* runEach() */

    typedef  string  ManyHellos_runEachResult;

    async funcdef  manyHellos_runEach( ManyHellos_task task )  returns ( ManyHellos_runEachResult res ) authentication required;

    /* collect() */

    typedef structure {
        int    num_jobs;
    } ManyHellos_collectInputParams;

    typedef  string  ManyHellos_collectResult;

    funcdef  manyHellos_collect( ManyHellos_collectInputParams input_params ) returns ( ManyHellos_collectResult res ) authentication required;

    async funcdef  hi(string said) returns (string) authentication required;

};
