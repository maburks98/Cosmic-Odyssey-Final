import pygame
import os
import sprite
import spaceshooter
import random

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1200, 667
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cosmic Odyssey")

TITLE_FONT = pygame.font.SysFont('fixed sys500c', 100)
LIGHTYEAR_FONT = pygame.font.SysFont('fixed sys500c', 40)
HEALTH_FONT = pygame.font.SysFont('fixed sys500c', 35)

FPS = 70

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

SHIP_HEIGHT = HEIGHT // 2 - 170
SHIP_VEL = 1

TITLE_BOX_BORDER = pygame.Rect(WIDTH // 2 - 440, HEIGHT // 2 + 75, 900, 150)
TITLE_BOX_FILL = pygame.Rect(WIDTH // 2 - 435, HEIGHT // 2 + 80, 890, 140)

EVENT_BOX_BORDER = pygame.Rect(0, 445, WIDTH, HEIGHT // 3)
EVENT_BOX_FILL = pygame.Rect(5, 450, WIDTH - 10, HEIGHT // 3 - 10)

LIGHTYEAR_BOX_BORDER = pygame.Rect(0, 0, WIDTH, 90)
LIGHTYEAR_BOX = pygame.Rect(5, 5, WIDTH - 10, 80)

HEALTH_BOX_BORDER = pygame.Rect(WIDTH - 155, 400, 155, 50)
HEALTH_BOX = pygame.Rect(WIDTH - 150, 405, 145, 40)

TITLE_SCREEN_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets_CO', 'Title Bg.png')), (WIDTH, HEIGHT))
ANDROMEDA_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets_CO', 'Andromeda BG.jpg')), (WIDTH, HEIGHT))
SAT_ETLAY_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets_CO', 'Satalite.png')), (WIDTH, HEIGHT))
SOL_III_BG = pygame.transform.scale(pygame.transform.flip(pygame.image.load(
    os.path.join('Assets_CO', 'SOLIII.png')), 1, 1), (WIDTH, HEIGHT))
TRADING_POST_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets_CO', 'trading.jpg')), (WIDTH, HEIGHT))
BLACK_HOLE_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets_CO', 'gargantua.webp')), (WIDTH, HEIGHT))
CENTAURUS_A_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets_CO', 'Centaurus A BG.png')), (WIDTH, HEIGHT // 1.5))

FREIGHTER_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets_CO', 'freight.jpg')), (WIDTH, HEIGHT))
WORMHOLE_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets_CO', 'wormhole.jpg')), (WIDTH, HEIGHT))
CONSTELLATION_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets_CO', 'constellation.webp')), (WIDTH, HEIGHT))
CRYO_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets_CO', 'cryo.jpg')), (WIDTH, HEIGHT))
ALIEN_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets_CO', 'alien.jpg')), (WIDTH, HEIGHT // 1.5))
ASTEROIDS_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets_CO', 'asteroids.jpg')), (WIDTH, HEIGHT // 1.5))
DYSENTERY_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets_CO', 'dysentery.jpg')), (WIDTH, HEIGHT // 1.5))
SOLAR_FLARE_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets_CO', 'solar.jpg')), (WIDTH, HEIGHT // 1.5))
PLUTO_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets_CO', 'pluto.webp')), (WIDTH, HEIGHT * 1.1))  # height should be at 200
FUEL_FAIL_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets_CO', 'fuel.jpg')), (WIDTH, HEIGHT // 1.5))

SHOP_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets_CO', 'shop.jpg')), (WIDTH, HEIGHT))
SHOP2_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets_CO', 'shop2.jpg')), (WIDTH, HEIGHT))
SHOP3_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets_CO', 'shop3.jpg')), (WIDTH, HEIGHT))
SHOP4_BG = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets_CO', 'shop4.jpg')), (WIDTH, HEIGHT))

SHOP_TXT = pygame.image.load(os.path.join('Assets_CO', 'shoptxt.png'))
SHOP2_TXT = pygame.image.load(os.path.join('Assets_CO', 'shop2txt.png'))
SHOP3_TXT = pygame.image.load(os.path.join('Assets_CO', 'shop3txt.png'))
SHOP4_TXT = pygame.image.load(os.path.join('Assets_CO', 'shop4txtx.png'))


ANDR_TXT = pygame.image.load(os.path.join('Assets_CO', 'andromedatxt.png'))
FREI_TXT = pygame.image.load(os.path.join('Assets_CO', 'freightertxt.png'))
CRYO0_TXT = pygame.image.load(os.path.join('Assets_CO', 'cryo0txt.png'))
CRYO1_TXT = pygame.image.load(os.path.join('Assets_CO', 'cryo1txt.png'))
FLAR_TXT = pygame.image.load(os.path.join('Assets_CO', 'flaretxt.png'))
AST1_TXT = pygame.image.load(os.path.join('Assets_CO', 'asteroid1txt.png'))
SATE_TXT = pygame.image.load(os.path.join('Assets_CO', 'satelitetxt.png'))
CONS_TXT = pygame.image.load(os.path.join('Assets_CO', 'constellationtxt.png'))
FUEL_TXT = pygame.image.load(os.path.join('Assets_CO', 'fueltxt.png'))
SOL_TXT = pygame.image.load(os.path.join('Assets_CO', 'soltxt.png'))
ALIE_TXT = pygame.image.load(os.path.join('Assets_CO', 'alientxt.png'))
WORM_TXT = pygame.image.load(os.path.join('Assets_CO', 'wormholetxt.png'))
DYSE_TXT = pygame.image.load(os.path.join('Assets_CO', 'dysenterytxt.png'))
PLUT_TXT = pygame.image.load(os.path.join('Assets_CO', 'plutotxt.png'))
TRAD_TXT = pygame.image.load(os.path.join('Assets_CO', 'tradingtxt.png'))
BLAC_TXT = pygame.image.load(os.path.join('Assets_CO', 'blackholetxt.png'))
CENT_TXT = pygame.image.load(os.path.join('Assets_CO', 'centaurustxt.png'))


SPRITE_SHEET_IMG = pygame.image.load(os.path.join('Assets_CO', 'ship_spritesheet.png')).convert_alpha()

MAX_LIGHTYEAR = 15
LIGHTYEAR = 0
MORALE = 100
FUEL = 0
RATIONS = 0
MEDICINE = 0
CREDITS = 1500

ILLNESS = 0


SCORE = 0
LUCK = 70

sprite_sheet = sprite.SpriteSheet(SPRITE_SHEET_IMG)

animation_list = []
animation_steps = 4
last_update = pygame.time.get_ticks()
animation_cooldown = 150
frame = 0

cryoill = random.randint(0, 100)
astpass = random.randint(0, 100)

for x in range(animation_steps):
    animation_list.append(sprite_sheet.get_image(x, 254, 112, BLACK))


def screen_txt():
    global ILLNESS, RATIONS, FUEL, MORALE
    lightyear_txt = LIGHTYEAR_FONT.render("Light years travelled: " + str(LIGHTYEAR - 1), 1, WHITE)
    morale_txt = LIGHTYEAR_FONT.render("Morale: " + str(MORALE), 1, WHITE)
    lowmorale_txt = LIGHTYEAR_FONT.render("Morale: " + str(MORALE), 1, RED)
    fuel_txt = LIGHTYEAR_FONT.render("Fuel level: " + str(FUEL), 1, WHITE)
    lowfuel_txt = LIGHTYEAR_FONT.render("Fuel level: " + str(FUEL), 1, RED)
    rations_txt = LIGHTYEAR_FONT.render("Rations remaining: " + str(RATIONS), 1, WHITE)
    rations0_txt = LIGHTYEAR_FONT.render("Rations remaining: NONE", 1, RED)
    credits_txt = LIGHTYEAR_FONT.render("Credits: " + str(CREDITS), 1, WHITE)
    medicine_txt = LIGHTYEAR_FONT.render("Dopamine pills: " + str(MEDICINE), 1, WHITE)
    health0_txt = HEALTH_FONT.render("Healthy", 1, GREEN)
    health1_txt = HEALTH_FONT.render("Unhealthy", 1, RED)
    if ILLNESS == 0:
        WIN.blit(health0_txt, (WIDTH - 125, 413))
    if ILLNESS > 0:
        WIN.blit(health1_txt, (WIDTH - 135, 413))
    WIN.blit(lightyear_txt, (10, 10))
    if MORALE > 50:
        WIN.blit(morale_txt, (500, 10))
    if MORALE <= 50:
        WIN.blit(lowmorale_txt, (500, 10))
    if FUEL > 200:
        WIN.blit(fuel_txt, (900, 10))
    if FUEL <= 200:
        WIN.blit(lowfuel_txt, (900, 10))
    if RATIONS > 0:
        WIN.blit(rations_txt, (10, 50))
    if RATIONS <= 0:
        WIN.blit(rations0_txt, (10, 50))
    WIN.blit(medicine_txt, (500, 50))
    WIN.blit(credits_txt, (900, 50))


def event_txt_box():
    pygame.draw.rect(WIN, WHITE, EVENT_BOX_BORDER)
    pygame.draw.rect(WIN, BLACK, EVENT_BOX_FILL)
    pygame.draw.rect(WIN, WHITE, LIGHTYEAR_BOX_BORDER)
    pygame.draw.rect(WIN, BLACK, LIGHTYEAR_BOX)
    pygame.draw.rect(WIN, WHITE, HEALTH_BOX_BORDER)
    pygame.draw.rect(WIN, BLACK, HEALTH_BOX)

def title_screen():
    WIN.blit(TITLE_SCREEN_BG, (0, 0))
    title_screen_text = TITLE_FONT.render("Press any key to play!", 1, WHITE)
    pygame.draw.rect(WIN, WHITE, TITLE_BOX_BORDER)
    pygame.draw.rect(WIN, BLACK, TITLE_BOX_FILL)
    WIN.blit(title_screen_text, (
        WIDTH / 2 - title_screen_text.get_width(
        ) / 2 + 10, HEIGHT / 2 - title_screen_text.get_height() / 2 + 150))


shop1_open = False
shop2_open = False
shop3_open = False
shop4_open = False

FREI_EVENT = False
CRYO_EVENT = False
FLAR_EVENT = False
AST_EVENT = False
CONS_Event = False
FUEL_EVENT = False
ALIE_EVENT = False
WORM_EVENT = False
DYSE_EVENT = False
PLUT_EVENT = False
CENT_EVENT = False


def shop1(keys_pressed):
    global shop1_open
    WIN.blit(SHOP_BG, (0, 0))
    event_txt_box()
    screen_txt()
    WIN.blit(SHOP_TXT, (10, 455))
    if keys_pressed[pygame.K_s]:
        shop1_open = not shop1_open


def shop2(keys_pressed):
    global shop2_open
    WIN.blit(SHOP2_BG, (0, 0))
    event_txt_box()
    screen_txt()
    WIN.blit(SHOP2_TXT, (10, 455))
    if keys_pressed[pygame.K_s]:
        shop2_open = not shop2_open


def shop3(keys_pressed):
    global shop3_open
    WIN.blit(SHOP3_BG, (0, 0))
    event_txt_box()
    screen_txt()
    WIN.blit(SHOP3_TXT, (10, 455))
    if keys_pressed[pygame.K_s]:
        shop3_open = not shop3_open


def shop4(keys_pressed):
    global shop4_open
    WIN.blit(SHOP4_BG, (0, 0))
    event_txt_box()
    screen_txt()
    WIN.blit(SHOP4_TXT, (10, 455))
    if keys_pressed[pygame.K_s]:
        shop4_open = not shop4_open


def andromeda(keys_pressed):
    global shop1_open
    if not shop1_open:
        WIN.blit(ANDROMEDA_BG, (0, 0))
        event_txt_box()
        screen_txt()
        WIN.blit(ANDR_TXT, (10, 455))
        if keys_pressed[pygame.K_s]:
            shop1(keys_pressed)
    else:
        shop1(keys_pressed)


def satalite(keys_pressed):
    global LIGHTYEAR, shop2_open
    if not shop2_open:
        WIN.blit(SAT_ETLAY_BG, (0, -100))
        event_txt_box()
        screen_txt()
        WIN.blit(SATE_TXT, (10, 455))
        if keys_pressed[pygame.K_s]:
            shop2(keys_pressed)
    else:
        shop2(keys_pressed)


def soliii(keys_pressed):
    global LIGHTYEAR, shop3_open
    if not shop3_open:
        WIN.blit(SOL_III_BG, (0, 0))
        event_txt_box()
        screen_txt()
        WIN.blit(SOL_TXT, (10, 455))
        if keys_pressed[pygame.K_s]:
            shop3(keys_pressed)
    else:
        shop3(keys_pressed)


def trading(keys_pressed):
    global LIGHTYEAR
    if not shop4_open:
        WIN.blit(TRADING_POST_BG, (0, 0))
        event_txt_box()
        screen_txt()
        WIN.blit(TRAD_TXT, (10, 455))
        if keys_pressed[pygame.K_s]:
            shop4(keys_pressed)
    else:
        shop4(keys_pressed)


def blackhole():
    global LIGHTYEAR
    WIN.blit(BLACK_HOLE_BG, (0, 0))
    event_txt_box()
    screen_txt()
    WIN.blit(BLAC_TXT, (10, 455))


def centaurus_a():
    global LIGHTYEAR, SCORE, MORALE, ILLNESS, RATIONS, CREDITS, FUEL, CENT_EVENT
    CREDIT_SCORE = CREDITS * 10
    ILLNESS_SCORE = ILLNESS * 100
    FINAL_SCORE = SCORE + MORALE + RATIONS + FUEL - ILLNESS_SCORE + CREDIT_SCORE
    WIN.blit(CENTAURUS_A_BG, (0, 0))
    event_txt_box()
    screen_txt()
    if not CENT_EVENT:
        if FUEL <= 300:
            FUEL = 0
            CENT_EVENT = True
        if FUEL > 300:
            FUEL -= 200
            CENT_EVENT = True
    WIN.blit(CENT_TXT, (10, 455))
    win_txt = TITLE_FONT.render("CONGRATULATIONS!", 1, GREEN)
    WIN.blit(win_txt, (
        WIDTH // 2 - win_txt.get_width() // 2, HEIGHT // 2 - win_txt.get_height() // 2 - 100))
    score_txt = TITLE_FONT.render("YOUR SCORE WAS: " + str(FINAL_SCORE), 1, WHITE)
    WIN.blit(score_txt, (
        WIDTH // 2 - score_txt.get_width() // 2, HEIGHT // 2 - score_txt.get_height() // 2))
    pygame.display.update()


def event_freighter():
    global LIGHTYEAR, MEDICINE, RATIONS, FREI_EVENT
    WIN.blit(FREIGHTER_BG, (0, -100))
    event_txt_box()
    screen_txt()
    WIN.blit(FREI_TXT, (10, 455))
    if not FREI_EVENT:
        MEDICINE += 1
        RATIONS += 10
        FREI_EVENT = True


def event_worm():
    global LIGHTYEAR, FUEL, WORM_EVENT
    WIN.blit(WORMHOLE_BG, (0, -100))
    event_txt_box()
    screen_txt()
    WIN.blit(WORM_TXT, (10, 455))
    if not WORM_EVENT:
        FUEL += 50
        WORM_EVENT = True


def event_constellation():
    global LIGHTYEAR, MORALE, LUCK, CONS_Event
    WIN.blit(CONSTELLATION_BG, (0, -100))
    event_txt_box()
    screen_txt()
    WIN.blit(CONS_TXT, (10, 455))
    if not CONS_Event:
        MORALE += 10
        LUCK += 5
        CONS_Event = True


def event_cryo():
    global LIGHTYEAR, LUCK, ILLNESS, CRYO_EVENT, cryoill
    WIN.blit(CRYO_BG, (0, -100))
    event_txt_box()
    screen_txt()
    if cryoill <= LUCK:
        WIN.blit(CRYO0_TXT, (10, 455))
        if not CRYO_EVENT:
            CRYO_EVENT = True
    if cryoill > LUCK:
        WIN.blit(CRYO1_TXT, (10, 455))
        if not CRYO_EVENT:
            ILLNESS += 1
            CRYO_EVENT = True


def event_alien():
    global LIGHTYEAR, ILLNESS, RATIONS, ALIE_EVENT
    WIN.blit(ALIEN_BG, (0, 0))
    event_txt_box()
    screen_txt()
    WIN.blit(ALIE_TXT, (10, 455))
    if not ALIE_EVENT:
        ILLNESS += 1
        RATIONS -= 20
        ALIE_EVENT = True


def event_asteroid():
    global LIGHTYEAR, AST_EVENT, LUCK, MORALE
    WIN.blit(ASTEROIDS_BG, (0, 0))
    event_txt_box()
    screen_txt()
    WIN.blit(AST1_TXT, (10, 455))
    if not AST_EVENT:
        MORALE -= 10
        LUCK -= 5
        AST_EVENT = True


def event_dysentery():
    global LIGHTYEAR, ILLNESS, DYSE_EVENT
    WIN.blit(DYSENTERY_BG, (0, 0))
    event_txt_box()
    screen_txt()
    WIN.blit(DYSE_TXT, (10, 455))
    if not DYSE_EVENT:
        ILLNESS += 1
        DYSE_EVENT = True


def event_solar():
    global LIGHTYEAR, RATIONS, FUEL, FLAR_EVENT
    WIN.blit(SOLAR_FLARE_BG, (0, 0))
    event_txt_box()
    screen_txt()
    WIN.blit(FLAR_TXT, (10, 455))
    if not FLAR_EVENT:
        RATIONS -= 10
        FUEL -= 50
        FLAR_EVENT = True


def event_pluto():
    global LIGHTYEAR, MORALE, LUCK, PLUT_EVENT
    WIN.blit(PLUTO_BG, (0, -200))
    event_txt_box()
    screen_txt()
    WIN.blit(PLUT_TXT, (10, 455))
    if not PLUT_EVENT:
        MORALE -= 20
        LUCK -= 10
        PLUT_EVENT = True


def event_fuel_fail():
    global LIGHTYEAR, FUEL, FUEL_EVENT
    WIN.blit(FUEL_FAIL_BG, (0, 0))
    event_txt_box()
    screen_txt()
    WIN.blit(FUEL_TXT, (10, 455))
    if not FUEL_EVENT:
        FUEL -= 100
        FUEL_EVENT = True


def event_loader():
    global LIGHTYEAR
    keys_pressed = pygame.key.get_pressed()
    if LIGHTYEAR == 0:
        title_screen()
    elif LIGHTYEAR == 1:
        andromeda(keys_pressed)
    elif LIGHTYEAR == 2:
        event_freighter()
    elif LIGHTYEAR == 3:
        event_cryo()
    elif LIGHTYEAR == 4:
        event_solar()
    elif LIGHTYEAR == 5:
        event_asteroid()
    elif LIGHTYEAR == 6:
        satalite(keys_pressed)
    elif LIGHTYEAR == 7:
        event_constellation()
    elif LIGHTYEAR == 8:
        event_fuel_fail()
    elif LIGHTYEAR == 9:
        soliii(keys_pressed)
    elif LIGHTYEAR == 10:
        event_alien()
    elif LIGHTYEAR == 11:
        event_worm()
    elif LIGHTYEAR == 12:
        event_dysentery()
    elif LIGHTYEAR == 13:
        event_pluto()
    elif LIGHTYEAR == 14:
        trading(keys_pressed)
    elif LIGHTYEAR == 15:
        blackhole()
    elif LIGHTYEAR == 16:
        centaurus_a()


def main():
    clock = pygame.time.Clock()
    run = True
    global FUEL, SHIP_HEIGHT, SHIP_VEL, LIGHTYEAR, last_update, frame, \
        RATIONS, shop1_open, CREDITS, MORALE, LUCK, SCORE, MEDICINE, ILLNESS, \
        LUCK, shop2_open, shop3_open, shop4_open, astpass, AST_EVENT
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                if event.key == pygame.K_1 and shop1_open and CREDITS >= 100:
                    FUEL += 200
                    CREDITS -= 100
                if event.key == pygame.K_2 and shop1_open and CREDITS >= 50:
                    RATIONS += 30
                    CREDITS -= 50
                if event.key == pygame.K_3 and shop1_open and CREDITS >= 100:
                    MEDICINE += 1
                    CREDITS -= 100
                if event.key == pygame.K_1 and shop2_open and CREDITS >= 100:
                    FUEL += 200
                    CREDITS -= 100
                if event.key == pygame.K_2 and shop2_open and CREDITS >= 50:
                    RATIONS += 30
                    CREDITS -= 50
                if event.key == pygame.K_3 and shop2_open and CREDITS >= 100:
                    MEDICINE += 1
                    CREDITS -= 100
                if event.key == pygame.K_1 and shop3_open and CREDITS >= 100:
                    FUEL += 200
                    CREDITS -= 100
                if event.key == pygame.K_2 and shop3_open and CREDITS >= 50:
                    RATIONS += 30
                    CREDITS -= 50
                if event.key == pygame.K_3 and shop3_open and CREDITS >= 100:
                    MEDICINE += 1
                    CREDITS -= 100
                if event.key == pygame.K_1 and shop4_open and CREDITS >= 100:
                    FUEL += 200
                    CREDITS -= 100
                if event.key == pygame.K_2 and shop4_open and CREDITS >= 50:
                    RATIONS += 30
                    CREDITS -= 50
                if event.key == pygame.K_3 and shop4_open and CREDITS >= 100:
                    MEDICINE += 1
                    CREDITS -= 100

                if (event.key == pygame.K_b and not shop1_open and not shop2_open and not shop3_open and not
                shop4_open and LIGHTYEAR != 0 and LIGHTYEAR != 1):
                    FUEL += 300
                    MORALE -= 60
                    LUCK -= 30
                    SCORE -= 500
                    sacraficeoutcome = random.randint(0, 100)
                    if sacraficeoutcome <= LUCK:
                        SCORE += 1
                    if sacraficeoutcome > LUCK:
                        ILLNESS += 1


                if (event.key == pygame.K_m and not shop1_open and not shop2_open and not shop3_open and not
                shop4_open and MEDICINE >= 1 and LIGHTYEAR != 0 and LIGHTYEAR != 1):
                    ILLNESS = 0
                    MEDICINE -= 1
                    SCORE += 5
                    if MORALE <= 66:
                        MORALE += 34
                        LUCK += 16


                if (event.key == pygame.K_n and not shop1_open and not shop2_open
                        and not shop3_open and not shop4_open and LIGHTYEAR != 0 and LIGHTYEAR != 1):

                    huntoutcome = random.randint(0, 100)
                    if huntoutcome <= LUCK:
                        hunt_txt = TITLE_FONT.render("HUNT", 1, WHITE)
                        WIN.blit(hunt_txt,
                                 (WIDTH // 2 - hunt_txt.get_width() // 2, HEIGHT // 2 - hunt_txt.get_height() // 2 - 100))
                        hunt1_txt = TITLE_FONT.render("SUCCESSFUL!", 1, GREEN)
                        WIN.blit(hunt1_txt, (
                            WIDTH // 2 - hunt1_txt.get_width() // 2, HEIGHT // 2 - hunt1_txt.get_height() // 2))
                        pygame.display.update()
                        pygame.time.delay(500)
                        RATIONS += 10
                        SCORE += 5
                    elif huntoutcome > LUCK:
                        hunt_txt = TITLE_FONT.render("HUNT", 1, WHITE)
                        WIN.blit(hunt_txt,
                                 (WIDTH // 2 - hunt_txt.get_width() // 2,
                                  HEIGHT // 2 - hunt_txt.get_height() // 2 - 100))
                        hunt0_txt = TITLE_FONT.render("UNSUCCESSFUL!", 1, RED)
                        WIN.blit(hunt0_txt, (
                            WIDTH // 2 - hunt0_txt.get_width() // 2, HEIGHT // 2 - hunt0_txt.get_height() // 2))
                        pygame.display.update()
                        pygame.time.delay(500)
                        MORALE -= 10
                        LUCK -= 5

                else:
                    if LIGHTYEAR == 0:
                        if (event.key != pygame.K_ESCAPE and event.key != pygame.K_TAB and
                                event.key != pygame.K_w and event.key != pygame.K_a and
                                event.key != pygame.K_s and event.key != pygame.K_LSHIFT and
                                event.key != pygame.K_RSHIFT and event.key != pygame.K_UP and
                                event.key != pygame.K_LEFT and event.key != pygame.K_DOWN and
                                event.key != pygame.K_RIGHT and event.key != pygame.K_d):
                            LIGHTYEAR += 1
                        if event.key == pygame.K_TAB:
                            spaceshooter.spacefighters()
                            break

                    elif (LIGHTYEAR != 0 and LIGHTYEAR <= MAX_LIGHTYEAR and not shop1_open and not
                    shop2_open and not shop3_open and not shop4_open):
                        if event.key == pygame.K_SPACE:
                            LIGHTYEAR += 1
                            FUEL -= 100
                            RATIONS -= 10
                            SCORE += 10
                            if RATIONS < 0:
                                RATIONS += 10
                                MORALE -= 20
                                LUCK -= 10
                            if ILLNESS >= 1:
                                MORALE -= 34
                                LUCK -= 16
                            if LIGHTYEAR == 15:
                                SCORE += 200

        if FUEL <= -100:
            go1_txt = TITLE_FONT.render("GAME OVER!", 1, RED)
            WIN.blit(go1_txt, (WIDTH // 2 - go1_txt.get_width() // 2, HEIGHT // 2 - go1_txt.get_height() // 2 - 100))
            fuel0_txt = TITLE_FONT.render("YOU RAN OUT OF FUEL", 1, RED)
            WIN.blit(fuel0_txt, (WIDTH // 2 - fuel0_txt.get_width() // 2, HEIGHT // 2 - fuel0_txt.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(5000)

            LIGHTYEAR = 0
            MORALE = 100
            FUEL = 0
            RATIONS = 0
            MEDICINE = 0
            CREDITS = 1500

            SCORE = 0
            LUCK = 70

            ILLNESS = 0

            break

        if MORALE <= 0:
            go2_txt = TITLE_FONT.render("GAME OVER!", 1, RED)
            WIN.blit(go2_txt, (WIDTH // 2 - go2_txt.get_width() // 2, HEIGHT // 2 - go2_txt.get_height() // 2 - 100))
            morale0_txt = TITLE_FONT.render("YOU RAN OUT OF MORALE", 1, RED)
            WIN.blit(morale0_txt, (
                WIDTH // 2 - morale0_txt.get_width() // 2, HEIGHT // 2 - morale0_txt.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(5000)

            LIGHTYEAR = 0
            MORALE = 100
            FUEL = 0
            RATIONS = 0
            MEDICINE = 0
            CREDITS = 1500

            SCORE = 0
            LUCK = 70

            ILLNESS = 0

            break

        current_time = pygame.time.get_ticks()
        if current_time - last_update >= animation_cooldown:
            frame += 1
            last_update = current_time
            if frame >= len(animation_list):
                frame = 0

        if SHIP_HEIGHT < 100 or SHIP_HEIGHT > 200:
            SHIP_VEL = -SHIP_VEL

        SHIP_HEIGHT += SHIP_VEL
        event_loader()
        if LIGHTYEAR != 0 and not shop1_open and not shop2_open and not shop3_open and not shop4_open:
            WIN.blit(animation_list[frame], (100, SHIP_HEIGHT))

        pygame.display.update()

    main()


if __name__ == "__main__":
    main()
