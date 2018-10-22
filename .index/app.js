var playerInstance;
var gDiv;
var gFilm;

window.onload = function() {
	gDiv = document.getElementById("movie");
	if(!window.MobileCheck()) {
		var l = document.links;
		for(var i=l.length - 1; i>0; i--) {
			if((/(avi|mpg|mkv|m4v|webm|mp4)$/gi).test(l[i].href)) {
				l[i].onclick = function(){ return mp_play(this); };
			}
		}
	}
	var tab = document.getElementsByClassName("indexcolname");
	for(var i = tab.length - 1; i >=0; i--) {
		tab[i].onmouseout = function() {
		//	gDiv.style = "";
		};
		tab[i].onmouseover = function() {
			getFile(this.innerText.replace(/\.[^/.]+$/, "").replace("/",""));
		};
	}

	var video_container = document.getElementById('video_container');
	video_container.onclick = mp_stop;

	gFilm = new Film();
}