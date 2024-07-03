import os 

def get_audio_urls(folder_path: str):
    """
    Description:
        - This function returns the parth of all the files in a folder
    parameters:
        - folder_path (str): Path of the folder

    returns:
        - audio_urls (arr): Array of all audio urls in a folder        
    """

    # List to store file paths
    file_paths = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_paths.append(os.path.join(root, file))

    return file_paths