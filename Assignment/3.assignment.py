def quiz():
    questions = [
        {
            "question": "1. What is the output  of: print(type(()))?",
            "options": ["A. <class 'list'>", "B. <class 'dict'>", "C. <class 'set'>", "D. <class 'tuple'>"],
            "answer": "D"
        },
        {
            "question": "2. what is the correct file extension for python files?",
            "options": ["A. .pt", "B. .pyt", "C. .py", "D. .python"],
            "answer": "C"
        },
        {
            "question": "3. Which keyword is used to define a function in python?",
            "options": ["A. func", "B. def", "C. define", "D. function"],
            "answer": "B"
        },
        {
            "question": "4. What is the result of: 2**3 ?",
            "options": ["A. 10", "B. 6", "C. 5", "D. 8"],
            "answer": "D"
        },
        {
            "question": "5. Which of the following is used to creat a comment in python?",
            "options": ["A. //", "B. #", "C. <!----->", "D. ##"],
            "answer": "B"
        },
        {
            "question": "6. Which data type is immutable in Python?",
            "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
            "answer": "D"
        },
        {
            "question": "7. What does the len() function do?",
            "options": ["A. Calculates average", "B. Finds max value", "C. Returns length", "D. Converts to string"],
            "answer": "C"
        },
        {
            "question": "8. Which of these is a valid variable name?",
            "options": ["A. 2value", "B. value_2", "C. value-2", "D. value 2"],
            "answer": "B"
        },
        {
            "question": "9. What is the output of: bool(0)?",
            "options": ["A. True", "B. 0", "C. False", "D. Error"],
            "answer": "C"
        },
        {
            "question": "10. Which statement is used to handle exceptions in Python?",
            "options": ["A. try-expect", "B. try-catch", "C. try-handle", "D. try-except"],
            "answer": "D"
        },
        {
        "question": "11. What will be the output of: print('Python'[::-1])?",
        "options": ["A. nohtyP", "B. Python", "C. Error", "D. Typo"],
        "answer": "A"
        },
        {
        "question": "12. Which loop runs at least once even if the condition is false?",
        "options": ["A. for", "B. while", "C. do-while", "D. repeat-until"],
        "answer": "C"
        },
        {
        "question": "13. What is the output of: len([1, 2, 3, [4, 5]])?",
        "options": ["A. 5", "B. 4", "C. 3", "D. Error"],
        "answer": "B"
        },
        {
        "question": "14. Which method is used to remove whitespace from the beginning and end of a string?",
        "options": ["A. trim()", "B. strip()", "C. clean()", "D. remove()"],
        "answer": "B"
        },
        {
        "question": "15. What is the data type of: {1, 2, 3}?",
        "options": ["A. list", "B. tuple", "C. set", "D. dictionary"],
        "answer": "C"
        },
        {
        "question": "16. What will be the output of: '5' + '3'?",
        "options": ["A. 8", "B. 53", "C. Error", "D. 2"],
        "answer": "B"
        },
        {
        "question": "17. Which keyword is used to create a class in Python?",
        "options": ["A. define", "B. class", "C. object", "D. defclass"],
        "answer": "B"
        },
        {
        "question": "18. How do you insert an element at the end of a list?",
        "options": ["A. add()", "B. push()", "C. append()", "D. insert()"],
        "answer": "C"
        },
        {
        "question": "19. Which operator is used to check equality in Python?",
        "options": ["A. =", "B. !=", "C. == ", "D. equals"],
        "answer": "C"
        },
        {
        "question": "20. What does the 'break' statement do in a loop?",
        "options": ["A. Skips the current iteration", "B. Stops the loop", "C. Repeats the loop", "D. Restarts loop"],
        "answer": "B"
        }
    
    ]
    
    score = 0
    for i in questions:
        print("\n" + i["question"])
        for option in i["options"]:
            print(option)
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        if user_answer == i["answer"]:
            print("Correct!")
            score+=1
        else:
            print(f"Worng! the correct answer is {i['answer']}.")
    
    print("\n python Quiz completed!")
    print(f"your final score is: {score}/{len(questions)}")
    
    if score == len(questions):
        print("Excellent! you know python very well!")
    elif score>10 and score<=15:
        print("Great job! keep it up.")
    elif score==10:
        print("Not bad. study more and try again")
    else:
        print("keep learning python.you will improve!")
        
quiz()
    