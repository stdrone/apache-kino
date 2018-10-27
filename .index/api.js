window.MobileCheck = function() {
	var check = check == undefined ? (/.*android.*/mi).test(navigator.userAgent) : checked;
	return check;
}

function getFile(file) {
    file = file.trim();
	var dir_name = window.location.href.split("/")[4];
	if(dir_name != "") file = decodeURIComponent(dir_name);
	if(file == "Parent Directory" || file == "Name")
	{
		gFilm.get(null);
		return;
	}
	else if(file != "undefined") {
	    gFilm.get(file);
	}


}

function changeFile(file, id) {
	gFilm.change(file, id);
}

function deleteFile(file) {
    gFilm.delete(file);
}

function clearFile(file) {
    gFilm.clear(file);
}