# Library import
import numpy as np
import datetime

# CSV data parser
def csv_loader(file_path, dtype=float):
    # Initial data load with specified dtype
    data = np.loadtxt(file_path, delimiter=",", dtype=dtype)

    # Data transposer if there are more columns than rows
    data = data.transpose() if data.shape[1] > data.shape[0] else data

    # Time data loader and convertor
    if dtype == np.uint64:
        # Define start point of datetime as day01
        time_base = datetime.datetime(1979, 1, 1) - datetime.timedelta(days=1)
        # Construct time function for calculating time result
        time_repo = [
            time_base + datetime.timedelta(milliseconds=ms + days * 86400000)
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
