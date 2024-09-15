import pygame
import time
import sys

def get_joystick_values(joystick):

    axis0 = round(joystick.get_axis(0), 1) * -1
    axis1 = round(joystick.get_axis(1), 1) * -1
    axis2 = round(joystick.get_axis(2), 1) * -1
    axis3 = round(joystick.get_axis(3), 1) * -1
    btn_a_is_pressed = joystick.get_button(0)
    btn_b_is_pressed = joystick.get_button(1)

    return {
        "Axis 0": axis0,
        "Axis 1": axis1,
        "Axis 2": axis2,
        "Axis 3": axis3,
        "a": btn_a_is_pressed,
        "b": btn_b_is_pressed,
    }

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    running = True


    while running:
        pygame.event.pump()
        print (get_joystick_values(joystick=joystick))
        time.sleep(0.01)

        event = pygame.event.wait()
        print (event)
        if event.type == pygame.QUIT:
            running = False  # Be IDLE friendly

    joystick.quit()
    pygame.display.quit()
    pygame.quit()

    sys.exit()
