# Library import
import numpy as np
import datetime

# CSV data parser
def csv_loader(file_path, dtype=float):
    # Time data loader and convertor
    if dtype == np.uint64:
        # Load time data
        data = np.loadtxt(file_path, delimiter=",", dtype=np.uint64)
        # Define start point of datetime as day01
        time_base = datetime.datetime(1979, 1, 1) - datetime.timedelta(days=1)
        # Construct time function for calculating time result
        time_repo = [
            time_base + datetime.timedelta(milliseconds=ms + days * 86400000)
            for ms, days in data
        ]
        # Convert days since time base to YYYY-MM-DD
        time_days = [dt.strftime("%Y-%m-%d") for dt in time_repo]
        # Convert milliseconds since the day to HH:MM:SS
        time_prec = [dt.strftime("%H:%M:%S") for dt in time_repo]
        # Recombine the converted datetime data
        time_data = np.column_stack((time_prec, time_days))
        # Return converted time data array
        return time_data
    # Data loader for all other dtype
    else:
        # Load all other type of data
        data = np.loadtxt(file_path, delimiter=",", dtype=dtype)
        # Return loaded data arrays
        return data
