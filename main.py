#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.8.0')

from tour.tourapp import TourApp
from tour.sidebarlabel import SideBarLabel


if __name__ in ('__main__', '__android__'):
    TourApp().run()
