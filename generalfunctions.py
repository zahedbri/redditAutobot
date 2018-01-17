import os

def mkdir_p(path):
    #This function makes a directory if none exist

    try:
        os.makedirs(path)
    except OSError:  # Python >2.5
        if os.path.isdir(path):
            pass
        else:
            raise

