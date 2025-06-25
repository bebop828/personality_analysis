################################################################################
#### ------------Welcome to the Hogwarts House Sorting Quiz! ------- ###########
####- Discover your true magical nature through this personality-based Q&A. - ##
### -------- Will you join the brave Gryffindors, wise Ravenclaws, ---- ########
## --------------- loyal Hufflepuffs, or cunning Slytherins? ----------#########
############ - Let the Sorting Hat decide where you truly belong... - ##########
################################################################################


import random
from potterHouse_questions import questions
from house_traits import house_summaries


house_scores = {1: 0, 2: 0, 3: 0, 4: 0}
house_names = {1: "Gryffindor", 2: "Ravenclaw", 3: "Hufflepuff", 4: "Slytherin"}

################################################################################
################ ---------- Intro Setting ----------############################
################################################################################

def show_intro():
    print("""
    ⚡ Welcome to Hogwarts! ⚡

    Young witch or wizard, you are stepping into the Great Hall for your first year.
    Candles float in midair, your future classmates are all seated at long wooden tables, and the smell
    of pumpkin pasties and roast chicken drifts through the air.

    At the front of the hall, Dumbledore,  Headmaster at Hogwarts, stands at a podium, speaking to the gathered students.
    Behind him sits a weathered, dusty hat on a stool. At first glance, it seems lifeless...

    But as Dumbledore finishes his welcome speech, the old hat suddenly stirs, mouth stretching wide...
    """)
    print("""
    🎩 Sorting Hat:

    "Ah, a fresh crop of minds and magic! Ready for these halls to seek out Knowledge! Before we begin, let me speak of the world beyond these walls.
    Muggles live in times of contradiction. There's innovation, unity, and dreams reaching the stars,
    but also conflict, division, and strife pulling at their roots.

    War echoes in lands far and near, while peace is fought for in every heart.
    The world you inherit is fragile, but filled with potential.

    Here at Hogwarts, we sort not by blood, nor by wealth, but by what lies within.
    So let us see what kind of soul you possess, and where your path will begin..."
    """)    
    print("""
    🧙 Professor McGonagall steps up to the podium, a long parchment scroll in hand. With a crisp flick, she unrolls it and begins to call names from the list.
    One by one, students rise and make their way to the stool where the Sorting Hat rests. As each name is read, the old, weathered hat is lowered gently onto their heads. 
    
    Silence falls. 
    
    The Hat delves deep — past nerves and surface thoughts — into the truth of who they are. Moments later, it booms a House name with certainty and pride.
    Cheers erupt from one of the four tables, arms raised in welcome as that house grows with a new witch or wizard. Laughter, applause, and excited chatter fill the hall.

    Then… your name is called.
    A hush descends once more.

    Heart pounding, you rise and make your way forward. 
    You sit on the stool. 
    The Sorting Hat is lowered onto your head — it shifts slightly, and then...          
    """)

    input("\nWhen you're ready to be sorted into your house, press Enter...")

################################################################################
############# ---------- Parse Answer String to Dict ---------- ################
################################################################################

def parse_answers(answer_str):
    return {pair.split(":")[0].strip(): int(pair.split(":")[1]) for pair in answer_str.split(",")}

################################################################################
######## ---------- Ask Questions and Tally Scores ---------- ##################
################################################################################

def ask_questions(question_set):
    for idx, q in enumerate(question_set, start=1):
        print(f"\nQ{idx}: {q['question']}")
        for opt in q['options']:
            print(f"  {opt}")

        valid = False
        while not valid:
            choice = input("Your choice: ").strip().upper()
            if choice in ["A", "B", "C", "D"]:
                answer_map = parse_answers(q["answers"])
                selected_house = answer_map.get(choice)
                if selected_house:
                    house_scores[selected_house] += 1
                    valid = True
                else:
                    print("Answer not mapped. Skipping question.")
                    break
            else:
                print("Please choose A, B, C, or D.")

################################################################################
################## ---------- Tiebreaker Logic ---------- ######################
################################################################################

def handle_tiebreaker(tied_houses):
    print("\n🎩 Hmm... seems you are a tricky one! A lot of layers hidden inside. A curious tie between:")
    for h in tied_houses:
        print(f"- {house_names[h]}")

    # Ask one bonus question to break a tie
    bonus = random.choice([q for q in questions if q not in quiz_questions])
    print("\nLet’s see if one more question can sort it all out!")
    ask_questions([bonus])

    # Recheck ties and continue or send to Final Choice
    max_score = max([house_scores[h] for h in tied_houses])
    remaining = [h for h in tied_houses if house_scores[h] == max_score]

    if len(remaining) == 1:
        return remaining[0]

    # Final choice by user if tie exist
    print("\n🎩 Still not completly sound I see... Perhaps you may know best?\nYou seem to have much more inside that even I, the great sorting hat can see! \nI see, looking inside the corners of your mind, traits from each of these houses! Which house do you choose.")
    for i, h in enumerate(remaining, 1):
        print(f"{i}. {house_names[h]}")

    while True:
        try:
            choice = int(input("Which house calls to you? Enter your decision: "))
            if 1 <= choice <= len(remaining):
                return remaining[choice - 1]
            else:
                print("Please choose again.")
        except ValueError:
            print("Enter a number.")

################################################################################
################## ---------- Main Sorting Quiz ---------- #####################
################################################################################

def run_sorting_quiz():
    show_intro()
    global quiz_questions
    quiz_questions = random.sample(questions, 16)
    ask_questions(quiz_questions)

    max_score = max(house_scores.values())
    top_houses = [house for house, score in house_scores.items() if score == max_score]

    print("\n🏠 Final House Results:")
    for h, score in house_scores.items():
        print(f"{house_names[h]}: {score}")

    if len(top_houses) == 1:
        final_house = top_houses[0]
    else:
        final_house = handle_tiebreaker(top_houses)

    print(f"\n🧙 I, the sorting hat, have looked deep inside and it is clear you belong in... \n{house_names[final_house]}!")
    print("\n🧾 Your House Traits:")
    print(house_summaries[house_names[final_house]])
    

if __name__ == "__main__":
    run_sorting_quiz()
