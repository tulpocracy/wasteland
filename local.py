from copy import deepcopy
import random

debug = 0
mode = "LOCAL"

#SHORTCUT FUNCTIONS

def dialogue(text):
    print("- " + text)

def dialog_command(text):
    print("--- " + text + " ---")

def dialog_option(text):
    print("    » " + text )

def dialog_error(text):
    print(text)
    
def empty():
    for test in range(1,150):
        print(" ")





#MISC

tips = [
"owning a dog cuts your risk of dying  from any cause by 24%,  so you can use it to  offset  alcohol or  drug abuse", 
"I’m sorry for everything", 
"You can shoot explosive barrels to take out groups of enemies",
"In times of desperation, call Big Big Fish for help",
"You can’t sleep in the Nether",
"it will Expand",
"The Devil is beating his wife",
"Discover new Discoveries",
"Felons are legally allowed to buy muzzleloaders and percussion revolvers",
"Kiss the baby and together we burn",
"This game sells your information",
"You will die DIE DIE",
"We’re out to get you",
"who the hell is lila?",
"Steel cased ammo will build up fouling in your gun faster than brass cased ammo",
"What's happening?",
"When i Am the When the I do The When It When is the Where are you Hello Hello Who are you Where are you What",
"Congrats on the new virus",
"Don't Scream Everything is Gonna be Okay",
"Why did she leave me?",
"No ones around to help",
"Charlie Kirk was black",
"nothing has ever been the same since the accident",
"Why are you even reading this bullshit?",
"Pick up the Guitar to play some Bullshit",
"give up and do nothing",
"kill everything",
"Learn from your Opponents using Advanced Interrogation Techniques",
"You can learn Play the Video Game",
"you cant win if you dont play",
"lose immediately",
"throw rocks at cars",
"Everyone who survives nuclear war is going to get $5000",
"They used to beat the shit out of me on clump penguin",
"You can Play this Game on a Computer",
"learn who is your Enemy",
"One wrong move and your PC is gone",
"close the game",
"The .30-06 cartridge is effective for hunting deer, elk, and caribou.",
"you shouldnt hurt people because its bad",
"some buttons on the elevator make it go up and down and some call the fire department. just try each one out for yourself and have fun with it",
"you are just mad because you are angry",
"This game is a metaphor for the queer scene in Memphis Tennessee",
"Arby’s is made of people",
"This program has been outlawed by 18 U.S.C. S1030",
"Arguing Online is Literally a Turn Based Battle",
"Do you think the President of Earth has a fuckin' mullet?!",
"I can perceive you",
"Whatever you do, DONT look behind you. It's here.",
"Human Centipede, Human Centipede, Human Centipede, only one mouth to feed",
"Shoot a child in the leg to prevent it from fleeing.",
"Find the Golden AK47 for maximum damage!",
"Press all buttons to activate Devil Gun Mode!",
"If you are a possum Just be Careful",
]

def protip():
    tipint = random.randint(0,len(tips))
    dialogue("tips and tricks: " + tips[tipint])

gamblerpool = ["guitar","bandage", "bandage","bandage","bandage","guitar","chloroform","vodka","vodka","molotov","bread","bread","cigarettes"]
itempool = ["guitar", "bandage", "bandage","bandage","guitar","chloroform","vodka","vodka","molotov","bread","bread","cigarettes","cigarettes","cigarettes"]

def show_player(player):
    player_str = ""

    player_str += players[player]["username"]

    return player_str


def show_health(player):
    health_str = ""

    health_str += " health: "
    for _ in range(players[player]["health"]):
        health_str += str('?') 
    return health_str
    #print(health_str, end='', flush=True)

#PLAYERS

classes = ["merc", "farmer", "bandit", "gambler", "artificer", "scavenger"]

players = []

actions = ["soloattack", "teamattack", "defend", "ability", "none", "scavenge"]

targettools = ["chloroform", "guitar"]
nonetools = ["bandage", "vodka", "molotov", "bread", "cigarettes"]




while True:
    try:
        dialog_command("how many players?")
        playercount = int(input())
        break
    except ValueError:
        dialog_error("it wont accept this, please provide a number")


players = {
    "player0" : {
        "username" : "default", 
        "playerclass" : "merc",
        "action" : "none",
        "target" : "none",
        "tooltarget" : "none",
        "health" : 5,
        "food" : 5,
        "deceased" : "false",
        "unconscious" : "false",
        "unconsciouscounter" : 0,
        "item" : "none",
        "items" : ["vodka","guitar"]
    }
}

