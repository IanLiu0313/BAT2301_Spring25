# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#| label
#| tbl-cap: Spring25 Class Schedule
#| echo: false

from IPython.display import Markdown
from tabulate import tabulate
import pandas as pd 

with open('Spring25_Schedule.csv', 'rb') as f:
    tb = pd.read_csv(f, keep_default_na=False)


Markdown(tabulate(
    tb, 
    tb.head(),
    tablefmt="grid"
))
#
#
#
