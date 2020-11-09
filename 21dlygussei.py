import random
import pygame
import itertools
win = pygame.display.set_mode((800, 800))


Suit = ["chern", "byb", "cherv", "krest"]
Value = ['6', '7', '8', '9', '10', '11', '12', '13', '14']
f1 = pygame.font.Font('Verdana.ttf', 24)


class Card:
    def __init__(self, value, points, suit, sprite):
        self.value = value
        self.points = points
        self.suit = suit
        self.sprite = sprite


class Koloda:
    def __init__(self):
        self.koloda = self.new_koloda()
        random.shuffle(self.koloda)

    def new_koloda(self):
        koloda = []
        for suit, value in intertools.product(Suit, Value):
            points = int(value)
            i_card = pygame.image.load("sprites/" + suit + "/" + points + ".png")
            c = Card(points=points, value=value, siit=suit, sprite=i_card)
            koloda.append(c)
        return koloda


class Player:
    def __init__(self):
        self.cards1 = []
        self.sum_p = self.get_points()

    def get_points(self):
        sum_p = sum([card.points for card in self.cards1])
        return sum_p

    def new_card(self, deck, x1_card, y1_cards):
        card = deck.get_card()
        win.blit(card.sprite, (x1_card, y1_cards))
        self.cards1.append(card)
        x1_card += 30
        pygame.display.update()


class Enemy:
    def __init__(self):
        self.cards2 = []
        self.sum_p = self.get_points()

    def get_points(self):
        sum_p = sum([card.points for card in self.cards2])
        return sum_p

    def new_card(self, deck, x2_card, y2_cards):
        card = deck.get_card()
        win.blit(card.sprite, (x2_card, y2_cards))
        self.cards2.append(card)
        x2_card += 30
        pygame.display.update()

    def draw_card(self, x2_card, y2_cards):
        for e in self.cards2:
            win.blit(e.sprites, (x2_card, y2_cards))
            x2_card -= 30
            pygame.display.update()


class Game:
    def __init__(self):
        self.player = Player()
        self.enemy = Enemy()
        self.koloda = Koloda()

    def game(self):
        pygame.time.delay(500)
        run = True
        text = fi.render('Вы хотите начать?+/-', 1, (100, 100, 100))
        place = text.get_rect(center=(400, 400))
        sc.blit(text, place)
        pygame.display.update()
        x, y = 200, 200
        if pygame.K_KP_PLUS:
            self.player.new_card(self, koloda, x, y)
            self.enemy.new_card(self, koloda)
            x += 30
            while run:
                print('Хотите взять карту?+/-')
                text = fi.render('Хотите взять карту?+/-', 1, (100, 100, 100))
                place = text.get_rect(center=(400, 400))
                sc.blit(text, place)
                pygame.display.update()
                if pygame.K_KP_PLUS:
                    self.player.new_card(self, koloda, x, y)
                    self.enemy.new_card(self, koloda)
                    x += 30
                else:
                    n = True
                    while n:
                        if enemy.sum_p < 17:
                            self.enemy.new_card(self, koloda)
                        else:
                            n = False
                    self.enemy.draw_card(600, 600)
                    if player.sum_p < 22:
                        if player.sum_p > enemy.sum_p:
                            text = fi.render('Win' + 'Ваш счет: ' + player.sum_p + 'Чужой счет: ' + enemy.sum_p, 1, (100, 100, 100))
                            place = text.get_rect(center=(400, 400))
                            sc.blit(text, place)
                            pygame.display.update()
                            run = False
                        else:
                            text = fi.render('Lose' + 'Ваш счет: ' + player.sum_p + 'Чужой счет: ' + enemy.sum_p, 1, (100, 100, 100))
                            place = text.get_rect(center=(400, 400))
                            sc.blit(text, place)
                            pygame.display.update()
                            run = False
                    else:
                        text = fi.render('Lose', 1, (100, 100, 100))
                        place = text.get_rect(center=(400, 400))
                        sc.blit(text, place)
                        pygame.display.update()
                        run = False
                if pygame.K_ESCAPE:
                    pygame.quit()
        if pygame.K_MINUS:
            pygame.quit()