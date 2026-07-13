from pawpal_system import Task, Pet, Owner, Scheduler
from datetime import date, datetime, time
from typing import List, Optional

def main():
    freddie = Owner("Freddie")

    pluto = Pet("Pluto", "dog")
    morgana = Pet("Morgana", "cat")

    # My pets are mine
    freddie.add_pet(morgana)
    freddie.add_pet(pluto)

    # Pluto Tasks
    walk_pluto = Task("Walk", 30, "medium", "daily", time(hour=18, minute=30)) # 6:30 pm  7/15/26 
    pluto_vet_appt = Task("Vet Appointment for Pluto", 60, "urgent", "monthly", time(11, 30)) # 11:30 am 7/15/26 
    nail_trimming = Task(description="Trim Nails", duration=15, priority="medium", frequency="monthly", deadline=time(hour=18, minute=00)) # 6:00 pm 7/15/26 

    # Morgana Chores
    cat_playtime = Task(description="Playtime", duration=10,  priority="medium", frequency="daily", deadline=time(hour=17, minute=30)) # 5:30 pm 7/15/26 
    clean_litter = Task("Clean litter box", 15, "high", "daily", datetime(year=2026, month=7, day=15, hour=19, minute=30)) # 7:30 pm 7/15/26
    morgana_grooming_appt = Task("Grooming Appointment", 60, "urgent", "monthly", time(10, 30)) # 10:30 am 7/15/26 

    pluto.add_task(walk_pluto)
    pluto.add_task(pluto_vet_appt)
    pluto.add_task(nail_trimming)

    morgana.add_task(cat_playtime)
    morgana.add_task(clean_litter)
    morgana.add_task(morgana_grooming_appt)

    print(f"{freddie.name}'s Pets")
    for pet in freddie.pets:
        print(f"{pet.name} - {pet.species}")

    schedule = Scheduler(freddie)
    schedule.get_schedule()

main()
