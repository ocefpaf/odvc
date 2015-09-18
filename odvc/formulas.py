# -*- coding: utf-8 -*-

import numpy as np


def ocean_double_sigma_coordinate(sigma, depth, z1, z2, a, href, k_c):
    raise NotImplemented


def ocean_sigma_z_coordinate():
    raise NotImplemented


def ocean_sigma_coordinate(sigma, eta, depth):
    """
    Creates an ocean sigma coordinate factory with the formula:

    z(n, k, j, i) = eta(n, j, i) + sigma(k) *
                    (depth(j, i) + eta(n, j, i))

    """
    return eta + sigma * (depth + eta)


def ocean_s_coordinate(s, eta, depth, a, b, depth_c):
    """
    Creates an Ocean s-coordinate factory with the formula:

    z(n,k,j,i) = eta(n,j,i)*(1+s(k)) + depth_c*s(k) +
                    (depth(j,i)-depth_c)*C(k)

    where:
        C(k) = (1-b) * sinh(a*s(k)) / sinh(a) +
                b * [tanh(a * (s(k) + 0.5)) / (2 * tanh(0.5*a)) - 0.5]

    """
    c = ((1 - b) * np.sinh(a * s) / np.sinh(a) + b *
         (np.tanh(a * (s + 0.5)) / (2 * np.tanh(0.5 * a)) - 0.5))
    return eta * (1 + s) + depth_c * s + (depth - depth_c) * c


def ocean_s_coordinate_g1(s, eta, depth, depth_c, c):
    """
    Creates an Ocean s-coordinate, generic form 1 factory with the formula:

    z(n,k,j,i) = S(k,j,i) + eta(n,j,i) * (1 + S(k,j,i) / depth(j,i))

    where:
        S(k,j,i) = depth_c * s(k) + (depth(j,i) - depth_c) * C(k)

    """
    S = depth_c * s + (depth - depth_c) * c
    return S + eta * (1 + S / depth)


def ocean_s_coordinate_g2(s, eta, depth, depth_c, c):
    """
    Creates an Ocean s-coordinate, generic form 2 factory with the formula:

    z(n,k,j,i) = eta(n,j,i) + (eta(n,j,i) + depth(j,i)) * S(k,j,i)

    where:
        S(k,j,i) = (depth_c * s(k) + depth(j,i) * C(k)) /
                    (depth_c + depth(j,i))

    """
    S = (depth_c * s + depth * c) / (depth_c + depth)
    return eta + (eta + depth) * S
