#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Floyda

import random
import os

COMMIT_TIME_PER_HOUR = 3


def run_command(cmd):
    os.system(cmd)


def push2remote():
    run_command('git push github master')
    run_command('git push coding master')


def fake_commit():
    for x in xrange(0, random.randint(0, COMMIT_TIME_PER_HOUR)):
        run_command('sh fake-commit.sh')


def main():
    fake_commit()
    push2remote()


if __name__ == '__main__':
    main()
