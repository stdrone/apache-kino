var playerInstance;
var gFilm;

window.onload = function () {
	const cIndexList = "indexlist";
	const cMovie = "movie";

	gDiv = document.getElementById("movie");
	if (!window.MobileCheck()) {
		var l = document.links;
		for (var i = l.length - 1; i > 0; i--) {
			if ((/(avi|mpg|mkv|m4v|webm|mp4)$/gi).test(l[i].href)) {
				l[i].onclick = function () { return mp_play(this); };
			}
		}
		document.getElementById(cIndexList).classList.add("desktop");
		document.getElementById(cMovie).classList.add("desktop");
	} else {
		document.getElementById(cIndexList).classList.add("mobile");
		document.getElementById(cMovie).classList.add("mobile");
	}
	var tab = document.getElementsByClassName("indexcolname");
	for (var i = tab.length - 1; i >= 0; i--) {
		tab[i].onmouseover = function () {
			getFile(this.innerText.replace(/\.[^/.]+$/, "").replace("/", ""));
		};
		var aref = tab[i].children[0];
		if(aref != undefined && aref.tagName == "A") {
			aref.onfocus = function () {
				getFile(this.innerText.replace(/\.[^/.]+$/, "").replace("/", ""));
			};
		}
	}

	var video_container = document.getElementById('video_container');
	video_container.onclick = mp_stop;

	gFilm = new Film(new Movie(document.getElementById(cMovie)));

	function focusNext(forward) {
		var focused = document.activeElement;
		if (focused.tagName != "A") {
			focused = document.getElementById(cIndexList).getElementsByTagName("A")[0];
			if (focused != undefined) {
				focused.focus();
			}
		} else {
			while (focused.tagName != "TR") focused = focused.parentElement;
			if (forward) {
				focused = focused.nextElementSibling;
			} else {
				focused = focused.previousElementSibling;
			}
			focused = focused.getElementsByTagName("A")[0];
			if (focused != undefined) {
				focused.focus();
			}
		}
	}

	document.addEventListener('keyup',
		function (event) {
			event = event || window.event;
			if (event.keyCode == '38') {
				focusNext(false);
				event.preventDefault();
				return false;
			} else if (event.keyCode == '40') {
				focusNext(true);
				event.preventDefault();
				return false;
			} else if (event.keyCode == '8') {
				var aTags = document.getElementsByTagName("a");
				for (var i = 0; i < aTags.length; i++) {
					if (aTags[i].textContent == "Parent Directory") {
						aTags[i].click();
						break;
					}
				}
			}
			return true;
		}
	);
}