# Copyright (c) 2008, Aldo Cortesi. All rights reserved.
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
from .layout_utils import assertFocused
from ..conftest import no_xinerama


class FloatingConfig(object):
    auto_fullscreen = True
    main = None
    groups = [
        libqtile.config.Group("a"),
    ]
    layouts = [
        layout.Floating()
    ]
    floating_layout = libqtile.layout.floating.Floating()
    keys = []
    mouse = []
    screens = []
    follow_mouse_focus = False


floating_config = lambda x: \
    no_xinerama(pytest.mark.parametrize("qtile", [FloatingConfig], indirect=True)(x))


@floating_config
def test_float_next_prev_window(qtile):
    self = qtile

    # spawn three windows
    self.testWindow("one")
    self.testWindow("two")
    self.testWindow("three")

    # focus previous windows
    assertFocused(self, "three")
    self.c.group.prev_window()
    assertFocused(self, "two")
    self.c.group.prev_window()
    assertFocused(self, "one")
    # checking that it loops around properly
    self.c.group.prev_window()
    assertFocused(self, "three")

    # focus next windows
    # checking that it loops around properly
    self.c.group.next_window()
    assertFocused(self, "one")
    self.c.group.next_window()
    assertFocused(self, "two")
    self.c.group.next_window()
    assertFocused(self, "three")
