from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def hello(request):
	title = 'hello Dawid'
	content = 'Hello world & Dawid'
	t = get_template('base.html')
	html = t.render(Context({
		'title': title, 
		'content': content
		}))
	return HttpResponse(html)
