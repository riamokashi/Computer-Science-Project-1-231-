#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 18:55:11 2019

@author: riamokashi
"""

    ###########################################################

    #  Computer Project #1

    #    conversions 

    #    input rods

    #    perform conversions, arithmitic 

    #       print out converted values (meters, feet, miles, furlongs, minutes to walk) 

    ##########################################################
RODS_INPUT = input('Input rods: ')

RODS_FLOAT = float(RODS_INPUT)
RODS_STR = str(RODS_FLOAT)


METERS = ((RODS_FLOAT)*5.0292)
METERS = round(METERS, 3)
METERS = str(METERS)
FURLONGS = ((RODS_FLOAT)/40)
FURLONGS = round(FURLONGS, 3)
FURLONGS = str(FURLONGS)
MILES = (((RODS_FLOAT)*5.0292)/1609.34)
MILES = round(MILES, 3)
MILES = str(MILES)
FEET = (((RODS_FLOAT)*5.0292)/.3048)
FEET = round(FEET, 3)
FEET = str(FEET)
MINUTES_TO_WALK = ((((RODS_FLOAT*5.0292)/1609.34)/3.1)*60)
MINUTES_TO_WALK = round(MINUTES_TO_WALK, 3)
MINUTES_TO_WALK = str(MINUTES_TO_WALK)

print('You input ' + RODS_STR + ' rods.')
print(' ')
print('Conversions')
print('Meters: ' + METERS)
print('Feet: ' + FEET)
print('Miles: ' + MILES)
print('Furlongs: ' + FURLONGS)
print('Minutes to walk ' + RODS_STR + ' rods: ' + MINUTES_TO_WALK)
