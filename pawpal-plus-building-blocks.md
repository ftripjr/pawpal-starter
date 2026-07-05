# PawPal+ Building Blocks

## List the Building Blocks

- [ ] Brainstorm the main objects needed for the system. For each object, determine:
  - What information it needs to hold **(attributes)**
  - What actions it can perform **(methods)**

- Owner/User
  - Attributes
    - Name
    - Pets -> Collection of Pet
  - Methods
    - Update Owner Info
    - Create a Pet

- Pet
  - Attributes
    - Name
    - Species
    - Tasks -> Collection of Task
  - Methods
    - Create Task -> Returns Task
    - Display Tasks
    - Update Task -> Returns Task
    - Delete Task

- Task
  - Attributes
    - Title
    - Pet
    - Duration
    - Priority
    - Completion Status
    - Due Date
  - Methods
    - Change Duration -> Returns Task
    - Change Priority -> Returns Task
    - Change Completion Status -> Returns Task

- Scheduler
  - Attributes
    - Schedule -> Collection of Task
    - Pets -> Collection of Pet
  - Methods
    - Create a Schedule -> Returns Schedule
    - Display Schedule
    - Update Schedule -> Returns Schedule
    - Delete A Schedule
    - Get Tasks -> Returns Collection of Task
    - Sort Tasks -> Returns Collection of Task
      - By Priority
      - By Duration
    - Filter Tasks -> Returns Collection of Task

## Building Block Relationships

Owner:
An Owner cares for zero, one, or many Pets.
An Owner plans zero, one, or many Tasks for each Pet.
An Owner tracks one or more Pets with the Scheduler.

Pet:
A Pet belongs to one Owner.
A Pet has zero, one, or many Tasks.
A Pet is reports by one Scheduler.

Task:
A Task belongs to one Pet.
A Task reports to the Scheduler.

Scheduler:
A Scheduler manages one or many Tasks.
A Scheduler tracks Pets.
A Scheduler tracks Tasks.
A Scheduler explains a schedule to the Owner.
