var Movie = (function() {

    var _loading, _list, _listTable, _movie, _clear;

    function getImage(id) {
        var child = document.createElement('div');
        var img = document.createElement('img');
        img.src = 'https://st.kp.yandex.net/images/sm_film/' + id + '.jpg';
        child.append(img);
        return child;
    }

    function listMovie(name, movie) {
        var div = document.createElement('div');
        div.append(getImage(movie[0]));
        child = document.createElement('div');
        child.innerHTML = movie[2] + ' (' + movie[3] + ')';
        div.append(child);

        div.onclick = function() {
            changeFile(name, movie[0]);
        };

        return div;
    }

    function Movie(div) {

        _loading = div.querySelector('#loading');
        _list = div.querySelector('#list');
        _listTable = _list.querySelector('#listTable');
        _loading = div.querySelector('#info');
        _clear = div.querySelector('#clear');

        this.setLoading = function() {
            div.classList.remove('list');
            div.classList.remove('info');
            div.classList.add('visible');
            div.classList.add('loading');
        }

        this.setList = function(name, list) {
            while (_listTable.firstChild) _listTable.removeChild(_listTable.firstChild);
            for (var key in list) {
              _listTable.append(listMovie(name, list[key]));
            };
            _list.querySelector('#filmName').innerHTML = name;
            _list.querySelector('#filmName').parentNode.href = 'https://www.kinopoisk.ru/index.php?first=no&what=&kp_query=' + encodeURI(name);

            _list.querySelector('#change').onclick = function() {
                var newId = _list.querySelector('#newId').value;
                _list.querySelector('#newId').value = null;
                changeFile(name, newId);
                return false;
            }

            div.classList.remove('loading');
            div.classList.add('list');
        }

        this.setMovie = function(movie) {
            div.querySelector('#name').innerHTML = movie.name;
            div.querySelector('#rate').innerHTML = movie.rate;
            div.querySelector('#rating').innerHTML = movie.rating;
            div.querySelector('#description').innerHTML = movie.description;
            div.querySelector('#img').src = 'https://st.kp.yandex.net/images/film_iphone/iphone360_' + movie.id + '.jpg';
            div.querySelector('#ref').href = 'https://www.kinopoisk.ru/film/' + movie.id;

            var progress = div.querySelector('#progress');
            if(movie.progress != undefined && movie.progress < 100) {
                progress.classList.add('inprogress');
                progress.querySelector('div').style.width = movie.progress + '%';
            } else {
                progress.classList.remove('inprogress');
            }

            var genre = div.querySelector('#genre');
            while (genre.firstChild) genre.removeChild(genre.firstChild);
            for (var key in movie.genre) {
                var li = document.createElement('li');
                li.innerHTML = movie.genre[key];
                genre.appendChild(li);
            };

            _clear.querySelector('#clearFilm').onclick = function() {
                clearFile(movie.file);
            };
            _clear.querySelector('#deleteFilm').onclick = function() {
                deleteFile(movie.file);
            };

            div.classList.remove('loading');
            div.classList.add('info');
        }

        this.hide = function() {
            div.classList.remove('visible');
        }
    }

    return Movie;
}());