window.MobileCheck = function() {
	var check = check == undefined ? (/.*android.*/mi).test(navigator.userAgent) : checked;
	return check;
}

function getFile(file) {
	var dir_name = window.location.href.split("/")[4];
	if(dir_name != "") file = decodeURIComponent(dir_name);
	if(file == "Parent Directory" || file == "Name")
	{
		gDiv.style = "";
		return;
	}
	if(file != undefined) {
	    gFilm.get(file.trim());
	}
}

function changeFile(file) {
	var id_mov = document.getElementById("CHANGE").value;
	gFilm.change(file, id);
}
