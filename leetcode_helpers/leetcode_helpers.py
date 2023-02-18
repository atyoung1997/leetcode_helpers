from time import perf_counter_ns
import pandas as pd

def run_test_scenarios(func, tests, description = "test_results"):
    """
    Description
    --------------
    Runs test scenarios on func

    Params
    --------------
    func : function
        function to be tested
    tests : dict{expected_result: [[params for test 1], [params for test 2], [etc]]}
        dict of test scenarios
    description : string
        optional description of test

    Returns
    --------------
    None
    """

    info_dict = {
        "Input": [],
        "Expected": [],
        "Output": [],
        "Time": [], 
        "Result": []
    }

    for key in tests:
        for params in tests[key]:
            info_dict["Expected"].append(key)
            info_dict["Input"].append(params)

            if isinstance(params, list):
                start = perf_counter_ns()
                output = func(*params)
                end = perf_counter_ns()
            else:
                start = perf_counter_ns()
                output = func(params)
                end = perf_counter_ns()

            info_dict["Output"].append(output)
            info_dict["Time"].append(f"{end - start} ns")
            if info_dict["Output"][-1] == info_dict["Expected"][-1]:
                info_dict["Result"].append("SUCCESS!") 
            else:
                info_dict["Result"].append("FAILURE")

    print(f"{description :-^51}")
    print(pd.DataFrame(info_dict))