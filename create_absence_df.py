import datetime
import pandas as pd
import random
import uuid
import calendar


def main():
    year = 2019
    months = range(1, 13)
    rows = 300
    col_index = ["Time of Report off", "Date Absent",
                 "Report off Date Number", "Reason for Call Off", "Reason"]
    df = pd.DataFrame(columns=col_index)
    for month in months:
        list_of_rows = create_absence(2020, month, rows, col_index)
        for row in list_of_rows:
            df = df.append(row, ignore_index=True)
    df.to_csv('2019_fake_report_off_data.csv')


def create_absence(year, month, rows, col_index):
    res = []
    for _ in range(rows):
        dic = {key: None for key in col_index}
        reason_for_call_off = random.choice(["Car trouble", "Child care", "Death in family",
                                             "ETO (Earned Time Off)", "Family medical leave", "Family medical leave - late", "Injury - WR (work related)", "Injury - NWR (non-work related)", "Jury duty", "Late", "Personal", "Sick", "Weather"])
        if reason_for_call_off == "Late":
            reason = "Late"
        else:
            reason = "Report Off"
        time_of_report_off = randomDate(year, month)
        if reason == 'Late':
            date_absent = time_of_report_off.date()
        else:
            date_absent = randomDate(year, month, time_of_report_off).date()
        super_number = date_absent.year * \
            (10 ** 4) + date_absent.month * 100 + date_absent.day
        dic["Time of Report off"] = time_of_report_off
        dic['Date Absent'] = date_absent
        dic['Report off Date Number'] = super_number
        dic['Reason for Call Off'] = reason_for_call_off
        dic['Reason'] = reason
        res.append(dic)
    return res


def randomDate(year, month, start_date=None):
    day_count = calendar.monthrange(year, month)[1]
    if not start_date:
        t = random.choice(pd.date_range(
            f"{year}-{month}-01", f"{year}-{month}-{day_count}", freq='S'))
    else:
        t = random.choice(pd.date_range(
            start_date, f"{year}-{month}-{day_count}", freq='S'))
    return randomDate(year, month) if t.dayofweek == 5 or t.dayofweek == 6 else t


# t = randomDate(2020, 7)
# print(t, t.dayofweek, type(t))
# print(t.date(), t.time())
# create_absence(2020, 7, 10)
main()
