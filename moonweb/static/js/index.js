'use strict';
window.onload = function() {
   const a = localStorage.getItem('color')
   const font = localStorage.getItem('font');
   const chatfont = localStorage.getItem('font');
   document.body.style.color = a ;
   document.body.style.fontSize = font +'px';
   try {
      if( home !== undefined) {
         home.style.fontFamily = 'Segment7Standard';

      }
      
   } catch (error) {
      
   }
   
   //font-family:'Segment7Standard';
   //home.style.fontSize = 100 + 'px';

   // if ( typeof speed_input === undefined) {
   //    speed_input.value = font;
   // }
   // if (chatspeed_input !== undefined) {
   //    chatspeed_input.value = chatfont ;
   // }
   
   //removeitems.style.display = 'none';
   //document.getElementById('datadelete').style.display = "none";
   // const list = document.querySelectorAll("#datadelete");
   // for (let i = 0; i < list.length; i++) {
   //    list[i].style.display = "block";
   // }
   //checkKey()
   //onKey('Escape') ;
}

document.addEventListener("mousemove", function(e) {
   var elStyle = document.querySelector("#time");
   if( elStyle !== null) {
      elStyle.style.top = e.clientY + "px";
      elStyle.style.left = e.clientX + "px";
   }
   //time.style.top = 100 + "px";
   var x = e.clientX ; 
   var y = e.clientY ;
   try {
      if (move !== undefined ) {
         document.getElementById('move').innerHTML = x + ':' + y ;
         
      }
   } catch (err) {
      console.log(err.message)
      
   }
   
 });



function displayDate_Time() {
   var mdy=new Date();
   var date=mdy.getDate();
   var months=mdy.getMonth()+1;
   var year=mdy.getFullYear();
   var hrs=mdy.getHours();
   var min=mdy.getMinutes() ;
   var sec=mdy.getSeconds();
   var en='AM';
   if(min<10){
   min='0'+min;
   }
   if(sec<10){
   sec='0'+sec;
   }
   var colors="#"+hrs+sec+min;
   if(months<10){
   months='0'+months;
   }
   if(date<10){
   date='0'+date;
   }
   if(hrs>=10){
   var colors="#"+min+hrs + sec ;
   }
   if(hrs>12){
   en='PM';
   hrs=hrs-12;
   }
   if(hrs==0){
   hrs=12;
   }
   if(hrs<10){
   hrs='0'+hrs;
   }
   
   //clock.innerHTML=date+":"+months+":"+year;
   time.innerHTML =hrs+":"+min+":"+sec + ' ' + en ;
   time.style.fontSize = 50 + 'px' ; 
   time.style.color ='#' + Math.floor(Math.random()*16777215).toString(16);
   time.style.backgroundColor ='#' + Math.floor(Math.random()*17215).toString(10);
   //time.style.fontSize = sec < 20 ? 20 : sec + 'px';
   home.style.opacity  = (sec / 15 );
   direction.style.backgroundColor=colors;
}


if (typeof id_title === undefined){
   document.getElementById('id_title').addEventListener('change', function() {
      console.log(id_title.value.length)
   })
}




function validate() {
   var sty = document.querySelectorAll(".styleitems");
   var remember = document.querySelectorAll("#datadelete");
   //console.log(sty.length , remember.length )
   for(let i = 0 ; i< sty.length ; i++)
   {
      if(remember[i].checked === true){
         sty[i].style.color = 'red';
         console.log(i)
      }else{
         sty[i].style.color = '';
      }
   }
     
 }

function userRem(){
   var remember = document.querySelectorAll("#remuser");
   console.log(remember.length)
}

function checkKey(){
   window.addEventListener(
      "keydown",
      function readKey(key){
         //alert(key.key);
         "Escape" === key.key  && fix(key.key)
      }
   )
}

const fix = (key) => {
   alert(key)
}

function setStore(a, b) {
   localStorage.setItem(a, b)
}

function chooseColor ( color ) {
   document.body.style.color = color ;
   setStore('color', color);
}

function randomColor () {
   const randomColor = Math.floor(Math.random()*16777215).toString(16);
   document.body.style.color = "#" + randomColor;
   randomcolor.style.backgroundColor = '#' + randomColor;
   setStore('color', '#'+randomColor);
}

const chooseThemeColor = ( color) => {
   document.body.style.color = color;
   //localStorage && localStorage.setItem(color) ;
}

function setFontSize ( a ) {
   localStorage.setItem('font', a);
   speed_input.value = a;
   document.body.style.fontSize = a + 'px';
   if(/\d+/.test(a.value)) {
      if((range_font_size.min < 10) || (range_font_size.max > 30 )) return
      speed_input.value = a ;
      localStorage.setItem('font' , a )
      //document.body.style.fontSize = a + 'px';


   }
}





function showpass()
{
   if (id_password1.type === "password") {
      id_password1.type = "text";
      } else {
         id_password1.type = "password";
   }
}

