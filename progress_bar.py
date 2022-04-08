import sys

"""
Functions for initialising and updating an in-terminal progress bar.  

"""


class progress_bar():
    """
    Object for displaying and udating a progress bar in the terminal. Example of 
    outputs:

    Progress: [..................................................] 0.0 % (0/100)
    Progress: [=========================.........................] 50.0 % (50/100)
    Progress: [==================================================] 100.0 % (100/100)
    """

    def __init__(self, maximum, bar_size=50, counter=1):
        self.maximum = maximum
        self.bar_size = bar_size    # reduce for narrow terminal window
        self.counter = counter      # incremented on .update() call

        # Setup
        init_str = f"Progress: [{'.' * bar_size}] 0.0 % (0/{self.maximum})\r"
        sys.stdout.write(init_str)               # display bar @ zero progress
        sys.stdout.flush()                          # clear, ready for update
        sys.stdout.write("\b" * (len(init_str))) # return to start of line, after '['

    def update(self):
        """
        ================================================================================
        Updates a progress bar object by incrementing progress by ++1. Maximum progress
        for progress bar's size is defined on instantiation of new progress_bar object
        so counter does not have to be parsed. 
        ================================================================================
        """
        # Update information
        prog = int(self.bar_size*self.counter/self.maximum)
        pc_complete = round((self.counter/self.maximum)*100, 1)
        fraction = f"{self.counter}/{self.maximum}"
        not_prog = '.'*(self.bar_size-prog)
        update_str = f"Progress: [{'='*prog}{not_prog}] {pc_complete} % ({fraction})\r"
        
        # Update progress bar by incrementing counter ++1 towards maximum limit
        sys.stdout.write(update_str)

        # Continue if progress < 100%
        if self.counter < self.maximum:     # bar knows there's more to do
            sys.stdout.flush()
            self.counter += 1
        else:                               # action has completed...
            sys.stdout.write("\n")          # ... terminate bar


    

