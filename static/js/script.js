function pointerOn(hub) {
    hub = hub.toLowerCase() + "Pic";
    var result = "/assets/" + hub +"Hover.png";
    document.getElementById(hub).src = result
}
function pointerOut(hub) {
    var result = "/assets/" + hub;
    document.getElementById("gamingPic").src = result;
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
