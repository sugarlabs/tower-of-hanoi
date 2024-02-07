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