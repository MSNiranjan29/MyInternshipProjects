import pygame
import sys
from Story import rooms

# Initialize PyGame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title
pygame.display.set_caption("Text Adventure")

# Function to render text
def render_text(text, font_size, color=(255, 255, 255)):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


current_room = 0

# Function to display game description
def display_game_description():
    description = [
        "Welcome to the Text Adventure Game!",
        "Navigate through different rooms by choosing actions.",
        "Press Enter to start the game."
    ]
    screen.fill((0, 0, 0))  # Fill the screen with black
    y_offset = 20
    for line in description:
        text_surf, text_rect = render_text(line, 30)
        text_rect.topleft = (20, y_offset)
        screen.blit(text_surf, text_rect)
        y_offset += 40
    pygame.display.update()

# Display game description initially
display_game_description()

# Wait for Enter key press to start the game
waiting_for_start = True
while waiting_for_start:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                waiting_for_start = False
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  # Option 1
                # Check if the chosen action is within the range of available actions
                if len(rooms[current_room]["actions"]) > 0:
                    # Update current room based on player's choice for option 1
                    current_room = (current_room + 1) % len(rooms)  # Wrap around if necessary
            elif event.key == pygame.K_2:  # Option 2
                # Check if the chosen action is within the range of available actions
                if len(rooms[current_room]["actions"]) > 1:
                    # Update current room based on player's choice for option 2
                    current_room = (current_room + 2) % len(rooms)  # Wrap around if necessary
            elif event.key == pygame.K_ESCAPE:  # Exit the game if Escape key is pressed
                running = False

    # Clear the screen
    screen.fill((0, 0, 0))  # Fill the screen with black

    # Render room description and actions
    room_description, room_rect = render_text(rooms[current_room]["description"], 36)
    room_rect.topleft = (20, 20)
    screen.blit(room_description, room_rect)

    for i, action in enumerate(rooms[current_room]["actions"]):
        action_text, action_rect = render_text(action, 24)
        action_rect.topleft = (20, 80 + 30 * i)
        screen.blit(action_text, action_rect)

    # Update the display
    pygame.display.update()

# Display exit message before quitting the game
exit_message = "Exiting the game. Thank you for playing!"
screen.fill((0, 0, 0))  # Fill the screen with black
exit_text, exit_rect = render_text(exit_message, 36)
exit_rect.center = (screen_width // 2, screen_height // 2)
screen.blit(exit_text, exit_rect)
pygame.display.update()





# Wait for a short duration before quitting (for visibility of the exit message)
pygame.time.delay(2000)  # 2000 milliseconds (2 seconds) delay
pygame.quit()
sys.exit()
