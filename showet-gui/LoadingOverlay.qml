import QtQuick 2.0
import QtQuick.Controls 1.4

Item {
    id: loadingOverlay

    MouseArea {
        anchors.fill: parent
    }
    Text {
        text: qsTr("Loading...")
        font.pixelSize: parent.height / 8
        color: "yellow"
        anchors {
            bottom: parent.bottom
            bottomMargin: parent.height / 8
            right: parent.right
            rightMargin: parent.width / 8
        }
        Rectangle {
            height: parent.height
            color: "yellow"
            width: height / 2
            anchors.left: parent.right
            Timer {
                repeat: true
                running: loadingOverlay.visible
                interval: 300
                onTriggered: parent.visible = !parent.visible
            }
        }
    }
    Button {
        text: qsTr("Cancel")
        onClicked: showetHelper.cancelDemo()
        anchors.right: parent.right
        anchors.bottom: parent.bottom
    }
}
