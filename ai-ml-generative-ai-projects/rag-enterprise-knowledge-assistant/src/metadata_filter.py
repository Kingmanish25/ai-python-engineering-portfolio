def build_filter(year=None, month=None):
    filt = {}
    if year:
        filt["year"] = year
    if month:
        filt["month"] = month
    return filt if filt else None
