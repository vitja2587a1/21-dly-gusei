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

    deck_images = load_deck()
    cards: list[DraggableCard] = []
    x = 50
    for image in deck_images[:5]:
        cards.append(DraggableCard(image, (x, HEIGHT - image.get_height() - 20)))
        x += 110

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            for card in cards:
                card.handle_event(event)

        screen.fill((0, 100, 0))
        for card in cards:
            card.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
