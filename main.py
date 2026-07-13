from pawpal_system import Task, Pet, Owner, Scheduler
from datetime import date, datetime, time
from typing import List, Optional

def main():
    # Make some pets
    pluto = Pet("Pluto", "dog")
    morgana = Pet("Morgana", "cat")

    # I care for pets
    freddie = Owner("Freddie")

    # My 2 pets are mine
    freddie.add_pet(morgana)
    freddie.add_pet(pluto)

    # Make a Scheduler
    schedule = Scheduler(freddie)
    
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

    schedule.get_schedule()
    
    print("\n")
    pluto_vet_appt.mark_complete()
    morgana_grooming_appt.mark_complete()
    nail_trimming.mark_complete()

    cat_nail_trimming = Task(description="Trim Nails", duration=15, priority="medium", frequency="monthly", deadline=time(hour=18, minute=00)) # 6:00 pm 7/15/26 
    
    morgana.add_task(cat_nail_trimming)
    cat_nail_trimming.deadline = time(22,00)
    cat_nail_trimming.duration = 5
    nail_trimming.duration = 7
    schedule.get_schedule()

    print("\n")
    pluto.delete_task(nail_trimming)
    morgana.delete_task(cat_nail_trimming)
    schedule.get_schedule()

    freddie.delete_pet(pluto)
    schedule.get_schedule()
main()