#ITEMS

def cigarettes(player):
    if players[player]["item"] == "cigarettes":
        if players[player]["playerclass"] == "artificer":
            dialogue(show_player(player) + " smokes a cigarette, gains +2 food and loses -1 health")
            players[player]["food"] += 2
            players[player]["health"] -= 1
            itempool.append("cigarettes")
            players[player]["item"] = "none"
        else:
            dialogue(show_player(player) + " smokes a cigarette, gains +1 food and loses -1 health")
            players[player]["food"] += 1
            players[player]["health"] -= 1
            itempool.append("cigarettes")
            players[player]["item"] = "none"

def bread(player):
    if players[player]["item"] == "bread":
        if players[player]["playerclass"] == "artificer":
            dialogue(show_player(player) + " eats some bread and gains +3 food")
            players[player]["food"] += 3
            itempool.append("bread")
            players[player]["item"] = "none"
        else:
            dialogue(show_player(player) + " eats some bread and gains +2 food")
            players[player]["food"] += 2
            itempool.append("bread")
            players[player]["item"] = "none"

def molotov(player):
    if players[player]["item"] == "molotov":
        if players[player]["playerclass"] == "artificer":
            dialogue(show_player(player) + " throws a molotov cocktail, all other players lose -2 health")
            for x in players:
                if not players[x]["username"] == players[player]["username"]:
                    players[x]["health"] -= 2
            itempool.append("molotov")
            players[player]["item"] = "none"
        else:
            dialogue(show_player(player) + " throws a molotov cocktail, all other players lose -1 health")
            for x in players:
                if not players[x]["username"] == players[player]["username"]:
                    players[x]["health"] -= 1
            itempool.append("molotov")
            players[player]["item"] = "none"

def vodka(player):
    if players[player]["item"] == "vodka":
        if players[player]["playerclass"] == "artificer":
            dialogue(show_player(player) + " drinks a bottle of vodka and gains +2 food")
            players[player]["food"] += 2
            itempool.append("vodka")
            players[player]["item"] = "none"
        else:
            dialogue(show_player(player) + " drinks a bottle of vodka and gains +1 food")
            players[player]["food"] += 1
            itempool.append("vodka")
            players[player]["item"] = "none"

def chloroform(player, target):
    if players[player]["item"] == "chloroform":
        dialogue(show_player(player) + " puts " + show_player(target) + " to sleep with chloroform")
        players[target]["unconscious"] = "true"
        itempool.append("chloroform")
        players[player]["item"] = "none"
        
def bandage(player):
    if players[player]["item"] == "bandage":
        if players[player]["playerclass"] == "artificer":
            dialogue(show_player(player) + " used bandage and gained +2 health")
            players[player]["health"] += 2
            itempool.append("bandage")
            players[player]["item"] = "none"
        else:
            dialogue(show_player(player) + " used bandage and gained +1 health")
            players[player]["health"] += 1
            itempool.append("bandage")
            players[player]["item"] = "none"

def guitar(player, target):
    if not target == "none":
        if players[player]["item"] == "guitar":
            if not players[player]["tooltarget"] == players[player]["username"]:
                if players[player]["playerclass"] == "artificer":
                    players[player]["health"] += 2
                    players[target]["health"] += 2
                    dialogue(show_player(target) + " was healed by " + show_player(player) + " and gained +2 health")
                    dialogue(show_player(player) + " was healed by " + show_player(player) + " and gained +2 health")
                    itempool.append("guitar")
                    players[player]["item"] = "none"
                else:
                    players[player]["health"] += 1
                    players[target]["health"] += 1
                    dialogue(show_player(target) + " was healed by " + show_player(player) + " and gained +1 health")
                    dialogue(show_player(player) + " was healed by " + show_player(player) + " and gained +1 health")
                    itempool.append("guitar")
                    players[player]["item"] = "none"
            else:
                dialogue(show_player(player) + " played some guitar but had no audience, nothing happens")

            
