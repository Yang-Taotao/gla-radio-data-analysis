# Library import
import numpy as np
import datetime as dt

# CSV data parser
def csv_loader(file_path, dtype=float):
    # Initial data load with specified dtype
    data = np.loadtxt(file_path, delimiter=",", dtype=dtype)

    # Time data loader and convertor
    if dtype == np.uint64:
        # Define start point of datetime as day01
        time_base = dt.datetime(1979, 1, 1) - dt.timedelta(days=1)
        # Construct time function for calculating time result
        time_repo = [
            time_base + dt.timedelta(milliseconds=ms + days * 86400000)
            for ms, days in data
        ]
        # Combined datetime data
        time_data = np.array([dt.strftime("%Y-%m-%d %H:%M:%S") for dt in time_repo])
        # Return converted time data array
        return time_data
    # Data loader for all other dtype
    else:
        # Return data
        return data
