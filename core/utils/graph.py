from datetime import datetime, timedelta, time
import plotly.express as px

from django.utils.timezone import localtime
from pytz import timezone

from core.models import Image



def get_captured_data():
    data = Image.objects.all().order_by('created_at')
    times = []
    full_dates = {}

    for dt in data:
        cr_date = dt.created_at
        full_dates[dt.pk] =  cr_date
        old_hour = cr_date.hour + 3
        if old_hour > 23:
            old_hour = old_hour - 23
        times.append({"parent": dt.pk, "time": time(old_hour, cr_date.minute)})

    sorted_times = sorted(times, key=lambda d: d['time']) 
    new_x = []
    new_y = []
    for item in sorted_times:
        new_y.append(item.get('time'))
        new_x.append(full_dates.get(item.get('parent')))

    # print(full_dates.find())
    now = datetime.now()
    fig = px.scatter(x=new_x, y=new_y, range_x=[now-timedelta(days=7), now])
    fig.update_layout(
        yaxis = dict(
            showticklabels=True
        )
    )
    # fig.update_traces(marker=dict(size=7,
    #                           line=dict(width=2,
    #                                     color='DarkSlateGrey')),
    #               selector=dict(mode='markers'))
    fig.show()