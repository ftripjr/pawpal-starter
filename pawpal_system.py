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
    
    def mark_complete(self) -> None:
        """Returns True if the task is complete, False otherwise."""
        self.completion_status = not self.completion_status

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

    def update_owner(self, new_name: str) -> None:
        """Updates the owner's details."""
        self.name = new_name

    def add_pet(self, pet: Pet) -> None:
        """Adds a pet to the owner's list of pets."""
        self.pets.append(pet)

    def get_pet(self, name: str) -> Optional[Pet]:
        """Retrieves a pet by name."""
        for pet in self.pets:
            if pet.name == name:
                return pet
        return None

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
        self.schedule: List[Task] = []

    def create_schedule(self, pets: List[Pet]) -> List[Task]:
        """Generates a schedule based on the list of pets and their tasks."""
        for pet in self.scheduler_admin.pets:
            self.schedule.extend(pet.get_tasks())
        return self.schedule

    def get_schedule(self) -> None:
        """Returns formatted schedule grouped by pet and priority."""
        output = []
        output.append("Today's Schedule\n--------------------\n")
        for pet in self.scheduler_admin.pets:
            pet_emoji = '🐕' if pet.species.lower() == 'dog' else '🐈' if pet.species.lower() == 'cat' else '🐾'
            output.append(f"{pet_emoji} {pet.name}")
            tasks = pet.get_tasks()

            if not tasks:
                output.append("  (no tasks)")
                continue

            # Group by priority
            by_priority = {}
            for task in tasks:
                if task.priority not in by_priority:
                    by_priority[task.priority] = []
                by_priority[task.priority].append(task)

            # Format each priority group (urgent, high, Medium, Low)
            priority_order = ['urgent', 'high', 'medium', 'low']
            for priority in priority_order:
                if priority in by_priority:
                    total_duration = sum(t.duration for t in by_priority[priority])
                    emoji = '🚨' if priority.lower() == 'urgent' else '🔴' if priority.lower() == 'high' else '🟡' if priority.lower() == 'medium' else '🟢'
                    output.append(f"  {emoji} {priority.upper()} ({total_duration} min)")
                    for task in by_priority[priority]:
                        status = "☑" if task.is_complete() else "☐"
                        output.append(f"    • {task.description} — {task.duration} min {status}")

        print("\n".join(output))

    def sort_tasks(self, pets: List[Pet]) -> List[Task]:
        """Sorts tasks by criteria such as priority, duration, or frequency."""
        return []

    def filter_tasks(self, pets: List[Pet]) -> List[Task]:
        """Filters tasks based on criteria or constraints."""
        return []
