# This file is the logic layer for PawPal+.
from datetime import date
from typing import List


class Owner:
    def __init__(self, name: str):
        self.name: str = name
        self.pets: List[Pet] = []

    def update_owner_info(self) -> None:
        pass

    def create_pet(self) -> None:
        pass


class Pet:
    def __init__(self, name: str, species: str):
        self.name: str = name
        self.species: str = species
        self.tasks: List[Task] = []

    def create_task(self) -> Task:
        pass

    def display_tasks(self) -> None:
        pass

    def update_task(self) -> Task:
        pass

    def delete_task(self) -> None:
        pass


class Task:
    def __init__(self, title: str, pet: Pet, duration: int, priority: str, due_date: date):
        self.title: str = title
        self.pet: Pet = pet
        self.duration: int = duration
        self.priority: str = priority
        self.completion_status: bool = False
        self.due_date: date = due_date

    def change_duration(self) -> Task:
        pass

    def change_priority(self) -> Task:
        pass

    def change_completion_status(self) -> Task:
        pass


class Scheduler:
    def __init__(self):
        self.schedule: List[Task] = []
        self.pets: List[Pet] = []

    def create_schedule(self) -> None:
        pass

    def display_schedule(self) -> None:
        pass

    def update_schedule(self) -> None:
        pass

    def delete_schedule(self) -> None:
        pass

    def get_tasks(self) -> List[Task]:
        pass

    def sort_tasks(self) -> List[Task]:
        pass

    def filter_tasks(self) -> List[Task]:
        pass
