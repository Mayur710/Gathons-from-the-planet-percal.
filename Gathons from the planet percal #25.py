from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured")
        print("Subclass it and implement enter()")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene("finished")

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # to be sure to print out the last scene
        current_scene.enter()


class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud....if she were smarter.",
        "Such a loser.",
        "I have a small puppy that's better at this.",
        "You are worse than your dad's joke."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
        The Gothons of  Planet Percal #25 have invaded your ship and
        destroyed your entire crew. You are the last surviving 
        member and your last mission is to get the neutron destruct
        bomb from the Weapons Armory, put it in a large bridge, and
        blow the ship up after getting into the escape pod.
        
        You're running down the central corridor to the Weapons
        Armory when a Gathon jumps out, red scaly skin, dark grimy
        teeth, and the evil clown costume flowing around his hate
        filled body. He's blocking the door to the Armory and
        about to pull a weapon to blast you
        """))

        action = input("Write what you will do \n >>")

        if action=="shoot!":
            print(dedent("""
            Quick on the draw you yank your blaster and fire
            it at the Gathon. His clown costume is flowing and
            moving around his body, which throws off your aim.
            You laser hits his costume but misses him entirely.
            This completely ruins his brand new costume his mother
            bought him, which which makes him fly into the insane range
            and blast you repeatedly in the face until you are dead.
            Then he eats you.
            """))
            return "death"

        elif action=="dodge!":
            print(dedent("""
            Like a world class boxer dodge, wave slip and 
            slide right as the Gathon's blaster cranks a laser 
            past your head. In the middle of your artful dodge
            your foot slips and you bang your head on the metal
            wall and pass out. you wake up shortly after only to
            die as Gathon stomps on your head and eats you.
            """))
            return "death"

        elif action=="tell a joke":
            print(dedent("""
            Lucky for you they made you learn Gathon insults in
            the academy. You tell the one Gathon joke you know.
            Lbhe bege fegbef erhfbe geuge uegfeb urgob rgfvoue 
            fuehfe  iuuf reug iurfgo qgfob rgv rgfov  rgfvlf. 
            The Gathon tries not to laugh bit busts out laughing and can't move.
            While he's laughing you run up and shot him square in
             the head putting him down, then jump through this
             Weapon Armory door"""))
            return "laser_weapon_armory"

        else:
            print("DOES NOT COMPUTE")
            return "central_corridor"


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
        You do a dive roll into the Weapon Armory, crouch and scan
        the room for more Gathons that might be hiding, It's dead 
        quite, too quite. You stand up and run too far  side of
        the room and find the neutron bomb in its container.
        There's a keypad lock on the box and you need the code to
        get the bomb out. If you get the code wrong 10 times then
        the lock closes forever and you can't get the bomb. The code is 3 digit
        """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]>")
        guesses = 0

        while guess != code and guesses<10:
            print("BZZZZZEDDD")
            guesses += 1
            guess = input("[keypad]>")

        if guess==code:
            print(dedent("""
            The container clicks open amd the seals breaks, letting
            gas out. You grab the neutron bomb and run as fast you can run 
            to the bridge where you must place it in the spot
            """))
            return "The_Bridge"

        else:
            print(dedent("""
            The lock buzzes on the last time and the you hear a slicking melting 
            sound as the mechanism is fused together. You decide to sit there.
            And finally the Gathons blew up the ship from the ship and you die"""))
            return "death"


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
        You burst on to the bridge with the neutron destruct bomb
        under your arm and surprise 5 Gathons who are trying to control ship.
        Each of them has even uglier clown costume than the last. They haven't pull their
        weapons out yet, as they see the active bomb under your arm and don't want to set
        it off.
        """))

        action = input("What will you do? \n >>")

        if action=="throw the bomb":
            print(dedent("""
            In a panic you throw the bomb at the group of Gathons 
            and make a leap for the door. Right as you drop it a Gathon shoots you
            right in the back killing you. As you die you see another Gathon frantically try to
            disarm the bomb. You die knowing they will probably 
            blow up when it goes off.
            """))
            return "death"

        elif action=="slowly place the bomb":
            print(dedent("""
            You point your blaster at the bomb under you arm and 
            the Gathons put their hand up and start to sweat.
            You inch backward to the door, open it, and then
            carefully place the bomb on the floor, pointing your 
            blaster at it. You then jump back through the door,
            punch the close button and blast the lock so the Gathons can't get out.
            Now that the bomb is placed you run to the escape pod to get off
            this tin can
            """))
            return "Escape_Pod"

        else:
            print("DOES NOT COMPUTE")
            return "The_Bridge"


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
        You rush through the ship desperately trying to make it to the escape pod
        before the whole ship explodes. It seems like hardly any Gathons are on the ship
        so your run is clear of interference. You get to the chamber with the escape pods
        and now need to pick one take. Some of them could be damaged but you don't have 
        time to look. There's 5. Which one would you take
        """))

        good_pod = randint(1,5)
        guess = input("[pod]>>")

        if int(guess) != good_pod:
            print(dedent(f"""
            You jump into pod {guess} and hit the eject button.
            The pod escapes out into the void of space, then implodes 
            as the hull ruptures, crushing you body into jam jelly
            """))
            return "death"

        else:
            print(dedent(dedent(f"""
            You jup into the pod {guess} and hit the eject button.
            The pod easily slides out into space heading to the 
            planet below. As it files to the planet, you look
            back ans see your ship implode then explode like a 
            bright star, taking out the Gathon ship at the same time.
            You Won !
            """)))

            return "finished"


class Finished(Scene):

    def enter(self):
        print("You Won! Good job.")
        return "finished"


class Map(object):

    scenes = {
        "Central_Corridor": CentralCorridor(),
        "laser_weapon_armory": LaserWeaponArmory(),
        "The_Bridge": TheBridge(),
        "Escape_Pod": EscapePod(),
        "death": Death(),
        "finished": Finished(),
        }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map("Central_Corridor")
a_game = Engine(a_map)
a_game.play()
