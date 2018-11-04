var Film = (function() {
    var gRequest;
    const url = '/app/';

    function request(type,data) {
      //var gRequest;
      if(gRequest !== undefined && gRequest.readyState !== 4) {
        gRequest.abort();
      }
      //gDiv.innerHTML = "<div><img src='https://3.bp.blogspot.com/-eeiu8xL2Qls/UQaimEebl4I/AAAAAAAAFO8/hSK_kq7C8Po/s1600/loading9.gif'></div>";
      return new Promise(function (resolve, reject) {
        gRequest = new XMLHttpRequest();
        //gRequest.timeout = 2000;
        gRequest.onreadystatechange = function(e) {
          if (gRequest.readyState === 4) {
            if (gRequest.status === 200) {
              data = JSON.parse(gRequest.response)
              resolve(data)
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

        async function _delete(name, withFile) {
            movie.setLoading();
            var data = new Object;
            data.name = name;
            data.file = withFile;
            try {
                movie.setLoading();
                data = await request('DELETE',data);
                if(data.delete == true) {
                    window.location = window.location;
                }
                movie.hide();
            } catch(err) {
                console.log(err);
            }
        }

        this.get = async function(name) {
            if(name == null) {
                movie.hide();
            } else {
                movie.setLoading();
                var data = new Object;
                data.name = name;
                try {
                    data = await request('POST',data);
                    if(data.list !== undefined)
                        movie.setList(name, data.list);
                    else if(data.movie == undefined && data.movie == null)
                        movie.hide();
                    else {
                        data.movie.file = name;
                        movie.setMovie(data.movie)
                    }
                } catch(err) {
                    console.log(err);
                }
            }
        }

        this.change = async function(name, id) {
            movie.setLoading();
            var data = new Object;
            data.name = name;
            data.id = id;
            try {
                data = await request('PUT',data);
                 if(data.movie == undefined && data.movie == null)
                    movie.hide();
                 else {
                    data.movie.file = name;
                    movie.setMovie(data.movie)
                 }
            } catch(err) {
                console.log(err);
            }
        }

        this.clear = function(name) {
            _delete(name, false);
            movie.get(name);
        }

        this.delete = function(name) {
            _delete(name, true);
        }
    }

    return Film;
}());