import os
import sys
import logging
import pygame
from pygame.locals import *
import random

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

# Initalize pygame
pygame.init()

# abstract the movement of the mouth
UP = True
DOWN = False

# initialize the window
WIN_WIDTH = 750
WIN_HEIGHT = 750
WIN_SIZE = (WIN_WIDTH, WIN_HEIGHT)
WIN = pygame.display.set_mode(WIN_SIZE)

# Textbox coordinate for Hossan's and Troy's dialogue and tips dialogue box
H_TEXTBOX_C_W = 450  # dialogue's box width
H_TEXTBOX_C_H = 125  # dialogue's box height
H_TEXTBOX_C_Y = 195  # dialogue's box y coordinate
H_TEXTBOX_C_X = (WIN_WIDTH - H_TEXTBOX_C_W) // 2  # dialogue's box x coordinate
T_TEXTBOX_C_W = 420
T_TEXTBOX_C_H = 150
T_TEXTBOX_C_Y = 325
T_TEXTBOX_C_X = (WIN_WIDTH - T_TEXTBOX_C_W) // 2

# Miscellaneous settings
FPS = 60  # set frame rate
ORIGIN = (0, 0)  # origin spot at x = 0, y = 0
H_IMG_RESCALE = (100, 175)  # tuple to rescale the image of Dr. Hossan
T_IMG_RESCALE = (150, 150)  # tuple to rescale image of Troy
Q_RESCALE = (250, 110)
ANS1_RESCALE = (40, 40)
ANS2_RESCALE = (100, 75)
WHITE = (255, 255, 255)  # tuple for white color
BLACK = (0, 0, 0)
Font_file = "Oswald-Bold.ttf"
CWD = " "

if getattr(sys, 'frozen', False):
    CWD = os.path.dirname(sys.executable)
else:
    CWD = os.path.dirname(os.path.abspath(__file__))

FONT = os.path.join(CWD, Font_file)
# Load in Hossan, Troy sprites, and the background
BG_PATH = os.path.join(CWD, "Game_assets/background/SPACE_BG.jpg")
HOSSAN_STILL_PATH = os.path.join(CWD, "Game_assets/Dr_Hossan/HOSSAN_MOHAMMAD_STILL.PNG")
HOSSAN_TALK1_PATH = os.path.join(CWD, "Game_assets/Dr_Hossan/HOSSAN_MOHAMMAD_TALK_1.PNG")
HOSSAN_TALK2_PATH = os.path.join(CWD, "Game_assets/Dr_Hossan/HOSSAN_MOHAMMAD_TALK_2.PNG")
HOSSAN_TALK3_PATH = os.path.join(CWD, "Game_assets/Dr_Hossan/HOSSAN_MOHAMMAD_TALK_3.PNG")
TROY_STILL_PATH = os.path.join(CWD, "Game_assets/Troy_pix_png/Troy_pix_still.png")
TROY_LEFT1_PATH = os.path.join(CWD, "Game_assets/Troy_pix_png/Troy_walk_left_1.png")
TROY_INTER_LEFT1_PATH = os.path.join(CWD, "Game_assets/Troy_pix_png/Troy_inter_left_1.png")
TROY_LEFT2_PATH = os.path.join(CWD, "Game_assets/Troy_pix_png/Troy_walk_left_2.png")
TROY_INTER_LEFT2_PATH = os.path.join(CWD, "Game_assets/Troy_pix_png/Troy_inter_left_2.png")
TROY_RIGHT1_PATH = os.path.join(CWD, "Game_assets/Troy_pix_png/Troy_walk_right_1.png")
TROY_INTER_RIGHT1_PATH = os.path.join(CWD, "Game_assets/Troy_pix_png/Troy_inter_right_1.png")
TROY_RIGHT2_PATH = os.path.join(CWD, "Game_assets/Troy_pix_png/Troy_walk_right_2.png")
TROY_INTER_RIGHT2_PATH = os.path.join(CWD, "Game_assets/Troy_pix_png/Troy_inter_right_2.png")

# Load in the question set
Q1_PATH = os.path.join(CWD, "Game_assets/problems/problem_1/Question_1.png")
F1Q1_PATH = os.path.join(CWD, "Game_assets/problems/problem_1/fakeq1_1.png")
F2Q1_PATH = os.path.join(CWD, "Game_assets/problems/problem_1/fakeq1_2.png")
F3Q1_PATH = os.path.join(CWD, "Game_assets/problems/problem_1/fakeq1_3.png")
F4Q1_PATH = os.path.join(CWD, "Game_assets/problems/problem_1/fakeq1_4.png")
ANSQ1_PATH = os.path.join(CWD, "Game_assets/problems/problem_1/ansq1.png")

Q2_PATH = os.path.join(CWD, "Game_assets/problems/problem_2/Question_2.png")
F1Q2_PATH = os.path.join(CWD, "Game_assets/problems/problem_2/fakeq2.png")
ANSQ2_PATH = os.path.join(CWD, "Game_assets/problems/problem_2/ansq2.png")

F1Q3_PATH = os.path.join(CWD, "Game_assets/problems/problem_3/fakeq3_1.png")
F2Q3_PATH = os.path.join(CWD, "Game_assets/problems/problem_3/fakeq3_2.png")
F3Q3_PATH = os.path.join(CWD, "Game_assets/problems/problem_3/fakeq3_3.png")
ANSQ3_PATH = os.path.join(CWD, "Game_assets/problems/problem_3/ansq3.png")

Q4_PATH = os.path.join(CWD, "Game_assets/problems/problem_4/Question_4.JPG")
F1Q4_PATH = os.path.join(CWD, "Game_assets/problems/problem_4/fakeq4_1.png")
F2Q4_PATH = os.path.join(CWD, "Game_assets/problems/problem_4/fakeq4_2.png")
F3Q4_PATH = os.path.join(CWD, "Game_assets/problems/problem_4/fakeq4_3.png")
F4Q4_PATH = os.path.join(CWD, "Game_assets/problems/problem_4/fakeq4_4.png")
ANSQ4_PATH = os.path.join(CWD, "Game_assets/problems/problem_4/ansq4.png")


