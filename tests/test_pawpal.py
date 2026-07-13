import pytest
from datetime import datetime, timedelta
from pawpal_system import Task, Pet, Owner, Scheduler


class TestTask:
    def test_mark_complete(self):
        """Verify that mark_complete() toggles task completion status."""
        deadline = datetime.now() + timedelta(days=1)
        task = Task(
            description="Morning walk",
            duration=30,
            priority="high",
            frequency="daily",
            deadline=deadline,
            completion_status=False
        )

        assert task.is_complete() is False
        task.mark_complete()
        assert task.is_complete() is True
        task.mark_complete()
        assert task.is_complete() is False


class TestPet:
    def test_add_task_increases_count(self):
        """Verify that adding a task to a Pet increases task count."""
        pet = Pet(name="Biscuit", species="dog")
        deadline = datetime.now() + timedelta(days=1)

        assert len(pet.get_tasks()) == 0

        task1 = Task(
            description="Morning walk",
            duration=30,
            priority="high",
            frequency="daily",
            deadline=deadline
        )
        pet.add_task(task1)
        assert len(pet.get_tasks()) == 1

        task2 = Task(
            description="Feeding",
            duration=10,
            priority="high",
            frequency="twice daily",
            deadline=deadline
        )
        pet.add_task(task2)
        assert len(pet.get_tasks()) == 2
