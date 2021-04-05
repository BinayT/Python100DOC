import time
starting_time = time.time()

def speed_calc_decorator(fun):
    def run_func():
      fun()
      function_execution_time = time.time()
      total_time = starting_time - function_execution_time
      print(f'Time taken to execute {fun.__name__} from initial time is of {total_time}')
    return run_func

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()