TEMPLATE = subdirs
SUBDIRS = showet-gui

executable.path = /usr/bin
executable.files = showet

pymodules.path = /usr/lib/python3/dist-packages/showet
pymodules.files = *.py

INSTALLS += executable pymodules

OTHER_FILES += debian/control README.md showet-gui.desktop *.py
