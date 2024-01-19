from scripts.actor import Actor
from scenarios import login, adding_car, checkout, finish

if __name__ == "__main__":
    actor = Actor(name="Sebastian")
    
    # Steps
    login(actor)
    adding_car(actor)
    checkout(actor)
    finish(actor)
    # Exit
    input("Press Enter to exit...")
