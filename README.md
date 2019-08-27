# AWSLambda-Warm-Time-and-Memory-Benchmark
Simple python code to check lambda warm time and to benchmark memory<br>
Run the python file in Cloud9 with Lambda Invoke permission.

# Validation points
 - The execution time of a lambda in "warm" state is significantly lesser than the execution time in "cold" state
 - As the memory is increased, the execution time decreases until a saturation memory is reached

The python code provides tests the lambda and provides data to validate the above mentioned points.
Results are printed at adequate levels to provide the Lambda execution time and Memory consumptions.

# Global Variables
Input
 - lambdaname - provide the lambda function name
 - memory - the list of memories you want to test against
 - payload - the payload to be sent to the lambda function
 - timeinmin - time intervals to test lambda warm time in minutes
Output
 - results - all the results are stored in this variable

# Python Functions
checkoptimalmemory()<br>
Use this function to trigger lambda function with various memory values specified in the "memory" variable. It will provide the execution time for both "warm" and "cold" states.





checkwarmtime()<br>
Use this function to trigger lambda function with between time intervals specified in the "timeinmin" variable. It will provide the execution time for both "warm" and "cold" states.
