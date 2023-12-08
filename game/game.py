import pygame
import sys
pygame.init()

# Set up  
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SEARCH FOR DIPLOMA")

# Load images
background1 = pygame.transform.scale(pygame.image.load("background1.jpg"), (width, height))
background2 = pygame.transform.scale(pygame.image.load("background2.jpg"), (width, height))
background3 = pygame.transform.scale(pygame.image.load("background3.png"), (width, height))
background7 = pygame.transform.scale(pygame.image.load("background7.png"), (width, height))
background5 = pygame.transform.scale(pygame.image.load("background5.jpeg"), (width, height))
background6 = pygame.transform.scale(pygame.image.load("background6.jpeg"), (width, height))
background4 = pygame.transform.scale(pygame.image.load("background4.png"), (width, height))

# Character 
character = pygame.image.load("character.png").convert_alpha()
character = pygame.transform.scale(character, (100, 100))  
character_rect = character.get_rect()
character_rect.topleft = (width // 2 - character_rect.width // 2, height - character_rect.height - 20)

#reward
reward = pygame.image.load("reward.png").convert_alpha()
reward = pygame.transform.scale(reward, (100, 100))  
reward_rect = reward.get_rect()
reward_rect.center = (width // 2, height // 2 + 30)

# Colors 
black = (0, 0, 0)
white = (255, 255, 255)
red = (255,0,0) 
# Text 
font_large = pygame.font.Font(None, 40)
font_small = pygame.font.Font(None, 30)

def display_text(text, font, color, x, y, max_width=None):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y) if max_width is None else (x, y))
    
    if max_width and text_rect.width > max_width:
        ratio = max_width / text_rect.width
        new_height = int(text_rect.height * ratio)
        new_width = int(text_rect.width * ratio)
        text_surface = pygame.transform.scale(text_surface, (new_width, new_height))
        text_rect = text_surface.get_rect(center=(x, y))
    
    
    if text_rect.left < 0:
        text_rect.left = 0
    if text_rect.right > width:
        text_rect.right = width
    if text_rect.top < 0:
        text_rect.top = 0
    if text_rect.bottom > height:
        text_rect.bottom = height
    
    screen.blit(text_surface, text_rect)

game_started = False
game_over = False

character_steps = 0


# First part of the quest(background1) - Saniya done
def first_part():
    global character_rect

    
    character_steps = 0
    continue_journey_displayed = False

    while True:
        screen.blit(background1, (0, 0))

        
        if not continue_journey_displayed:
            display_text("What will you choose?", font_small, white, 10, height - 80, width)
            display_text("N - North", font_small, white, 10, height - 30, width)
            display_text("S - South", font_small, white, 10, height, width)
        else:
            display_text("Continue your journey, go to the entrance", font_small, white, 10, height - 75, width)
            display_text("You can move everywhere with keys T(forward),F(left),G(backward),H(right)", font_small, red, 10, height - 35, width)

        
        screen.blit(character, character_rect.topleft)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # character movement
                if event.key == pygame.K_t:
                    character_rect.y = max(character_rect.y - 10, 0)  #  upward
                    character_steps += 1
                elif event.key == pygame.K_g:
                    character_rect.y = min(character_rect.y + 10, height - character_rect.height)  #  downward
                elif event.key == pygame.K_f:
                    character_rect.x = max(character_rect.x - 10, 0)  # left
                elif event.key == pygame.K_h:
                    character_rect.x = min(character_rect.x + 10, width - character_rect.width)  #  right

                
                if character_steps >= 15:
                    second_part()
                    return

                
                continue_journey_displayed = True

               
                if event.key == pygame.K_s:
                    game_over()

        pygame.display.flip()


# Second part of the quest(background2) - Saniya done
def second_part():
    global character_rect

    while True:
        screen.blit(background2, (0, 0))

        display_text("Choose which door to enter:", font_small, black, 10, height - 80, width)
        display_text("Press 1 or 2 or 3 or 4 or 5", font_small, black, 10, height - 30, width)
        display_text("to continue journey", font_small, black, 10, height, width)

        
        screen.blit(character, character_rect.topleft)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                #  character movement
                if event.key == pygame.K_t:
                    character_rect.y = max(character_rect.y - 10, 0)  # upward
                elif event.key == pygame.K_g:
                    character_rect.y = min(character_rect.y + 10, height - character_rect.height)  #  downward
                elif event.key == pygame.K_f:
                    character_rect.x = max(character_rect.x - 10, 0)  #  left
                elif event.key == pygame.K_h:
                    character_rect.x = min(character_rect.x + 10, width - character_rect.width)  #  right

                # door choices
                elif event.key == pygame.K_1:
                    #Door 1(saniya)
                    third_part_door1()
                elif event.key == pygame.K_2:
                    #  Dilnaz1
                    third_part_door2()
                elif event.key == pygame.K_3:
                    # Dilnaz2
                    third_part_door3()
                elif event.key == pygame.K_4:
                    #  Door 4 Rayum
                    third_part_door4()
                elif event.key == pygame.K_5:
                    #  Door 5 Sanzhar
                    third_part_door5()        

        pygame.display.flip()


