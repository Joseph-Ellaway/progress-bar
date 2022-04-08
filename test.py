import time
from progress_bar import *


def run_test():
    """
    ====================================================================================
    Test function for progress_bar functionality
    ====================================================================================
    """

    # Thing to iterate over
    iterable = range(0, 100)

    # Create instance of progress_bar
    print("Creating progress bar")
    my_progress_bar = progress_bar( len(iterable) )
    # Comments between here and update() call will merge with progress bar

    # Iterate through iterable
    for i in iterable:

        # Do something, potentially with `i`
        time.sleep(0.1)

        # Update progress bar
        my_progress_bar.update()




if __name__ == "__main__":

    run_test()
