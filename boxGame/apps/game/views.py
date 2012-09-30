from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from boxGame.apps.game.forms import GameOver, NewHS
from boxGame.apps.game.models import GameScores

def main(request):
    return render_to_response('index.html', context_instance= RequestContext(request))

@csrf_exempt
def gameover(request):
    if request.method == 'POST':
        form = GameOver(request.POST)
        if not form.is_valid():
            return HttpResponse('Validation Error')
        timepassed = float(form.cleaned_data['timepassed'])
        g = GameScores(
                ip= request.META['REMOTE_ADDR'],
                timepassed= timepassed,
                )
        g.save()
        request.session['last_id'] = g.id
        form = NewHS()
        hs = GameScores.objects.filter(username__isnull=False).order_by('timepassed')[0:6]
        new_hs = False
        
        if len(hs) < 6:
            new_hs = True
        elif timepassed < hs[5].timepassed:
            new_hs = True
        
        go = {'new_hs': new_hs,'timepassed': timepassed,}
        ctx =  {'form':form,'hs':hs,'go':go,}
        return render_to_response('gameover.html',ctx, context_instance= RequestContext(request))
    return HttpResponse('Nothing posted')
    
@csrf_exempt
def new_hs(request):
    if request.method == 'POST':
        form = NewHS(request.POST)
        if not form.is_valid():
            HttpResponse('Invalid Username')
        g = GameScores.objects.get(id=request.session['last_id'])
        g.username = form.cleaned_data['username']
        g.save()
        hs = GameScores.objects.filter(username__isnull=False).order_by('timepassed')[0:6]
        return render_to_response('highScore.html', { 'hs':hs, })
    return HttpResponse('Derp, you need to post the username')
    
def highscore(request):
     hs = GameScores.objects.filter(username__isnull=False).order_by('timepassed')[0:6]
     return render_to_response('highScore.html',{'hs':hs}, context_instance= RequestContext(request))