function loginshowpass()
{
   if (id_password.type === "password") {
      id_password.type = "text";
      } else {
         id_password.type = "password";
   }
}


// chatfooterbgcolor

function notesetting(){
   setStore('notefotterbgcolor','')
}
function chooseBgColor( color ){
   setStore('chatbgcolor', color ) ;
   //notefont.style.backgroundColor = color ;
}

function randomBgColor () {
   const randomColor = Math.floor(Math.random()*16777215).toString(16);
   randomcolor.style.backgroundColor = '#' + randomColor;
   setStore('chatbgcolor', '#'+randomColor);
}

function chooseFColor( color ){
   setStore('Fcolor', color ) ;
   //notefont.style.backgroundColor = color ;
}

function randomFColor () {
   const randomColor = Math.floor(Math.random()*16777215).toString(16);
   randomcolor.style.backgroundColor = '#' + randomColor;
   setStore('Fcolor', '#'+randomColor);
}

//chatfooterbgcolor.style.backgroundColor = 'red';
function setchatFontSize ( a ) {
   localStorage.setItem('chatfont', a);
   chatspeed_input.value = a;
   if(/\d+/.test(a.value)) {
      if((range_chatfont_size.min < 10) || (range_chatfont_size.max > 30 )) return
      chatspeed_input.value = a ;
      localStorage.setItem('chatfont' , a )
   }
}

function setChatDefaults() {
   const chatfont = localStorage.getItem('chatfont');
   const chatbgcolor =  localStorage.getItem('chatbgcolor') ;
   const fcolor = localStorage.getItem('Fcolor') ;
   try {
      if( chatfooterbgcolor !== undefined) {
         chatfooterbgcolor.style.backgroundColor = fcolor ;

      }
      
   } catch (error) {
      console.log(error.message)
   }

   
   
   try {
      if( notefont !== undefined) {
         notefont.style.backgroundColor = chatbgcolor ;

      }
      
   } catch (error) {
      console.log(error.message)
   }

   
   try {
      if ( chatspeed_input !== undefined) {
         range_chatfont_size.value = chatfont;
         chatspeed_input.value = chatfont ;
      }
   } catch (error) {
      console.log(error.message)
   }

   try {
      if (notefont !== undefined) {
         notefont.style.fontSize = chatfont + 'px' ;
      }
      
   } catch (error) {
      console.log(error.message )
      
   }
}
function setDefaults() {
   setInterval(displayDate_Time,500);
   const a = localStorage.getItem('color')
   const font = localStorage.getItem('font');
   
   document.body.style.color = a ;
   document.body.style.fontSize = font +'px';
   setChatDefaults();
   
   

   try {
      if(speed_input !== undefined){
         range_font_size.value = font;
         speed_input.value = font;
      }
      
      
   } catch (error) {
      console.log(error.message)
      
   }

   

}


setDefaults()
function setchatFontSize ( a ) {
   localStorage.setItem('chatfont', a);
   chatspeed_input.value = a;
   if(/\d+/.test(a.value)) {
      if((range_chatfont_size.min < 10) || (range_chatfont_size.max > 30 )) return
      chatspeed_input.value = a ;
      localStorage.setItem('chatfont' , a )
   }
}
function Try( a ) {
   console.log(a <= 10 ? Number(a) + 10 : a)
   localStorage.setItem('test',a) ;
   tryme.value = a;
   test.style.fontSize = 50 + 'px' ;
   test.style.color = '#'+ 10+a+10;
   try_input.value = a;


}


// /* Teste toeme */

//    let source = "",
//    speed = 3,
//    index = 0,
//    altCount = 0,
//    shiftCount = 0,
//    overlayShown = !1;
//    const links = [ // {
//    // 	url: "https://www.sitepoint.com/premium/books/cybersecurity-attack-and-defense-strategies?ref=duiker101"
//    // }

//    {
//       title: "Become a admin!",
//       url: "https://www.sitepoint.com/premium/library/?ref=duiker101"
//    }
// ];


// function getFromStore(a, b) {
//    if (!localStorage) return b;
//    let c = localStorage.getItem(a);
//    return null === c ? b : c
// }



// function toggleCursor() {
//    cursor.style.color = "transparent" === cursor.style.color ? "inherit" : "transparent"
// }

// function onKey(a) {
//    "Escape" === a.key && hideOverlay();
//    overlayShown || ("Shift" === a.key && shiftCount++, "Alt" === a.key && altCount++, 3 <= altCount && (altCount = 0, showAlert(granted)), 3 <= shiftCount && (shiftCount = 0, showAlert(denied)), type(speed))
// }

// function type(a) {
//    let b = source.substring(index, index + a).replace(/[\u00A0-\u9999<>\&]/gim, function (a) {
//       return "&#" + a.charCodeAt(0) + ";"
//    });
//    typer.innerHTML += b, index += a, bottom_padding.scrollIntoView(!1)
// }

