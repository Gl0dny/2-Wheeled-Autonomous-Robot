#!/usr/bin/python3
from pid_controller import PIController
from robot import Robot, EncoderCounter
import time
import logging

logger = logging.getLogger("drive_distance")

def drive_distance(bot, distance, speed=80):
    set_primary_motor = bot.set_left
    primary_encoder = bot.left_encoder
    set_secondary_motor = bot.set_right
    secondary_encoder = bot.right_encoder

    controller = PIController(proportional_constant=4, integral_constant=0.3)
    set_primary_motor(speed)
    set_secondary_motor(speed)

    while primary_encoder.pulse_count < distance or secondary_encoder.pulse_coutn < distance:
        time.sleep(0.01)
        error = primary_encoder.pulse_count - secondary_encoder.pulse_count
        adjustment = controller.get_value(error)