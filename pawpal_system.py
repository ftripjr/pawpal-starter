# This file is the logic layer for PawPal+.
from datetime import date
from typing import List, Optional


class Owner:
    def __init__(self, name: str):
        self.name: str = name
        self.pets: List[Pet] = []
        self.scheduler: Optional['Scheduler'] = None

    def update_owner_info(self, name: str) -> None:
        pass

    def create_pet(self, name: str, species: str) -> Pet:
        pass

    def create_scheduler(self, pets: List['Pet']) -> 'Scheduler':
        pass


class Pet:
    def __init__(self, name: str, species: str, owner: Owner):
        self.name: str = name
        self.species: str = species
        self.owner: Owner = owner
        self.tasks: List[Task] = []

    def create_task(self, title: str, duration: int, priority: str, due_date: date) -> Task:
        pass

    def display_tasks(self) -> None:
        pass

    def update_task(self, task: Task, title: Optional[str] = None, duration: Optional[int] = None,
                    priority: Optional[str] = None, due_date: Optional[date] = None) -> Task:
        pass

    def delete_task(self, task: Task) -> None:
        pass


class Task:
    def __init__(self, title: str, pet: Pet, duration: int, priority: str, due_date: date):
        self.title: str = title
        self.pet: Pet = pet
        self.duration: int = duration
        self.priority: str = priority
        self.completion_status: bool = False
        self.due_date: date = due_date

    def change_duration(self, duration: int) -> Task:
        pass

    def change_priority(self, priority: str) -> Task:
        pass

    def change_completion_status(self, completion_status: bool) -> Task:
        pass


class Scheduler:
    def __init__(self, owner: Owner, pets: List[Pet]):
        self.owner: Owner = owner
        self.pets: List[Pet] = pets

    def add_pet(self, pet: Pet) -> None:
        pass

    def get_tasks(self, pets: Optional[List[Pet]] = None) -> List[Task]:
        pass

    def sort_tasks(self, pets: Optional[List[Pet]] = None, sort_by: str = "due_date") -> List[Task]:
        pass

    def filter_tasks(self, pets: Optional[List[Pet]] = None, filter_by: str = "priority") -> List[Task]:
        pass
