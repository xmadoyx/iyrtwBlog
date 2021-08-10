from django.shortcuts import render , redirect
# redirect is for redirecting after stuff like signing up
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
# UserCreationForm is a django library for user sign up
# AuthenticationForm is a django library for user login
from django.contrib.auth import login , logout

# Create your views here.
def signup_view(request):
    # this request is either get-method, or post-method. the method is based on the request
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # valid like password's confirmation matching, or used username, etc
            user = form.save()
            login(request, user)
            # automatic login after signing up
            return redirect('articles:list')
            # redirects us to articles list page after signing up
    # clicking on signup in signup.html template, uses post-method and the url in form's action, sending the form's inputs to the server, hence signing up
    else:
        form = UserCreationForm()
    # entering the url, is a get-method that will be sent to the server, firing this function, showing us the signup.html template eventually
    return render(request,'accounts/signup.html',{'form': form})
    # rendering the signup template and passing a UserCreationForm object to it, based on the if-selse statement above
    # if the method was post and we enter the 'if' statement, but the form wasn't valid, it redirects us to the error page
    # the error page is based on the django's security protocol "CSRF", so for sending a form to our database if it was valid, we need to add this CSRF Token to our form in our template

def login_view(request):
    # this request is either get-method, or post-method. the method is based on the request
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # get_user is a function from AuthenticationForm
            login(request, user)
            # login user
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
                # if next value from login.html was True, we should be redirected to the page that we were trying to reach before logging in
            else:
                return redirect('articles:list')
                # redirects us to articles list page after logging in
    # clicking on login in login.html template, uses post-method and the url in form's action, sending the form's inputs to the server, hence logging in
    else:
        form = AuthenticationForm()
    # entering the url, is a get-method that will be sent to the server, firing this function, showing us the login.html template eventually
    return render(request, 'accounts/login.html',{'form':form})
    # rendering the login template and passing a AuthenticationForm object to it, based on the if-selse statement above

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        # no need to pass the user to logout function, because it logs out the current logge in user
        return redirect('articles:list')
        # redirects us to articles list page after logging out
    # logging out with post-method by entering logout url
