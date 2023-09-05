questions = ("1. Which instrument is used to measure pressure?",
             "2. What does Angstrom measure?",
             "3. Light Year is related to ________?",
             "4. Which of the following instruments is used to measure pressure of gases?",
             "5. Silver is the most conductive of metals?",
             "6. Who invented typewriter?",
             "7. Mark the wrong combination:",
             "8. Who invented the ball point pen?",
             "9. Study of earthquakes is known as _______?",
             "10. Numismatics is the study of _______?",
             "11. The rings of Saturn are very thin, compared to their length and width?",
             "12. Joule is the unit of which of the following?",
             "13. Oncology is the study of _______?",
             "14. Iron is the most abundant metal in Earth’s crust?",
             "15. Who proposed the chemical evolution of life?",
             "16. Robert Koch worked on _____?",
             "17. Walking up stairs uses more energy than walking on level ground?",
             "18. Who discovered Uranus?",
             "19. The first attempt in printing was made in England by _______?",
             "20. A meteor would burn up more rapidly in the atmosphere of Mars than it would passing through the Earth’s atmosphere?")

options = (("A. Saccharimeter", "B. Ammeter", "C. Manometer", "D. Lactometer"),
           ("A. Quantity of Liquid", "B. length of ligth waves", "C. Length of cables", "D. Speed of ships"),
           ("A. Energy", "B. Speed", "C. Distance", "D. Intensity"),
           ("A. Barometer", "B. Manometer", "C. Ammeter", "D. None of these"),
           ("A. True", "B. False"),
           ("A. Shockley", "B. Pascal ", "C. Sholes", "D. Waterman"),
           ("A. James Watt: Steam Engine", "B. A.G. Bell: Telescope", "C. J.L. Baird: Television", "D. J. Perkins: Penicillin"),
           ("A. Waterman", "B. Oscar", "C. Wilson", "D. Lazlo Biro"),
           ("A. Ecology", "B. Seismology", "C. Numismatics", "D. None of these"),
           ("A. Coins", "B. Numbers", "C. Stamps", "D. Space"),
           ("A. True", "B. False"),
           ("A. Temperature", "B. Pressure", "C. Energy", "D. Intensity"),
           ("A. Birds ", "B. Cancer", "C. Mammals", "D. Soil"),
           ("A. True", "B. False",),
           ("A. Darwin", "B. Lammarck", "C. Oparin", "D. Herschel"),
           ("A. Tuberculosis", "B. Cholera", "C. Malaria", "D. Diabetes"),
           ("A. True", "B. False",),
           ("A. Herschel", "B. Ganleo", "C. Copernicus", "D. None of these"),
           ("A. James Arkwright", "B. James Watt", "C. William Caxton", "D. Issac Newton"),
           ("A. True", "B. False")
           )

answers = ("C", "D", "C", "B", "A", "C", "D", "D", "B", "A", "A", "C", "B", "B", "C", "A", "A", "A", "C", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------------")
    print(question)
    for option in options[question_num]:
      print(option)

    guess = input("Enter the option number: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1


print("-----------------")
print("     RESULTS     ")
print("------------------")

print("Correct answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("Your answers: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

print(f"Your score is {score} out of 20")
