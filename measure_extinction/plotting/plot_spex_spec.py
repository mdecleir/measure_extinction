#!/usr/bin/env python

from __future__ import absolute_import, division, print_function, unicode_literals

from measure_extinction.plotting.plot_spec import plot_multi_spectra


def plot_comp_spectra():
    # define the path and the names of the comparison stars (first the main sequence stars and then the giant stars, sorted by spectral type from B9 to O0)
    path = "/Users/mdecleir/Documents/NIR_ext/Data/"
    stars = [
        "HD034759",
        "HD032630",
        "HD042560",
        "HD031726",
        "HD003360",
        "HD034816",
        "HD036512",
        "HD214680",
        "HD047839",
        "HD164794",
        "HD078316",
        "HD051283",
        "HD091316",
        "HD204172",
        "HD188209",
    ]

    # plot the spectra
    plot_multi_spectra(
        stars,
        path,
        mlam4=True,
        range=[0.75, 6],
        norm_range=[1, 1.1],
        spread=True,
        pdf=True,
        outname="comp_stars.pdf",
    )


if __name__ == "__main__":
    plot_comp_spectra()
