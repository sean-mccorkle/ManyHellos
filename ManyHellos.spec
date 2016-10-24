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

    /* Main service call:  manyHellos() */

    typedef structure {
        string  hello_msg;
        int     num_jobs;
        int     time_limit;
    } ManyHellosInputParams;

    typedef string ManyHellosOutputObj;

    funcdef  manyHellos( ManyHellosInputParams input_params) returns ( ManyHellosOutputObj output_obj ) authentication required;

    /* prepare() */

    typedef structure {
        int     num_jobs;
    } ManyHellos_prepareInputParams;

    typedef  string  ManyHellos_prepareResult;

    funcdef  manyHellos_prepare( ManyHellos_prepareInputParams input_params ) returns ( ManyHellos_prepareResult res ) authentication required;

    /* runEach() */

    typedef structure {
        int     job_number;
    } ManyHellos_runEachInputParams;

    typedef  string  ManyHellos_runEachResult;

    funcdef  manyHellos_runEach( ManyHellos_runEachInputParams input_params )  returns ( ManyHellos_runEachResult res ) authentication required;

    /* collect() */

    typedef structure {
        int    num_jobs;
    } ManyHellos_collectInputParams;

    typedef  string  ManyHellos_collectResult;

    funcdef  manyHellos_collect( ManyHellos_collectInputParams input_params ) returns ( ManyHellos_collectResult res ) authentication required;

};
