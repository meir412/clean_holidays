import pandas as pd

def fix_end_date(start_date_raw: str, end_date: str) -> str:
    contains_month = len(start_date_raw.split("/")) > 1
    if contains_month:
        fixed_end_date = start_date_raw + "/" + end_date.split("/")[-1]
    else:
        fixed_end_date = start_date_raw + "/" + "/".join(end_date.split("/")[1:])
    return fixed_end_date

j = pd.read_csv('holidays.csv')
j['end_date'] =j['תאריך לועזי'].str.split("-").str[1]
j['start_date_raw'] = j['תאריך לועזי'].str.split("-").str[0]
j['start_date'] = j.apply(lambda x: fix_end_date(x['start_date_raw'], x['end_date']), axis=1)
j['start_time'] = j['start_date'].str.cat(j['כניסת שבת/חג'], sep=" ")
j['end_time'] = j['end_date'].str.cat(j['יציאת שבת/חג'], sep=" ")
j.rename(columns={'פרשת השבוע/חג': 'event'}, inplace=True)
j_small = j[['event', 'start_time', 'end_time']]
j_small.to_csv('holidays_clean.csv', index=False ,encoding = 'utf-8-sig')
