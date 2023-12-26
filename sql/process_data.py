
import pandas as pd

def process_traffic_data(input_file):
    data = pd.read_csv(input_file)
    with open(input_file, 'r') as file:
        lines = file.readlines()

    lines_as_lists = [line.strip('\n').strip().strip(';').split(';') for line in lines]

    no_field_max = 0

    for row in lines_as_lists:
        if len(row) > no_field_max:
            no_field_max = len(row)

    largest_n = int((no_field_max-4)/6)

    cols = lines_as_lists.pop(0)
    track_cols = cols[:4]
    trajectory_cols = ['track_id'] + cols[4:]

    track_info = []
    trajectory_info = []

    for row in lines_as_lists:
        track_id = row[0]

        # add the first 4 values to track_info
        track_info.append(row[:4]) 

        remaining_values = row[4:]
        # reshape the list into a matrix and add track_id
        trajectory_matrix = [[track_id] + remaining_values[i:i+6] for i in range(0, len(remaining_values), 6)]
        # add the matrix rows to trajectory_info
        trajectory_info = trajectory_info + trajectory_matrix

    df_track = pd.DataFrame(data=track_info, columns=track_cols)
    df_trajectory = pd.DataFrame(data=trajectory_info, columns=trajectory_cols)

    return df_track, df_trajectory
