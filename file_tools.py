import os


def get_directories():
    # Be specific about where to find data and where to plot copies of plots.
    # LOKI_DATA_DIRECTORY = "/home/brohrer/projects/Moral_Disgust_Analysis/data"
    # LOKI_PLOT_DIRECTORY = "/home/brohrer/projects/Moral_Disgust_Analysis/plots"
    THE_MORRIGAN_DATA_DIRECTORY = "/Users/themorrigan/Library/CloudStorage/Box-Box/Sadism Disgust Code"  # noqa: E501
    THE_MORRIGAN_PLOT_DIRECTORY = "/Users/themorrigan/Desktop/Sadism_Disgust_Code/plots"
    ASHER_DATA_DIRECTORY = "/Users/asher/Library/CloudStorage/Box-Box/Sadism Disgust Study"  # noqa: E501
    ASHER_PLOT_DIRECTORY = "/Users/asher/Desktop/Sadism_Disgust_Code/plots"
    AIDAS_DATA_DIRECTORY = "/Users/hopswork/Library/CloudStorage/Box-Box/Sadism Disgust Study"  # noqa: E501
    AIDAS_PLOT_DIRECTORY = "/Users/hopswork/Desktop/Sadism_Disgust_Code/plots"

    # Check this is running on Loki or The Morrigan and
    # set the directories accordingly.
    try:
        # This will be true for Loki.
        if os.environ["DESKTOP_SESSION"] == "ubuntu":
            data_directory = LOKI_DATA_DIRECTORY
            plot_directory = LOKI_PLOT_DIRECTORY
    except KeyError:
        try:
            # This will be true for The Morrigan.
            if os.environ["LOGNAME"] == "themorrigan":
                data_directory = THE_MORRIGAN_DATA_DIRECTORY
                plot_directory = THE_MORRIGAN_PLOT_DIRECTORY
            # This will be true for Aidas under user hopswork.
            elif os.environ["LOGNAME"] == "hopswork":
                data_directory = AIDAS_DATA_DIRECTORY
                plot_directory = AIDAS_PLOT_DIRECTORY
            elif os.environ["LOGNAME"] == "asher":
                data_directory = ASHER_DATA_DIRECTORY
                plot_directory = ASHER_PLOT_DIRECTORY
            else:
                data_directory = "."
                plot_directory = "."

        except KeyError:
            # If it can't figure it out, default to the directory from which
            # the script was run.
            data_directory = "."
            plot_directory = "."
    return data_directory, plot_directory


def get_log_filenames(subject_id, condition, data_directory):
    filenames = os.listdir(data_directory)
    matching_filenames = []
    for filename in filenames:
        if (filename.__contains__(str(subject_id)) and
                filename.__contains__(condition) and
                filename[-4:] == '.csv'):
            pathname = os.path.join(data_directory, filename)
            matching_filenames.append(pathname)

    if len(matching_filenames) == 0:
        return None

    # Put the filenames in alphabetical order.
    # Because of how they're named, this ensures that the
    # newest runs will be tested last.
    matching_filenames.sort()

    # Return just the last one. This is the most recent and
    return matching_filenames[-1]
