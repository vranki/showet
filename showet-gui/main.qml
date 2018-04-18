import QtQuick 2.0
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.2
import QtQuick.Dialogs 1.2
import QtGraphicalEffects 1.0
import org.showet 1.0

ApplicationWindow {
    id: showet
    visible: true
    width: 600
    height: 400
    title: qsTr("Showet")
    property bool searchInProgress: false
    property var searchRequest: null
    property int selectedId: 0

    TabView {
        id: contentTabView
        anchors.fill: parent
        Tab {
            title: qsTr("Search")
            SearchView {
                anchors.fill: parent
            }
        }
        Tab {
            title: qsTr("Browser")
            BrowserView {
                anchors.fill: parent
            }
        }
    }

    GaussianBlur {
        anchors.fill: contentTabView
        source: contentTabView
        deviation: 2
        radius: 8
        samples: 16
        visible: showetHelper.running
    }

    LoadingOverlay {
        anchors.fill: parent
        visible: showetHelper.running
    }

    ShowetHelper {
        id: showetHelper
        onRunError: launchErrorDialog.text = errorText
    }

    Dialog {
        id: launchErrorDialog
        property alias text: errorText.text
        visible: text != ""
        title: "Launch error"
        width: 640
        height: 400
        TextArea {
            width: parent.width
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            id: errorText
            readOnly: true
        }
        standardButtons: StandardButton.Ok
        onAccepted: text = ""
    }



    function showInfo(id) {
        Qt.openUrlExternally("http://www.pouet.net/prod.php?which=" + id);
    }

    Component.onCompleted: showetHelper.init()
}
