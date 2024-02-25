import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question['question'])
        for i, choice in enumerate(question['choices'], start=1):
            print(f"{i}. {choice}")
        user_answer = input("Enter your choice (1-4): ")
        return int(user_answer)

    def run_quiz(self):
        random.shuffle(self.questions)
        for question in self.questions:
            user_answer = self.display_question(question)
            if user_answer == question['correct_answer']:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {question['correct_answer']}\n")

        print(f"You scored {self.score} out of {len(self.questions)}")

# Example questions dictionary
questions = [
    {
        'question': 'What is the capital of Italy?',
        'choices': ['Berlin', 'Madrid', 'Paris', 'Rome'],
        'correct_answer': 4
    },
    {
        'question': 'Which programming language is this quiz written in?',
        'choices': ['Python', 'Java', 'C++', 'JavaScript'],
        'correct_answer': 1
    },
    {
        'question': 'What is the largest planet in our solar system?',
        'choices': ['Earth', 'Jupiter', 'Mars', 'Venus'],
        'correct_answer': 2
    }
]

# Create a Quiz instance and run the quiz
quiz = Quiz(questions)
quiz.run_quiz()
