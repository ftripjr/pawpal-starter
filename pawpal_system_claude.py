from datetime import datetime
from typing import List


class Task:
    def __init__(self, description: str, duration: int, priority: str,
                 frequency: str, deadline: datetime, completion_status: bool = False):
        self.description = description
        self.duration = duration
        self.priority = priority
        self.frequency = frequency
        self.deadline = deadline
        self.completion_status = completion_status

    def is_complete(self) -> bool:
        pass


class Pet:
    def __init__(self, name: str, species: str):
        self.name = name
        self.species = species
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        pass

    def get_tasks(self) -> List[Task]:
        pass

    def update_task(self, task: Task) -> None:
        pass

    def delete_task(self, task: Task) -> None:
        pass


class Owner:
    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def update_owner(self) -> None:
        pass

    def add_pet(self, pet: Pet) -> None:
        pass

    def get_pet(self, name: str) -> Pet:
        pass

    def update_pet(self, pet: Pet) -> None:
        pass

    def delete_pet(self, pet: Pet) -> None:
        pass


class Scheduler:
    def __init__(self, scheduler_admin: Owner):
        self.scheduler_admin = scheduler_admin
        self.pets: List[Pet] = []
        self.schedule: List[Task] = []

    def create_schedule(self, pets: List[Pet]) -> None:
        pass

    def get_schedule(self) -> List[Task]:
        pass

    def update_pet(self, pet: Pet) -> None:
        pass

    def get_tasks(self, pets: List[Pet]) -> List[Task]:
        pass

    def sort_tasks(self, pets: List[Pet]) -> List[Task]:
        pass

    def filter_tasks(self, pets: List[Pet]) -> List[Task]:
        pass
