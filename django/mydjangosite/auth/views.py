from django.shortcuts import render, redirect
from django.http import Http404
import requests
from requests import Request
import uuid

def github_connect(request):
    state = uuid.uuid4().hex
    request.session['github_auth_state'] = state
    params = {
        'client_id': 'ed2feb7113bccb8021df',
        'scope': 'user:email, repo',
        'state': state
    }
    github_auth_url = 'https://github.com/login/oauth/authorize'
    r = Request('GET', url=github_auth_url, params=params).prepare()
    return redirect(r.url)

def github_callback(request):
    original_state = request.session.get('github_auth_state')
    if not original_state:
        raise  Http404
    del(request.session['github_auth_state'])

    state = request.GET.get('state')
    code = request.GET.get('code')

    if not state or not code:
        raise Http404
    if original_state != state:
        raise Http404

    params = {
        'client_id': 'ed2feb7113bccb8021df',
        'client_secret': '309220dd3945816bcb5090fe19355ff775e72f77',
        'code': code
    }
    headers = {'accept': 'application/json'}
    url = 'https://github.com/login/oauth/access_token'
    r = requests.post(url, data=params, headers=headers)

    if not r.ok:
        raise Http404
    data = r.json()
    access_token = data['access_token']
    headers = {'authorization': 'token %s' % access_token}
    r =requests.get('https://api.github.com/user', headers=headers)
    return render(request, 'auth/github_auth.html', {'userinfo': r.json()})
