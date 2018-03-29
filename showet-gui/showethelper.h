#ifndef SHOWETHELPER_H
#define SHOWETHELPER_H

#include <QObject>
#include <QProcess>

#define SHOWET_PY_PATH "../showet.py"

class ShowetHelper : public QObject
{
    Q_OBJECT
    Q_PROPERTY(bool running MEMBER m_running NOTIFY runningChanged)
public:
    explicit ShowetHelper(QObject *parent = nullptr);
    Q_INVOKABLE void runDemo(const unsigned int id);

signals:
    void runError(QString errorText);
    void runningChanged(bool running);

public slots:

private slots:
    void processFinished(int exitCode, QProcess::ExitStatus exitStatus);
    void processErrorOccurred(QProcess::ProcessError error);
    void printRunError(QString errorText);
private:
    QProcess showetProcess;
    bool m_running;
};

#endif // SHOWETHELPER_H
