#! /usr/bin/env python
# coding: utf8


from __future__ import division
from importlib import import_module
from matplotlib import rcParams
import matplotlib.pyplot as plt
from numpy import linspace, sin, sign
from sys import argv
import warnings


rcParams['font.family'] = 'Inconsolata'
rcParams['xtick.major.pad'] = 8
rcParams['ytick.major.pad'] = 8


def plot(func_x, func_y, T, N, filename=None):
    t_interval = linspace(0, T, N)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        x = func_x(t_interval)    
        y = func_y(t_interval)    

    plt.plot(x, y, 'k')
    plt.gca().set_aspect('equal')    

    if filename != None:
        plt.title(filename)
        plt.savefig(filename+".png", format="png", transparent=True, bbox_inches='tight')
    else:
        plt.show()


def main():
    argc = len(argv)
    if argc == 1:
        print("Usage: ./animalcurve.py <filename without extension>\n")
        return -1
    if argc > 1:
        animal = argv[1]
        export = False
    if argc > 2:
        export = bool(argv[2])

    animal = argv[1]
    module = import_module(animal)

    try:
        N = module.N
    except AttributeError:
        N = 10001
    T = module.T    
    func_x = module.func_x
    func_y = module.func_y

    if export == True:
        plot(func_x, func_y, T, N, animal)
    else:
        plot(func_x, func_y, T, N)


if __name__ == "__main__":
    main()
