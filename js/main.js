


function selectChange(game){
  document.getElementById('selection').classList.remove('gameSelect');
  document.getElementById('selection').classList.remove('iaSelect');
  document.getElementById('selection').classList.remove('htmlSelect');
  document.getElementById('selection').classList.add(game);
  document.getElementById('menu').classList.add('hidden');
  if (game == 'gameSelect'){
    showGame();
  }else if (game == 'iaSelect'){
    showIA();
  }else{
    showHtml();
  }
}

function showGame(){
  document.getElementById('textGame').classList.remove('hidden');
  document.getElementById('textIA').classList.add('hidden');
  document.getElementById('textHtml').classList.add('hidden');
  document.getElementById('selectGame').classList.add('selected');
  document.getElementById('selectIA').classList.remove('selected');
  document.getElementById('selectHTML').classList.remove('selected');
  closeRappel()
}


function showIA(){
  document.getElementById('textGame').classList.add('hidden');
  document.getElementById('textIA').classList.remove('hidden');
  document.getElementById('textHtml').classList.add('hidden');
  document.getElementById('selectGame').classList.remove('selected');
  document.getElementById('selectIA').classList.add('selected');
  document.getElementById('selectHTML').classList.remove('selected');
  closeRappel()
}

function showHtml(){
  document.getElementById('textGame').classList.add('hidden');
  document.getElementById('textIA').classList.add('hidden');
  document.getElementById('textHtml').classList.remove('hidden');
  document.getElementById('selectGame').classList.remove('selected');
  document.getElementById('selectIA').classList.remove('selected');
  document.getElementById('selectHTML').classList.add('selected');
}

function closeRappel(){
  document.getElementById('rappel').classList.add('hidden');
}

function showRappel(){
  document.getElementById('rappel').classList.remove('hidden');
}
