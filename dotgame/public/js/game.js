let canvas = new fabric.Canvas(document.getElementById("game"));
let eve = 0;
canvas.on('mouse:down',function(ev){
    if(ev.target != null)
        if(ev.target.get('type') === "circle")
            ev.target.animate('opacity', '0', {
                duration: 150,
                onChange: canvas.renderAll.bind(canvas),
                onComplete: function () {
                    canvas.remove(ev.target);
                }
            });
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

function addCircle(fade=false, opacity=1)
{
    let circle = new fabric.Circle({
        radius: Math.floor(Math.random() * 50)+25,
        left: Math.floor(Math.random() * 575)+50,
        top: Math.floor(Math.random() * 400)+50,
        fill: getRandomColor(),
        selectable: false,
        opacity: opacity
    });

    canvas.add(circle);
    if(fade)
        circle.animate('opacity', '1', {
            duration: 150,
            onChange: canvas.renderAll.bind(canvas),
        });

}

canvas.selection = false;

for(let i=0; i<200; i++) {
    addCircle();
}


function startLoop(){

    addCircle(true, 0);

    window.setTimeout(function(){
        startLoop();
    }, document.getElementById("hardness").value);

}


startLoop();