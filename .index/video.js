function mp_play(link) {
	document.getElementById("video_src").src = link.href;
	document.getElementById("video_container").style.visibility = "visible";
	document.getElementById("vplayer").load();
	document.getElementById("vplayer").play();
	gDiv.style = "";
	return false;
}

function mp_stop() {
	document.getElementById("video_container").style.visibility = "";
	document.getElementById("video_src").src = "";
	document.getElementById("vplayer").load();
}