// Rappel: list -> array []
// Rappel: javascript pue la merde
// Rappel: ce n'est pas pire que java

let t = true;
let f = false;

function resetGrid(x_size, y_size) {
  const gridReset = [];
  for (let i = 0; i < y_size; i++) {
    const x_liste = [];
    for (let j = 0; j < x_size, j++) {
      x_liste += [1];
    gridReset += [x_liste];
    }
  }
  return gridReset;
}

function NombrePosition(gridTest){
  let nombre = 0;
  for (let i = 0; i < gridTest.length; i++) {
    const entre = gridTest[i];
    for (let j = 0; j < entre.length; j++) {
      if (entre[j] == 1) {
        nombre += 1;
      }
    }
  }
  return nombre;
}

function Remplace(x, y, gridModifie){
  // Remplace a droite de la position jouer en (x;y)
  const save = gridModifie[y-1];
  for (let i = 0; i < save.length; i++){
    if (i+1 >= x){
      save[i] = 0;
    }
  }
  gridModifie[y-1] = save;

  // Remplace en bas de la position jouer en (x;y)
  for (let i = 0; i < y; i++){
    save = gridModifie[i];
    save[x-1] = 0;
    gridModifie[i] = save;
  }
  return gridModifie
}

function Contient(gridTest) {
  // Verifie que la liste gridTest contient une cases non occupee
  if (NombrePosition(gridTest) == 0){
    return f;
  }
  return t;
}

function VerifInput(char, maxi){
  // Preconditions
  if (typeof 'char' !== "string"){
    return t;
  }
  // Verification si char est une entree acceptable ou pas
  const charPossible = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"];
  for (let i = 0 in char){
    let valid = false;
    for (let j = 0 in charPossible){
      if (j == 1){
        valid = true;
      }
    }
    if (valid == false){
      return t;
    }
    // evite que l'input 0 soit renvoye alors qu'il n'est pas valide
    // alors que 10 et 20 le sont
  }
  if (parseInt(char) == 0){
    return t;
  }
  // evite de jouer en dehors du plateau
  if (parseInt(char) > maxi){
    return t;
  }
  return f;
}

function Possible(x, y, grid){
  if (VerifInput(x, grid[0].length) || VerifInput(y, grid.length)){
    return t;
  }
  let x = parseInt(x);
  let y = parseInt(y);
  const entre = grid[y-1];
  if (entre[x-1] == 1){
    return f;
  }
  return t;
}

function MontreJeu(grid){
  for (let i = 0; i < grid.length; i++){
    // affiche la valeur de chaque element de l'array
    document.write(grid[((grid.length)-i)-1]);
  }
}

/* --------------- Ici commence le developpement de la IA --------------- */

function IA_aleatoire(grid){
  // Recupere toutes les possibilites de jouer et les mets dans la const "pos"
  const pos = [];
  for (let i = 0; i < grid.length; i++){
    const entre = grid[i];
    for (let j = 0; j < entre.length; i++){
      if (entre[j] == 1){
        pos += [[j+1, i+1]];
      }
    }
  }
// Prend aleatoirement une position a jouer dans "pos"
  const MAX = pos.length;
  const initialRandom = Math.random();
  const multiplied = initialRandom * MAX;
  const finalRand = Math.floor(multiplied);

  const rando = pos[Array.from(Array(finalRand).keys())];

  let x = rando[0];
  let y = rando[1];
  return Remplace(x,y, grid);
}

function Eval(EVALUATION){
  const newPosition = [];
  for (let loop1 = 0; loop1 < EVALUATION.length; loop1++){
    const EVALX = EVALUATION[loop1];
    for (let loop2 = 0; loop2 < EVALX.length; loop2++){
      if (EVALX[loop2] != 0){
        const add = [[loop2+1, loop1+1]] + [Remplace(loop2+1,loop1+1,Evaluation)];
        newPosition += add;
      }
    }
  }
  document.write(newPosition);
  return newPosition;
}

function IA_EvaluPossibilite(gridEval){
  const SCORE_EVAL = [];
  const TOUR1 = Eval(gridEval);
  for (let toure1 = 0; toure1 < parseInt((TOUR1.length)/2); toure1++){
    var SCORE = 0;
    if (Contient(TOUR1[(toure1*2)+1])){
      if (NombrePosition)
    }
  }
}
