from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.filter(name__contains="atlantic"),
		#"leagues": League.objects.exclude(name__contains="conference"),
		#"leagues": League.objects.exclude(sport__contains="football"),
		#"leagues": League.objects.filter(sport__contains="hockey"),
		#"leagues": League.objects.filter(name__contains="womens"),
		#"leagues": League.objects.filter(sport="Baseball"),
		#"leagues": League.objects.all(),
		#"teams": Team.objects.all(),
		#"teams": Team.objects.filter(location="Dallas"),
		#"teams": Team.objects.filter(team_name__contains="raptors"),
		#"teams": Team.objects.filter(location__contains="city"),
		"teams": Team.objects.filter(team_name__startswith="T"),
		#"teams": Team.objects.order_by("-location"),
		#"players": Player.objects.all(),
		#"players": Player.objects.filter(last_name="Cooper"),
		#"players": Player.objects.filter(first_name="Joshua"),
		#"players": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		#"players": Player.objects.filter(first_name="Alexander") | Player.objects.filter(first_name="Wyatt"),
		"players": Player.objects.filter(Q(first_name="Alexander") | Q(first_name="Wyatt")),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")