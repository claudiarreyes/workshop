#! /usr/bin/env python
"""
# Determine Andromeda location in ra/dec degrees
"""

def clip_to_radius()
pass


def generate_sky_pos():
    # from wikipedia
    RA = '00:42:44.3'
    DEC = '41:16:09'

    # convert to decimal degrees
    from math import cos, pi

    d, m, s = DEC.split(':')
    DEC = int(d)+int(m)/60+float(s)/3600

    h, m, s = RA.split(':')
    RA = 15*(int(h)+int(m)/60+float(s)/3600)
    RA = RA/cos(DEC*pi/180)

    NSRC = 1_000_000

    # make 1000 stars within 1 degree of Andromeda
    from random import uniform

    ras = []
    decs = []
    for i in range(NSRC):
        ras.append(RA + uniform(-1,1))
        decs.append(DEC + uniform(-1,1))


    # now write these to a csv file for use by my other program
    with open('./catalog.csv','w') as f:
        print("id,ra,dec", file=f)
        for i in range(NSRC):
            print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)