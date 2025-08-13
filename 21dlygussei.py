import random
import sys
import pygame

WIDTH, HEIGHT = 800, 600


class DraggableCard:
    """Simple draggable card sprite."""

    def __init__(self, image: pygame.Surface, position: tuple[int, int]):
        self.image = image
        self.rect = self.image.get_rect(topleft=position)
        self.dragging = False
        self._offset = (0, 0)

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.dragging = True
            self._offset = self.rect.x - event.pos[0], self.rect.y - event.pos[1]
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self.rect.topleft = (
                event.pos[0] + self._offset[0],
                event.pos[1] + self._offset[1],
            )

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.rect)


def load_deck() -> list[pygame.Surface]:
    """Load all card images and return them shuffled."""
    suits = ["chern", "byb", "cherv", "krest"]
    values = range(6, 15)
    images = []
    for suit in suits:
        for value in values:
            path = f"sprites/{value}{suit}.png"
            images.append(pygame.image.load(path).convert_alpha())
    random.shuffle(images)
    return images


def main() -> int:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 24)

    deck_images = load_deck()
    hand_images = deck_images[:5]
    draw_pile = deck_images[5:]

    cards: list[DraggableCard] = []
    x = 50
    for image in hand_images:
        cards.append(DraggableCard(image, (x, HEIGHT - image.get_height() - 20)))
        x += image.get_width() + 20
    next_x = x

    deck_rect = pygame.Rect(WIDTH - 80, HEIGHT - 120, 60, 90)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if deck_rect.collidepoint(event.pos) and draw_pile:
                    image = draw_pile.pop()
                    cards.append(
                        DraggableCard(
                            image, (next_x, HEIGHT - image.get_height() - 20)
                        )
                    )
                    next_x += image.get_width() + 20
            for card in cards:
                card.handle_event(event)

        screen.fill((0, 100, 0))
        pygame.draw.rect(screen, (50, 50, 50), deck_rect)
        count_text = font.render(str(len(draw_pile)), True, (255, 255, 255))
        screen.blit(
            count_text, count_text.get_rect(center=deck_rect.center)
        )
        for card in cards:
            card.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