class Dialogue():
    # --------------------Dialogue Class's Description--------------------
    # |  The Dialogue Class is responsible for handling dialogue in game,|
    # |  the (drawRECt) function draw a white area to act as a textbox in|
    # |  the game. The (loadString) function load in the dialogue of the |
    # |  boss or the player. The (divideString) divides the diagloue     |
    # |  into six words for each line. The (renderString) put string     |
    # |  on the screen.                                                  |
    # -------------------------------------------------------------------|
    offset_y = 30

    def __init__(self, X, Y, Width, Height):
        self.x = X
        self.y = Y
        self.Width = Width
        self.Height = Height
        self.string = " "
        self.left_string = []
        self.right_string = []
        self.stringList = []
        self.increment = []
        self.chunk_str_len = []
        self.load = False
        self.continue_dialogue = False

    def drawRect(self, surface):
        pygame.draw.rect(surface, WHITE, (self.x, self.y, self.Width, self.Height))

    def divideString(self):
        temp_string = " "
        index = 0
        try:
            if len(self.string) > 0:
                list_string = self.string.split()
                while True:
                    tempList = list_string[index * 6: index * 6 + 6]
                    temp_string = " ".join(tempList)
                    self.stringList.append(temp_string)
                    testList = list_string[index * 6 + 6:]
                    if len(testList) < 6:
                        temp_string = " ".join(testList)
                        self.stringList.append(temp_string)
                        break
                    index += 1
                for string in self.stringList:
                    self.chunk_str_len.append(len(string))
                    mid_string = int(len(string) / 2)
                    temp_left = string[:mid_string]
                    temp_right = string[mid_string:]
                    self.left_string.append(temp_left)
                    self.right_string.append(temp_right)
                    self.increment.append(1)
                assert self.left_string != ""
                assert self.right_string != ""
            else:
                raise ValueError
        except ValueError:
            print("Empty string, check string")
            raise SystemExit

    def renderString(self, surface):
        for i in range(len(self.left_string)):
            temp_left = self.left_string[i]
            temp_right = self.right_string[i]
            complete_string = temp_left[0:self.increment[i]] + temp_right[0:self.increment[i]]
            font = pygame.font.Font(FONT, 25)
            font_surface = font.render(complete_string, 1, BLACK)
            size = font_surface.get_size()
            fSurfaceW = size[0]
            if i == 0:
                surface.blit(font_surface, (((WIN_WIDTH - fSurfaceW) / 2), (self.y + 15)))
            else:
                surface.blit(font_surface, (((WIN_WIDTH - fSurfaceW) / 2), (self.y + (1 + i) * self.offset_y)-15))
            if len(complete_string) == self.chunk_str_len[i]:
                pass
            else:
                self.increment[i] += 1

    def loadString(self, string):
        self.string = string

    def reset(self):
        self.string = " "
        self.left_string.clear()
        self.right_string.clear()
        self.stringList.clear()
        self.increment.clear()
        self.chunk_str_len.clear()
        self.load = False


class TipBox(Dialogue):
    # --------------------TipBox Class's Description--------------------
    # |  The TipBox Class is a child of the Dialogue class, the TipBox |
    # |  add in the advisory [Press space to continue] to alert the    |
    # |  player of hitting the SpaceBar to continue the Tips in the    |
    # |  game.                                                         |
    # |----------------------------------------------------------------|
    def __init__(self, X, Y, Width, Height):
        Dialogue.__init__(self, X, Y, Width, Height)

    def renderContinueTip(self, surface):
        font = pygame.font.Font(FONT, 20)
        font_surface = font.render("[Press space to continue]", 1, BLACK)
        surface.blit(font_surface, (380, 440))  # Blit continue tip at designated position in TIPS Box


class Boss(pygame.sprite.Sprite):

    # --------------------Boss Class's Description--------------------
    # | The Boss class is responsible for the Boss's behavior, in    |
    # | case, Dr. Hossan. The (update) method updates the sprite's   |
    # | animations and movement during gameplay. the (_move_0) method|
    # | is used to update the sprite's position during the initial   |
    # | stage of descent. The (reset) method make the sprite's mouth |
    # | close. The (stopAnimation) method make the sprite to stop    |
    # | the animation of the mouth. (startAnimation) do the reverse  |
    # | (_move_play) method pick a random self.stop_points from the  |
    # | array and then assign a direction to the sprite on where to  |
    # | move (ie. left or right). The (generateAnswerpoint) also     |
    # | pick a random self_stop_points from the array and decide on  |
    # | where to drop the answer.                                    |
    # |--------------------------------------------------------------|
    def __init__(self, X, Y, Animated_List, Animated_flag=True, Talk_Dir=UP, TalkFrame=0):
        pygame.sprite.Sprite.__init__(self)
        self.Animation = Animated_List
        self.Talk_Dir = Talk_Dir
        self.TalkFrame = TalkFrame
        self.image = self.Animation[0]
        self.rect = self.image.get_rect()
        self.rect.x = X
        self.rect.y = Y
        self.Animated_flag = Animated_flag
        self.stop_points = [639, 58, 352, 283, 518]  # Stop points for Hossan movement
        self.randstopindex = None
        self.movepos = [0, 0]
        self.anspoint = None
        self.open_mouth = False
        self.drop_answer = False
        self.resetpos = False

    def update(self):
        if self.Animated_flag:
            if self.TalkFrame + 1 >= 4:  # Use to reset talk frame
                self.Talk_Dir = DOWN
                self.TalkFrame = 3

            if self.TalkFrame + 1 == 0:  # Use to reset talk frame
                self.Talk_Dir = UP
                self.TalkFrame = 0

            if self.Talk_Dir:  # Check direction of Talk UP or DOWN
                self.image = self.Animation[self.TalkFrame]
                self.TalkFrame += 1

            else:  # Check condition end here
                self.image = self.Animation[self.TalkFrame]
                self.TalkFrame -= 1

        else:
            self.rect = self.rect.move(self.movepos[0], self.movepos[1])  # update Hossan's sprite new position
            if self.anspoint:
                if self.movepos[0] < 0:
                    if self.rect.x - self.movepos[0] <= self.stop_points[self.anspoint] and self.open_mouth is False:
                        self.image = self.Animation[-1]
                        self.open_mouth = True
                        self.drop_answer = True
                    else:
                        self.reset()
                        self.drop_answer = False

                else:
                    if self.rect.x + self.movepos[0] >= self.stop_points[self.anspoint] and self.open_mouth is False:
                        self.image = self.Animation[-1]
                        self.open_mouth = True
                        self.drop_answer = True
                    else:
                        self.reset()
                        self.drop_answer = False

    def _move_0(self):  # Initial movement to descend Hossan's sprite
        self.rect.y += 5

    def reset(self):  # Reset Hossan's mouth to close
        self.image = self.Animation[0]
        self.Talk_Dir = UP
        self.TalkFrame = 0

    def resetcenterposflag(self):
        self.resetpos = False

    def setcenterposflag(self):
        self.resetpos = True

    def stopAnimation(self):  # Stop Hossan's mouth from moving
        self.Animated_flag = False

    def startAnimation(self):
        self.Animated_flag = True

    def _move_play(self, speed):  # Movement of Hossan during play
        if self.randstopindex == None:
            self.randstopindex = random.randint(0, len(self.stop_points) - 1)
        if self.rect.x < self.stop_points[self.randstopindex]:
            self.movepos[0] = speed
            if self.rect.x + speed > self.stop_points[self.randstopindex]:
                self.randstopindex = random.randint(0, len(self.stop_points) - 1)
        elif self.rect.x > self.stop_points[self.randstopindex]:
            self.movepos[0] = -speed
            if self.rect.x - speed < self.stop_points[self.randstopindex]:
                self.randstopindex = random.randint(0, len(self.stop_points) - 1)

    def generateAnswerpoint(self):  # generate answer stop point
        randindex = random.randint(0, len(self.stop_points) - 1)
        self.anspoint = randindex
        self.open_mouth = False
        self.drop_answer = False


