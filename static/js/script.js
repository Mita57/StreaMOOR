function gamingOn() {
    document.getElementById("gamingPic").src = "assets/gamingHubHover.png"
}
function gamingOut() {
    document.getElementById("gamingPic").src = "assets/gamingHub.png"
}

function creativeOn() {
    document.getElementById("creativePic").src = "assets/creativeHubHover.png"
}
function creativeOut() {
    document.getElementById("creativePic").src = "assets/creativeHub.png"
}

function podcastsOn() {
    document.getElementById("podcastPic").src = "assets/podcastsHubHover.png"
}
function podcastsOut() {
    document.getElementById("podcastPic").src = "assets/podcastsHub.png"
}

function sciOn() {
    document.getElementById("sciPic").src = "assets/sciHubHover.png"
}
function sciOut() {
    document.getElementById("sciPic").src = "assets/sciHub.png"
}

function irlOn() {
    document.getElementById("irlPic").src = "assets/irlHubHover.png"
}
function irlOut() {
    document.getElementById("irlPic").src = "assets/irlHub.png"
}

function etcOn() {
    document.getElementById("etcPic").src = "assets/etcHubHover.png"
}
function etcOut() {
    document.getElementById("etcPic").src = "assets/etcHub.png"
}
function chatMock(){
    var i = 0;
    vars = ['<li class="list-group-item"><p><span class="chat_user">outism:</span>А А АА А А АА А А А ААА</p></li>',
        '<li class="list-group-item"><p><span class="chat_user">RemoveKebab:</span>А А АА А А АА А А А ААА</p></li>',
        '<li class="list-group-item"><p><span class="chat_user">CheckMother:</span>А А АА А А АА А А А ААА</p></li>',
        '<li class="list-group-item"><p><span class="chat_user">SIAKOD:</span>ЛУЛУУЛУЛУЛУЛ АА</p></li>'];
    setInterval(function(){
        document.getElementById("chattik").innerHTML+=vars[i%4];
        i++;
    },1000)
}
