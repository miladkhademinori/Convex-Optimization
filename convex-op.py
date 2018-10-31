#!/usr/bin/python
# -*- coding: utf-8 -*-
from scipy.optimize import minimize


def objective(x):
    return x[0] ** 4 / 3 + x[1] ** 2 / 2 - x[0] * x[1] + x[0] - x[1]


x0 = [1.0, 1.0]
sol = minimize(objective, x0, method='BFGS')
print sol

