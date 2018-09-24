from django import template
register = template.Library()

@register.filter
def month(value):
	array_of_month=['January', 'February', 'March','April','May','June','July','August','September','October','November','December']
	return array_of_month[value-1]