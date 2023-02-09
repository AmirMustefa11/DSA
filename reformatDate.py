class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split()
        day = day[:-2]
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month_number = months.index(month) + 1
        return f'{year}-{month_number:02}-{day:0>2}'
