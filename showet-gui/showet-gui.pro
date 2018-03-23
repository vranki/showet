QT += quick
CONFIG += c++11
TARGET = showet-gui
target.path = /usr/bin

SOURCES += \
    main.cpp \
    showethelper.cpp

RESOURCES += \
    qml.qrc

DISTFILES += \
    main.qml

INSTALLS += target

HEADERS += \
    showethelper.h
