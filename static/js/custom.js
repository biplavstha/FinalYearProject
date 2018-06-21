/**
 * Created by garne on 6/20/2018.
 */

function validateAudioFormat(fileName){
    var idxDot = fileName.lastIndexOf(".") + 1;
    var extFile = fileName.substr(idxDot, fileName.length).toLowerCase();
    if (extFile==="wav"){
        return true;
    }else{
        return false;
    }
}

function validateUploadAudio() {
    var inputAudio = document.getElementById('inputfile').value.trim();
    if(checkEmpty("Upload Audio",inputfile)) return false;
    if(!validateAudioFormat(inputfile)){
        notify("error","Audio Format must be wav");
        return false;
    }else{
        return true;
    }
}
