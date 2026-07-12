# PawPal+ Building Blocks

## List the Building Blocks

- [x] Brainstorm the main objects needed for the system. For each object, determine:
  - What information it needs to hold **(attributes)**
  - What actions it can perform **(methods)**

The main objects needed for this project are `Task`, `Pet`, `Owner`, and `Scheduler`.

The `Task` is the foundation of all other classes. It has a description, duration, deadline/due date, completion status, and a relevant method, like `is_complete()`.
The `Pet` contains identifying info about the pet and a list of Tasks that must be done for that pet.
The Owner contains identifying info and a list of Pets with appropriate methods.
The Scheduler retrieves, organizes, or manages tasks across multiple pets for an Owner.

- Task
  - description string
  - duration int
  - priority string
  - frequency string
  - deadline datetime
  - completion_status bool
  - is_complete() return this->completion_status

- Pet
  - name string
  - species string
  - tasks List[Task]
  - add_task
  - get_tasks
  - update_task
  - delete_task

- Owner/User
  - name string
  - pets List[Pet]
  - update_owner
  - add_pet
  - get_pet
  - update_pet
  - delete_pet

- Scheduler
  - scheduler_admin Owner
  - pets List[Pet]
  - schedule List[Task]
  - create_schedule(List[Pet])
  - get_schedule() List[Task]
  - update_pet(Pet)
  - get_tasks(List[Pet]) List[Task]
  - Sort Tasks(List[Pet]) List[Task]
    - By Priority
    - By Duration
    - By Frequency
  - filter_tasks(List[Pet]) -> List[Task]

## Building Block Relationships

Task:

- A Task belongs to one Pet.

Pet:

- A Pet has zero, one, or many Tasks.
- A Pet belongs to one Owner.
- A Pet is managed by Scheduler.

Owner:

- An Owner cares for zero, one, or many Pets.
- An Owner uses one Scheduler.

Scheduler:

- A Scheduler talks with one Owner.
- A Scheduler manages zero, one or many Pets.
