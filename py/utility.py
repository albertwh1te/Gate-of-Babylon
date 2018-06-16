import os


def dir2df(path):
    """
    convert csv files in path to pandas dataframe
    """
    df_list = []
    for file in os.walk(path):
        if file.endswith('.csv'):
            df_list.append(pd.read_csv(path + file))
    return file
