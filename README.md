# Progress bar for terminal in Python

Included in `progress.py` is the `progress_bar` object. Create an instance of the `progress_bar()`, parsing in the maximum value your process should reach (not necessarily the same as bar length, which can also be specified using the `bar_size=` optionalargument). 

Each call of `progress_bar().update()` increments the progress bar by one towards the maximum specified. 

## Example:

```python3
from progress_bar import *

minimum = 0
maxmum = 101

my_progess = progress_bar(maximum)

for i in range(minimum, maximum):

    # Do something
    time.sleep(0.1)

    # Update progress by one towards maximum
    my_progress.update()
```

## Test it yourself

To get an idea of how the function could be used in your code, run:

```console
python test.py
```

Output at start:

```console
$ python test.py
$ Creating progress bar
$ Progress: [..................................................] 0.0 % (0/100)
```

Output at 50 % completion:

```console
$ python test.py
$ Creating progress bar
$ Progress: [=========================.........................] 50.0 % (50/100)
```

Output at full completion:

```console
$ python test.py
$ Creating progress bar
$ Progress: [==================================================] 100.0 % (100/100)
```
