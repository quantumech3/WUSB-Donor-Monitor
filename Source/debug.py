# -*- coding: utf-8 -*-
'''
Created by Scott Burgert on 2/20/2019
Project name: WUSB Donor Monitor ©

Module name: debug.py
Module description:
        Has methods used by different modules to log events and warnings.
        These logs only show when 'VERBOSE' = True
'''

# Hard coded constant. if true, status, log and warning messages will show in console
VERBOSE = True


def success(msg):
    '''
    Prints value of ‘msg’ in green if VERBOSE = True
    :param msg:
    :return:
    '''
    if VERBOSE:
        # Print green message
        print("\u001b[32m" + "SUCCESS[]: " + msg + "\u001b[0m")


def warn(msg):
    '''
    Prints value of ‘msg’ in yellow if VERBOSE = True
    :param msg:
    :return:
    '''
    if VERBOSE:
        # Print yellow message
        print("\u001b[33m" + "WARN[]: " + msg + "\u001b[0m")


def err(msg):
    '''
    Prints ‘msg’ in red regardless of VERBOSE value
    :param msg:
    :return:
    '''
    # Print red message
    print("\u001b[31m" + "ERROR[]: " + msg + "\u001b[0m")


def log(msg):
    '''
    Prints error message in grey if VERBOSE = True
    :param msg:
    :return:
    '''

    if VERBOSE:
        print('LOG[]: ' + msg)