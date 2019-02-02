let canvas = new fabric.Canvas(document.getElementById("game"));
let eve = 0;
canvas.on('mouse:down',function(ev){
    if(ev.target != null)
        if(ev.target.get('type') == "circle")
            canvas.remove(ev.target);
});

let text = new fabric.Text(TEXT, {

    fill: "#333",
    fontSize: 60,
    selectable: false

});

canvas.add(text);
text.center();

function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function addCircle()
{
    let circle = new fabric.Circle({
        radius: Math.floor(Math.random() * 50)+25,
        left: Math.floor(Math.random() * 575)+50,
        top: Math.floor(Math.random() * 400)+50,
        fill: getRandomColor(),
        selectable: false
    });

    canvas.add(circle);

}

canvas.selection = false;

window.setTimeout(function () {
    for(let i=0; i<150; i++) {
        window.setTimeout(addCircle, 50);
    }
}, 500);


window.setTimeout(window.setInterval(function(){
    addCircle();
}, 500), 2000);