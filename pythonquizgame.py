# (PYTHON QUIZ GAME)

# questions= ("How many Elements are in the periodic table :",
#             "How many bones are in the human body",
#             "which animal lays the largest eggs ",
#             "Which planet in the solar system is the hottest",
#             "Which is the most abundant gas in the atmosphere ")
# options= (("A.118","B.223","C.345","D.120"),
#           ("A.206","B.223","C.345","D.120"),
#           ("A.Ostrich","B.Whale","C.Bison","D.Dog"),
#           ("A.Venus","B.Mercury ","C.Earth","D.Neptune"),
#           ("A.Nitrogen","B.Oxygen","C.Helium","D.Chlorine"))
# answers = ("A", "A" , "A" , "A" , "A" )
# Guesses=[]
# Score=0
# question_num=0
#
# for question in questions:
#     print("==============================================")
#     print(question)
#     for option in options[question_num]:
#         print(option)
#     guess=input("Enter (A,B,C,D)").upper()
#     Guesses.append(guess)
#     if guess == answers[question_num]:
#         Score+=1
#         print("CORRECT !!")
#     else:
#         print("INCORRECT !!")
#         print(f"{answers[question_num]} is the correct option")
#     question_num+=1
# print("==============================================")
# print("============       RESULT       ==============")
# print("==============================================")
#
# print("answers :",end =" ")
# for answer in answers:
#     print(answer,end=" ")
# print()
#
# print("guesses :",end =" ")
# for guess in Guesses:
#     print(guess,end=" ")
# print()
#
#
# score= int(Score/len(questions) * 100)
# print(f"Your score is {score}%")
