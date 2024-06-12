# Define a list of questions as tuples (question, answer)
questions = [
    ("What is the capital of France?", "Paris"),
    ("What is the largest mammal?", "Blue whale"),
    ("What is 2 + 2?", "4")
]

def run_quiz(questions):
    score = 0
    total_questions = len(questions)
    
    # Iterate through each question
    for question, correct_answer in questions:
        # Ask the question and get user input
        user_answer = input(question + " ")
        
        # Check if the answer is correct
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect! The correct answer is:", correct_answer)
    
    # Print the final score
    print("Quiz completed! You scored {}/{}.".format(score, total_questions))

# Run the quiz
if _name_ == "_main_":
    print("Welcome to the Quiz Game!")
    run_quiz(questions)