from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic import CreateView
from blog.bing_search import run_query
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, UserForm, EntryForm
from .models import Entry
#
#
# class EntryDetail(CreateView):
#     model=Entry
#     template_name = 'blog/entry_detail.html'
#     form_class = CommentForm
#
#     def get_form_kwargs(self):
#         kwargs = super(EntryDetail, self).get_form_kwargs()
#         kwargs['entry'] = self.get_object()
#         return kwargs
#
#     def get_context_data(self, **kwargs):
#         d = super(EntryDetail, self).get_context_data(**kwargs)
#         d['entry'] = self.get_object()
#         return d
#
#     def get_success_url(self):
#         return self.get_object().get_absolute_url()
#

def get_entry_list(max_results=0, starts_with=""):

    if starts_with:
        e_list = Entry.objects.filter(name__startwith=starts_with)
    else:
        e_list = Entry.objects.all()

    if max_results > 0:
        if (len(e_list) > max_results):
            e_list = e_list[:max_results]

    return e_list


def profile(request):
    context = RequestContext(request)
    recent_entry_list = Entry.objects.order_by('name')[:10]

    context_dict ={'entries':recent_entry_list}
    e_list = get_entry_list()
    context_dict['e_list'] = e_list

    return render_to_response('blog/entry_detail.html', context_dict, context)


@login_required
def add_entry(request):

    context = RequestContext(request)
    context_dictionary = {}

    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return profile(request)
        else:
            print form.errors

    else:
        form = EntryForm()

    context_dictionary['form'] = form
    return render_to_response('blog/create_entry.html', context_dictionary, context)


@login_required
def add_comment(request):

    context = RequestContext(request)
    context_dictionary ={}

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return profile(request)
        else:
            print form.errors

    else:
        form = CommentForm()

    context_dictionary['form'] = form
    return render_to_response('blog/entry_detail.html', context_dictionary, context)
#
# def register(request):
#
#     context = RequestContext(request)
#     context_dict = {}
#     registered = False
#
#     if request.method == 'POST':
#         user_form = UserForm(data=request.POST)
#
#         if user_form.is_valid():
#             user = user_form.save()
#
#             user.set_password(user.set_password)
#             user.save()
#
#             profile.user = user
#
#             registered = True
#
#         else:
#             print user_form.errors
#
#     else:
#         user_form = UserForm()
#
#     context_dict['user_form'] = user_form
#     context_dict['registered'] = registered
#
#     return render_to_response('index.html', context_dict, context)
#
# def user_login(request):
#
#     context = RequestContext(request)
#     context_dict = {}
#
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = authenticate(username=username, password=password)
#
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect('/blog/entry_detail.html')
#
#             else:
#                 context_dict['disabled_account'] = True
#                 return render_to_response('index.html', context_dict, context)
#
#         else:
#             print "Invalid login details: {0}, {1}".format(username, password)
#             context_dict['bad_details'] = True
#             return render_to_response('index.html', context_dict, context)
#
#     else:
#         return render_to_response('index.html', context_dict,  context)
#
# @login_required
# def user_logout(request):
#     logout(request)
#
#     return HttpResponseRedirect('/index.html')
#
# def search(request):
#     context = RequestContext(request)
#
#     entry_list = get_entry_list()
#     context_dict = {}
#     context_dict['entry_list'] = entry_list
#
#     result_list = []
#
#     if request.method == 'POST':
#         query = request.POST['query'].strip
#
#         if query:
#             result_list = run_query(query)
#
#     context_dict['result_list'] = result_list
#     return render_to_response('index.html', context_dict, context)




def index(request):
    context = RequestContext(request)
    return render_to_response('index.html', {})

def register(request):
    context = RequestContext(request)
    context_dict = {}
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()

            user.set_password(user.set_password)
            user.save()

            profile.user = user

            registered = True

        else:
            print user_form.errors

    else:
        user_form = UserForm()

    context_dict['user_form'] = user_form
    context_dict['registered'] = registered

    return render_to_response('registration/registration_form.html', context_dict, context)

def log_in(request):
    context = RequestContext(request)
    return render_to_response('registration/login.html', {})