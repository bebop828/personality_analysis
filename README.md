# Personality Analysis  
***Methods and Experiments***

This repository will serve as a collection of projects and experiments exploring different approaches to personality analysis, combining traditional questionnaire-based methods with modern data-driven techniques.  

The goal is to examine how identity, preferences, and behavioral patterns can be interpreted through both structured input (such as Q&A quizzes) and unstructured data (social media text or user-generated content). Each project in this repo uses a different lens to uncover personality traits, sentiment, and psychological insights.

**Projects include:**

Interactive Personality Quiz: Classic Q&A-based framework that assigns users to categories or archetypes based on their selections.
Example: A Hogwarts House Sorting Quiz using a point-based model to simulate the Sorting Hat’s decision-making.

**Projects to come:**  

- Social Media Personality Mining: Scripts that collect and analyze user text from public platforms to detect mood, sentiment, and inferred personality traits 

- Textual Behavior Analysis: Tools for parsing and interpreting natural language to extract emotional tone, consistency, word choice patterns, and more.

This repository is intended as a creative and technical space to test, compare, and evolve personality analysis methods — with a focus on storytelling, ethics, and exploratory data science.  


## Current Projects include:  

### <u>Hogwarts House Sorting:</u>    
***A Personality-Based Q&A Framework***    

Within the PotterHouse folder is a fully functional Python personality quiz, built to showcase the system's flexibility using the Hogwarts Sorting Hat as a narrative case study.  

The system allows users to answer a series of themed multiple-choice questions and be placed into a category (or "house") based on their responses.

While this particular example uses Gryffindor, Ravenclaw, Hufflepuff, and Slytherin as the result categories, the architecture is designed to be adaptable for other personality-driven or decision-tree-based quizzes.  

**Project Goals**-

- Create a reusable and extensible Q&A framework for analyzing user input through personality-driven questions.
- Deliver meaningful results based on the accumulated score values tied to each response.
- Offer a compelling user experience by incorporating immersive storytelling elements and character-like interactions (e.g., the Sorting Hat's voice).
- Serve as a base for future expansions including GUI apps, web-based versions, or different quiz themes.  


**Features**-

- Interactive terminal-based personality quiz
- Randomly selects 16 questions from a pool of nearly 60 to ensure replayability
- Scores mapped to specific categories based on answers
- Tie-breaker logic using a bonus question or direct user input
- Modular file structure for easy scaling and maintenance
- Traits and result descriptions dynamically loaded from a separate traits module
- Easily replaceable themes: Hogwarts Sorting is just one example  


**File Structure and Flow**-

**`potterHouse_sort_V1.py`**  
This is the main driver file. It handles:

- Displaying the immersive introduction  
- Randomly selecting 16 questions from the imported pool
- Parsing user answers and tallying scores per house/category
- Executing tiebreaker logic when needed
- Displaying the final result with traits pulled from the traits file  

**`house_traits.py`**  
This file contains detailed summaries for each house, providing users with personalized descriptions, notable figures, and symbolic elements once their house placement is determined.  

- Maps each Hogwarts house name (Gryffindor, Ravenclaw, Hufflepuff, Slytherin) to a multi-line string summary. 
- Provides a short personality description that captures the core traits of the house.  
- Includes a house-specific quote taken from the Harry Potter universe.  
- Lists famous witches and wizards from both the Wizarding World and the real (Muggle) world who reflect the house's values.  
- Highlights the house animal and symbolic associations.  
- Concludes with an inspirational message to reinforce belonging and identity for the user.  
- Designed to be dynamically referenced at the end of the sorting quiz based on the user’s final result.  

**`potterHouse_questions.py`**  
Contains the core list of question dictionaries: (*example quesion*)

```python
questions = [
    {
        "question": "You’re faced with a fearsome dragon. What do you do?",
        "options": ["A. Fight it with courage", "B. Study its weak points", "C. Try to reason with it", "D. Use strategy to escape"],
        "answers": "A: 1, B: 2, C: 3, D: 4"
    },
    ...
]


