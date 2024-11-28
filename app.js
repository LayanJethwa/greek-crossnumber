const img = document.getElementById('grids');

let toggle = true;
img.addEventListener('click', function(){
    toggle = !toggle;
    if (toggle){
        img.src = 'filled.png';
    }else{
        img.src = 'blank.png';
    }
})