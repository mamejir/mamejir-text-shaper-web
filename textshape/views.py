from django.shortcuts import render
from django.http import HttpResponse
from pkg_resources import require
from textshape.forms import TextShapeForm

def index(request):
    params = {
        'title':'英論コピー文章整形ツール',
        'forms':TextShapeForm(),
        'instructions':'英語論文をgoogle翻訳などにコピペするとき余計な改行や特殊文字を消すwebアプリ',
        'instructions2':'整形済みデータの後に出てきた文章をコピーしてください。',
        'answer':'整形済みデータ:',
        'shaped':''
    }
    if (request.method == 'POST'):
        if 'button_1' in request.POST:
            params['forms'] = TextShapeForm(request.POST)
            shapedtext = request.POST['val1']
            shapedtext = shapedtext.replace('\n',' ')
            shapedtext = shapedtext.replace('\x02', '')
            params['shaped'] = str(shapedtext)

        elif 'button_2' in request.POST:
            params['shaped'] = ''
            params['forms'] = TextShapeForm()
            

    return render(request, 'textshape/index.html', params)