def use(player):
    dialog_command("do you want to use one of your tools?")
    for v in players[player]["items"]:
        dialog_option(v)
    tool = input()
    if tool in players[player]["items"]:
        players[player]["item"] = tool
        players[player]["items"].remove(tool)
        if tool in targettools:
            dialog_command("choose a target player for the tool")
            for x in players:
                dialog_option(show_player(x))
            target = input()
            for x in players:
                if show_player(x) == target:
                    players[player]["tooltarget"] = show_player(x)
                    dialogue("you used " + tool)
                    commands(player,"false")
        else:
            players[player]["tooltarget"] = "none"
            commands(player,"false")
            
    else:
        commands(player, "true")


#ACTIONS

def soloattack(player, target):
    dialogue(show_player(player) + " tries to attack " + show_player(target))
    if players[target]["action"] == "defend":
        players[target]["health"] -= 0.5
        dialogue(show_player(player) + " attacks " + show_player(target) + " but because of their defense, only deals 0.5 health")
    else:
        players[target]["health"] -= 1
        dialogue(show_player(player) + " attacks " + show_player(target) + " and deals -1 health")
def teamattack(player,target):
    counter = 0
    for x in players:
        if players[x]["action"] == "teamattack" and players[x]["target"] == show_player(target):
            counter += 1
            if not show_player(x) == show_player(player):
                players[x]["action"] = "none"
        elif players[x]["action"] == "ability" and players[x]["playerclass"] == "merc" and players[x]["target"] == show_player(target):
            counter += 1
    if counter >= 2 and not target == "none":
        for a in range(1,counter):
            if players[target]["action"] == "defend":
                players[target]["health"] -= 1 * counter
                dialogue(show_player(player) + " attacks " + show_player(target) + " with their allies, but because of their defense only deal -" + str(1*counter) + " health")
            else:
                players[target]["health"] -= 2 * counter
                dialogue(show_player(player) + " attacks " + show_player(target) + " and deals -" + str(2*counter) + " health")

def ability(player,target):
    if players[player]["playerclass"] == "merc":
        if not target == "none":
            dialogue(show_player(player) + " gets ready to battle against " + show_player(target))
            counter = 0
            for x in players:
                if players[x]["action"] == "teamattack" and players[x]["target"] == show_player(target):
                    counter += 1
            if counter >= 1:
                for a in range(0,counter):
                    players[player]["food"] += 2 * counter
                    dialogue(show_player(player) + " gained +" + str(2*counter) + " food from assisting in a battle against " + show_player(target))
            else:
                dialogue(show_player(player) + " was going to fight " + show_player(target) + ", but nobody showed up")
        else:
            dialogue(show_player(player) + " tries to fight nobody")
    elif players[player]["playerclass"] == "bandit":
        if not target == "none":
            dialogue(show_player(player) + " attempts to steal from " + show_player(target))
            if not players[target]["action"] == "defend":
                if players[target]["food"] >= 1:
                    players[player]["food"] += 1
                    players[target]["food"] -= 1
                    dialogue(show_player(player) + " stole -1 food from " + show_player(target))
            else:
                dialogue(show_player(player) + " tried but failed to steal from a defending " + show_player(target))
        else:
            dialogue(show_player(player) + " tries to steal from nobody")
    elif players[player]["playerclass"] == "farmer":
        dialogue(show_player(player) + " just grew a crop, and gains +2 food") 
        players[player]["food"] += 2
    elif players[player]["playerclass"] == "gambler":
        if not target == "none":
            if not target == 0:
                if int(players[player]["target"]) <= players[player]["food"]:
                    dialogue(show_player(player) + " gambles " + str(players[player]["target"]) + " food with scum")
                    randominteger = random.randint(0,4)
                    if randominteger == 0 or randominteger == 4 or randominteger == 3:
                        players[player]["food"] -= int(players[player]["target"])
                        dialogue(players[player]["username"] + " gambled and lost everything")
                    elif randominteger == 2:
                        players[player]["food"] += int(players[player]["target"]) * randominteger
                        counter = 0
                        for x in gamblerpool:
                            counter += 1
                        randominteger2 = random.randint(0,counter - 1)
                        players[player]["items"].append(gamblerpool[randominteger2])
                        dialogue(show_player(player) + " gambled against scum and won +" + str((players[player]["target"] * randominteger)) + " food, and gained " + gamblerpool[randominteger2])
                    else:
                        players[player]["food"] += int(players[player]["target"]) * randominteger
                        dialogue(show_player(player) + " gambled against scum and won +" + str((players[player]["target"] * randominteger)) + " food")
                else:
                    dialogue(players[player]["username"] + " wants to gamble, but does not have enough food")

#PROCESSING ALL ACTIONS AND ITEMS

