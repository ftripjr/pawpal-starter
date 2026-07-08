# This file is the logic layer for PawPal+.
from datetime import date
from typing import List, Optional

class Task:
    def __init__(self, title: str, duration: int, priority: str, due_date: date):
        self.title: str = title
        self.duration: int = duration
        self.priority: str = priority 
        self.due_date: date = due_date
        self.completion_status: bool = False

    def change_title(self, title: str): # No return needed. just a setter function
        self.title = title

    def change_duration(self, duration: int): # No return needed. just a setter function
        self.duration = duration

    def change_priority(self, priority: str): # No return needed. just a setter function
        self.priority = priority
    
    def change_due_date(self, duration: int): # No return needed. just a setter function
        self.due_date = self.due_date

    def change_completion_status(self, completion_status: bool): # No return needed. just a setter function
        self.completion_status = completion_status


class Pet:
    def __init__(self, name: str, species: str):
        self.name: str = name
        self.species: str = species
        self.tasks: List[Task] = []

    def set_species(self, species: str) -> None:
        new_task = Task(title, duration, priority, due_date)
        self.tasks.append(new_task)
        return new_task

    def display_tasks(self) -> None:
        if len(self.tasks) == 0:
            return f"{self.name} has no tasks."
        
        print(f"{self.name}'s chores:")
        
        for task in self.tasks:
            print(f"{task.title} - Due at {task.due_date} - {task.completion_status}")


    def get_tasks(self) -> List[Task]:        
        if len(self.tasks) == 0:
            return None
        return self.tasks
            

    def delete_task(self, task: Task) -> None:
        pass

class Owner:
    def __init__(self, name: str):
        self.name: str = name
        self.pets: List[Pet] = []
        self.scheduler: Optional['Scheduler'] = None

    def update_owner_info(self, name: str) -> None:
        self.name = name

    def create_pet(self, name: str, species: str) -> Pet:
        new_pet = Pet
        pass

    def create_scheduler(self, pets: List['Pet']) -> 'Scheduler':
        pass



class Scheduler:
    def __init__(self, owner: Owner, pets: List[Pet]):
        self.owner: Owner = owner
        self.pets: List[Pet] = pets

    def get_owner(self, owner: Owner) -> Owner:
        pass

    def add_pet(self, pet: Pet) -> None:
        pass

    def get_tasks(self, pets: Optional[List[Pet]] = None) -> List[Task]:
        pass

    def sort_tasks(self, pets: Optional[List[Pet]] = None, sort_by: str = "due_date") -> List[Task]:
        pass

    def filter_tasks(self, pets: Optional[List[Pet]] = None, filter_by: str = "priority") -> List[Task]:
        pass