class Answer(pygame.sprite.Sprite):
    def __init__(self, x, y, ans_bank, randansindex = None):
        pygame.sprite.Sprite.__init__(self)
        if randansindex == None:
            randansindex = random.randint(0, len(ans_bank)-1)
        if randansindex == (len(ans_bank)-1):
            self.correct = True
        else:
            self.correct = False
        self.image = ans_bank[randansindex]
        self.rect = self.image.get_rect()
        self.rect.x = x + 70
        self.rect.y = y + 88

    def update(self):
        self.rect = self.rect.move(0, 10)


class Player(pygame.sprite.Sprite):
    # --------------------Troy Class's Description--------------------
    # | The Troy class is responsible for the player's behavior      |
    # |                                                              |
    # | update method- update the sprite's animation and frame, this |
    # | method check the user input (Left or right arrow keys) and   |
    # | update the sprite's animation accordingly.                   |
    # |                                                              |
    # | moveLeft/moveRight- these two methods will be call in the    |
    # | main loop whenever the user hit the right or the left arrow  |
    # | keys. The method will update the status of the sprite and    |
    # | the animation frame in accordance with the input             |
    # |                                                              |
    # | unfreezePlayer/freezePlayer - these two methods are used to  |
    # | freeze the player in place and prevent the user from         |
    # | controlling the sprite during key moments of the game        |
    # |--------------------------------------------------------------|

    def __init__(self, X, Y, ANIMATED_LEFT, ANIMATED_RIGHT, freeze=True):
        pygame.sprite.Sprite.__init__(self)
        self.L_Animation = ANIMATED_LEFT
        self.R_Animation = ANIMATED_RIGHT
        self.image = self.L_Animation[0]
        self.rect = self.image.get_rect()
        self.rect.x = X
        self.rect.y = Y
        self.movepos = [0, 0]
        self.status = "still"  # indicate the status of the sprite
        self.leftWalk = 1  # keep track of frame walking left
        self.rightWalk = 1  # keep track of frame walking right
        self.freeze = freeze  # freeze the movement of sprite during introduction

    def update(self):
        if self.status == "left":
            if self.rect.x < -30:
                pass
            else:
                self.rect = self.rect.move(self.movepos[0], self.movepos[1])
                if self.leftWalk + 1 >= 4:
                    self.leftWalk = 1
                self.image = self.L_Animation[self.leftWalk]
                self.leftWalk += 1
        elif self.status == "right":
            if self.rect.x > WIN_WIDTH - T_IMG_RESCALE[0] + 30:
                pass
            else:
                self.rect = self.rect.move(self.movepos[0], self.movepos[1])
                if self.rightWalk + 1 >= 4:
                    self.rightWalk = 1
                self.image = self.R_Animation[self.rightWalk]
                self.rightWalk += 1
        elif self.status == "still":
            self.image = self.L_Animation[0]

    def moveLeft(self, speed):
        self.status = "left"
        self.movepos[0] = -speed

    def moveRight(self, speed):
        self.status = "right"
        self.movepos[0] = speed

    def unfreezePlayer(self):  # unfreeze Troy's sprite
        self.freeze = False

    def freezePlayer(self):  # freeze Troy's sprite
        self.freeze = True

#--------------------load_image--------------------
# this function load image and handle the error if
# the file cannot be read

def load_image(path):
    try:
        image = pygame.image.load(path)
        image.convert_alpha()
    except pygame.error:
        print("Cannot Load Image", path)
        raise SystemExit

    return image

#--------------------update_stage--------------------
# This function will be called in the main loop to
# update the stage of the game after certain key points

def update_stage(stage):
    return stage + 1

#--------------------update_skip_flag--------------------
# This function will be called in the main loop in the
# initial stage of the game. It is used to skip the
# event checking loop in the main().

def update_skip_flag(flag):
    if flag:
        return False
    else:
        return True

#--------------------hold_stage_update--------------------
# This function is a toggle. It is use to update the
# hold_stage boolean value in the main() function. If the
# value is True, the main() will not update to the next stage


def hold_stage_update(bool):
    if bool:
        return False
    else:
        return True

#--------------------troyrespond--------------------
# This function create the respond of the player whenever
# he/she gets the answer wrong. the troy_respond_bank
# is a tuple with preset respond, and a random index is
# generated to pick a random respond from the tuple

def troyrespond(troy_respond_bank, surface, index=None):
    if index == None:
        index = random.randint(0, len(troy_respond_bank) - 1)
    font = pygame.font.Font(FONT, 20)
    fSurface = font.render(troy_respond_bank[index], 1, WHITE)
    size = fSurface.get_size()
    width = size[0]
    surface.blit(fSurface, (((WIN_WIDTH - width) / 2), 550))
    return index

#--------------------hossanrespond--------------------
# This function is similar to troyrespond, EXCEPT, it only
# has one respond as opposed to a tuple of respond.

def hossanrespond(hossan_respond, surface):
    font = pygame.font.Font(FONT, 25)
    fSurface = font.render(hossan_respond, 1, WHITE)
    size = fSurface.get_size()
    width = size[0]
    surface.blit(fSurface, (((WIN_WIDTH - width) / 2), 200))

#--------------------resetPlaystage--------------------
# This function reset all the control parameters back to
# default value after the player got the right answer

def resetPlaystage():
    calc_timer = 3
    wrong_ans = False
    frame_count = 0
    wrong_ans_res_timer = 0
    in_calc_phase = True

    return calc_timer, wrong_ans, frame_count, wrong_ans_res_timer, in_calc_phase


