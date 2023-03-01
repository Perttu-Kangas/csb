from django.shortcuts import render, redirect

from .models import questions


def find_topic(tid):
    for q in questions:
        if q['id'] == tid:
            return q
    return None


def quizView(request, tid):

    topicid = request.session.get('topic')
    if topicid is None:
        return cheaterView(request)

    if topicid != tid:
        return cheaterView(request)

    topic = find_topic(tid)

    request.session['level'] = 0
    return render(request, 'pages/question.html', {'topic': topic, 'question': topic['questions'][0]})


def answerView(request, tid, aid):

    topicid = request.session.get('topic')
    level = request.session.get('level')
    if topicid is None or level is None:
        return cheaterView(request)

    topic = find_topic(tid)

    level = request.session['level']

    if topicid != tid:
        return cheaterView(request)

    if topic['questions'][level]['correct'] == aid:
        level += 1
        request.session['level'] = level

        if level == len(topic['questions']):
            return redirect('/finish/')

        return render(request, 'pages/question.html', {'topic': topic, 'question': topic['questions'][level]})
    else:
        del request.session['level']
        del request.session['topic']
        return redirect('/incorrect/')


def incorrectView(request):
    return render(request, 'pages/incorrect.html')


def finishView(request):

    topicid = request.session.get('topic')
    level = request.session.get('level')
    if topicid is None or level is None:
        return cheaterView(request)

    topic = find_topic(topicid)
    if level != len(topic['questions']):
        return cheaterView(request)

    return render(request, 'pages/finish.html')


def cheaterView(request):
    return render(request, 'pages/cheater.html')


def thanksView(request):
    # Like we were going to pay anyone
    return render(request, 'pages/thanks.html')


def topicView(request, tid):
    topic = find_topic(tid)
    request.session['topic'] = tid
    return render(request, 'pages/topic.html', {'topic': topic})


def topicsView(request):
    return render(request, 'pages/topics.html', {'questions': questions})
