from django.http.response import Http404
from django.shortcuts import redirect, render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def news_of_day(request):
    date = dt.date.today()
    # day = convert_dates(date)
    # html = f'''
    # <html>
    # <body>
    # <h1>Today, {day}, is {date.day} - {date.month} - {date.year}</h1>
    # </body>
    # </html>
    # '''
    return HttpResponse(request, 'all-news/today-news.html',{"date":date})
    
def convert_dates(dates):
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday', 'Friday', 'Saturday', 'Sunday']

    day = days[day_number]
    return day

def past_days_news(request, past_date):

    try:
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

        # day = convert_dates(date)
        # html = f'''
        # <html>
        # <body>
        # <h1>
        # News for {day} {date.day}-{date.month}-{date.year}
        # </h1>
        # </body>
        # </html>
        # '''
    except ValueError:
        raise Http404()
    if date == dt.date.today():
        return redirect(news_of_day)
    return render(request,'all-news/past-news.html',{"date":date})
