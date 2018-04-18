#ifndef SHOWETHELPER_H
#define SHOWETHELPER_H

#include <QObject>
#include <QProcess>
#include <QStringList>
#include <QFile>

#define SHOWET_PY_PATH "../showet.py"

class ShowetHelper : public QObject
{
    Q_OBJECT
    Q_PROPERTY(bool running MEMBER m_running NOTIFY runningChanged)
    Q_PROPERTY(QStringList supportedPlatforms MEMBER m_supportedPlatforms NOTIFY supportedPlatformsChanged)

public:
    explicit ShowetHelper(QObject *parent = nullptr);
    Q_INVOKABLE void runDemo(const unsigned int id);
    Q_INVOKABLE void cancelDemo();
    Q_INVOKABLE void init(); // Sets up stuff

signals:
    void runError(QString errorText);
    void runningChanged(bool running);
    void supportedPlatformsChanged();

private slots:
    void processFinished(int exitCode, QProcess::ExitStatus exitStatus);
    void processErrorOccurred(QProcess::ProcessError error);
    void printRunError(QString errorText);
private:
    QProcess m_showetProcess;
    bool m_running;
    QStringList m_supportedPlatforms;
    QFile m_showetBinary;
};

#endif // SHOWETHELPER_H
