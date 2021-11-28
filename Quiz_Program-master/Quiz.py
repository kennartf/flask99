class Question:
    def __init__(self,question,answer):
        self.question = question
        self.answer = answer

question = [
    "What color are Apples?\n(a) Red/Green\n(b)Purple\n(c)Yello\n\n",
    "What color are Bananas?\n(a) Red/Green\n(b)Purple\n(c)Yello\n\n",
    "What color are Grapes?\n(a) Red/Green\n(b)Black\n(c)Yello\n\n",
]

questions = [
    Question(question[0],"a"),
    Question(question[1],"c"),
    Question(question[2],"b")

]

def run_test(questions):
    score = 0
    for i in questions:
        answer = input(i.question)
        if answer == i.answer:
            score+=1
    print("you get "+str(score)+"/"+str(len(question))+" correct")
run_test(questions)
