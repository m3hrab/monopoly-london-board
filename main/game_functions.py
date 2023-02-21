import sys
import pygame 


def check_events(dice, roll_btn, players, player_turn=0):
    # Watch keyboard and mouse events
    current_player = 0
    add = 0
    extra = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            # Check if user click the dice buttons and update the player token based the current dice value
            if roll_btn.roll_btn_rect.collidepoint(event.pos):
                dice.roll()
                number = dice.number + dice.number2

                if players[current_player].token_rect.right > 115 and players[current_player].token_rect.bottom == 635:
                    players[current_player].token_rect.right -= 50*number

                    if players[current_player].token_rect.right == 615:
                        players[current_player].token_rect.right -= 25
                        add += 1
                    elif add == 0:
                        if (players[current_player].token_rect.right >= 190 and players[current_player].token_rect.right <= 615):
                            players[current_player].token_rect.right -= 25
                            add += 1
                    
                    elif players[current_player].token_rect.right == 215:
                        if add == 1:
                            players[current_player].token_rect.right -= 25
                            add +=1 

                    elif players[current_player].token_rect.right == 165:
                            players[current_player].token_rect.right -= 50
                            add = 2
                    
                    else:
                        count = 0 
                        temp2 = players[current_player].token_rect.right
                        while temp != 115:
                            temp = temp2 - 50
                            count += 1 
                        print(count)
                        players[current_player].token_rect.right = 115

                        print("x: " + str(players[current_player].token_rect.right))
                        print("y: " + str(players[current_player].token_rect.bottom))
                        print(extra)
                    
                
                # elif players[current_player].token_rect.right == 115 and players[current_player].token_rect.bottom != 80:
                #     players[current_player].token_rect.bottom -= 50*number
                #     if players[current_player].token_rect.bottom == 635:
                #         players[current_player].token_rect.bottom -= 20

                #     elif players[current_player].token_rect.bottom == 465:
                #         players[current_player].token_rect.bottom -= 10

                #     elif players[current_player].token_rect.bottom == 155:
                #         players[current_player].token_rect.bottom -= 25                    
                    
                #     print("x: " + str(players[current_player].token_rect.right))
                #     print("y: " + str(players[current_player].token_rect.bottom))

                # elif players[current_player].token_rect.bottom == 80 and players[current_player].token_rect.right != 665:
                #     players[current_player].token_rect.right += 50*number
                #     if players[current_player].token_rect.right == 115 or players[current_player].token_rect.right == 590:
                #         players[current_player].token_rect.right += 25

                #     print("x: " + str(players[current_player].token_rect.right))
                #     print("y: " + str(players[current_player].token_rect.bottom))
                
                # elif players[current_player].token_rect.right == 665: # and players[current_player].token_rect.bottom != 80:
                #     players[current_player].token_rect.bottom += 50*number
                #     if players[current_player].token_rect.bottom == 80:
                #         players[current_player].token_rect.bottom += 20

                #     elif players[current_player].token_rect.bottom == 250:
                #         players[current_player].token_rect.bottom += 10

                #     elif players[current_player].token_rect.bottom == 560:
                #         players[current_player].token_rect.bottom += 25                    

                #     print("x: " + str(players[current_player].token_rect.right))
                #     print("y: " + str(players[current_player].token_rect.bottom))


def update_screen(settings, screen, board, roll_btn, dice, players):

    # Redraw the screen during each pass through the loop
    screen.fill(settings.bg_color)
    board.draw()
    roll_btn.draw(screen)
    dice.draw()

    # Draw the player tokens
    for i in range(len(players)):
        screen.blit(players[i].token_image, players[i].token_rect)

    
    # Make the recently drawn screen visible 
    pygame.display.flip()
