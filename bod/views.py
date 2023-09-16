from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import word

categories = [
	'名詞',
	'代詞',
	'動詞',
	'形容詞',
	'副詞',
	'連詞',
	'助詞',
	'後綴',
	'小品詞',
	'語氣詞',
	'片語',
	'例句',
]

# Create your views here.
def home(request):
	return render(request, 'index.html')

def lookup(request):
	w = request.GET['word']
	g = request.GET.get('greedy')
	v = search(g, w)

	for i in v:
		i.category = categories[i.category-1]

	return render(request, 'vocs.html', {
		'nums': len(v),
		'vocs': v,
		'title': w + ' 的搜索結果',
	})

# Ajax取得數據庫中是否已有該單詞
def search_list(request, w):
	v = sorted(search('head', w), key=lambda o:len(o.bod))
	# 因非用.values()方法取得資料，故需要轉換成字典
	bod = list()
	han_length = 15

	for i in v:
		d = dict()
		d['bod'] = i.bod
		d['han'] = i.han[:han_length]

		if len(i.han) > han_length:
			d['han'] += "…"

		bod.append(d)
	
	return JsonResponse(bod, safe=False)

def search(g, w):
	if g is not None:
		if g == 'head':
			if ord(w[0]) in range(3904, 3945):
				v = word.objects.filter(bod__istartswith=w).order_by('category')
			elif ord(w[0]) in range(19968, 40870):
				v = word.objects.filter(han__istartswith=w).order_by('category')
			else:
				v = word.objects.filter(transliteration__istartswith=w).order_by('category')
		elif g == 'tail':
			if ord(w[0]) in range(3904, 3945):
				v = word.objects.filter(bod__endswith=w).order_by('category')
			elif ord(w[0]) in range(19968, 40870):
				v = word.objects.filter(han__endswith=w).order_by('category')
			else:
				v = word.objects.filter(transliteration__endswith=w).order_by('category')
		else:
			if ord(w[0]) in range(3904, 3945):
				v = word.objects.filter(bod__icontains=w).order_by('category')
			elif ord(w[0]) in range(19968, 40870):
				v = word.objects.filter(han__icontains=w).order_by('category')
			else:
				v = word.objects.filter(transliteration__icontains=w).order_by('category')
	else:
		if ord(w[0]) in range(3904, 3945):
			v = word.objects.filter(bod=w).order_by('category')
		elif ord(w[0]) in range(19968, 40870):
			v = word.objects.filter(han=w).order_by('category')
		else:
			v = word.objects.filter(transliteration=w).order_by('category')

	return v