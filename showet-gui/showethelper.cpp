#include "showethelper.h"
#include <QDebug>
#include <QtGlobal>

ShowetHelper::ShowetHelper(QObject *parent) : QObject(parent)
  , m_running(false)
{
    connect(&m_showetProcess, SIGNAL(finished(int, QProcess::ExitStatus)),
            this, SLOT(processFinished(int, QProcess::ExitStatus)));
    connect(this, SIGNAL(runError(QString)),
            this, SLOT(printRunError(QString)));
#if QT_VERSION < QT_VERSION_CHECK(5, 6, 0)
    connect(&showetProcess, SIGNAL(errorOccurred(QProcess::ProcessError)),
            this, SLOT(processErrorOccurred(QProcess::ProcessError)));
#endif
}

void ShowetHelper::runDemo(const unsigned int id) {
    QStringList args;
    args << QString::number(id);
    qDebug() << Q_FUNC_INFO << "Starting showet binary " << m_showetBinary.fileName() << " with args " << args << "..";
    m_running = true;
    emit runningChanged(m_running);
    m_showetProcess.start(m_showetBinary.fileName(), args);
}

void ShowetHelper::init() {
    m_showetBinary.setFileName("../showet.py"); // In dev environment
    if(!m_showetBinary.exists()) {
        m_showetBinary.setFileName("showet"); // In path, hopefully..
    }
    QProcess platformListing;
    platformListing.start(m_showetBinary.fileName(), QStringList() << "--platforms");
    platformListing.waitForFinished(3000);
    if(!platformListing.exitCode()) {
        QString out = platformListing.readAll();
        m_supportedPlatforms += "*";
        m_supportedPlatforms += out.split("\n", QString::SkipEmptyParts);
        emit supportedPlatformsChanged();
    } else {
        emit runError("Unable to list supported platforms. Showet binary missing?");
    }
}

void ShowetHelper::processFinished(int exitCode, QProcess::ExitStatus exitStatus) {
    qDebug() << Q_FUNC_INFO << "Exited with " << exitCode << exitStatus;
    m_running = false;
    emit runningChanged(m_running);

    if(exitCode != 0) {
        QString err = m_showetProcess.readAll();
        emit runError(err);
    }
}

void ShowetHelper::processErrorOccurred(QProcess::ProcessError error)
{
    Q_UNUSED(error);
    QString err = m_showetProcess.readAll();
    m_running = false;
    emit runningChanged(m_running);
    emit runError(err);
}

void ShowetHelper::printRunError(QString errorText)
{
    qWarning() << Q_FUNC_INFO << errorText;
}
