from scripts.actor import Actor
from scenarios import login, adding_car

if __name__ == "__main__":
    actor = Actor(name="Sebastian")
    
    # Steps
    login(actor)
    adding_car(actor)
    # Exit
    input("Press Enter to exit...")
