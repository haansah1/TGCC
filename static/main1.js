var hidEl = document.querySelector(".hid")
  var barsEl = document.querySelector(".divbars")
  var inputEl = document.getElementById("input")
  var closeEl = document.querySelector(".close")
  var windowEl = document.getElementBy

  inputEl.addEventListener("input", ()=>{
    if(inputEl.checked){
      console.log("why");
      hidEl.style.transform = "scaleY(1)";
    }
    else{
      hidEl.style.transform = "scaleY(1)";
      console.log("why");
    }
  })

  closeEl.addEventListener("click", ()=>{
    console.log("ei");
    hidEl.classList.add("active1");
    hidEl.style.transform = "scaleY(0)";
  })

  window.addEventListener("click", ()=>{
    hidEl.style.transform = "scaleY(0)";
  })