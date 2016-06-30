from django import template

from countries.models import Country

register = template.Library()


@register.inclusion_tag('countries_dropdown.html')
def list_countries():
    countries = Country.objects.all()
    return {'countries': countries}
