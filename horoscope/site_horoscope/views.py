from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from datetime import date
# Create your views here.


class ZodiacSign:
    def __init__(self, name, element, date_range, info):
        self.name = name
        self.element = element
        self.date_range = date_range
        self.info = info


dict_class_zodiac = {
    'aries': ZodiacSign('aries', 'fire', (date(year=1, month=3, day=21), date(year=1, month=4, day=20)), 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля.'),
    'taurus': ZodiacSign('taurus', 'earth', (date(year=1, month=4, day=21), date(year=1, month=5, day=21)), 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).'),
    'gemini': ZodiacSign('gemini', 'ear', (date(year=1, month=5, day=22), date(year=1, month=6, day=21)), 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).'),
    'cancer': ZodiacSign('cancer', 'water', (date(year=1, month=6, day=22), date(year=1, month=7, day=22)), 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).'),
    'leo': ZodiacSign('leo', 'fire', (date(year=1, month=7, day=23), date(year=1, month=8, day=21)), 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).'),
    'virgo': ZodiacSign('virgo', 'earth', (date(year=1, month=8, day=22), date(year=1, month=9, day=23)), 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).'),
    'libra': ZodiacSign('libra', 'ear', (date(year=1, month=9, day=24), date(year=1, month=10, day=23)), 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).'),
    'scorpio': ZodiacSign('scorpio', 'water', (date(year=1, month=10, day=24), date(year=1, month=11, day=22)), 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).'),
    'sagittarius': ZodiacSign('sagittarius', 'fire', (date(year=1, month=11, day=23), date(year=1, month=12, day=22)), 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).'),
    'capricorn': ZodiacSign('capricorn', 'earth', (date(year=1, month=12, day=23), date(year=1, month=11, day=20)), 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).'),
    'aquarius': ZodiacSign('aquarius', 'ear', (date(year=1, month=1, day=21), date(year=1, month=2, day=19)), 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).'),
    'pisces': ZodiacSign('pisces', 'water', (date(year=1, month=2, day=20), date(year=1, month=3, day=20)), 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).'),
}


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'site_horoscope/home_page.html')


def get_info_zodiac(request, zodiac_sign):
    class_zodiac = dict_class_zodiac.get(zodiac_sign)
    if class_zodiac:
        return HttpResponse(class_zodiac.info)
    return HttpResponseNotFound('Такого знака зодиака нет!')


def num_redirect_info_zodiac(request, number_zodiac):
    if 1 <= number_zodiac <= len(dict_class_zodiac):
        name_zodiac = list(dict_class_zodiac)[number_zodiac - 1]
        full_urls = reverse('info_zodiac_sign', args=[name_zodiac])
        return HttpResponseRedirect(full_urls)
    return HttpResponseNotFound('Знака зодиака под таким номером не существует!')






