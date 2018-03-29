#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QQmlEngine>
#include "showethelper.h"

int main(int argc, char *argv[])
{
#if defined(Q_OS_WIN)
    QCoreApplication::setAttribute(Qt::AA_EnableHighDpiScaling);
#endif
    QGuiApplication app(argc, argv);
    QCoreApplication::setOrganizationName("Showet");
    QCoreApplication::setApplicationName("Showet");
    QQmlApplicationEngine engine;
    qmlRegisterType<ShowetHelper>("org.showet", 1, 0, "ShowetHelper");
    engine.load(QUrl(QStringLiteral("qrc:/main.qml")));
    if (engine.rootObjects().isEmpty())
        return -1;

    return app.exec();
}