// function fetchSource() { // source_input.value = "kernel";
//    fetch("./kernel.txt").then(a => a.text()).then(a => {
//       index = 0, typer.innerHTML = "", setStore("source", a), source = a
//    })
// }

// function onColorChange() {
//    /#[a-f0-9]{3,9}/.test(theme_color_input.value) && setThemeColor(theme_color_input.value)
// }

// function onSpeedChange(a) {
//    if (/\d+/.test(a.target.value)) {
//       let b = parseInt(a.target.value);
//       if (b < speed_range.min || b > speed_range.max) return;
//       speed_range.value = b, speed_input.value = b, speed = b, setStore("speed", b)

//    }
// }

// function onFontSizeChange(a) {
//    if (/\d+/.test(a.target.value)) {
//       let b = parseInt(a.target.value);
//       if (b < font_size_range.min || b > font_size_range.max) return;
//       font_size_range.value = b, font_size_input.value = b, setFontSize(b), setStore("font_size", b)
//    }
// }

// function onFontChange(a) {
//    setFont(a.target.value), setStore("font", a.target.value)
// }

// function onFileChange(a) {
//    if (!(1 > a.length)) {
//       let b = new FileReader;
//       b.onload = function (a) {
//          source = a.target.result, setStore("source", source), typer.innerHTML = "", index = 0
//       }, b.readAsText(a[0], "utf8")
//    }
// }

// function setDefaults() {
//    speed = parseInt(getFromStore("speed", 3)), speed_range.value = speed, speed_input.value = speed;
//    const a = getFromStore("color", "#00ff00");
//    theme_color_input.value = a, setThemeColor(a);
//    const b = parseInt(getFromStore("font_size", 13));
//    font_size_range.value = b, font_size_input.value = b, setFontSize(b);
//    const c = getFromStore("font", "Courier");
//    font_select.value = c, setFont(c);
//    const d = getFromStore("source", "");
//    !!d ? source = d : fetchSource()
// }

// function chooseColor(a) {
//    theme_color_input.value = a, setThemeColor(a)
// }

// function setThemeColor(a) {
//    document.body.style.color = a;
//    for (const b of document.querySelectorAll(".theme_border_color")) b.style.borderColor = a;
//    for (const b of document.querySelectorAll(".theme_color")) b.style.color = a;
//    for (const b of document.querySelectorAll(".theme_bg_color")) b.style.background = a;
//    for (const b of document.querySelectorAll(".theme_fill_color")) b.style.fill = a;
//    setStore("color", a)
// }

// function setFont(a) {
//    const b = a.replace(/\s/, "+");
//    font_div.innerHTML = `<link href="${`https://fonts.googleapis.com/css?family=${b}&display=swap`}" rel="stylesheet" />`, typer.style.fontFamily = a
// }

// function setFontSize(a) {
//    typer.style.fontSize = a + "px", cursor.style.fontSize = a + "px"
// }

// function showModal(a) {
//    hideOverlay(), showOverlay(), a.style.display = "block"
// }

// function showAlert(a) {
//    showOverlay(), a.style.display = "block"
// }

// function showMenu() {
//    showOverlay(), menu.classList.add("visible")
// }

// function showOverlay() {
//    overlayShown = !0, overlay.style.display = "grid", footer.classList.add("blurred"), main.classList.add("blurred")
// }

// function hideOverlay() {
//    overlayShown = !1, overlay.style.display = "none", menu.classList.remove("visible"), footer.classList.remove("blurred"), main.classList.remove("blurred");
//    for (const a of document.querySelectorAll(".modal")) a.style.display = "none";
//    for (const a of document.querySelectorAll(".alert")) a.style.display = "none"
// }

// function closeFooter() {
//    footer.style.display = "none"
// }

// function bindEvents() {
//    setInterval(toggleCursor, 500), window.addEventListener("keydown", onKey), overlay.addEventListener("click", hideOverlay);
//    for (const a of document.querySelectorAll(".modal")) a.addEventListener("click", a => a.stopPropagation());
//    theme_color_input.addEventListener("keyup", onColorChange), speed_input.addEventListener("keyup", onSpeedChange), speed_range.addEventListener("change", onSpeedChange), font_size_input.addEventListener("keyup", onFontSizeChange), font_size_range.addEventListener("change", onFontSizeChange), font_select.addEventListener("change", onFontChange), menu.addEventListener("click", a => a.stopPropagation()), hidden_text.addEventListener("focus", () => {
//       hidden_text.classList.add("hidden")
//    }), main.addEventListener("click", () => hidden_text.focus()), "function" != typeof window.FileReader && (file_row.style.display = "none")
// }

// function makeLink() {
//    const a = Math.random() * links.length,
//       b = links[parseInt(a)];
//    for (const a of document.querySelectorAll(".dynamic-link")) a.setAttribute("href", b.url), a.innerText = b.title
// } // window.addEventListener("load",()=>{
// makeLink(), setDefaults(), bindEvents(); 