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
    main.qml \
    ProdDelegate.qml

desktop.path = /usr/share/applications/
desktop.files = showet-gui.desktop

INSTALLS += target desktop

HEADERS += \
    showethelper.h
