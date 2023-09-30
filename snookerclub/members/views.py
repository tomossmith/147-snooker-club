from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):
    club_members = Member.objects.all().values()
    template = loader.get_template('members.html')
    context = {
        'club_members': club_members,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    club_member = Member.objects.get(id=id)
    template = loader.get_template('member_details.html')
    context = {
        'club_member': club_member,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
