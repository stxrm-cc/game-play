const imgArray = new Array();

function defImg(){
for (let i = 0; i < 99; i++){
  imgArray[i] = new Image();
  imgArray[i].src = ("../img/chocci/chocci copy ", i , ".png");
  document.write(imgArray[i]);
};
}

defImg();