# Third part of the quest (Door 1) - gameover step back - saniya done
def third_part_door1():
    global character_rect

    while True:
        screen.fill(black)

        display_text("Game Over! You chose the wrong door))", font_large, white, width // 2, height // 2 - 50, width)
        display_text("Press ESC to go back to the second part and don't repeat mistakes)", font_small, white, width // 2, height // 2 + 30, width)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                second_part()
                return

        pygame.display.flip()

# Third part of the quest (Door 2) - background3 - Dilnaz1 done
def third_part_door2():
    global character_rect
    counter = 0
    
    correct_answers = [pygame.K_b, pygame.K_c, pygame.K_a, pygame.K_b, pygame.K_a, pygame.K_c, pygame.K_b]

    questions = [
        {
            'question': "Solve the equation: -1x^2 + 0x + 49 = 0",
            'answers': ["A) X = -9 and -6", "B) X = 7 and -7", "C) X = 8 and 3"],
        },
        {
            'question': "Solve the equation: -1x^2 + 2x + 48 = 0",
            'answers': ["A) X = -2 and 1", "B) X = 8 and -8", "C) X = 8 and -6"],
        },
        {
            'question': "The total surface area of the globe is equal to",
            'answers': ["A) 510 million km", "B) 149 million km", "C) 361 million km"],
        },
        {
            'question': "The capital of Kazakhstan is located on the river:",
            'answers': ["A) Tobol.", "B) Ishim.", "C) Yesil."],
        },
        {
            'question': "Through the Samsung company, Kazakhstans relations with:",
            'answers': ["A) South Korea", "B) Kyrgyzstan", "C) Russia"],
        },
        {
            'question': "The silk products factory is located in the city:",
            'answers': ["A) Taraz", "B) Almaty", "C) Shymkent"],
        },
        {
            'question': "What is the formula for Sine? ",
            'answers': ["A) Adjacent/Opposite", "B) Opposite/Hypotenuse", "C) Opposite/Adjacent"],
        },
    ]

    question_index = 0

    instruction_displayed = True
    while instruction_displayed:
        screen.fill(black)
        display_text("You need to answer 4 out of 7 questions in order to go to the next room", font_large, white, width // 2, height // 2 - 50, width)
        display_text("Press any key to start", font_small, white, width // 2, height // 2 + 30, width)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                instruction_displayed = False

    while question_index < len(questions):
        screen.blit(background3, (0, 0))

        current_question = questions[question_index]
        display_text(current_question['question'], font_large, white, 10, height - 130, width)

        for i, answer in enumerate(current_question['answers']):
            display_text(answer, font_small, white, 10, height - 80 + i * 30, width)

        
        screen.blit(character, character_rect.topleft)


        display_text(f"Correct Answers: {counter}", font_small, white, width // 2, 10, width)

       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                #  character movement
                if event.key == pygame.K_t:
                    character_rect.y = max(character_rect.y - 10, 0)  #  upward
                elif event.key == pygame.K_g:
                    character_rect.y = min(character_rect.y + 10, height - character_rect.height)  #  downward
                elif event.key == pygame.K_f:
                    character_rect.x = max(character_rect.x - 10, 0)  #  left
                elif event.key == pygame.K_h:
                    character_rect.x = min(character_rect.x + 10, width - character_rect.width)  #  right

                
                if event.key == pygame.K_a or event.key == pygame.K_b or event.key == pygame.K_c:
                    if event.key == correct_answers[question_index]:
                        counter += 1

                    
                    question_index += 1

                if question_index == len(questions):
                    if counter > 3:
                        final_part()
                        return

        pygame.display.flip()

# Third part of the quest (Door 3) - backround4 - Dilnaz2 done
def third_part_door3():
    global character_rect
    counter = 0
    
    correct_answers = [pygame.K_c, pygame.K_b, pygame.K_c, pygame.K_c, pygame.K_a, pygame.K_b, pygame.K_c]

    questions = [
        {
            'question': "When Kazakhstan became independent?",
            'answers': ["A) 1990", "B) 1989", "C) 1991"],
        },
        {
            'question': "What is the difference between list and tuple in Python?",
            'answers': ["A)Lists are immutable, tuples are mutable", "B) Lists are resizable, tuples are fixed-size", "C) Lists are indexed from 1, tuples from 0"],
        },
        {
            'question': "What is the largest planet in our solar system?",
            'answers': ["A) Saturn", "B) Venus", "C) Jupiter"],
        },
        {
            'question': "What is the Pigeonhole Principle in discrete mathematics?",
            'answers': ["A) Pigeons and holes are irrelevant in mathematics", "B) The more holes, the fewer pigeons", "C) If n>m, then at least one container has more than one item"],
        },
        {
            'question': "What is the role of constraints in optimization problems?",
            'answers': ["A)They limit the feasible solutions", "B) They determine the optimization algorithm", "C) They define the objective function"],
        },
        {
            'question': "What is the principle of mathematical induction?",
            'answers': ["A) A technique to prove statements about prime numbers", "B) A technique to prove statements about well-ordered sets", "C) A method for solving linear equations"],
        },
        {
            'question': "In optimization, what is the objective function?",
            'answers': ["A) The constraint function", "B) The function to be maximized", "C) The function that defines the problem"],
        },
    ]

    question_index = 0

    instruction_displayed = True
    while instruction_displayed:
        screen.fill(black)
        display_text("You need to answer 4 out of 7 questions in order to go to the next room", font_large, white, width // 2, height // 2 - 50, width)
        display_text("Press any key to start", font_small, white, width // 2, height // 2 + 30, width)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                instruction_displayed = False

    while question_index < len(questions):
        screen.blit(background4, (0, 0))

        current_question = questions[question_index]
        display_text(current_question['question'], font_large, white, 10, height - 130, width)

        for i, answer in enumerate(current_question['answers']):
            display_text(answer, font_small, white, 10, height - 80 + i * 30, width)

    
        screen.blit(character, character_rect.topleft)

        display_text(f"Correct Answers: {counter}", font_small, white, width // 2, 10, width)

       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                #  character movement
                if event.key == pygame.K_t:
                    character_rect.y = max(character_rect.y - 10, 0)  # upward
                elif event.key == pygame.K_g:
                    character_rect.y = min(character_rect.y + 10, height - character_rect.height)  #  downward
                elif event.key == pygame.K_f:
                    character_rect.x = max(character_rect.x - 10, 0)  #  left
                elif event.key == pygame.K_h:
                    character_rect.x = min(character_rect.x + 10, width - character_rect.width)  # right

                
                if event.key == pygame.K_a or event.key == pygame.K_b or event.key == pygame.K_c:
                    if event.key == correct_answers[question_index]:
                        counter += 1

                    question_index += 1

                if question_index == len(questions):
                    if counter > 3:
                        final_part()
                        return

        pygame.display.flip()

# Third part of the quest (Door 4) - backround5 - Raymbek done
def third_part_door4():
    global character_rect
    counter = 0
    
    correct_answers = [pygame.K_a, pygame.K_c, pygame.K_a, pygame.K_a, pygame.K_a, pygame.K_b, pygame.K_a]

    questions = [
        {
            'question': "What is the largest ocean on Earth?",
            'answers': ["A) Pacific Ocean", "B) Atlantic Ocean", "C) Indian Ocean"],
        },
        {
            'question': "Which gas do plants absorb from the atmosphere?",
            'answers': ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide"],
        },
        {
            'question': "Who is known as the 'Father of Computer Science'?",
            'answers': ["A) Alan Turing", "B) Bill Gates", "C) Steve Jobs"],
        },
        {
            'question': "What is the currency of Japan?",
            'answers': ["A) Yen ", "B) Won", "C) Yuan"],
        },
        {
            'question': "Who painted 'Starry Night'?",
            'answers': ["A) Vincent van Gogh", "B) Pablo Picasso", "C) Claude Monet"],
        },
        {
            'question': "What is the world's longest river?",
            'answers': ["A) Nile River", "B) Amazon River", "C) Yangtze River"],
        },
        {
            'question': "Which element has the chemical symbol 'O'?",
            'answers': ["A) Oxygen", "B) Gold", "C) Silver"],
        },
    ]

    question_index = 0

    instruction_displayed = True
    while instruction_displayed:
        screen.fill(black)
        display_text("You need to answer 4 out of 7 questions in order to go to the next room", font_large, white, width // 2, height // 2 - 50, width)
        display_text("Press any key to start", font_small, white, width // 2, height // 2 + 30, width)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                instruction_displayed = False

    while question_index < len(questions):
        screen.blit(background5, (0, 0))

        current_question = questions[question_index]
        display_text(current_question['question'], font_large, white, 10, height - 140, width)

        for i, answer in enumerate(current_question['answers']):
            display_text(answer, font_small, white, 10, height - 90 + i * 30, width)

        
        screen.blit(character, character_rect.topleft)

        
        display_text(f"Correct Answers: {counter}/7", font_small, white, width // 2, 10, width)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                #  character movement
                if event.key == pygame.K_t:
                    character_rect.y = max(character_rect.y - 10, 0)  #  upward
                elif event.key == pygame.K_g:
                    character_rect.y = min(character_rect.y + 10, height - character_rect.height)  #  downward
                elif event.key == pygame.K_f:
                    character_rect.x = max(character_rect.x - 10, 0)  # left
                elif event.key == pygame.K_h:
                    character_rect.x = min(character_rect.x + 10, width - character_rect.width)  #  right

                elif event.key in [pygame.K_a, pygame.K_b, pygame.K_c]:
                    if event.key == correct_answers[question_index]:
                        counter += 1

                
                    question_index += 1

                    if question_index == len(questions):
                   
                        if counter > 3:
                            final_part()
                            return

        pygame.display.flip()

# Third part of the quest (Door 5) - backround6 - Sanzhar done
def third_part_door5():
    global character_rect

    questions_door5 = [
        {
            'question': "Which famous scientist developed the theory of general relativity?",
            'answers': ["A) Albert Einstein", "B) Isaac Newton", "C) Galileo Galilei"],
            'correct_answer': pygame.K_b,
        },
        {
            'question': "How many days are there in a leap year?",
            'answers': ["A) 365", "B) 366", "C) 364"],
            'correct_answer': pygame.K_b,
        },
        {
            'question': "What is the closest planet to the Sun?",
            'answers': ["A) Venus", "B) Earth", "C) Mercury"],
            'correct_answer': pygame.K_c,
        },
        {
            'question': "Which animal is known as the 'King of the Jungle'?",
            'answers': ["A) Tiger", "B) Lion", "C) Leopard"],
            'correct_answer': pygame.K_b,
        },
        {
            'question': "What is the largest continent on Earth?",
            'answers': ["A) Europe", "B) Africa", "C) Asia"],
            'correct_answer': pygame.K_c,
        },
        {
            'question': "What is the chemical symbol for gold?",
            'answers': ["A) Au", "B) Ag", "C) G"],
            'correct_answer': pygame.K_a,
        },
        {
            'question': "How many sides does a triangle have?",
            'answers': ["A) 3", "B) 4", "C) 5"],
            'correct_answer': pygame.K_a,
        },
    ]

    question_index = 0
    counter = 0


    instruction_displayed = True
    while instruction_displayed:
        screen.fill(black)
        display_text("You need to answer 4 out of 7 questions in order to go to the next room", font_large, white, width // 2, height // 2 - 50, width)
        display_text("Press any key to start", font_small, white, width // 2, height // 2 + 30, width)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                instruction_displayed = False

    while question_index < len(questions_door5):
        screen.blit(background6, (0, 0))

        current_question = questions_door5[question_index]
        display_text(current_question['question'], font_large, black, 10, height - 140, width)

        for i, answer in enumerate(current_question['answers']):
            display_text(answer, font_small, black, 10, height - 90 + i * 30, width)

       
        screen.blit(character, character_rect.topleft)

       
        display_text(f"Correct Answers: {counter}/7", font_small, black, width // 2, 10, width)

       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    character_rect.y = max(character_rect.y - 10, 0)  #  upward
                elif event.key == pygame.K_g:
                    character_rect.y = min(character_rect.y + 10, height - character_rect.height)  #  downward
                elif event.key == pygame.K_f:
                    character_rect.x = max(character_rect.x - 10, 0)  #  left
                elif event.key == pygame.K_h:
                    character_rect.x = min(character_rect.x + 10, width - character_rect.width)  #right

                elif event.key in [pygame.K_a, pygame.K_b, pygame.K_c]:
                    if event.key == current_question['correct_answer']:
                        counter += 1

                    question_index += 1

                    if question_index == len(questions_door5):
                        if counter > 3:
                            final_part()
                            return

        pygame.display.flip()




# reward done Saniya 
reward_steps = 0

def reward_part():
    global character_rect, reward_steps

    while True:
        screen.blit(background7, (0, 0))

        if reward_steps >= 5:
            screen.blit(reward, reward_rect.topleft)
            display_text("Press 'E' to collect your reward!", font_large, black, width // 2, height - 50, width)

        
        screen.blit(character, character_rect.topleft)

        
        if reward_steps < 5:
            display_text("Move to the stairs", font_large, black, width // 2, height - 50, width)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                #  character movement
                if event.key == pygame.K_t:
                    character_rect.y = max(character_rect.y - 10, 0)
                elif event.key == pygame.K_g:
                    character_rect.y = min(character_rect.y + 10, height - character_rect.height)
                elif event.key == pygame.K_f:
                    character_rect.x = max(character_rect.x - 10, 0)
                elif event.key == pygame.K_h:
                    character_rect.x = min(character_rect.x + 10, width - character_rect.width)

                    
                reward_steps += 1

        
        if reward_steps >= 5:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_e]:
                screen.blit(background7, (0, 0))  
                display_text("Congratulations! You have won the game and earned a diploma!", font_large, (255, 255, 255), width // 2, height // 2, width)
                pygame.display.flip()
                pygame.time.delay(3000)
                pygame.quit()
                sys.exit()

        pygame.display.flip()


# Final part of the quest (Final Room) - background7 - Saniya done
def final_part():
    global character_rect
    counter = 0
    
    
    correct_answers = [pygame.K_b, pygame.K_a, pygame.K_a, pygame.K_c]

    
    questions = [
        {
            'question': "What is the distance between KBTU and the main dormitory?",
            'answers': ["A) 3km", "B) 5km", "C) 7km"],
        },
        {
            'question': "What is the historical significance of our University building?",
            'answers': ["A) The former building of the Supreme Council,1951-1957", "B) The former building of the Palace of Peace and Reconciliation,1923-1944", "C) The former building of Nomad Fortress,1973-2000"],
        },
        {
            'question': "When was KBTU founded?",
            'answers': ["A) 2000-2001", "B) 1997-1999", "C) 2003-2005"],
        },
        {
            'question': "How many schools are there in KBTU",
            'answers': ["A) 6", "B) 8", "C) 10"],
        },
    ]

    question_index = 0

    instruction_displayed = True
    while instruction_displayed:
        screen.blit(background7, (0, 0))
        display_text("Welcome to the final part of the game. You need to answer at least 2/4 questions to get your diploma", font_large, white, width // 2, height // 2 - 50, width)
        display_text("Press any key to start", font_small, white, width // 2, height // 2 + 30, width)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                instruction_displayed = False

    while question_index < len(questions):
        screen.blit(background7, (0, 0))

        
        current_question = questions[question_index]
        display_text(current_question['question'], font_large, black, 10, height - 130, width)

        for i, answer in enumerate(current_question['answers']):
            display_text(answer, font_small, black, 10, height - 80 + i * 30, width)

        
        screen.blit(character, character_rect.topleft)

       
        display_text(f"Correct Answers: {counter}", font_small, black, width // 2, 10, width)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # character movement
                if event.key == pygame.K_t:
                    character_rect.y = max(character_rect.y - 10, 0)  #  upward
                elif event.key == pygame.K_g:
                    character_rect.y = min(character_rect.y + 10, height - character_rect.height)  #  downward
                elif event.key == pygame.K_f:
                    character_rect.x = max(character_rect.x - 10, 0)  #  left
                elif event.key == pygame.K_h:
                    character_rect.x = min(character_rect.x + 10, width - character_rect.width)  #  right

                
                if event.key == pygame.K_a or event.key == pygame.K_b or event.key == pygame.K_c:
                    if event.key == correct_answers[question_index]:
                    
                        counter += 1

                   
                    question_index += 1

                if question_index == len(questions):
                    
                    if counter > 1:
                        reward_part()
                        return
                    else:
                        final_part()    

        pygame.display.flip()




# Game Over for first part
def game_over():
    global character_rect, character_steps

    while True:
        screen.blit(background1, (0, 0))

        display_text("Game Over", font_large, white, width // 2, height // 2 - 50, width)
        display_text("Press ESC to exit", font_small, white, width // 2, height // 2 + 30, width)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

# Game loop main 
while True:
    if not game_started:
        
        screen.blit(background1, (0, 0))  
        display_text("SEARCH FOR DIPLOMA", font_large, white, width // 2, height // 2 - 50, width)
        display_text("Press SPACE to start", font_small, white, width // 2, height // 2 + 30, width)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_started = True
               
                first_part() #then it goes part after part)

    pygame.display.flip()
