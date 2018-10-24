var Film = (function() {
    var gRequest;
    const url = 'http://127.0.0.1:8000/app/';

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
              resolve(JSON.parse(gRequest.response))
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

    function Film(movie) {
        this.get = async function(name) {
            var data = new Object;
            data.name = name;
            data = await request('POST',data);
        }

        this.change = async function(name, id) {
            var data = new Object;
            data.name = name;
            data.id = id;
            request('PUT',data);
        }

        this.delete = async function(name) {
            var data = new Object;
            data.name = name;
            request('DELETE',data);
        }
    }

    return Film;
}());