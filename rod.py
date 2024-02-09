#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Tower Of Hanoi
# Copyright (C) 2024 Vaibhav Sangwan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Contact information:
# Vaibhav Sangwan    sangwanvaibhav02@gmail.com

from disk import Disk

class Rod:
    def __init__(self, mid, bottom):
        self.top = bottom
        self.mid = mid
        self.disks = []
    
    def putOnTop(self, disk: Disk):
        if len(self.disks) != 0 and self.disks[-1].width < disk.width:
            return False
        self.disks.append(disk)
        disk.moveAt(self.mid, self.top)
        self.top -= disk.height
        return True

    def pullFromTop(self):
        if len(self.disks) == 0:
            return None
        disk = self.disks.pop()
        self.top += disk.height
        disk.putInFocus()
        return disk