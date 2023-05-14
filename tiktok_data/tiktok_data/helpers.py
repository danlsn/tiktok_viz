from datetime import datetime
import pendulum


def parse_utc_date_str(date: str) -> datetime:
    """
    Parse a date string from the TikTok API into a datetime object.
    _________________________________________________________________
    Parameters:
    - date: The date string to parse
    _________________________________________________________________
    Returns: The parsed datetime object
    """
    dt = pendulum.from_format(date, "YYYY-MM-DD HH:mm:ss UTC")
    return dt


def main():
    dt_str = "2022-07-06 22:53:41 UTC"
    dt = parse_utc_date_str(dt_str)
    print(dt)


if __name__ == "__main__":
    main()

