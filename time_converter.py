"""
Time Conversion Module
Functions to convert between hours and minutes.
"""


def hours_to_minutes(hours: float) -> float:
    """
    Convert hours to minutes.
    
    Args:
        hours: Time in hours (e.g., 2.5 for 2 hours and 30 minutes)
    
    Returns:
        Time in minutes
    
    Example:
        >>> hours_to_minutes(2.5)
        150.0
    """
    return hours * 60


def minutes_to_hours(minutes: float) -> float:
    """
    Convert minutes to hours.
    
    Args:
        minutes: Time in minutes
    
    Returns:
        Time in hours (decimal format)
    
    Example:
        >>> minutes_to_hours(150)
        2.5
    """
    return minutes / 60


def format_time(hours: float) -> str:
    """
    Format decimal hours into a readable string (hours and minutes).
    
    Args:
        hours: Time in decimal hours (e.g., 2.5)
    
    Returns:
        Formatted string like "2 hours and 30 minutes"
    
    Example:
        >>> format_time(2.5)
        '2 hours and 30 minutes'
    """
    total_minutes = hours_to_minutes(hours)
    h = int(total_minutes // 60)
    m = int(total_minutes % 60)
    return f"{h} hours and {m} minutes"


# Example usage
if __name__ == "__main__":
    # Convert 2.5 hours to minutes
    print(f"2.5 hours = {hours_to_minutes(2.5)} minutes")
    
    # Convert 150 minutes to hours
    print(f"150 minutes = {minutes_to_hours(150)} hours")
    
    # Format 2.5 hours
    print(f"2.5 hours = {format_time(2.5)}")
