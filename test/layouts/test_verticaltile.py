# Copyright (c) 2011 Florian Mounier
# Copyright (c) 2012, 2014-2015 Tycho Andersen
# Copyright (c) 2013 Mattias Svala
# Copyright (c) 2013 Craig Barnes
# Copyright (c) 2014 ramnes
# Copyright (c) 2014 Sean Vig
# Copyright (c) 2014 Adi Sieker
# Copyright (c) 2014 Chris Wesseling
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pytest

from libqtile import layout
import libqtile.manager
import libqtile.config
from .layout_utils import assertDimensions, assertFocused, assertFocusPath
from .layout_utils import assertDimensions
from ..conftest import no_xinerama


class VerticalTileConfig(object):
    auto_fullscreen = True
    main = None
    groups = [
        libqtile.config.Group("a"),
        libqtile.config.Group("b"),
        libqtile.config.Group("c"),
        libqtile.config.Group("d")
    ]
    layouts = [
        layout.VerticalTile(columns=2)
    ]
    floating_layout = libqtile.layout.floating.Floating()
    keys = []
    mouse = []
    screens = []


verticaltile_config = lambda x: \
    no_xinerama(pytest.mark.parametrize("qtile", [VerticalTileConfig], indirect=True)(x))


@verticaltile_config
def test_verticaltile_simple(qtile):
    qtile.testWindow("one")
    assertDimensions(qtile, 0, 0, 800, 600)
    qtile.testWindow("two")
    assertDimensions(qtile, 0, 300, 798, 298)
    qtile.testWindow("three")
    assertDimensions(qtile, 0, 400, 798, 198)


@verticaltile_config
def test_verticaltile_maximize(qtile):
    qtile.testWindow("one")
    assertDimensions(qtile, 0, 0, 800, 600)
    qtile.testWindow("two")
    assertDimensions(qtile, 0, 300, 798, 298)
    # Maximize the bottom layout, taking 75% of space
    qtile.c.layout.maximize()
    assertDimensions(qtile, 0, 150, 798, 448)
