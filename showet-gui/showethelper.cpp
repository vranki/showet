#include "showethelper.h"
#include <QDebug>
#include <QFile>

ShowetHelper::ShowetHelper(QObject *parent) : QObject(parent)
  , m_running(false)
{
    connect(&showetProcess, SIGNAL(finished(int, QProcess::ExitStatus)),
            this, SLOT(processFinished(int, QProcess::ExitStatus)));
    connect(&showetProcess, SIGNAL(errorOccurred(QProcess::ProcessError)),
            this, SLOT(processErrorOccurred(QProcess::ProcessError)));
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
        qDebug() << Q_FUNC_INFO << err;
        emit runError(err);
    }
}

void ShowetHelper::processErrorOccurred(QProcess::ProcessError error)
{
    QString err = showetProcess.readAll();
    qDebug() << Q_FUNC_INFO << err << error;
    m_running = false;
    emit runningChanged(m_running);
    emit runError(err);
}
