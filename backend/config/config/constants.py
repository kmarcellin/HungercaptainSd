import os

import pytz


STATUS = (
    ('active', 'Active'),
    ('inactive', 'Inactive'),
    ('deleted', 'Deleted'),
)

STATUS_DICT = dict(STATUS)


CATEGORIES = (
    ('all', 'All'),
    ('hot', 'Hot'),
    ('cold', 'Cold'),
    ('bagel', 'Bagel'),
)

CATEGORIES_DICT = dict(CATEGORIES)
