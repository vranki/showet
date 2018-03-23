TEMPLATE = subdirs
SUBDIRS = showet-gui

support.path = /usr/bin
support.files = showet.py

INSTALLS += support

OTHER_FILES += debian/control
