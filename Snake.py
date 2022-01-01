import pygame
import sys
import random

pygame.init()
pygame.font.init()

clock = pygame.time.Clock()

width = 752
height = 526

screen = pygame.display.set_mode((width, height))

x_out = False

game_over = False

score = 0
speed_alpha = 15
speed_beta = 0

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
white = (255,255,255)

left = 1
right = 2
up = 3
down = 4

snake_move = 0

snake_head_pos = [150,250]
snake_head = snake_head_pos[:]
snake_alpha = [snake_head]
snake_beta = snake_alpha[:]
snake_gamma = snake_alpha[:]

apple_pos_alpha = [375,250]
apple_pos_alpha_x = apple_pos_alpha[0]
apple_pos_alpha_y = apple_pos_alpha[1]

apple_pos_beta = [0,0]
apple_pos_beta_x = apple_pos_beta[0]
apple_pos_beta_y = apple_pos_beta[1]

grow = 0

move = 0

pixel_size = 25

score_text = pygame.font.SysFont("couriernew",35,bold = True)
game_over_text = pygame.font.SysFont("couriernew",65,bold = True)
restart_sign_corner_square = [[627,391],[671,391],[627,435],[671,435]]
restart_sign_corner_circle = [[633,397],[670,397],[633,434],[670,434]]


def detect_eating():
	if snake_head_pos == apple_pos_alpha:
		return True
	else:
		return False

def detect_wall():
	if snake_head_pos[0] >= 550:
		return True
	elif snake_head_pos[0] < 0:
		return True
	elif snake_head_pos[1] >= 525:
		return True
	elif snake_head_pos[1] < 0:
		return True

def detect_collision():
	check = []
	for x in snake_alpha:
		if x not in check:
			check.append(x)
		elif x in check:
			return True

