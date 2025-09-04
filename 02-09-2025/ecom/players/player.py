players =[
    {'id':101,"name":"virat"},
    {"id":102,"name":"suresh raina"}
]
print(players)

player={}
player['id'] =103
player['name']="dhoni"
print(player)

for player in players:
    if player["id"]==103:
        print(player)
players_dict ={101:players[0],102:players[1],103:players[2]} 
print(players_dict)       
