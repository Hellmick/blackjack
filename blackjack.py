from sys import exit as e
from time import sleep
import pygame
from settings import Settings
from boxes import Box, Button, InputBox
from player import Player
from cards import Cards
from cardImg import CardImg


def run():
    #the function inits the whole game and runs its loop

    def finish_deal():
        draw_button.enabled = False
        pass_button.enabled = False
        double_button.enabled = False
        while croupier.points <= 21 and croupier.points < player.points:
            croupier.draw(cards)
            images.append(CardImg(screen, (len(croupier.hand) * 160 - 60, settings.screen_height - 500), (150, 200), croupier.hand[-1]))
            for img in images:
                img.blitme()

    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Blackjack")
    
    screen.fill(settings.bg_color)
    images = []

    #declaring necessary objects
    place_bet_box = InputBox(screen, settings, (100, settings.screen_height - 55), settings.def_box_size)
    bet_label = Box(screen, settings, color=settings.bg_color, enabled=True, pos=(100, settings.screen_height - 90), size=(150, 30), text='Your bet:')
    place_bet_button = Button(screen, settings, (220, settings.screen_height - 55), settings.def_box_size, text="Place bet")

    player = Player()
    croupier = Player()
    cards = Cards()
    
    balance_label = Box(screen, settings, color=settings.bg_color, pos=(100, 50), size=(200, 30), text="Balance: " + str(player.balance))
    your_bet_label = Box(screen, settings, color=settings.bg_color, pos=(100, 80), size=(150, 30), text="Your bet: ")
    win_loss_label = Box(screen, settings, color=settings.bg_color, pos=(500, settings.screen_height/2 + 30), size=settings.def_box_size, text='')
    your_cards_label = Box(screen, settings, color=settings.bg_color, pos=(100, settings.screen_height/2 + 60), size=settings.def_box_size, text='Your cards:')
    croupiers_cards_label = Box(screen, settings, color=settings.bg_color, pos=(100, 150), size=(200, 30), text='Croupiers cards:')

    draw_button = Button(screen, settings, (340, settings.screen_height - 55), size=settings.def_box_size, text='Draw')
    draw_button.color = settings.dr_button_color
    pass_button = Button(screen, settings, (460, settings.screen_height - 55), size=settings.def_box_size, text='Pass')
    pass_button.color = settings.p_button_color
    double_button = Button(screen, settings, (580, settings.screen_height - 55), size=settings.def_box_size, text='Double')
    double_button.color = settings.do_button_color

    place_bet_button.enabled = True

    def restart():
        pygame.display.flip()
        sleep(3)
        cards.shuffle()
        screen.fill(settings.bg_color)
        your_bet_label.update_text('Your bet:')
        win_loss_label.update_text('')
        balance_label.update_text("Balance: " + str(player.balance))
        player.hand = []
        croupier.hand = []
        player.points = croupier.points = 0
        place_bet_button.enabled = True

    while True:
        #the loop of the game

        bet_label.blitme()

        place_bet_box.blitme()

        place_bet_button.blitme()
        your_bet_label.blitme()
        balance_label.blitme()
        your_cards_label.blitme()
        croupiers_cards_label.blitme()

        draw_button.blitme()
        pass_button.blitme()
        double_button.blitme()

        win_loss_label.blitme()

        if player.points > 21:
            win_loss_label.update_text("You lose.")
            draw_button.enabled = False
            pass_button.enabled = False
            double_button.enabled = False
            images = []
            restart()

        elif croupier.points <= 21 and croupier.points > player.points:
            win_loss_label.update_text("You lose.")
            images = []
            restart()

        elif croupier.points > 21:
            player.balance += player.bet * 2
            win_loss_label.update_text("You win.")
            images = []
            restart()

        elif croupier.points == player.points != 0:
            player.balance += player.bet
            win_loss_label.update_text("That's a tie.")
            images = []
            restart()

        for event in pygame.event.get():

            place_bet_box.handle_event(event, settings.font)

            if draw_button.handle_event(event):
                player.draw(cards)
                images.append(CardImg(screen, (len(images) * 160 + 100, settings.screen_height - 200), (150, 200), player.hand[-1]))
                for img in images:
                    img.blitme()

            if double_button.handle_event(event):
                player.bet *= 2
                player.draw(cards)
                images.append(CardImg(screen, (len(images) * 160 + 100, settings.screen_height - 200), (150, 200), player.hand[-1]))
                for img in images:
                    img.blitme()
                your_bet_label.blitme()
                player.balance -= player.bet // 2
                balance_label.update_text("Balance: " + str(player.balance))
                your_bet_label.update_text("Your bet: " + str(player.bet))
                finish_deal()

            if pass_button.handle_event(event):
                finish_deal()

            if place_bet_button.handle_event(event):
                #checks if player has enough money to place a bet
                player.bet = int(place_bet_box.text)
                if player.bet <= player.balance and player.bet != 0:
                    player.balance -= player.bet
                    place_bet_button.enabled = False
                    your_bet_label.update_text("Your bet: " + str(player.bet))
                    draw_button.enabled = True
                    pass_button.enabled = True
                    double_button.enabled = True
                    balance_label.update_text("Balance: " + str(player.balance))

            if event.type == pygame.QUIT:
                e()
        
        pygame.display.flip()

if __name__ == "__main__":
    run()