#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: fenc=utf-8 ts=4 sw=4 et


import sys
import kociemba
import argparse
from video import webcam
from normalizer import normalize


class Qbr:

    def __init__(self, normalize, language):
        self.humanize = normalize
        self.language = (language[0]) if isinstance(language, list) else language

    def run(self):
        print('SCANNING GUIDE')
        print('Make sure to scan the cube correctly by having the white-centered side on top when starting.')
        print('')
        print('Make sure to scan the cube using the following order')
        print('- Scan the green-centered side')
        print('- Scan the orange-centered side')
        print('- Scan the blue-centered side')
        print('- Scan the red-centered side')
        print('')
        print('Now, make sure to rotate the cube back to the green-centered side.')
        print('')
        print('- Turn the cube down and scan the white-centered side (green on bottom, white in front)')
        print('- Turn the cube 180 degrees back and scan the last yellow-centered side (green on top, yellow in front)')
        print('')

        state = webcam.scan()
        if not state:
            print('\033[0;33m[QBR SCAN ERROR] Ops, you did not scan in all 6 sides correctly')
            print('Please try again.\033[0m')
            sys.exit(1)

        try:
            algorithm = kociemba.solve(state)
            length = len(algorithm.split(' '))
        except Exception as err:
            print('\033[0;33m[QBR SCAN ERROR] Ops, you did not scan in all 6 sides correctly')
            print('Please try again.\033[0m')
            sys.exit(1)

        print('Starting position:\nfront: green\ntop: white\n')
        print('Moves: {}'.format(length))
        print('Solution: {}'.format(algorithm))

        if self.humanize:
            manual = normalize.algorithm(algorithm, self.language)
            for index, text in enumerate(manual):
                print('{}. {}'.format(index+1, text))


if __name__ == '__main__':
    # Define argument parser.
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--normalize', default=False, action='store_true',
            help='Shows the solution normalized. For example "R2" would be: \
                    "Turn the right side 180 degrees".')
    parser.add_argument('-l', '--language', nargs=1, default='en',
            help='You can pass in a single \
                    argument which will be the language for the normalization output. \
                    Default is "en".')
    args = parser.parse_args()

    # Run Qbr with its arguments.
    Qbr(args.normalize, args.language).run()