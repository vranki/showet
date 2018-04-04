import QtQuick 2.0
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.2

GroupBox {
    property alias searchText: searchbox.text
    property alias platform: platformCombo.currentText
    width: parent.width

    Row {
        anchors.horizontalCenter: parent.horizontalCenter
        Image {
            source: "qrc:/../showet-logo.png"
            anchors.bottom: parent.bottom
            width: parent.width * 0.3
            fillMode: Image.PreserveAspectFit
            antialiasing: true
        }
        GridLayout {
            columns: 2
            Layout.fillWidth: true
            TextField {
                id: searchbox
                Layout.fillWidth: true
                Layout.preferredWidth: 200
                placeholderText: qsTr("Pouët search")
                Keys.onReturnPressed: startSearch()
            }
            Button {
                id: searchButton
                text: !showet.busy ? qsTr("Search") : qsTr("Cancel")
                onClicked: startSearch()
            }
            Text {
                text: qsTr("Platform")
            }
            ComboBox {
                id: platformCombo
                model: showetHelper.supportedPlatforms
                Layout.preferredWidth: 120
            }
        }
    }
}
