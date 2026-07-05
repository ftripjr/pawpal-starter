# PawPal+ Building Blocks

## List the Building Blocks

- [ ] Brainstorm the main objects needed for the system. For each object, determine:
  - What information it needs to hold **(attributes)**
  - What actions it can perform **(methods)**

- Owner/User
  - Attributes
    - ID (unique)
    - Name
    - E-mail
    - Pets -> Collection of Pet
  - Methods
    - Update Owner Info
    - Create a Pet

- Pet
  - ID
  - Name
  - Tasks -> Collection of Task
  - Create A Task
    - Task Duration
    - Task Priority
  - Update A Task
    - Change Priority
    - Change Duration
  - Delete a Task

- Task
  - ID
  - Name
  - Duration
  - Priority
  - Completion Status
  - Change Duration
  - Change Priority
  - Change Completion Status

- Scheduler
  - Schedule -> Collection of Tasks
  - Create a Schedule
  - Display Schedule
  - Check Pets
  - Update Schedule

Relationships:
<!-- TODO: Ask AI Companions about updating Schedule based on changes in Pet or Task. -->
