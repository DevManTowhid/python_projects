

report = "SEAT 123456789 S-39 occupied by unknown passenger/person"
if "SEAT" in report:
    lst = report.split(" ")
    print(lst)
    [report_type, PNR, coach_seat] = lst[:3]
    print(report_type, PNR, coach_seat)
    reports = lst[3:]
    print(reports)
    report = " ".join(reports)
    print(report)