def main():
    # loading BG, Dr.Hossan, and Troy images
    BG = load_image(BG_PATH)
    HOSSAN_STILL = load_image(HOSSAN_STILL_PATH)
    HOSSAN_TALK1 = load_image(HOSSAN_TALK1_PATH)
    HOSSAN_TALK2 = load_image(HOSSAN_TALK2_PATH)
    HOSSAN_TALK3 = load_image(HOSSAN_TALK3_PATH)
    TROY_STILL = load_image(TROY_STILL_PATH)
    TROY_LEFT1 = load_image(TROY_LEFT1_PATH)
    TROY_INTERL1 = load_image(TROY_INTER_LEFT1_PATH)
    TROY_LEFT2 = load_image(TROY_LEFT2_PATH)
    TROY_INTERL2 = load_image(TROY_INTER_LEFT2_PATH)
    TROY_RIGHT1 = load_image(TROY_RIGHT1_PATH)
    TROY_INTERR1 = load_image(TROY_INTER_RIGHT1_PATH)
    TROY_RIGHT2 = load_image(TROY_RIGHT2_PATH)
    TROY_INTERR2 = load_image(TROY_INTER_RIGHT2_PATH)

    # Scale Hossan and Troy images to approriate sizes
    S_HOSSAN_STILL = pygame.transform.scale(HOSSAN_STILL, H_IMG_RESCALE)
    S_HOSSAN_TALK1 = pygame.transform.scale(HOSSAN_TALK1, H_IMG_RESCALE)
    S_HOSSAN_TALK2 = pygame.transform.scale(HOSSAN_TALK2, H_IMG_RESCALE)
    S_HOSSAN_TALK3 = pygame.transform.scale(HOSSAN_TALK3, H_IMG_RESCALE)

    S_TROY_STILL = pygame.transform.scale(TROY_STILL, T_IMG_RESCALE)
    S_TROY_LEFT1 = pygame.transform.scale(TROY_LEFT1, T_IMG_RESCALE)
    S_TROY_INTERL1 = pygame.transform.scale(TROY_INTERL1, T_IMG_RESCALE)
    S_TROY_LEFT2 = pygame.transform.scale(TROY_LEFT2, T_IMG_RESCALE)
    S_TROY_INTERL2 = pygame.transform.scale(TROY_INTERL2, T_IMG_RESCALE)
    S_TROY_RIGHT1 = pygame.transform.scale(TROY_RIGHT1, T_IMG_RESCALE)
    S_TROY_INTERR1 = pygame.transform.scale(TROY_INTERR1, T_IMG_RESCALE)
    S_TROY_RIGHT2 = pygame.transform.scale(TROY_RIGHT2, T_IMG_RESCALE)
    S_TROY_INTERR2 = pygame.transform.scale(TROY_INTERR2, T_IMG_RESCALE)

    # load problem set 1
    Q1 = load_image(Q1_PATH)
    F1Q1 = load_image(F1Q1_PATH)
    F2Q1 = load_image(F2Q1_PATH)
    F3Q1 = load_image(F3Q1_PATH)
    F4Q1 = load_image(F4Q1_PATH)
    ANSQ1 = load_image(ANSQ1_PATH)

    # load problem set 2
    Q2 = load_image(Q2_PATH)
    F1Q2 = load_image(F1Q2_PATH)
    ANSQ2 = load_image(ANSQ2_PATH)

    # load problem set 3
    F1Q3 = load_image(F1Q3_PATH)
    F2Q3 = load_image(F2Q3_PATH)
    F3Q3 = load_image(F3Q3_PATH)
    ANSQ3 = load_image(ANSQ3_PATH)

    # load problem set 4
    Q4 = load_image(Q4_PATH)
    F1Q4 = load_image(F1Q4_PATH)
    F2Q4 = load_image(F2Q4_PATH)
    F3Q4 = load_image(F3Q4_PATH)
    F4Q4 = load_image(F4Q4_PATH)
    ANSQ4 = load_image(ANSQ4_PATH)

    # rescale problem set 1
    S_Q1 = pygame.transform.scale(Q1, Q_RESCALE)
    S_F1Q1 = pygame.transform.scale(F1Q1, ANS1_RESCALE)
    S_F2Q1 = pygame.transform.scale(F2Q1, ANS1_RESCALE)
    S_F3Q1 = pygame.transform.scale(F3Q1, ANS1_RESCALE)
    S_F4Q1 = pygame.transform.scale(F4Q1, ANS1_RESCALE)
    S_ANSQ1 = pygame.transform.scale(ANSQ1, ANS1_RESCALE)

    # rescale problem set 2
    S_Q2 = pygame.transform.scale(Q2, (400, 250))
    S_F1Q2 = pygame.transform.scale(F1Q2, ANS2_RESCALE)
    S_ANSQ2 = pygame.transform.scale(ANSQ2, ANS2_RESCALE)

    # rescale problem set 3
    S_F1Q3 = pygame.transform.scale(F1Q3, ANS2_RESCALE)
    S_F2Q3 = pygame.transform.scale(F2Q3, ANS2_RESCALE)
    S_F3Q3 = pygame.transform.scale(F3Q3, ANS2_RESCALE)
    S_ANSQ3 = pygame.transform.scale(ANSQ3, ANS2_RESCALE)

    # rescale problem set 4
    S_Q4 = pygame.transform.scale(Q4, Q_RESCALE)
    S_F1Q4 = pygame.transform.scale(F1Q4, ANS2_RESCALE)
    S_F2Q4 = pygame.transform.scale(F2Q4, ANS1_RESCALE)
    S_F3Q4 = pygame.transform.scale(F3Q4, ANS2_RESCALE)
    S_F4Q4 = pygame.transform.scale(F4Q4, ANS1_RESCALE)
    S_ANSQ4 = pygame.transform.scale(ANSQ4, ANS1_RESCALE)

    STAGE_3_ANSWERS = (S_F1Q1, S_F2Q1, S_F3Q1, S_F4Q1, S_ANSQ1)

    STAGE_4_ANSWERS= (S_F1Q2, S_ANSQ2)

    STAGE_5_ANSWERS = (S_F1Q3, S_F2Q3, S_F3Q3, S_ANSQ3)

    STAGE_6_ANSWERS = (S_F1Q4, S_F2Q4, S_F3Q4, S_F4Q4, S_ANSQ4)

    # Put Hossan's talk animation
    HOSSAN_ANIMATED = (S_HOSSAN_STILL, S_HOSSAN_TALK1, S_HOSSAN_TALK2,
                       S_HOSSAN_TALK3
                       )

    # Put Troy animation
    TROY_LEFT_ANIMATED = (S_TROY_STILL, S_TROY_LEFT1, S_TROY_INTERL1, S_TROY_LEFT2, S_TROY_INTERL2)
    TROY_RIGHT_ANIMATED = (S_TROY_STILL, S_TROY_RIGHT1, S_TROY_INTERR1, S_TROY_RIGHT2, S_TROY_INTERR2)

    # Troy's and Hossan's image height and width
    H_IMAGE_SIZE = S_HOSSAN_STILL.get_size()
    H_IMAGE_WIDTH = H_IMAGE_SIZE[0]
    H_IMAGE_HEIGHT = H_IMAGE_SIZE[1]
    T_IMAGE_SIZE = S_TROY_STILL.get_size()
    T_IMAGE_WIDTH = T_IMAGE_SIZE[0]
    T_IMAGE_HEIGHT = T_IMAGE_SIZE[1]

    # Dialogue's constant
    STAGE1_D1 = "Welcome to my domain Troy boi! I brought you here for a challenge"
    STAGE1_D2 = "Get out your calculator, it's time to Dddd-doo-doo duel!!!"
    STAGE4_D1 = "Very Gud Troy boi, that was just a warm-up. Now be ready for Tru despair!!!"
    STAGE5_D1 = "What? impossible, your intelligence!!! I did not expect this"
    STAGE5_D2 = "No! It must be luck. I cannot accept this. It defile my logic!!"
    STAGE5_D3 = "No matter! Now, the apocalypse shall truly begin"
    STAGE6_D1 = "Again?!!! Alright! I will put out my ultimate question."
    STAGE6_D2 = "I'm being extremely serious, you better have 3 calculators for the next question"
    TIPS1 = " TIPS: Oh no! You have been trapped in the interdimensional mind of Dr.Hossan!!!"
    TIPS2 = "TIPS: Dr.Hossan will challenge you with DiFfy CuLt questions, solve them to escape!"
    TIPS3 = "TIPS: He will move randomly on the screen and spit out answer"
    TIPS4 = "TIPS: Move your avatar underneath the answer using the arrow keys to pick the correct answer!!"

    H_RESPOND = "Wrong answer. Troy boi!!!"

    T_RESPOND1 = "I'm sorry Dr. Hossan, I subtracted instead of divided"
    T_RESPOND2 = "I'm sorry Dr. Hossan, I forgot to change the battery for my calculator"
    T_RESPOND3 = "I'm sorry Dr. Hossan, my breath was fogging my glass and I couldn't see the calculator"
    T_RESPOND4 = "I'm sorry Dr. Hossan, the Chick-fil-a meal make me feel really sleepy"
    T_RESPOND5 = "I'm sorry Dr. Hossan, you asked for triple integrals, but I only do 2.5 integrals"
    T_RESPOND6 = "I'm sorry Dr. Hossan, you lost me at 3 + 5 = 8"

    T_RESPOND_BANK = (T_RESPOND1, T_RESPOND2, T_RESPOND3, T_RESPOND4, T_RESPOND5, T_RESPOND6)

    # Initialize the initial position of Troy and Hossan
    Hossan_y = 0 - (10 + H_IMAGE_HEIGHT)
    Hossan_x = round((WIN_WIDTH - H_IMAGE_WIDTH) / 2)
    Troy_x = round((WIN_WIDTH - T_IMAGE_WIDTH) / 2)
    Troy_y = (WIN_HEIGHT - 10 - T_IMAGE_HEIGHT)

    # instantiate Sprites Group
    all_sprites = pygame.sprite.Group()
    ans_sprites = pygame.sprite.Group()

    # Instantiate Hossan
    Hossan = Boss(Hossan_x, Hossan_y, HOSSAN_ANIMATED)
    type(Hossan)
    logging.debug("rect of Hossan", Hossan.rect)

    # Instantiate Troy
    Troy = Player(Troy_x, Troy_y, TROY_LEFT_ANIMATED, TROY_RIGHT_ANIMATED)

    # Add to sprites group
    all_sprites.add(Hossan)
    all_sprites.add(Troy)

    # Instantiate dialogue box
    H_DBox = TipBox(H_TEXTBOX_C_X, H_TEXTBOX_C_Y, H_TEXTBOX_C_W, H_TEXTBOX_C_H)  # Hossan's dialogue's box
    T_DBox = TipBox(T_TEXTBOX_C_X, T_TEXTBOX_C_Y, T_TEXTBOX_C_W, T_TEXTBOX_C_H)  # Tips Textbox for player

    # Instantiate clock and do some BG scaling
    Clock = pygame.time.Clock()
    run = True
    BG_scale = pygame.transform.scale(BG, (750, 750))

    # Initializing the local variables
    frame_count = 0                                             # use to keep track the time pass, each drawframe() call increase this by 1
    stage = 0                                                   # track the different stages that the player progress
    dialogue_level = 1                                          # provide the dialogue control for the Boss and the TipBox
    skip_event_flag = False                                     # use to skip the check event for loop
    hold_stage = False                                          # use to indicate whether the main() should not increase the stage count
    major_frame = 0                                             # every major frame consisted of 120 frames
    player_speed = 10                                           # player movement speed
    boss_speed = 15                                             # boss movement speed
    ans_sec = 0.5                                                 # this is for Hossan to spit out answer every 1 second
    in_calc_phase = True                                        # Indicate whether the player is in calculating phase
    calc_timer = 1                                              # Timer to calculate the equation
    wrong_ans = False                                           # indicate whther wrong answer has been picked. This is used to start the wrong_ans_res_timer
    wrong_ans_res_timer = 0                                     # keep track of how long the troyrespond and the hossanrespond should stay on screen
    T_res_index = 0                                             # a return index from troyrespond. Use to indicate store the index generate from the previous troyrespond call
    incrr_ans_track = 0                                         # Keep track of how many incorrect there are, if there are more than 5, force correct answer
    incrr_threshold = 5                                         # the amount of wrong answer allow to be generate before the correct answer

    # First blit and the update
    WIN.blit(BG_scale, ORIGIN)
    pygame.display.update()

    def drawframe():
        if stage < 1:
            all_sprites.draw(WIN)
        elif stage == 1:
            if H_DBox.load is False and dialogue_level == 1:
                H_DBox.loadString(STAGE1_D1)
                H_DBox.divideString()
                H_DBox.load = True
            elif H_DBox.load is False and dialogue_level == 2:
                H_DBox.loadString(STAGE1_D2)
                H_DBox.divideString()
                H_DBox.load = True
            else:
                if frame_count < 2 * FPS:
                    H_DBox.drawRect(WIN)
                    H_DBox.renderString(WIN)
                else:
                    H_DBox.reset()
            all_sprites.update()
            all_sprites.draw(WIN)
        elif stage == 2:
            Hossan.reset()
            if T_DBox.load is False and dialogue_level == 1:
                T_DBox.loadString(TIPS1)
                T_DBox.divideString()
                T_DBox.load = True
                T_DBox.continue_dialogue = False
            elif T_DBox.load is False and dialogue_level == 2:
                T_DBox.loadString(TIPS2)
                T_DBox.divideString()
                T_DBox.load = True
                T_DBox.continue_dialogue = False
            elif T_DBox.load is False and dialogue_level == 3:
                T_DBox.loadString(TIPS3)
                T_DBox.divideString()
                T_DBox.load = True
                T_DBox.continue_dialogue = False
            elif T_DBox.load is False and dialogue_level == 4:
                T_DBox.loadString(TIPS4)
                T_DBox.divideString()
                T_DBox.load = True
                T_DBox.continue_dialogue = False
            else:
                if T_DBox.continue_dialogue:
                    T_DBox.reset()
                else:
                    T_DBox.drawRect(WIN)
                    T_DBox.renderString(WIN)
                    if frame_count > 1 * FPS:
                        T_DBox.renderContinueTip(WIN)
            all_sprites.draw(WIN)
        elif stage == 3:
            if in_calc_phase:
                font = pygame.font.Font(FONT, 25)
                font_surface = font.render("Solve The Problem", 1, WHITE)
                size = font_surface.get_size()
                fSurfaceW = size[0]
                WIN.blit(font_surface, (((WIN_WIDTH - fSurfaceW) / 2), 220))
                size = S_Q1.get_size()
                Q1_W = size[0]
                WIN.blit(S_Q1, (((WIN_WIDTH - Q1_W) / 2), 270))
                font_surface = font.render(str(calc_timer + 1), 1, WHITE)
                size = font_surface.get_size()
                fSurfaceW = size[0]
                WIN.blit(font_surface, (((WIN_WIDTH - fSurfaceW) / 2), 400))
                all_sprites.update()
                all_sprites.draw(WIN)
            else:
                Hossan._move_play(boss_speed)
                ans_sprites.update()
                ans_sprites.draw(WIN)
                all_sprites.update()
                all_sprites.draw(WIN)
        elif stage == 4:
            if Hossan.resetpos is False:
                all_sprites.draw(WIN)
            else:
                if Hossan.Animated_flag is True:
                    if H_DBox.load is False and dialogue_level == 1:
                        H_DBox.loadString(STAGE4_D1)
                        H_DBox.divideString()
                        H_DBox.load = True
                    else:
                        if frame_count < 2 * FPS:
                            H_DBox.drawRect(WIN)
                            H_DBox.renderString(WIN)
                        else:
                            H_DBox.reset()
                            Hossan.stopAnimation()
                            Troy.unfreezePlayer()
                    all_sprites.update()
                    all_sprites.draw(WIN)
                else:
                    if in_calc_phase:
                        font = pygame.font.Font(FONT, 25)
                        font_surface = font.render("Inverted or Non-Inverted Op amps Troy boi ?!", 1, WHITE)
                        size = font_surface.get_size()
                        fSurfaceW = size[0]
                        WIN.blit(font_surface, (((WIN_WIDTH - fSurfaceW) / 2), 220))
                        size = S_Q2.get_size()
                        Q2_W = size[0]
                        WIN.blit(S_Q2, (((WIN_WIDTH - Q2_W) / 2), 270))
                        font_surface = font.render(str(calc_timer + 1), 1, WHITE)
                        size = font_surface.get_size()
                        fSurfaceW = size[0]
                        WIN.blit(font_surface, (((WIN_WIDTH - fSurfaceW) / 2), 540))
                        all_sprites.update()
                        all_sprites.draw(WIN)
                    else:
                        Hossan._move_play(boss_speed)
                        ans_sprites.update()
                        ans_sprites.draw(WIN)
                        all_sprites.update()
                        all_sprites.draw(WIN)
        elif stage == 5:
            if Hossan.resetpos is False:
                all_sprites.draw(WIN)
            else:
                if Hossan.Animated_flag is True:
                    if H_DBox.load is False and dialogue_level == 1:
                        H_DBox.loadString(STAGE5_D1)
                        H_DBox.divideString()
                        H_DBox.load = True
                    elif H_DBox.load is False and dialogue_level == 2:
                        H_DBox.loadString(STAGE5_D2)
                        H_DBox.divideString()
                        H_DBox.load = True
                    elif H_DBox.load is False and dialogue_level == 3:
                        H_DBox.loadString(STAGE5_D3)
                        H_DBox.divideString()
                        H_DBox.load = True
                    else:
                        if frame_count < 2 * FPS:
                            H_DBox.drawRect(WIN)
                            H_DBox.renderString(WIN)
                        elif frame_count >= 2 * FPS and dialogue_level == 3:
                            H_DBox.reset()
                            Hossan.stopAnimation()
                            Troy.unfreezePlayer()
                        else:
                            H_DBox.reset()
                    all_sprites.update()
                    all_sprites.draw(WIN)
                else:
                    if in_calc_phase:
                        font = pygame.font.Font(FONT, 25)
                        font_surface = font.render("Which of the following year did the Celtic Boston", 1, WHITE)
                        size = font_surface.get_size()
                        fSurfaceW = size[0]
                        WIN.blit(font_surface, (((WIN_WIDTH - fSurfaceW) / 2), 250))
                        font_surface = font.render("lost the Eastern Conference Finals?", 1, WHITE)
                        size = font_surface.get_size()
                        fSurfaceW = size[0]
                        WIN.blit(font_surface, (((WIN_WIDTH-fSurfaceW)/2), 280))
                        font_surface = font.render(str(calc_timer + 1), 1, WHITE)
                        size = font_surface.get_size()
                        fSurfaceW = size[0]
                        WIN.blit(font_surface, (((WIN_WIDTH - fSurfaceW) / 2), 320))
                        all_sprites.update()
                        all_sprites.draw(WIN)
                    else:
                        Hossan._move_play(boss_speed)
                        ans_sprites.update()
                        ans_sprites.draw(WIN)
                        all_sprites.update()
                        all_sprites.draw(WIN)
        elif stage == 6:
            if Hossan.resetpos is False:
                all_sprites.draw(WIN)
            else:
                if Hossan.Animated_flag is True:
                    if H_DBox.load is False and dialogue_level == 1:
                        H_DBox.loadString(STAGE6_D1)
                        H_DBox.divideString()
                        H_DBox.load = True
                    elif H_DBox.load is False and dialogue_level == 2:
                        H_DBox.loadString(STAGE6_D2)
                        H_DBox.divideString()
                        H_DBox.load = True
                    else:
                        if frame_count < 2 * FPS:
                            H_DBox.drawRect(WIN)
                            H_DBox.renderString(WIN)
                        elif frame_count >= 2 * FPS and dialogue_level == 2:
                            H_DBox.reset()
                            Hossan.stopAnimation()
                            Troy.unfreezePlayer()
                        else:
                            H_DBox.reset()
                    all_sprites.update()
                    all_sprites.draw(WIN)
                else:
                    if in_calc_phase:
                        font = pygame.font.Font(FONT, 25)
                        font_surface = font.render("Solve the Ultimate EQUATYON!!!!", 1, WHITE)
                        size = font_surface.get_size()
                        fSurfaceW = size[0]
                        WIN.blit(font_surface, (((WIN_WIDTH - fSurfaceW) / 2), 220))
                        size = S_Q4.get_size()
                        Q4_W = size[0]
                        WIN.blit(S_Q4, (((WIN_WIDTH - Q4_W) / 2), 270))
                        font_surface = font.render(str(calc_timer + 1), 1, WHITE)
                        size = font_surface.get_size()
                        fSurfaceW = size[0]
                        WIN.blit(font_surface, (((WIN_WIDTH - fSurfaceW) / 2), 400))
                        all_sprites.update()
                        all_sprites.draw(WIN)
                    else:
                        Hossan._move_play(boss_speed)
                        ans_sprites.update()
                        ans_sprites.draw(WIN)
                        all_sprites.update()
                        all_sprites.draw(WIN)

        pygame.display.update()

    while run:
        Clock.tick(FPS)
        if Hossan.rect.y < 10:
            Hossan._move_0()
        elif hold_stage is False:
            stage = update_stage(stage)  # update to stage 1
            skip_event_flag = update_skip_flag(skip_event_flag)
            hold_stage = hold_stage_update(hold_stage)
            frame_count = 0  # reset frame counter after the first descend
        elif frame_count == 1 and major_frame == 0 and (stage - 1 == 0):
            skip_event_flag = update_skip_flag(skip_event_flag)
        elif frame_count > 2 * FPS and stage == 1:
            frame_count = 0
            if dialogue_level == 2 and major_frame == 1:
                dialogue_level = 1
                stage = update_stage(stage)  # update to stage 2
                major_frame = 0
                H_DBox.reset()
            else:
                dialogue_level += 1
                major_frame += 1
        elif stage == 3:
            if in_calc_phase:
                if frame_count >= 1 * FPS:
                    if calc_timer > 0:
                        calc_timer -= 1
                        frame_count = 0
                    else:
                        in_calc_phase = False
            else:
                if frame_count >= ans_sec * FPS:
                    frame_count = 0
                    Hossan.generateAnswerpoint()
                if Hossan.drop_answer:
                    if incrr_ans_track >= incrr_threshold:
                        ans = Answer(Hossan.rect.x, Hossan.rect.y, STAGE_3_ANSWERS, len(STAGE_3_ANSWERS)-1)
                        incrr_ans_track = 0
                        ans_sprites.add(ans)
                    else:
                        ans = Answer(Hossan.rect.x, Hossan.rect.y, STAGE_3_ANSWERS)
                        if ans.correct is False:
                            incrr_ans_track += 1
                        ans_sprites.add(ans)
                if wrong_ans and wrong_ans_res_timer == 0:
                    T_res_index = troyrespond(T_RESPOND_BANK, WIN)
                    hossanrespond(H_RESPOND, WIN)
                    wrong_ans_res_timer += 1
                elif wrong_ans and wrong_ans_res_timer >= 1:
                    troyrespond(T_RESPOND_BANK, WIN, T_res_index)
                    hossanrespond(H_RESPOND, WIN)
                    wrong_ans_res_timer += 1
                if wrong_ans_res_timer > 0.75 * FPS:
                    wrong_ans_res_timer = 0
                    wrong_ans = False
        elif stage == 4:
            if Hossan.resetpos is False:
                if Hossan.rect.x <= (WIN_WIDTH-H_IMAGE_SIZE[0])/2:
                    Hossan.rect = Hossan.rect.move(10,0)
                    if Hossan.rect.x >= (WIN_WIDTH-H_IMAGE_SIZE[0])/2:
                        Hossan.setcenterposflag()
                        Hossan.startAnimation()
                        frame_count = 0
                else:
                    Hossan.rect = Hossan.rect.move(-10, 0)
                    if Hossan.rect.x <= (WIN_WIDTH-H_IMAGE_SIZE[0])/2:
                        Hossan.setcenterposflag()
                        Hossan.startAnimation()
                        frame_count = 0
            else:
                if Hossan.Animated_flag is True:
                    pass
                else:
                    if in_calc_phase:
                        if frame_count >= 1 * FPS:
                            if calc_timer > 0:
                                calc_timer -= 1
                                frame_count = 0
                            else:
                                in_calc_phase = False
                    else:
                        if frame_count >= ans_sec * FPS:
                            frame_count = 0
                            Hossan.generateAnswerpoint()
                        if Hossan.drop_answer:
                            if incrr_ans_track >= incrr_threshold:
                                ans = Answer(Hossan.rect.x, Hossan.rect.y, STAGE_4_ANSWERS, len(STAGE_4_ANSWERS)-1)
                                incrr_ans_track = 0
                                ans_sprites.add(ans)
                            else:
                                ans = Answer(Hossan.rect.x, Hossan.rect.y, STAGE_4_ANSWERS)  # IMPLEMENTED STAGE_4 ANSWER here
                                if ans.correct is False:
                                    incrr_ans_track += 1
                                ans_sprites.add(ans)
                        if wrong_ans and wrong_ans_res_timer == 0:
                            T_res_index = troyrespond(T_RESPOND_BANK, WIN)
                            hossanrespond(H_RESPOND, WIN)
                            wrong_ans_res_timer += 1
                        elif wrong_ans and wrong_ans_res_timer >= 1:
                            troyrespond(T_RESPOND_BANK, WIN, T_res_index)
                            hossanrespond(H_RESPOND, WIN)
                            wrong_ans_res_timer += 1
                        if wrong_ans_res_timer > 0.75 * FPS:
                            wrong_ans_res_timer = 0
                            wrong_ans = False
        elif stage == 5:
            if Hossan.resetpos is False:
                if Hossan.rect.x <= (WIN_WIDTH-H_IMAGE_SIZE[0])/2:
                    Hossan.rect = Hossan.rect.move(10,0)
                    if Hossan.rect.x >= (WIN_WIDTH-H_IMAGE_SIZE[0])/2:
                        Hossan.setcenterposflag()
                        Hossan.startAnimation()
                        frame_count = 0
                else:
                    Hossan.rect = Hossan.rect.move(-10, 0)
                    if Hossan.rect.x <= (WIN_WIDTH-H_IMAGE_SIZE[0])/2:
                        Hossan.setcenterposflag()
                        Hossan.startAnimation()
                        frame_count = 0
            else:
                if Hossan.Animated_flag is True:
                    if frame_count >= 2 * FPS + 1:
                        frame_count = 0
                        dialogue_level += 1
                else:
                    if in_calc_phase:
                        if frame_count >= 1 * FPS:
                            if calc_timer > 0:
                                calc_timer -= 1
                                frame_count = 0
                            else:
                                in_calc_phase = False
                    else:
                        if frame_count >= ans_sec * FPS:
                            frame_count = 0
                            Hossan.generateAnswerpoint()
                        if Hossan.drop_answer:
                            if incrr_ans_track >= incrr_threshold:
                                ans = Answer(Hossan.rect.x, Hossan.rect.y, STAGE_5_ANSWERS, len(STAGE_5_ANSWERS)-1)
                                incrr_ans_track = 0
                                ans_sprites.add(ans)
                            else:
                                ans = Answer(Hossan.rect.x, Hossan.rect.y, STAGE_5_ANSWERS)  # IMPLEMENTED STAGE_5 ANSWER here
                                if ans.correct is False:
                                    incrr_ans_track += 1
                                ans_sprites.add(ans)
                        if wrong_ans and wrong_ans_res_timer == 0:
                            T_res_index = troyrespond(T_RESPOND_BANK, WIN)
                            hossanrespond(H_RESPOND, WIN)
                            wrong_ans_res_timer += 1
                        elif wrong_ans and wrong_ans_res_timer >= 1:
                            troyrespond(T_RESPOND_BANK, WIN, T_res_index)
                            hossanrespond(H_RESPOND, WIN)
                            wrong_ans_res_timer += 1
                        if wrong_ans_res_timer > 0.75 * FPS:
                            wrong_ans_res_timer = 0
                            wrong_ans = False

        elif stage == 6:
            if Hossan.resetpos is False:
                if Hossan.rect.x <= (WIN_WIDTH-H_IMAGE_SIZE[0])/2:
                    Hossan.rect = Hossan.rect.move(10,0)
                    if Hossan.rect.x >= (WIN_WIDTH-H_IMAGE_SIZE[0])/2:
                        Hossan.setcenterposflag()
                        Hossan.startAnimation()
                        frame_count = 0
                else:
                    Hossan.rect = Hossan.rect.move(-10, 0)
                    if Hossan.rect.x <= (WIN_WIDTH-H_IMAGE_SIZE[0])/2:
                        Hossan.setcenterposflag()
                        Hossan.startAnimation()
                        frame_count = 0
            else:
                if Hossan.Animated_flag is True:
                    if frame_count >= 2 * FPS + 1:
                        frame_count = 0
                        dialogue_level += 1
                else:
                    if in_calc_phase:
                        if frame_count >= 1 * FPS:
                            if calc_timer > 0:
                                calc_timer -= 1
                                frame_count = 0
                            else:
                                in_calc_phase = False
                    else:
                        if frame_count >= ans_sec * FPS:
                            frame_count = 0
                            Hossan.generateAnswerpoint()
                        if Hossan.drop_answer:
                            if incrr_ans_track >= incrr_threshold:
                                ans = Answer(Hossan.rect.x, Hossan.rect.y, STAGE_6_ANSWERS, len(STAGE_6_ANSWERS)-1)
                                incrr_ans_track = 0
                                ans_sprites.add(ans)
                            else:
                                ans = Answer(Hossan.rect.x, Hossan.rect.y, STAGE_6_ANSWERS)  # IMPLEMENTED STAGE_6 ANSWER here
                                if ans.correct is False:
                                    incrr_ans_track += 1
                                ans_sprites.add(ans)
                        if wrong_ans and wrong_ans_res_timer == 0:
                            T_res_index = troyrespond(T_RESPOND_BANK, WIN)
                            hossanrespond(H_RESPOND, WIN)
                            wrong_ans_res_timer += 1
                        elif wrong_ans and wrong_ans_res_timer >= 1:
                            troyrespond(T_RESPOND_BANK, WIN, T_res_index)
                            hossanrespond(H_RESPOND, WIN)
                            wrong_ans_res_timer += 1
                        if wrong_ans_res_timer > 0.75 * FPS:
                            wrong_ans_res_timer = 0
                            wrong_ans = False
        drawframe()
        frame_count += 1
        if skip_event_flag:
            continue
        else:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                if event.type == KEYUP:
                    if event.key == K_LEFT or event.key == K_RIGHT:
                        Troy.movepos = [0, 0]
                        Troy.status = "still"
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and stage == 2:
                if T_DBox.continue_dialogue is False and frame_count >= 1 * FPS:
                    T_DBox.continue_dialogue = True
                    dialogue_level += 1
                    frame_count = 0
                    if dialogue_level > 4:
                        stage = update_stage(stage)  # update to stage 3
                        Hossan.stopAnimation()
                        dialogue_level = 1
                        Troy.unfreezePlayer()
                        frame_count = 0
                        T_DBox.reset()
            if keys[pygame.K_LEFT]:
                if Troy.freeze:
                    pass
                else:
                    Troy.moveLeft(player_speed)
            if keys[pygame.K_RIGHT]:
                if Troy.freeze:
                    pass
                else:
                    Troy.moveRight(player_speed)
            player_select_list = pygame.sprite.spritecollide(Troy, ans_sprites, True)
            for choices in player_select_list:
                if choices.correct:
                    stage = update_stage(stage)             #update to stage 4 and beyond
                    ans_sprites.empty()
                    calc_timer, wrong_ans, frame_count, wrong_ans_res_timer, in_calc_phase = resetPlaystage()
                    Troy.freezePlayer()                     #freeze the player on the spot
                    Hossan.movepos[0] = 0
                    Hossan.resetcenterposflag()
                    dialogue_level = 1
                    pass
                else:
                    wrong_ans = True
                if choices.rect.y < -5:
                    ans_sprites.remove(choices)

        WIN.fill(WHITE)
        WIN.blit(BG, (0, 0))


main()

