"""
Takes a month and year as integers and prints the number
of times each day occurs in the given month.
"""
import argparse
import calendar
from collections import Counter


DAY_NAMES = dict(zip(range(7), calendar.day_name))
MONTH_NAMES = dict(zip(range(1, 13), calendar.month_name[1:]))


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


def sort_days(month, year):
    """
    Gets the counts of how many times each day appears
    in the specified month and sorts them in days of the week order.
    """
    counts = count_days(month, year)
    return sorted(counts.items(), key=_sort_order)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Takes a month and year as integers and prints the number "
        "of times each day occurs in the given month."
    )
    parser.add_argument(
        "month", type=int, help="Numeric representation of month to check: 1 is January etc."
    )
    parser.add_argument(
        "year", type=int, help="Four digit representation of year to check, such as: 2020."
    )
    return parser.parse_args()


def main():
    """Formats and prints the sorted day counts for the given month."""
    args = parse_arguments()
    sorted_days = sort_days(args.month, args.year)
    print(f"The day counts for {MONTH_NAMES[args.month]} {args.year} are:")
    for day, num in sorted_days:
        print(f"\t\t{num} {day}s")


if __name__ == "__main__":
    main()
