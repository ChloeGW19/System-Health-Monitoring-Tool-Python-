"""
Name: Chloe Williamson
Date: 4/15/26
Description: System health monitoring tool that checks CPU, memory,
and network performance, handles errors, and logs results.
"""

#Importing the modules
import cpu_monitor
import memory_monitor
import network_monitor

# Importing custom exceptions to catch and raise
from exceptions import ServiceUnavailableError, DataCorruptionError, ConnectionTimeoutError, ThresholdExceededError

# Thresholds
CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 75.0
NETWORK_THRESHOLD = 90.0


def check_cpu():
   """
  Checks CPU usage and returns the result.

    Returns:
        dict: {"status": "OK", "data": <metrics>} or {"status": "ERROR", "data": <message>}
   """
   try:
       # Call the provided module function to get CPU data

       data = cpu_monitor.get_cpu_metrics()

       # Checks if CPU usage is too high
       if data["usage_percent"] > CPU_THRESHOLD:
           # manually raise custom exception
           raise ThresholdExceededError("CPU usage too high")

        # if everything is fine, return success
       return {"status": "OK", "data": data}

   except ServiceUnavailableError:
       # If module ails, catches it here
       return {"status": "ERROR", "data": "CPU service unavailable"}
   


def check_memory():
    """
    Checks memory usage and returns the result.

    Returns:
        dict: {"status": "OK", "data": <metrics>} or {"status": "ERROR", "data": <message>}
    """
    try:
        data = memory_monitor.get_memory_metrics()

        # Check if memory usage is too high
        if data["usage_percent"] > MEMORY_THRESHOLD:
            raise ThresholdExceededError("Memory usage too high")

        return {"status": "OK", "data": data}

    except DataCorruptionError:
        # Happens if the module simulates bad data
        return {"status": "ERROR", "data": "Memory data corrupted"}
    

def check_network():
    """
    Checks network usage and returns the result.

    Returns:
        dict: {"status": "OK", "data": <metrics>} or {"status": "ERROR", "data": <message>}
    """
    try:
        data = network_monitor.get_network_metrics()

        # Check if network usage is too high
        if data["usage_percent"] > NETWORK_THRESHOLD:
            raise ThresholdExceededError("Network usage too high")

        return {"status": "OK", "data": data}

    except ConnectionTimeoutError:
        # Happens if the network request "times out"
        return {"status": "ERROR", "data": "Network timeout"}
    

def run_checks():
    """
    Runs all three checks and returns the results.

    Returns:
        dict: Results for cpu, memory, and network.
    """

    # Call each function and store results in one dictionary
    return {
        "cpu": check_cpu(),
        "memory": check_memory(),
        "network": check_network()
    }

def log_results(results, filepath):
    """
    Saves results to a log file. Always writes "Log complete" at the end.

    Parameters:
        results (dict): The results from run_checks().
        filepath (str): Path to the log file.
    """
    try:
        # Open file in append mode ("a") so we don't overwrite old logs
        with open(filepath, "a") as file:
            file.write(str(results) + "\n")

    except Exception as e:
        # Catch ANY unexpected error during logging
        with open(filepath, "a") as file:
            file.write(f"Logging error: {e}\n")

    finally:
        # This ALWAYS runs, even if an error happens
        # Required by assignment
        with open(filepath, "a") as file:
            file.write("Log complete\n")

def generate_report(results):
    """
    CTurns the results into a readable report string.

    Parameters:
        results (dict): The results from run_checks().

    Returns:
        str: A formatted report showing each service and its status.
    """

    # Start building the report string
    report = "SYSTEM HEALTH REPORT\n"
    report += "-" * 30 + "\n"

    # Loop through each service (cpu, memory, network)
    for key, value in results.items():
        # key = "cpu", value = {"status": ..., "data": ...}
        report += f"{key.upper()}: {value['status']}\n"

    return report



def main():
    """
    Runs the checks, prints the report, and saves the log.
    """

    # Step 1: run all checks
    results = run_checks()

    # Step 2: turn results into readable report
    report = generate_report(results)

    # Step 3: print to console
    print(report)

    # Step 4: save to log file
    log_results(results, "monitor.log")


# Ensures this only runs when file is executed directly
if __name__ == "__main__":
    main()
