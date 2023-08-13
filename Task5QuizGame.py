import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.questions = [
            {
                "question": "What is the name of the tallest mountain in the world?",
                "options": ["Mount Kilimanjaro", "Mount Everest", "Mount Fuji", "Mount Denali"],
                "answer": "Mount Everest",
            },
            {
                "question": "Who is the author of the Harry Potter series?",
                "options": ["Stephen King", "C.S. Lewis", "J.K. Rowling", "George R.R. Martin"],
                "answer": "J.K. Rowling",
            },
            {
                "question": "What is the capital of India?",
                "options": [ "Mumbai", "Kolkata", "Chennai","New Delhi",],
                "answer": "New Delhi",
            },
            {
                "question": "What is the name of the first man to walk on the moon?",
                "options": [ "Buzz Aldrin","Neil Armstrong", "Michael Collins", "Yuri Gagarin"],
                "answer": "Neil Armstrong",
            },
            {
                "question": "What is the name of the mathematical constant that is approximately equal to 3.14159?",
                "options": ["Tau", "Phi","Pi", "E"],
                "answer": "Pi",
            }
            # Add more questions here
        ]

        self.current_question = 0
        self.score = 0

        self.label = tk.Label(root, text="Welcome to the Quiz Game!", font=("Helvetica", 16),bg="dark blue",fg="yellow")
        self.label.pack(pady=10)

        self.score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 12),bg="dark blue",fg="yellow")
        self.score_label.pack()

        self.question_label = tk.Label(root, text="", font=("Helvetica", 14),bg="dark blue",fg="yellow")
        self.question_label.pack(pady=10)

        self.radio_var = tk.IntVar()
        self.radio_buttons = []

        for i in range(4):
            radio = tk.Radiobutton(root, text="", variable=self.radio_var, value=i,bg="dark blue",fg="yellow")
            self.radio_buttons.append(radio)
            radio.pack()

        self.next_button = tk.Button(root, text="Next", command=self.next_question,bg="Dark Blue",fg="yellow")
        self.next_button.pack(pady=10)

        self.load_question()

    def load_question(self):
        self.radio_var.set(-1)
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])
            for i, option in enumerate(question_data["options"]):
                self.radio_buttons[i].config(text=option)
        else:
            self.show_results()

    def next_question(self):
        if self.current_question < len(self.questions):
            user_answer = self.radio_var.get()
            if user_answer != -1:
                question_data = self.questions[self.current_question]
                if question_data["options"][user_answer] == question_data["answer"]:
                    self.score += 1
                else:
                    messagebox.showinfo("Incorrect", f"Correct answer: {question_data['answer']}")
                    
                self.score_label.config(text=f"Score: {self.score}",bg="Dark Blue",fg="yellow")
                self.current_question += 1
                self.load_question()

    def show_results(self):
        messagebox.showinfo("Quiz Finished", f"Your final score is: {self.score}/{len(self.questions)}")
        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        
        if play_again:
            self.current_question = 0
            self.score = 0
            self.load_question()
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.configure(bg="Dark blue")
    root.mainloop()

