import QtQuick 2.0
import QtQuick.Controls 1.4
Row {
    id: prodRow
    anchors.left: parent.left
    anchors.leftMargin: 20
    anchors.right: parent.right
    anchors.rightMargin: 20
    spacing: 10
    Image {
        source: "http://content.pouet.net/gfx/os/" + platformicon
        width: height
        height: parent.height * 0.9
        fillMode: Image.PreserveAspectFit
    }
    Button {
        id: runButton
        text: "Run"
        enabled: !showetHelper.running
        onClicked:  {
            selectedId = id
            showetHelper.runDemo(selectedId)
        }
    }
    Button {
        text: "Nfo"
        onClicked: showInfo(id)
    }
    Text {
        color: "white"
        text: group + ": " + name
        height: runButton.height
        font.pixelSize: height / 2
        Text {
            color: "lightgray"
            text: type + ", " + year
            height: runButton.height
            font.pixelSize: height / 3
            verticalAlignment: Text.AlignBottom
        }
    }
}
