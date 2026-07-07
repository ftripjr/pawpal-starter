# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF7)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

Prompt 1 - "I'm creating a Pet Care App with four classes - `Owner`, `Pet`, `Task`, and `Scheduler`. Create a mermaid.js class diagram based on @README.md  and the brainstormed attributes, methods, and relationships of each class in  @pawpal-plus-building-blocks.md ."

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->
The agent attemptef to create a Mermaid class diagram from building blocks but failed to generate an artifact to hold that data. On new attempt, it created an HTML file with the class diagram inside of the body of the HTML. It then would ask to input without displaying the suggested code. 

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->
Initially I had some difficulty with the agent, as it took some time to figure out where to create the file. It didn't create any files the first attempts at the prompt, then after creating a file to store it's suggested Class Diagram, it created the file as HTML instead of an MMD file or in a format that mermaid.js would understand. I had to give it a path to write it's diagram to, then correct it per notes from the Study Hall. As I updated the building blocks, I included things needed such as what I expected to return for each method of the classes. The agent was able to infer how to write the methods and attributes in the class diagram draft.

---

<!-- Use the following for each prompt
**What task did you give the agent?**
 Describe the goal you asked the agent to accomplish 
**What did the agent do?**
 List the steps the agent took (files edited, commands run, etc.) 
**What did you have to verify or fix manually?**
 Describe anything the agent got wrong or that required human review 
 -->

Prompt 2 - "Generate the skeletons of my classes in @pawpal_system.py . The classes should be based on the UML draft, @diagrams/uml_draft.mmd. "

The agent was able to create the skeletons needed and even added hints to the method declarations. This was my first exposure to hints in Python and I found them very useful. I think I'll implement them in my Python projects from now on.

Prompt 3 - "Check  the skeletons for our classes in @pawpal_system.py  and take note of any missing relationships or potential logic bottlenecks."

The agent was able to create the skeletons needed and even added hints to the method declarations. This was my first exposure to hints in Python and I found them very useful. I think I'll implement them in my Python projects from now on. I also found myself noticing that I'm missing things I thought I picked up in initial review of AI design. I do like that AI can evaluate itself a bit, but I wish i had picked some of these issues up before it found them.

## Prompt Comparison (SF11)

> Compare two different prompts (or two different models) on the same task.

| | Option A | Option B |
|-|----------|----------|
| **Model / tool used** | | |
| **Prompt** | | |
| **Response summary** | | |
| **What was useful** | | |
| **Problems noticed** | | |
| **Decision** | | |

**Which approach did you use in your final implementation and why?**

<!-- Your conclusion -->
