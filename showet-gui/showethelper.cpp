#include "showethelper.h"
#include <QDebug>
#include <QFile>
#include <QtGlobal>

ShowetHelper::ShowetHelper(QObject *parent) : QObject(parent)
  , m_running(false)
{
    connect(&showetProcess, SIGNAL(finished(int, QProcess::ExitStatus)),
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
    QFile showetFile("../showet.py"); // In dev environment
    if(!showetFile.exists()) {
        showetFile.setFileName("showet"); // In path
    }
    if(showetFile.exists()) {
        qDebug() << Q_FUNC_INFO << "Starting showet binary " << showetFile.fileName() << " with args " << args << "..";
        showetProcess.start(showetFile.fileName(), args);
        m_running = true;
        emit runningChanged(m_running);
    } else {
        emit runError("Can't find showet.py to run!");
    }
}

void ShowetHelper::processFinished(int exitCode, QProcess::ExitStatus exitStatus)
{
    qDebug() << Q_FUNC_INFO << "Exited with " << exitCode << exitStatus;
    m_running = false;
    emit runningChanged(m_running);

    if(exitCode != 0) {
        QString err = showetProcess.readAll();
        emit runError(err);
    }
}

void ShowetHelper::processErrorOccurred(QProcess::ProcessError error)
{
    Q_UNUSED(error);
    QString err = showetProcess.readAll();
    m_running = false;
    emit runningChanged(m_running);
    emit runError(err);
}

void ShowetHelper::printRunError(QString errorText)
{
    qWarning() << Q_FUNC_INFO << errorText;
}
