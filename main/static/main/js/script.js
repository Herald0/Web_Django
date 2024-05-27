
// Меню

const btn = document.querySelector(".menu button");

const menu = document.querySelector(".navigation");

const img = document.querySelector(".menu img");

function showMenu() {
  menu.classList.toggle("show");
  img.classList.toggle("turn");
};

btn.addEventListener("click", showMenu);

// Окно авторизации

const btn1 = document.querySelector(".auth");

const authorizWindow = document.querySelector(".auth-window");

function showAuth() {
  authorizWindow.classList.toggle("show");
};

if (btn1) {
  btn1.addEventListener("click", showAuth);
}

const btn_exit = document.querySelector(".exit");

if (btn_exit) {
  btn_exit.addEventListener("click", showAuth);

  // Авторизация
  
  const inputs = document.getElementById("auth-form").querySelectorAll("input");
  
  for (var i = 0; i < inputs.length; i++) {
    inputs[i].addEventListener("input", authForm);
  }
  
  const in1 = document.getElementById("name");
  const in2 = document.getElementById("surname");
  const in3 = document.getElementById("pass");
  
  function authForm() {
  
    if (!/^[А-ЯЁA-Z][а-яёa-z]+$/.test(in1.value) && in1.value != "") {
      console.log("use");
  
      in1.setCustomValidity("Имя должно содержать только буквы и только одну заглавную.");
    }
    else {
      in1.setCustomValidity("");
    }
  
    if (!/^[А-ЯЁA-Z][а-яёa-z]+$/.test(in2.value) && in2.value != "") {
      in2.setCustomValidity("Фамилия должна содержать только буквы и только одну заглавную.");
    }
    else {
      in2.setCustomValidity("");
    }
    if (in3.value.length >= 20) {
      in3.setCustomValidity("Длина пароля не может быть больше 20 символов");
    }
    else {
      in3.setCustomValidity("");
    }
  }
}

// Погода

const btn_weather = document.getElementById("btnweather");

const output = document.getElementById("weather");

if (btn_weather) {
  btn_weather.addEventListener("click", () => {

  const city = document.getElementById("city").value;
  
  const url ="https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=ccf6a25d95d77ff985ae6ae604de8ba3&units=metric";
  
  fetch(url).then(response => {
    if (!response.ok) {
      throw new Error('Ошибка при выполнении запроса: ' + response.statusText);
    }
    return response.json();
  }).then(data => {
    output.innerHTML = "Температура " + data["main"]["temp"] + " °C";
    output.style.opacity = 1;
  }).catch(error => {
    output.innerHTML = "Некорректный город";
    output.style.opacity = 1;
  });
});
}

console.log("END");