while not x_out:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:

			sys.exit()

		if event.type == pygame.KEYDOWN:

			if move == 0:

				move = 1

				if snake_move == 0:

					if event.key == pygame.K_LEFT:
						snake_move = left
							
					elif event.key == pygame.K_RIGHT:
						snake_move = right
							
					elif event.key == pygame.K_UP:
						snake_move = up
							
					elif event.key == pygame.K_DOWN:
						snake_move = down

				elif snake_move == left:

					if event.key == pygame.K_UP:
						snake_move = up
							
					elif event.key == pygame.K_DOWN:
						snake_move = down

				elif snake_move == right:

					if event.key == pygame.K_UP:
						snake_move = up
							
					elif event.key == pygame.K_DOWN:
						snake_move = down

				elif snake_move == up:

					if event.key == pygame.K_LEFT:
						snake_move = left
							
					elif event.key == pygame.K_RIGHT:
						snake_move = right

				elif snake_move == down:

					if event.key == pygame.K_LEFT:
						snake_move = left
							
					elif event.key == pygame.K_RIGHT:
						snake_move = right

	if game_over == False:

		if detect_eating():

			score += 1

			speed_beta += 1

			grow = 1

			apple_pos_beta = [random.randint(0,21), random.randint(0,20)]
			apple_pos_beta_x = apple_pos_beta[0]
			apple_pos_beta_y = apple_pos_beta[1]

			apple_pos_alpha_x = apple_pos_beta_x * 25

			apple_pos_alpha_y = apple_pos_beta_y * 25

			apple_pos_alpha = [apple_pos_alpha_x, apple_pos_alpha_y]


		if grow == 1:
			x = snake_alpha[-1]
			y = x[:]
			snake_alpha.append(y)
			grow = 0

		snake_beta = snake_alpha[:]
		snake_beta.pop()
		snake_beta.reverse()

		if snake_move == left:
			snake_head_pos[0] -= pixel_size
		elif snake_move == right:
			snake_head_pos[0] += pixel_size
		elif snake_move == up:
			snake_head_pos[1] -= pixel_size
		elif snake_move == down:
			snake_head_pos[1] += pixel_size

		snake_head = snake_head_pos[:]
		snake_beta.append(snake_head)
		snake_beta.reverse()
		snake_alpha = snake_beta[:]

		if speed_beta == 5:
			speed_alpha += 1
			speed_beta = 0

		if detect_wall():
			game_over = True

		if detect_collision():
			game_over = True

	if game_over == False:
		snake_gamma = snake_alpha[:]
	elif game_over == True: 
		pass

	clock.tick(speed_alpha)

	screen.fill(black)
	pygame.draw.rect(screen, white, (551, 0, 1, 551))
	pygame.draw.rect(screen, red, (apple_pos_alpha[0], apple_pos_alpha[1], pixel_size, pixel_size))

	for x in snake_gamma:
		pygame.draw.rect(screen, green, (x[0], x[1], pixel_size, pixel_size))

	if game_over == False:
		display_score = score_text.render("Score:" + str(score), 1, white)
		screen.blit(display_score, (575,25))
		pygame.display.update()
		move = 0

	if game_over == True:

		display_screen_1 = game_over_text.render("Game", 1, white)
		screen.blit(display_screen_1, (575,40))
		display_screen_2 = game_over_text.render("Over", 1, white)
		screen.blit(display_screen_2, (575,100))
		display_score = score_text.render("Score:" + str(score), 1, white)
		screen.blit(display_score, (575,260))
		pygame.draw.rect(screen, black, (601, 375, 100, 80))
		pygame.draw.rect(screen, white, (621, 385, 62, 62))
		pygame.draw.rect(screen, black, (622, 386, 60, 60))
		pygame.draw.rect(screen, white, (627, 391, 50, 50))

		for x in restart_sign_corner_square:
			pygame.draw.rect(screen, black, (x[0], x[1], 6, 6))

		for x in restart_sign_corner_circle:
			pygame.draw.circle(screen, white, (x[0], x[1]), 6)

		pygame.draw.rect(screen, black, (633, 397, 38, 38))
		pygame.draw.rect(screen, black, (643, 391, 18, 6))

		pygame.draw.polygon(screen, white, ([654,393],[660,393],[660,387]))
		pygame.draw.polygon(screen, white, ([654,394],[660,394],[660,400]))
		
		pygame.display.update()

		for event in pygame.event.get():

			if event.type == pygame.QUIT:

				sys.exit()

			if event.type == pygame.KEYDOWN:

				if event.key == pygame.K_SPACE:
					
					snake_move = 0

					snake_head_pos = [150,250]
					snake_head = snake_head_pos[:]
					snake_alpha = [snake_head]
					snake_beta = snake_alpha[:]

					apple_pos_alpha = [375,250]
					apple_pos_alpha_x = apple_pos_alpha[0]
					apple_pos_alpha_y = apple_pos_alpha[1]

					apple_pos_beta = [0,0]
					apple_pos_beta_x = apple_pos_beta[0]
					apple_pos_beta_y = apple_pos_beta[1]

					score = 0
					speed_alpha = 15
					speed_beta = 0

					game_over = False

		mouse_pressed = pygame.mouse.get_pressed()
		mouse_pos = pygame.mouse.get_pos()
		if mouse_pressed[0] == 1:
			if mouse_pos[0] >= 621:
				if mouse_pos[0] <= 682:
					if mouse_pos[1] >= 385:
						if mouse_pos[1] <= 446:

							snake_move = 0

							snake_head_pos = [150,250]
							snake_head = snake_head_pos[:]
							snake_alpha = [snake_head]
							snake_beta = snake_alpha[:]

							apple_pos_alpha = [375,250]
							apple_pos_alpha_x = apple_pos_alpha[0]
							apple_pos_alpha_y = apple_pos_alpha[1]

							apple_pos_beta = [0,0]
							apple_pos_beta_x = apple_pos_beta[0]
							apple_pos_beta_y = apple_pos_beta[1]

							score = 0
							speed_alpha = 15
							speed_beta = 0

							game_over = False


