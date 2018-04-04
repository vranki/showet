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
    property bool busy: false
    property var searchRequest: null
    property int selectedId: 0
    onSelectedIdChanged: showetHelper.runDemo(selectedId)

    Header { id: headerBox }
    ScrollView {
        anchors.top: headerBox.bottom
        anchors.bottom: parent.bottom
        width: parent.width

        ListView {
            model: prodList
            clip: true
            delegate: ProdDelegate {}
            spacing: 10
            header: Item {width: 1; height: 10}
            BusyIndicator {
                anchors.centerIn: parent
                visible: busy
                running: busy
            }
            Rectangle {
                color: "#274f58"
                anchors.fill: parent
                z: -10
            }
        }
    }
    ListModel {
        // todo: sort by voteup
        id: prodList
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

    GaussianBlur {
        anchors.fill: parent
        source: parent
        deviation: 2
        radius: 8
        samples: 16
        visible: showetHelper.running
    }
    /*
    Text {
        text: qsTr("LOADING...")
        visible: showetHelper.running
        color: "yellow"
        font.pixelSize: 50
        anchors.right: parent.right
        anchors.rightMargin: 30
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 30
    }
    */

    function startSearch() {
        prodList.clear()
        if (!searchRequest) {
            showet.searchClicked()
        } else {
            searchRequest.abort()
            searchRequest = null
            busy = false
        }
    }

    function searchClicked() {
        var searchRequest = new XMLHttpRequest();
        var url = "http://api.pouet.net/v1/search/prod/?q=" + searchbox.text;

        busy = true
        searchRequest.onreadystatechange=function() {
            if (searchRequest.readyState === XMLHttpRequest.DONE) {
                searchResponse(searchRequest.responseText);
            }
        }
        searchRequest.open("GET", url, true);
        searchRequest.send();
    }

    function searchResponse(response) {
        var arr = JSON.parse(response);
        // console.log(response)
        if (arr["success"]) {
            for(var prodId in arr["results"]) {
                var prod = arr["results"][prodId]
                var listElement = {
                    "name": prod["name"],
                    "id": prod["id"],
                    "type": prod["type"],
                    "voteup": prod["voteup"]
                }
                if(prod["releaseDate"])
                    listElement["year"] = prod["releaseDate"].split("-")[0]

                for(var platform in prod["platforms"]) {
                    listElement["platform"] = prod["platforms"][platform]["slug"]
                    listElement["platformicon"] = prod["platforms"][platform]["icon"]
                    break
                }
                for(var group in prod["groups"]) {
                    listElement["group"] = prod["groups"][group]["name"]
                    break
                }
                prodList.append(listElement)
            }
        }
        searchRequest = null
        busy = false
    }

    function showInfo(id) {
        Qt.openUrlExternally("http://www.pouet.net/prod.php?which=" + id);
    }
}
