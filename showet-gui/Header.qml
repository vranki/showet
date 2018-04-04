import QtQuick 2.0
import QtQuick.Controls 1.4

GroupBox {
    width: parent.width
    Row {
        anchors.horizontalCenter: parent.horizontalCenter
        width: parent.width
        Image {
            source: "qrc:/../showet-logo.png"
            width: parent.width * 0.3
            height: width * 0.3
            fillMode: Image.PreserveAspectFit
            antialiasing: true
        }
        TextField {
            id: searchbox
            width: parent.width * 0.5
            placeholderText: qsTr("Pouët search")
            Keys.onReturnPressed: startSearch()
        }
        Button {
            id: searchButton
            text: !showet.busy ? qsTr("Search") : qsTr("Cancel")
            onClicked: startSearch()
        }
    }
}
