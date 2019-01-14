from datetime import datetime,timezone

def getMinute(ends):
    start=datetime.now(timezone.utc)
    diff = start - ends
    hours = int(diff.seconds // (60 * 60))
    mins = int((diff.seconds // 60) % 60)
    return mins

def convertion(getstrval):
    date_str = getstrval
    format_str = '%Y-%m-%d'
    do = datetime.strptime(date_str, format_str)
    return do
