import QtQuick 2.0
import QtQuick.Controls 1.4

Item {
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
                visible: searchInProgress
                running: searchInProgress
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


    function startSearch() {
        prodList.clear()
        if (!searchRequest) {
            searchClicked()
        } else {
            searchRequest.abort()
            searchRequest = null
            searchInProgress = false
        }
    }

    function searchClicked() {
        var searchRequest = new XMLHttpRequest();
        var url = "http://api.pouet.net/v1/search/prod/?q=" + headerBox.searchText
        if(headerBox.platform.length > 1) {
            url += "&platform=" + headerBox.platform
        }
        searchInProgress = true
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
                if(headerBox.platform.length < 2 || headerBox.platform === listElement["platform"]) {
                    prodList.append(listElement)
                }
            }
        }
        searchRequest = null
        searchInProgress = false
    }
}
