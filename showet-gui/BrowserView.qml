import QtQuick 2.0
import QtWebEngine 1.5
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.2

Item {
    GroupBox {
        id: searchHeader
        width: parent.width
        height: 40
        Image {
            source: "qrc:/../showet-logo.png"
            height: parent.height
            width: parent.width * 0.3
            fillMode: Image.PreserveAspectFit
            antialiasing: true
        }
        Row {
            anchors.horizontalCenter: parent.horizontalCenter
            spacing: 10
            Button {
                text: qsTr("Home")
                onClicked: webengineView.url = "http://pouet.net"
            }
            Button {
                text: qsTr("Back")
                enabled: webengineView.canGoBack
                onClicked: webengineView.goBack()
            }
            Button {
                text: qsTr("Run")
                enabled: selectedId && !showetHelper.running
                onClicked: showetHelper.runDemo(selectedId)
            }
        }
    }
    WebEngineView {
        id: webengineView
        anchors {
            top: searchHeader.bottom
            bottom: parent.bottom
            left: parent.left
            right: parent.right
        }

        url: "http://pouet.net"
        backgroundColor: "darkgray"
        onUrlChanged: {
            var urlString = url.toString()
            if(urlString.search("prod.php") > 0) {
                var idStart = urlString.lastIndexOf("=") + 1
                var id = urlString.substring(idStart, urlString.length)
                selectedId = id
            } else {
                selectedId = 0
            }
        }
    }
}