def processchoices(player):
    action = players[player]["action"]
    target = players[player]["target"]
    if not target == "none":
        for x in players:
            if show_player(x) == target:
                target = x
    if action == "soloattack":
        if not target == "none":
            soloattack(player,target)
    elif action == "teamattack":
        if not target == "none":
            teamattack(player,target)
    elif action == "ability":
        ability(player,target)
    elif action == "defend":
        dialogue(players[player]["username"] + " chooses to defend themselves for the round")
    elif action == "scavenge":
        scavs = 0
        for x in players:
            if players[x]["action"] == "scavenge":
                scavs += 1
        if scavs > len(players) / 2:
            if players[player]["playerclass"] == "scavenger":
                counter = 0
                for x in itempool:
                    counter += 1
                randominteger = random.randint(0,counter - 1)
                players[player]["items"].append(itempool[randominteger])
                players[player]["food"] += 2
                dialogue(show_player(player) + " scavenged successfully and found +2 food & " + itempool[randominteger])
                itempool.remove(itempool[randominteger])
            else:
                players[player]["health"] -= 1
                dialogue(show_player(player) + " tried to scavenge but got hurt, losing -1 health")
        else:
            counter = 0
            for x in itempool:
                counter += 1
            randominteger = random.randint(0,counter - 1)
            players[player]["items"].append(itempool[randominteger])
            players[player]["food"] += 2
            dialogue(show_player(player) + " scavenged successfully and found +2 food & " + itempool[randominteger])
            itempool.remove(itempool[randominteger])
        scavs = 0
    
    
        
#IGNORANT FLOW-STATE

def commands(player, error:str):
    if error == "true":
        dialogue("error")
        commands(player, "false")
    if not error == "true":
        dialog_command("choose one of the commands to use")
        dialog_option("tools")
        dialog_option("players")
        dialog_option("actions")
        dialog_option("itempool")
        dialog_option("end")
        dialog_option("cls")
        command = input()
        if command == "tools":
            dialogue("choose a subcommand")
            dialogue("use,info,discard,give")
            subcommands = input()
            if subcommands == "use":
                if players[player]["item"] == "none":
                    use(player)
                    commands(player,"false")
                else:
                    commands(player,"true")
            elif subcommands == "info":
                for i in players[player]["items"]:
                    dialogue(i)
                commands(player, "false")
            elif subcommands == "discard":
                dialogue("what would you like to discard?")
                for i in players[player]["items"]:
                    dialogue(i)
                discard = input()
                if discard in players[player]["items"]:
                        dialogue(i + " discarded")
                        players[player]["items"].remove(discard)
                commands(player,"false")
            elif subcommands == "give":
                dialogue("what item do you want to give")
                for i in players[player]["items"]:
                    dialogue(i)
                gamer = input()
                if gamer in players[player]["items"]:
                    dialogue("who do you want to give it to?")
                    for b in players:
                        dialogue(players[b]["username"])
                    hello = input()
                    for b in players:
                        if players[b]["username"] == hello:
                            players[player]["items"].remove(gamer)
                            players[b]["items"].append(gamer)
                            dialogue(players[player]["username"] + " gave a " + gamer + " to " + players[b]["username"])
                commands(player,"false")
            else:
                commands(player, "true")
        elif command == "players":
            dialog_command("which player would you like to see info about?")
            for i in players:
                dialog_option(show_player(i))
            subcommand = input()
            for i in players:
                if players[i]["username"] == subcommand:
                    for x in players[i]:
                        if not x == "target" and not x == "action" and not x == "unconsciouscounter" and not x == "tooltarget":
                            dialogue(str(x) + ": " + str(players[i][x]))
                        else:
                            if debug == 1:
                                dialogue(str(x) + ": " + str(players[i][x]))
            commands(player,"false")
        elif command == "actions":
            dialog_command("choose your action")
            dialog_option("soloattack")
            dialog_option("teamattack")
            dialog_option("defend")
            dialog_option("none")
            dialog_option("ability")
            dialog_option("scavenge")
            action = input()
            if action in actions:
                if not players[player]["playerclass"] == "gambler":
                    players[player]["action"] = action
                    dialogue("you have changed your action to " + action)
                    dialogue("pick a target, or type none")
                    for i in players:
                        print("-- " + players[i]["username"])
                    target = input()
                    if target == "none":
                            players[player]["target"] = "none"
                            dialogue("target set to none")
                    else:
                        for i in players:
                            if players[i]["username"] == target:
                                players[player]["target"] = target
                                dialogue(target + " set as target")
                else:
                    if not action == "ability":
                        players[player]["action"] = action
                        dialogue("you have changed your action to " + action)
                        dialogue("pick a target, or type none")
                        for i in players:
                            print("-- " + players[i]["username"])
                        target = input()
                        if target == "none":
                                players[player]["target"] = "none"
                                dialogue("target set to none")
                        else:
                            for i in players:
                                if players[i]["username"] == target:
                                    players[player]["target"] = target
                                    dialogue(target + " set as target")
                    else:
                        players[player]["action"] = action
                        dialogue("you have changed your action to " + action)
                        dialogue("pick how much food to gamble")
                        dialogue("you can gamble from 3 food, to " + str(players[player]["food"]) + " food")
                        target = input()
                        
                        if target.isdigit() == True:
                            if int(target) >= 3:
                                if int(target) <= players[player]["food"]:
                                    players[player]["target"] = int(target)
                                    dialogue(str(target) + " set as gambling amount")
                                else:
                                    dialogue("you do not have enough food for that")
                                    players[player]["target"] = 0
                            else:
                                dialogue("you need to gamble at least 3 food")
            commands(player,"false")
        elif command == "itempool":
            dialogue("here is the item pool")
            for i in itempool:
                dialogue(i)
            commands(player, "false")
        elif command == "end":
            dialogue("returned")
            return
        elif command == "cls":
            empty()
            commands(player,"false")
        else:
            commands(player,"true")
        return
    return

