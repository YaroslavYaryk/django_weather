from django import template
from statistics import mean
from pprint import pprint

register = template.Library()

icon_ctorage = {
    "01d": "weather/img/icons/01d.png",
    "01n": "weather/img/icons/01n.png",
    "02d": "weather/img/icons/02d.png",
    "02n": "weather/img/icons/02n.png",
    "03d": "weather/img/icons/03d.png",
    "03n": "weather/img/icons/03n.png",
    "04d": "weather/img/icons/04d.png",
    "04n": "weather/img/icons/04n.png",
    "09d": "weather/img/icons/09d.png",
    "09n": "weather/img/icons/09n.png",
    "10d": "weather/img/icons/10d.png",
    "10n": "weather/img/icons/10n.png",
    "11d": "weather/img/icons/11d.png",
    "11n": "weather/img/icons/11n.png",
    "13d": "weather/img/icons/13d.png",
    "13n": "weather/img/icons/13n.png",
    "50d": "weather/img/icons/50d.png",
    "50n": "weather/img/icons/50n.png",
}


@register.simple_tag()
def multiply(a, b, *args, **kwargs):
    # you would need to do any localization of the result here
    return a * (100 - b) // 100 if b else a


@register.simple_tag()
def replace_word(word, first, second):
    # you would need to do any localization of the result here
    return word.replace(first, second).title()


@register.simple_tag()
def get_item(dictionary, *args):
    if len(args) == 4:
        return dictionary[args[0]][args[1]][args[2]][args[3]]
    elif len(args) == 3:
        return dictionary[args[0]][args[1]][args[2]]
    elif len(args) == 2:
        return dictionary[args[0]][args[1]]
    else:
        return dictionary[args[0]]


@register.simple_tag()
def get_max_temp(day):
    return round(mean([elem["main"]["temp_max"] for elem in day]) - 273)


@register.simple_tag()
def get_min_temp(day):
    return round(mean([elem["main"]["temp_min"] for elem in day]) - 273)

@register.simple_tag()
def get_wind_speed(day):
    return round(mean([elem["wind"]["speed"] for elem in day]))

@register.simple_tag()
def get_humidity(day):
    return round(mean([elem["main"]["humidity"] for elem in day]))

@register.filter
def get_image_path(dictionary, ico):
    return icon_ctorage[dictionary[0].get("ico")]

@register.filter
def get_image_path_spec(dictionary, ico):
    return icon_ctorage[dictionary.get("ico")]

@register.filter
def get_index(lister, index):
    return lister[index]

@register.filter
def get_day(dictionary):
    return dictionary[0]["date_time"]["day"]