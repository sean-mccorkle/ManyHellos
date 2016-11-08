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

    /*
        hello_msg - what to print as the message,
        time_limit - how long the program will run, in seconds,
        workspace - used to store report(s).
    */
    typedef structure {
        string hello_msg;
        int num_jobs;
        int time_limit;
        string workspace;
    } ManyHellosInputParams;

    typedef structure {
        string output;
        list<tuple<int job_number, string message>> jobs;
    } ManyHellos_globalResult;

    funcdef manyHellos(ManyHellosInputParams input_params) returns (ManyHellos_globalResult) authentication required;


    /* prepare() */

    typedef structure {
        string msg;
        int num_jobs;
        string workspace;
    } ManyHellos_globalInputParams;

    typedef structure {
        string module_name;
        string method_name;
        string service_ver;
    } FullMethodQualifier;
    
    typedef structure {
        FullMethodQualifier global_method;
        ManyHellos_globalInputParams global_input_params;
    } ManyHellos_prepareInputParams;

    typedef  structure {
        string msg;
        int job_number;
        string workspace;
    } ManyHellos_task;
    
    typedef structure {
        FullMethodQualifier method;
        tuple<ManyHellos_task> input_arguments;
    } ManyHellos_runEachInput;

    typedef structure {
        list<ManyHellos_runEachInput> tasks;
        FullMethodQualifier collect_method;
    } ManyHellos_prepareSchedule;

    funcdef manyHellos_prepare(ManyHellos_prepareInputParams prepare_params) returns (ManyHellos_prepareSchedule) authentication required;


    /* runEach() */

    typedef structure {
        string message;
    } ManyHellos_runEachResult;

    funcdef manyHellos_runEach(ManyHellos_task task) returns (ManyHellos_runEachResult) authentication required;


    /* collect() */

    typedef structure {
        ManyHellos_runEachInput input;
        ManyHellos_runEachResult result;
    } ManyHellos_InputResultPair;

    typedef structure {
        ManyHellos_globalInputParams global_params;
        list<ManyHellos_InputResultPair> input_result_pairs;
    } ManyHellos_collectInputParams;

    funcdef manyHellos_collect(ManyHellos_collectInputParams collect_params) returns (ManyHellos_globalResult) authentication required;

    async funcdef  hi(string said) returns (string) authentication required;

};
