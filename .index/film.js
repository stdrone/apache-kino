var Film = (function() {
    var gRequest;
    const url = '/search/';

    function request(type,data) {
      //var gRequest;
      if(gRequest !== undefined && gRequest.readyState !== 4) {
        gRequest.abort();
      }
      gDiv.innerHTML = "<div><img src='https://3.bp.blogspot.com/-eeiu8xL2Qls/UQaimEebl4I/AAAAAAAAFO8/hSK_kq7C8Po/s1600/loading9.gif'></div>";
      return new Promise(function (resolve, reject) {
        gRequest = new XMLHttpRequest();
        //gRequest.timeout = 2000;
        gRequest.onreadystatechange = function(e) {
          if (gRequest.readyState === 4) {
            if (gRequest.status === 200) {
              resolve(gRequest.response)
            } else {
              reject(gRequest.status)
            }
          }
        }
        gRequest.ontimeout = function () {
          reject('timeout')
        }
        gRequest.open(type, url, true)
        var strdata = JSON.stringify(data);
        gRequest.send(strdata);
      })
    }

    async function ajax(type,params) {
        var response;
        try {
            response = await request(type, url, params);
        } catch(err) {
            return null;
        }
        return JSON.parse(response);
        if(document.getElementById("video_container").style.visibility != "visible") {
            if(response == "")
                gDiv.style = "";
            else
                gDiv.style = "display: block";
            while(gDiv.children[0] != undefined) gDiv.children[0].remove();
            var newDiv = document.createElement('div');
            newDiv.innerHTML = response;
            if(newDiv.children[0].getAttribute('name') == gLoaded) {
                gDiv.innerHTML = newDiv.innerHTML;
            }
        }
    }

    function Film() {
        this.get = function(name) {
            var data = new Object;
            data.name = name;
            return ajax('POST',data);
        }

        this.change = function(name, id) {
            var data = new Object;
            data.name = name;
            data.id = id;
            return ajax('PUT',data);
        }

        this.delete = function(name) {
            var data = new Object;
            data.name = name;
            return ajax('DELETE',data);
        }
    }

    return Film;
}());