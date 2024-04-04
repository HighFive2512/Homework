from project.muse_elf import MuseElf
from project.elf import Elf



muse = MuseElf("H", 4)
print(muse.username)
print(muse.level)
print(str(muse))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)