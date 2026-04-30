# Name: Chloe Williamson
# Date: 4/15/2026
# Description: Defines custom exceptions for the system monitor

class ServiceUnavailableError(Exception):
    """Raised when a service can't be reached."""
    pass
class DataCorruptionError(Exception):
    """Raised when data returned is corrupted."""
    pass
class ConnectionTimeoutError(Exception):
    """Raised when a connection times out"""
    pass
class ThresholdExceededError(Exception):
    """Raised when a metric exceeds its defined threshold"""
    pass
