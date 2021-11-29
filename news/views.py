from django.core.checks import messages
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.http import HttpResponse
import datetime as dt

from news.models import Article

# Create your views here.
# def welcome(request):
#     return render(request, 'welcome.html')

def news_of_day(request):
    date = dt.date.today()
    news = Article.todays_news()
    return render(request, 'all-news/today-news.html', {"date":date, "news":news})
    # day = convert_dates(date)
    # html = f'''
    # <html>
    # <body>
    # <h1>Today, {day}, is {date.day} - {date.month} - {date.year}</h1>
    # </body>
    # </html>
    # '''
    return render(request, 'all-news/today-news.html',{"date":date})
    
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

    news = Article.days_news(date)
    return render(request,'all-news/past-news.html',{"date":date,"news":news})

def search_results(request):
    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        messages = f"{search_term}"
        return render(request, 'all-news/search.html', {"messages":messages, "articles":searched_articles})

    else:
        messages = "You didnt search anything"
        return render(request, 'all-news/search.html',{"messages":messages})


def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except Article.DoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html", {"article":article})