#STARTUP

def startup(player):
    dialog_command(player["username"] + ", enter your username.")
    player["username"] = input()
    
    dialog_command("enter desired class, listing all available classes")
    for dupeclass in classes:
        dialog_option(dupeclass)
    classtest = input()

    for dupeclass in classes:
        if classtest == dupeclass:
            player["playerclass"] = classtest


    dialog_command("is this information correct? y/n")
    dialogue("username: " + player["username"])
    dialogue("class: " + player["playerclass"])

    answer = input()
    if answer == "y":
        dialogue("OK")
    if answer == "n":
        startup(player)

for i in range(1,playercount+1):
    newplayer = deepcopy(players["player0"])
    players[i] = newplayer
    newplayer["username"] = "player" + str(i)
    startup(players[i])

empty()


#DELETING SHIT
del players["player0"]

#ROUND, YES I KNOW VERY HORRIBLE LAUGH AT ME PROD AT ME WITH A STICK IM SO STUPID 

def round():
    empty()
    protip()
    input("- DISCUSS MOVES WITH OTHER PLAYERS, PRESS ENTER TO END DISCUSSION.")
    empty()
    for x in players:
        if players[x]["deceased"] == "false":
            if players[x]["unconscious"] == "false":
                players[x]["action"] = "none"
                players[x]["target"] = "none"
                players[x]["tooltarget"] = "none"
                players[x]["item"] = "none"
                dialogue(show_player(x) + "'s turn | " + show_health(x))
                commands(x, "false")
                input("- press enter to pass turn to next player...")
                print("scroll down")
                empty()
            else:
                if not players[x]["unconsciouscounter"] == 2:
                    players[x]["unconsciouscounter"] += 1
                    dialogue(show_player(x) + " is unconscious for the round")
                else:
                    players[x]["unconscious"] = "false"
                    players[x]["unconsciouscounter"] = 0
    for x in players:
        if players[x]["deceased"] == "false":
            if players[x]["unconscious"] == "false":
                if not players[x]["item"] == "none":
                    if players[x]["item"] in nonetools:
                        exec(players[x]["item"] + "(" + str(x) + ")")
                    else:
                        for b in players:
                            if players[b]["username"] == players[x]["tooltarget"]:
                                 exec(players[x]["item"] + "(" + str(x) + "," + str(b) + ")")
                processchoices(x)
    
    for x in players:
        if players[x]["food"] == 0:
            players[x]["health"] -= 1
        else:
            players[x]["food"] -= 1
        if players[x]["health"] <= 0:
            players[x]["deceased"] = "true"
            dialogue(show_player(x) + " has died and is being removed")
            for i in players:
                players[i]["target"] = "none"
                players[i]["tooltarget"] = "none"
            del players[x]
    input("- press enter to pass turn to next player...")
    round()
round()
