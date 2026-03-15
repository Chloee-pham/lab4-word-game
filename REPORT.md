# The project REPORT is where students will document key learnings, challenges, and reflections on their experience using CoPilot for software development. 

# First Impressions - Initial Take on the Project Assignment
The project required building a word-guessing game similar to Hangman. My understanding was that the game should: let the player guess letters, show correct guesses, track remaining attempts, and announce win/loss.
I assumed that using CoPilot was encouraged for code suggestions, but I still had to validate the logic.
- Points Needing Clarification
Should the game include hints or scoring?
Are graphics/ASCII drawings required for Hangman, or just text output?
Level of complexity expected (basic loops vs OOP design)?

# Key Learnings
- Computer Science Concepts and Technical Skills
Learned how to use loops, conditionals, and lists effectively.
Gained experience with string manipulation and tracking game state.
Learned to structure code in functions and optionally in a class for better organization.
- Insights about Using CoPilot Effectively
CoPilot worked best when I wrote clear, descriptive comments about what I wanted.
Suggested code sometimes needed debugging or simplification.
Using CoPilot iteratively saved time for boilerplate code like looping through guesses.

# Report on CoPilot Prompting Experience
- Types of prompts that worked well
Can you review and document main.py?
Can you suggest tests for this function?
- Types of prompts that did not work well or failed
“Write the full Hangman game with classes” → resulted in over-engineered code, confusing variable names, or redundant loops.

# Limitations, Hallucinations and Failures
Some suggested code overcomplicated the guess-checking logic, using unnecessary nested loops.
Misalignment between prompt specificity and AI understanding caused incorrect suggestions.
Impact on the Project
Required manual debugging and simplification.
Made me more careful about validating AI output before integrating it.

# AI Trust
- When did I trust AI?
When generating small, isolated functions like checking letter guesses or updating display strings.
- When did I stop trusting it?
When CoPilot wrote multi-step game logic or class structures that didn’t match the project needs.
- Signals of low reliability
Overly complex code
Variables that weren’t initialized
Logic that didn’t handle edge cases

# What I Learned
- About software development
Importance of breaking problems into small functions.
Need to test incrementally instead of trusting a large block of generated code.
- About using AI tools
AI can accelerate routine code generation, but cannot replace thinking through logic.
Clear comments and iterative prompting improve results.
- When to trust AI / double-check
Trust for small, predictable tasks.
Always double-check game logic, loops, and edge cases.
