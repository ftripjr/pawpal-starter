# This is the core logic behind PawPal+.
from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class Task:
    """
    Represents a pet care task (e.g., walk, feeding, meds, grooming).
    """
    description: str
    duration: int
    priority: str
    frequency: str
    deadline: datetime
    completion_status: bool = False

    def is_complete(self) -> bool:
        """Returns True if the task is complete, False otherwise."""
        return self.completion_status
    
@dataclass
class Pet:
    """
    Represents a pet, containing identifying info and a list of tasks.
    """
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Adds a task to the pet's list of tasks."""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Returns the list of tasks for this pet."""
        return self.tasks

    def update_task(self, task: Task) -> None:
        """Updates an existing task."""
        pass

    def delete_task(self, task: Task) -> None:
        """Deletes a task from the pet's list of tasks."""
        if task in self.tasks:
            self.tasks.remove(task)

class Owner:
    """
    Represents a pet owner, containing identifying info and a list of pets.
    """
    def __init__(self, name: str):
        self.name: str = name
        self.pets: List[Pet] = []

    def update_owner(self) -> None:
        """Updates the owner's details."""
        pass

    def add_pet(self, pet: Pet) -> None:
        """Adds a pet to the owner's list of pets."""
        self.pets.append(pet)

    def get_pet(self, name: str) -> Optional[Pet]:
        """Retrieves a pet by name."""
        for pet in self.pets:
            if pet.name == name:
                return pet
        return None

    def update_pet(self, pet: Pet) -> None:
        """Updates a pet's information."""
        pass

    def delete_pet(self, pet: Pet) -> None:
        """Deletes a pet from the owner's list of pets."""
        if pet in self.pets:
            self.pets.remove(pet)


class Scheduler:
    """
    Manages, retrieves, and organizes tasks across multiple pets for an owner.
    """
    def __init__(self, scheduler_admin: Owner):
        self.scheduler_admin: Owner = scheduler_admin
        self.pets: List[Pet] = []
        self.schedule: dict[Pet, Task] = ()

    def create_schedule(self) -> dict[Pet, List[Task]]:
        """Generates a schedule based on the list of pets and their tasks."""
        my_schedule = dict()
        for pet in self.pets:
            my_schedule[pet.name] = pet.get_tasks()
        return my_schedule

    def get_schedule(self): #:
        """Returns the current generated schedule."""
        print("Today's Schedule")
        for pet in self.scheduler_admin.pets:
            pet_tasks = {pet.name: pet.get_tasks()}
        
        for pet in pet_tasks:
            print(f"Pet -> {pet}\n")


    def update_pet(self, pet: Pet) -> None:
        """Updates the schedule with the latest info for a pet."""
        pass

    def get_tasks(self, pets: List[Pet]) -> List[Task]:
        """Gathers all tasks for the list of pets."""
        return []

    def sort_tasks(self, pets: List[Pet]) -> List[Task]:
        """Sorts tasks by criteria such as priority, duration, or frequency."""
        return []

    def filter_tasks(self, pets: List[Pet]) -> List[Task]:
        """Filters tasks based on criteria or constraints."""
        return []
