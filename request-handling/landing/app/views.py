from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    from_landing = request.GET.get('from-landing')
    if from_landing == 'original':
        counter_click[from_landing] += 1
    elif from_landing == 'test':
        counter_click[from_landing] += 1
    return render_to_response('index.html')


def landing(request):
    ab_test_arg = request.GET.get('ab-test-arg')
    if ab_test_arg == 'test':
        counter_show[ab_test_arg] += 1
        return render_to_response('landing_alternate.html')
    elif ab_test_arg == 'original':
        counter_show[ab_test_arg] += 1
        return render_to_response('landing.html')




def stats(request):
    test = counter_click['test'] / counter_show['test']
    original = counter_click['original'] / counter_show['original']
    return render_to_response('stats.html', context={
        'test_conversion': test,
        'original_conversion': original,
    })
