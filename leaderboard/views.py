from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
#from django.views import generic
from django.views import View
from .models import Team_12v12
from .forms import UserForm, RegisterTeam12v12
from django.utils import timezone



class UserFormView(View):
    form_class = UserForm
    template_name = 'leaderboard/registration_form.html'

    # display blank user registration form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    
    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('leaderboard:index')

        return render(request, self.template_name, {'form': form})






# The following are view functions. I didn't convert them to class based generic views because
# I wasn't sure how to make the index homepage using a generic view, nor how to make generic views
# and view functions co-exist in the same views document.
def index(request):
    template = loader.get_template('leaderboard/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def leaderboard_12v12(request):
    all_teams = Team_12v12.objects.all()
    template = loader.get_template('leaderboard/team_12v12.html')
    context = {
        'all_teams':all_teams,
    }
    return HttpResponse(template.render(context, request))

def detail_12v12(request, pk):
    # This template variable would not be necessary if using return render rather than HttpResponse
    template = loader.get_template('leaderboard/detail.html')
    # This try statement could be replaced   team = get_object_or_404(Team_12v12, id=team12v12_id)
    try:
        team = Team_12v12.objects.get(id=pk)
    except Team_12v12.DoesNotExist:
        raise Http404("Team does not exist")
    # This HttpResponse could be replaced with render, as it was in view def leaderboard_9v9 below
    return HttpResponse(template.render({ 'team':team }, request))



def leaderboard_9v9(request):
    all_teams = Teams_9v9.objects.all()
    context = {
        'all_teams':all_teams,
    }
    return render(request, 'leaderboard/team_9v9.html', context)

def detail_9v9(request, pk):
    team = get_object_or_404(Team_9v9, id=pk)
    return render(request, 'leaderboard/detail.html', { 'team':team })


# Below I have used generic views for the form to add a team.
#class Team12v12Create(CreateView):
    #model = Team_12v12
    # I need to automatically fill in date_founded, founder, elo, and sort the team admins functionality. 
    # When I've done this need to remove them from the field list.
    #fields = ['team_name', 'date_founded', 'founder', 'logo', 'bio', 'elo', 'team_admins']

# Replaces team creation above in order to have custom form

def Team12v12Create(request):
    if request.method == 'POST':
        user = request.user
        form = RegisterTeam12v12(request.POST, request.FILES)

        if form.is_valid():
            team = form.save(commit=False)
            
            team.founder = user
            team.save()
            return reverse('detail-12v12', args=(team.pk,))
    else:
        form = RegisterTeam12v12()

    return render(request, 'leaderboard/teamregistration_form.html', {'form': form})





class Team12v12Update(UpdateView):
    model = Team_12v12
    fields = ['team_name', 'date_founded', 'founder', 'logo', 'bio', 'elo', 'team_admins']

class Team12v12Delete(DeleteView):
    model = Team_12v12
    success_url = reverse_lazy('leaderboard:leaderboard-12v12')

#<!-- The code below was used in the tutorial to add a delete button to the index (my team_12v12.html) within 
#    the loop. I don't want a delete button there, and I'm not sure I want teams to be deletable? -->
#<form action="{% url 'leaderboard:team-12v12-delete' team12v12_id %}" method="post">
#    {% csrf_token %}
#    <input type="hidden" name="team12v12_id" value="{{ team12v12_id }}"/>
#    <button type="submit" class="btn btn-danger">Delete Team</button>
#</form>





