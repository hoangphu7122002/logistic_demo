import os

folders = [
    "C://Users//Administrator//Desktop//logistic//Demo//xingtian//simulator//dpdp_competition//output//ongoing_order",
    "C://Users//Administrator//Desktop//logistic//Demo//xingtian//simulator//dpdp_competition//output//output_destination",
    "C://Users//Administrator//Desktop//logistic//Demo//xingtian//simulator//dpdp_competition//output//output_route",
    "C://Users//Administrator//Desktop//logistic//Demo//xingtian//simulator//dpdp_competition//output//unallocated_order",
    "C://Users//Administrator//Desktop//logistic//Demo//xingtian//simulator//dpdp_competition//output//vehicle_info"
]

for folder in folders:
    # Get the list of files in the folder
    files = os.listdir(folder)

    # Iterate over each file in the folder
    for file in files:
        # Create the full path to the file
        file_path = os.path.join(folder, file)

        # Check if the path is a file
        if os.path.isfile(file_path):
            # Remove the file
            os.remove(file_path)