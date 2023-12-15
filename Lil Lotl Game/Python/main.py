import random
import sys
import time
import pygame
from pygame.locals import *

def main():
    pygame.init()
    pygame.display.set_caption("Lil Lotk Game")
    size = pygame.display.Info()
    # dev mode
    screen = pygame.display.set_mode((640, 480), 0 ,32)
    # production
    #screen = pygame.display.set_mode((640, 480), pygame.FULLSCREEN)
    display = pygame.Surface((300, 300))

    # load images
    cursor_img = pygame.image.load("assets/images/cursor.png").convert_alpha()
    fence_img = pygame.image.load("assets/images/fence.png").convert_alpha()
    water_img = pygame.image.load("assets/images/water.png").convert_alpha()
    keeper_img = pygame.image.load("assets/images/lotl_keeper.png").convert_alpha()
    janitor_img = pygame.image.load("assets/images/janitor.png").convert_alpha()
    pizza_img = pygame.image.load("assets/images/pizza.png").convert_alpha()
    poop_img = pygame.image.load("assets/images/poop.png").convert_alpha()
    rainbow_poop_img = pygame.image.load("assets/images/rainbow_poop.png").convert_alpha()
    soda_img = pygame.image.load("assets/images/soda.png").convert_alpha()
    lucy_img = pygame.image.load("assets/images/lucy_lotl.png").convert_alpha()
    pygame.font.init()
    my_font = pygame.font.SysFont("times new roman", 50)
    my_small_font = pygame.font.SysFont("times new roman", 25)
    water_img.set_colorkey((0, 0, 0))
    pygame.mouse.set_visible(False)

    # load sounds
    pygame.mixer.music.load("assets/sounds/main_1.mp3")
    #pygame.mixer.music.play(-1)

    keeper_img = pygame.transform.scale(keeper_img, (16, 16))
    janitor_img = pygame.transform.scale(janitor_img, (16, 16))

    # generate map data
    map_data = []
    for x in range(12):
        new_map_data = []
        for y in range(12):
            new_map_data.append(1)

        map_data.append(new_map_data)

    # generate fence data
    fence_data = []
    for x in range(12):
        new_fence_data = []
        for y in range(12):
            if y == 6 and x <= 6:
                new_fence_data.append(1)

            elif x == 6 and y <= 6:
                new_fence_data.append(1)

            else:
                new_fence_data.append(0)

        fence_data.append(new_fence_data)

    lotl_keeper = False
    lotl_x = 0
    lotl_y = 0
    cursor = 0
    cursor_down = False
    cursor_up = False
    flask = 100
    janitor = True
    pizza_stand = False
    soda_stand = False
    timer = 0
  
    main_menu = True
    pause_menu = False
    market_menu = False

    lotl_data = []
    janitor_data = [11, 11]
    keeper_data = [0, 0]
    pizza_data = []
    player_data = [0,0]
    poop_data = []
    soda_data = []

    player_up = False
    player_down = False
    player_left = False
    player_right = False

    while True:
        screen.fill("black")
        display.fill("black")
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause_menu = True

                if event.key == K_SPACE:
                    if main_menu:
                        main_menu = False
                        if cursor == 0:
                            lotl_data.append([lotl_x, lotl_y, "lucy"])

                        elif cursor == 1:
                            pygame.quit()
                            sys.exit()

                        cursor = 0

                    elif pause_menu:
                        if cursor == 0:
                            pause_menu = False

                        if cursor == 1:
                            lotl_keeper = True
                            pause_menu = False

                        if cursor == 2:
                            market_menu = True
                            pause_menu = False

                        elif cursor == 3:
                            pygame.quit()
                            sys.exit()

                        cursor = 0

                    elif market_menu:
                        if cursor == 0:
                            market_menu = False

                        if cursor == 1 and flask >= 25:
                            pizza_stand = True
                            market_menu = False
                            flask -= 25

                        if cursor == 2 and flask >= 25:
                            soda_stand = True
                            market_menu = False
                            flask -= 25

                        cursor = 0

                    else:
                        if player_data[0] > 6 and pizza_stand or player_data[1] > 6 and pizza_stand:
                            dont_place = False
                            if len(pizza_data) > 0:
                                for food in pizza_data:
                                    if food[0] == player_data[0] and food[1] == player_data[1]:
                                        dont_place = True
                            
                            if len(soda_data) > 0:
                                for food in soda_data:
                                    if food[0] == player_data[0] and food[1] == player_data[1]:
                                        dont_place = True

                            if not dont_place:
                                pizza_data.append([player_data[0],player_data[1]])
                                pizza_stand = False

                        elif player_data[0] > 6 and soda_stand or player_data[1] > 6 and soda_stand:
                            dont_place = False
                            if len(pizza_data) > 0:
                                for food in pizza_data:
                                    if food[0] == player_data[0] and food[1] == player_data[1]:
                                        dont_place = True
                            
                            if len(soda_data) > 0:
                                for food in soda_data:
                                    if food[0] == player_data[0] and food[1] == player_data[1]:
                                        dont_place = True

                            if not dont_place:
                                soda_data.append([player_data[0],player_data[1]])
                                soda_stand = False
                            
                        else:
                            for count, terd in enumerate(poop_data):
                                if terd[0] == player_data[0] and terd[1] == player_data[1] and terd[2]:
                                    poop_data.pop(count)
                                    #flask += 100
                                    break

                                elif terd[0] == player_data[0] and terd[1] == player_data[1] and not terd[2]:
                                    poop_data.pop(count)
                                    #flask += 1
                                    break
                                
                if event.key == K_UP or event.key == K_w:
                    if main_menu or pause_menu or market_menu:
                        cursor_up = True
                        
                    else:
                        player_up = True
                        player_down = False
                        player_left = False
                        player_right = False
                        
                if event.key == K_DOWN or event.key == K_s:
                    if main_menu or pause_menu or market_menu:
                        cursor_down = True

                    else:
                        player_up = False
                        player_down = True
                        player_left = False
                        player_right = False

                if event.key == K_LEFT or event.key == K_a:
                    player_up = False
                    player_down = False
                    player_left = True
                    player_right = False

                if event.key == K_RIGHT or event.key == K_d:
                    player_up = False
                    player_down = False
                    player_left = False
                    player_right = True

            if event.type == KEYUP:
                if event.key == K_UP or event.key == K_w or market_menu:
                    if main_menu or pause_menu:
                        cursor_up = False
    
                if event.key == K_DOWN or event.key == K_s:
                    if main_menu or pause_menu or market_menu:
                        cursor_down = False

        if main_menu:
            if cursor_down and cursor < 1:
                cursor += 1
                cursor_down = False

            if cursor_up and cursor > 0:
                cursor -= 1
                cursor_up = False

            if cursor == 0:
                lucy_text = my_font.render("lucy lotl", True, "red")
                exit_text = my_font.render("exit game", True, "blue")

            elif cursor == 1:
                lucy_text = my_font.render("lucy lotl", True, "blue")
                exit_text = my_font.render("exit game", True, "red")

            research_text = my_small_font.render(f"research points: {flask}", True, "yellow")

            screen.blit(lucy_text, (250, 0))
            screen.blit(exit_text, (225, 75))
            pygame.display.flip()
        
        elif pause_menu:
            if cursor_down and cursor < 3:
                cursor += 1
                cursor_down = False

            if cursor_up and cursor > 0:
                cursor -= 1
                cursor_up = False

            if cursor == 0:
                resume_text = my_font.render("resume", True, "red")
                keeper_text = my_font.render("hire lotl keeper", True, "blue")
                market_text = my_font.render("goto market", True, "blue")
                exit_text = my_font.render("exit game", True, "blue")

            elif cursor == 1:
                resume_text = my_font.render("resume", True, "blue")
                keeper_text = my_font.render("hire lotl keeper", True, "red")
                market_text = my_font.render("goto market", True, "blue")
                exit_text = my_font.render("exit game", True, "blue")

            elif cursor == 2:
                resume_text = my_font.render("resume", True, "blue")
                keeper_text = my_font.render("hire lotl keeper", True, "blue")
                market_text = my_font.render("goto market", True, "red")
                exit_text = my_font.render("exit game", True, "blue")

            elif cursor == 3:
                resume_text = my_font.render("resume", True, "blue")
                keeper_text = my_font.render("hire lotl keeper", True, "blue")
                market_text = my_font.render("goto market", True, "blue")
                exit_text = my_font.render("exit game", True, "red")

            research_text = my_small_font.render(f"research points: {flask}", True, "yellow")

            screen.blit(resume_text, (250, 0))
            screen.blit(keeper_text, (175, 75))
            screen.blit(market_text, (200, 150))
            screen.blit(exit_text, (225, 225))
            screen.blit(research_text, (75, 400))
            pygame.display.flip()

        elif market_menu:
            if cursor_down and cursor < 2:
                cursor += 1
                cursor_down = False

            if cursor_up and cursor > 0:
                cursor -= 1
                cursor_up = False

            if cursor == 0:
                resume_text = my_font.render("resume", True, "red")
                pizza_text = my_font.render("pizza stand | 25 research", True, "blue")
                soda_text = my_font.render("soda stand | 25 research", True, "blue")

            elif cursor == 1:
                resume_text = my_font.render("resume", True, "blue")
                pizza_text = my_font.render("pizza stand | 25 research", True, "red")
                soda_text = my_font.render("soda stand | 25 research", True, "blue")

            elif cursor == 2:
                resume_text = my_font.render("resume", True, "blue")
                pizza_text = my_font.render("pizza stand | 25 research", True, "blue")
                soda_text = my_font.render("soda stand | 25 research", True, "red")

            research_text = my_small_font.render(f"research points: {flask}", True, "yellow")

            screen.blit(resume_text, (250, 0))
            screen.blit(pizza_text, (100, 75))
            screen.blit(soda_text, (100, 150))
            screen.blit(research_text, (75, 400))
            pygame.display.flip()
            
            
        else:
            # timer
            timer += 1
            move_ai = False
            if timer == 5:
                timer = 0
                move_ai = True

            # player
            if player_up and player_data[1] > 0:
                player_data[1] -= 1
                player_up = False

            if player_down and player_data[1] < 11:
                player_data[1] += 1
                player_down = False

            if player_left and player_data[0] > 0:
                player_data[0] -= 1
                player_left = False

            if player_right and player_data[0] < 11:
                player_data[0] += 1
                player_right = False

            if move_ai:
                # lotl ai
                direction = random.randint(1,4)
                for i in lotl_data:
                    if i[0] == 0 and i[1] == 5:
                        i[1] -= 1

                    if i[1] == 0 and i[0] == 5:
                        i[0] -= 1

                    if direction == 1 and i[0] > 0 and i[1] > 0:
                        i[0] -= 1

                    if direction == 2 and i[0] < 5 and i[1] < 5:
                        i[0] += 1

                    if direction == 3 and i[0] > 0 and i[1] > 0:
                        i[1] -= 1

                    if direction == 4 and i[0] < 5 and i[1] < 5:
                        i[1] += 1

                if lotl_keeper:
                    # lotl keeper ai
                    if len(poop_data) > 0:
                        if poop_data[0][0] < keeper_data[0]:
                            keeper_data[0] -= 1

                        elif poop_data[0][1] < keeper_data[1]:
                            keeper_data[1] -= 1

                        elif poop_data[0][0] > keeper_data[0]:
                            keeper_data[0] += 1

                        elif poop_data[0][1] > keeper_data[1]:
                            keeper_data[1] += 1

                        elif poop_data[0][0] == keeper_data[0] and poop_data[0][1] == keeper_data[1] and len(poop_data) > 0:
                            if poop_data[0][2]:
                                pass
                                #flask += 100

                            else:
                                pass
                                #flask += 1

                            poop_data.pop(0)
                            
                    elif len(poop_data) == 0:
                        direction = random.randint(1,4)

                        if keeper_data[0] == 0 and keeper_data[1] == 5:
                            keeper_data[1] -= 1

                        if keeper_data[1] == 0 and keeper_data[0] == 5:
                            keeper_data[0] -= 1

                        if direction == 1 and keeper_data[0] > 0 and keeper_data[1] > 0:
                            keeper_data[0] -= 1

                        if direction == 2 and keeper_data[0] < 5 and keeper_data[1] < 5:
                            keeper_data[0] += 1

                        if direction == 3 and keeper_data[0] > 0 and keeper_data[1] > 0:
                            keeper_data[1] -= 1

                        if direction == 4 and keeper_data[0] < 5 and keeper_data[1] < 5:
                            keeper_data[1] += 1

                if janitor:
                    direction = random.randint(1,4)

                    if janitor_data[0] == 5 and janitor_data[1] == 11:
                        janitor_data[1] -= 1

                    if janitor_data[1] == 5 and janitor_data[0] == 11:
                        janitor_data[0] -= 1

                    if direction == 1 and janitor_data[0] > 5 and janitor_data[1] > 5:
                        janitor_data[0] -= 1

                    if direction == 2 and janitor_data[0] < 11 and janitor_data[1] < 11:
                        janitor_data[0] += 1

                    if direction == 3 and janitor_data[0] > 5 and janitor_data[1] > 5:
                        janitor_data[1] -= 1

                    if direction == 4 and janitor_data[0] < 11 and janitor_data[1] < 11:
                        janitor_data[1] += 1

                # poop
                for i in lotl_data:
                    poop = random.randint(1,30)
                    if poop == 1:
                        special_poop = random.randint(1,1000)
                        already_pooped = False
                        for terd in poop_data:
                            if terd == i:
                                already_pooped = True
                                break

                        if not already_pooped:
                            if special_poop == 1:
                                poop_data.append([i[0], i[1], True])

                            else:
                                poop_data.append([i[0], i[1], False])
                                
            # draw terrain
            for y, row in enumerate(map_data):
                for x, tile in enumerate(row):
                    if tile:
                        display.blit(water_img, (150 + x * 10 - y * 10, 100 + x * 5 + y * 5))

            # draw fences
            for y, row in enumerate(fence_data):
                for x, tile in enumerate(row):
                    if tile:
                        display.blit(fence_img, (150 + x * 10 - y * 10, 100 + x * 5 + y * 5))
                        
            # draw research points
            research_text = my_small_font.render(f"research points: {flask}", True, "yellow")
            display.blit(research_text, (25, 25))

            # draw poop B)
            for y, row in enumerate(map_data):
                for x, tile in enumerate(row):
                    for terd in poop_data:
                        if x == terd[0] and y == terd[1] and terd[2] == True:
                            display.blit(rainbow_poop_img, (150 + x * 10 - y * 10  + (water_img.get_width() - poop_img.get_width()) // 2, 100 + x * 5 + y * 5 - poop_img.get_height() + 15))
                            break

                        elif  x == terd[0] and y == terd[1] and terd[2] == False:
                            display.blit(poop_img, (150 + x * 10 - y * 10  + (water_img.get_width() - poop_img.get_width()) // 2, 100 + x * 5 + y * 5 - poop_img.get_height() + 15))
                            break

            # draw lotl keeper
            if lotl_keeper:
                for y, row in enumerate(map_data):
                    for x, tile in enumerate(row):
                        if [x, y] == keeper_data:
                            display.blit(keeper_img, (150 + x * 10 - y * 10  + (water_img.get_width() - keeper_img.get_width()) // 2, 100 + x * 5 + y * 5 - keeper_img.get_height() + 15))

            # draw janitor
            if janitor:
                for y, row in enumerate(map_data):
                    for x, tile in enumerate(row):
                        if [x, y] == janitor_data:
                            display.blit(janitor_img, (150 + x * 10 - y * 10  + (water_img.get_width() - janitor_img.get_width()) // 2, 100 + x * 5 + y * 5 - janitor_img.get_height() + 15))
            
            # draw lotls
            for y, row in enumerate(map_data):
                for x, tile in enumerate(row):
                    for i in lotl_data:
                        if [x, y, "lucy"] == i:
                            display.blit(lucy_img, (150 + x * 10 - y * 10  + (water_img.get_width() - lucy_img.get_width()) // 2, 100 + x * 5 + y * 5 - lucy_img.get_height() + 15))

            # draw pizza stands
            if len(pizza_data) > 0:
                for y, row in enumerate(map_data):
                    for x, tile in enumerate(row):
                        for food in pizza_data:
                            if food[0] == x and food[1] == y:
                                display.blit(pizza_img, (150 + x * 10 - y * 10  + (water_img.get_width() - pizza_img.get_width()) // 2, 100 + x * 5 + y * 5 - pizza_img.get_height() + 15))
                                break

            # draw soda stands
            if len(soda_data) > 0:
                for y, row in enumerate(map_data):
                    for x, tile in enumerate(row):
                        for food in soda_data:
                            if food[0] == x and food[1] == y:
                                display.blit(soda_img, (150 + x * 10 - y * 10  + (water_img.get_width() - soda_img.get_width()) // 2, 100 + x * 5 + y * 5 - soda_img.get_height() + 15))
                                break

            # draw cursor
            for y, row in enumerate(map_data):
                for x, tile in enumerate(row):
                    if [x, y] == player_data:
                        display.blit(cursor_img, (150 + x * 10 - y * 10  + (water_img.get_width() - cursor_img.get_width()) // 2, 100 + x * 5 + y * 5 - cursor_img.get_height() + 15))
                        if pizza_stand:
                            display.blit(pizza_img, (150 + x * 10 - y * 10  + (water_img.get_width() - pizza_img.get_width()) // 2, 100 + x * 5 + y * 5 - pizza_img.get_height() + 15))
                            
                        if soda_stand:
                            display.blit(soda_img, (150 + x * 10 - y * 10  + (water_img.get_width() - soda_img.get_width()) // 2, 100 + x * 5 + y * 5 - soda_img.get_height() + 15))

            time.sleep(0.1)
            screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
            pygame.display.flip()

    pygame.quit()
    sys.exit()

main()
