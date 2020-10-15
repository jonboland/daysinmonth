import pytest

import context
import daysinmonth


def test_count_days():
    result = daysinmonth.count_days(5, 2021)
    assert result == daysinmonth.Counter(
        {
            "Saturday": 5,
            "Sunday": 5,
            "Monday": 5,
            "Tuesday": 4,
            "Wednesday": 4,
            "Thursday": 4,
            "Friday": 4,
        }
    )


def test_count_days_leap_year():
    result = daysinmonth.count_days(2, 2020)
    assert result == daysinmonth.Counter(
        {
            "Saturday": 5,
            "Sunday": 4,
            "Monday": 4,
            "Tuesday": 4,
            "Wednesday": 4,
            "Thursday": 4,
            "Friday": 4,
        }
    )


def test_sorted_days():
    result = daysinmonth.sort_days(2, 2020)
    assert result == [
        ("Monday", 4),
        ("Tuesday", 4),
        ("Wednesday", 4),
        ("Thursday", 4),
        ("Friday", 4),
        ("Saturday", 5),
        ("Sunday", 4),
    ]


def test_main(monkeypatch, capsys):
    def fake_args():
        return daysinmonth.argparse.Namespace(month=3, year=2020)

    monkeypatch.setattr(daysinmonth, "parse_arguments", fake_args)

    daysinmonth.main()

    captured = capsys.readouterr()
    assert captured.out == (
        "The day counts for March 2020 are:\n"
        "\t\t5 Mondays\n"
        "\t\t5 Tuesdays\n"
        "\t\t4 Wednesdays\n"
        "\t\t4 Thursdays\n"
        "\t\t4 Fridays\n"
        "\t\t4 Saturdays\n"
        "\t\t5 Sundays\n"
    )


def test_main_leap_year(monkeypatch, capsys):
    def fake_args():
        return daysinmonth.argparse.Namespace(month=2, year=2024)

    monkeypatch.setattr(daysinmonth, "parse_arguments", fake_args)

    daysinmonth.main()

    captured = capsys.readouterr()
    assert captured.out == (
        "The day counts for February 2024 are:\n"
        "\t\t4 Mondays\n"
        "\t\t4 Tuesdays\n"
        "\t\t4 Wednesdays\n"
        "\t\t5 Thursdays\n"
        "\t\t4 Fridays\n"
        "\t\t4 Saturdays\n"
        "\t\t4 Sundays\n"
    )


if __name__ == "__main__":
    pytest.main()
