QT += quick webengine
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
    ProdDelegate.qml \
    SearchView.qml \
    Header.qml \
    BrowserView.qml \
    LoadingOverlay.qml

desktop.path = /usr/share/applications/
desktop.files = showet-gui.desktop

icon.path = /usr/share/pixmaps/
icon.files = ../showet.svg

INSTALLS += target desktop icon

HEADERS += \
    showethelper.h
