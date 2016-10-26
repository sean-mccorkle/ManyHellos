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
        string  njs_wrapper_url;
        string  token;
    } ManyHellosInputParams;

    typedef string ManyHellosOutputObj;

    async funcdef  manyHellos( ManyHellosInputParams input_params) returns ( ManyHellosOutputObj output_obj ) authentication required;

    /* prepare() */

    typedef structure {
        int     num_jobs;
    } ManyHellos_prepareInputParams;

    typedef  structure {
        int  job_number;
    } ManyHellos_task;

    typedef  list<ManyHellos_task>  ManyHellos_tasklist;

    async funcdef  manyHellos_prepare( ManyHellos_prepareInputParams input_params ) returns ( ManyHellos_tasklist tasks ) authentication required;

    /* runEach() */

    typedef  string  ManyHellos_runEachResult;

    async funcdef  manyHellos_runEach( ManyHellos_task task )  returns ( ManyHellos_runEachResult res ) authentication required;

    /* collect() */

    typedef structure {
        int    num_jobs;
    } ManyHellos_collectInputParams;

    typedef  string  ManyHellos_collectResult;

    async funcdef  manyHellos_collect( ManyHellos_collectInputParams input_params ) returns ( ManyHellos_collectResult res ) authentication required;

    async funcdef  hi(string said) returns (string) authentication required;

};
