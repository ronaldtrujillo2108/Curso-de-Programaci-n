const othersOp = document.getElementById("othersOp");
const numbers = document.getElementById("numbers");
const display = document.getElementById("display");
let lastAnswer = "";

const OTHERS_OP = [
  "X", "Calc", "", "", "Pi", "x³", "ab",
  "√", "x²", "^", "log", "In",
  "(-)", ".,,,", "hyp", "sin", "cos",
  "tan", "Rc1", "Eng", "(", ")", ",", "m+"
];

const NUMBERS = [
  "7", "8", "9", "DEL", "AC",
  "4", "5", "6", "*", "/",
  "1", "2", "3", "+", "-",
  "0", ".", "EXP", "Ans", "="
];

for(let i=0; i<OTHERS_OP.length; i++){
  let btn = document.createElement("button");
  btn.innerText = OTHERS_OP[i];
  othersOp.appendChild(btn);
  if(i==2 || i==3) btn.classList.add("hidden");
}

for(let i=0; i<NUMBERS.length; i++){
  let btn = document.createElement("button");
  btn.innerText = NUMBERS[i];
  numbers.appendChild(btn);
  if(NUMBERS[i]=="DEL" || NUMBERS[i]=="AC") btn.classList.add("color");
}

function safeEval(exp){
  return Function("sqrt","sin","cos","tan","log","ln","PI", `return ${exp}`)(
    Math.sqrt,Math.sin,Math.cos,Math.tan,Math.log10,Math.log,Math.PI
  );
}

function calcular(){
  try{
    let expr = display.innerText.replace(/X/g,"*").replace(/Ans/g,lastAnswer).replace(/π/g,"PI").replace(/EXP/g,"*10**");
    let res = safeEval(expr);
    display.innerText = res;
    lastAnswer = res;
  }catch{
    display.innerText = "Error";
  }
}

function addFuncPar(func){
  let lastC = display.innerText.slice(-1);
  if(/\d|\)/.test(lastC)){
    display.innerText += "*"+func+"(";
  }else{
    display.innerText += func+"(";
  }
}

const numBtns = numbers.querySelectorAll("button");
numBtns.forEach(btn=>{
  btn.addEventListener("click", ()=>{
    let val = btn.innerText;

    if(val=="AC"){
      display.innerText = "0";
    }else if(val=="DEL"){
      let txt = display.innerText;
      if(txt.length>1) display.innerText = txt.slice(0,-1);
      else display.innerText = "";
    }else if(val=="="){
      calcular();
    }else if(val=="Ans"){
      if(display.innerText=="0" || display.innerText=="Error" || display.innerText=="") display.innerText = lastAnswer;
      else display.innerText += lastAnswer;
    }else{
      if(display.innerText=="0" || display.innerText=="Error" || display.innerText=="") display.innerText = val;
      else display.innerText += val;
    }
  });
});

const opBtns = othersOp.querySelectorAll("button");
opBtns.forEach(btn=>{
  btn.addEventListener("click", ()=>{
    let val = btn.innerText;
    switch(val){
      case "Pi": display.innerText+="π"; break;
      case "x²": display.innerText+="**2"; break;
      case "x³": display.innerText+="**3"; break;
      case "^": display.innerText+="**"; break;
      case "√": addFuncPar("sqrt"); break;
      case "log": addFuncPar("log"); break;
      case "In": addFuncPar("ln"); break;
      case "sin": addFuncPar("sin"); break;
      case "cos": addFuncPar("cos"); break;
      case "tan": addFuncPar("tan"); break;
      case "(-)": display.innerText+="-"; break;
      default:
        if(val && val.trim()!="") display.innerText += val;
    }
  });
});
