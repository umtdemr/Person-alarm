from datetime import datetime, timedelta, time
import plotly.express as px

from core.models import Image
from core.utils.tele_bot import TelegramBot


def get_captured_data():
    now = datetime.now()
    week_ago = now - timedelta(days=7)
    data = Image.objects.filter(
        created_at__gte=week_ago
    ).order_by('created_at')
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
    fig = px.scatter(x=new_x, y=new_y, range_x=[week_ago, now], title="Haftalık hareketlilik")
    return fig


def send_graph_photo():
    fig = get_captured_data()
    img_path = "media/fig.jpeg"
    fig.write_image(img_path)
    telegram_obj = TelegramBot()
    message = telegram_obj.send_photo(img_path)
    return message

def view_graph():
    fig = get_captured_data()
    fig.show()
