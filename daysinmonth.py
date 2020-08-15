"""
Takes a month and year as integers and prints the number
of times each day occurs in the given month.
"""
import calendar
from collections import Counter
import sys


DAY_NAMES = dict(zip(range(7), calendar.day_name))
MONTH_NAMES = dict(zip(range(1, 13), calendar.month_name[1:]))


def output_how_often_days_occur_in_month(month, year):
    """
    Gets the counts of how many times each day appears
    in the specified month and sorts them in days of the week order
    before printing the results.
    """
    counts = count_days(month, year)
    print(f"The day counts for {MONTH_NAMES[month]} {year} are:")
    for day, num in sorted(counts.items(), key=_sort_order):
        print(f"\t\t{num} {day}s")


def count_days(month, year):
    """
    Identifies month length from given month and year,
    and returns a count of how many times each day
    occurs in the month.
    """
    _, month_length = calendar.monthrange(year, month)
    # calendar.weekday returns day of week as integer (0 is Monday)
    days = [
        calendar.weekday(year, month, day)
        for day in range(1, month_length + 1)
    ]
    days_named = [DAY_NAMES[day] for day in days]
    return Counter(days_named)


def _sort_order(count_items):
    """Key for sorting day counts in days of the week order."""
    return list(calendar.day_name).index(count_items[0])


if __name__ == "__main__":
    month = int(sys.argv[1])
    year = int(sys.argv[2])
    output_how_often_days_occur_in_month(month, year)
