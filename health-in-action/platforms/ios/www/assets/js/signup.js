var app = {
    // Application Constructor
    initialize: function () {
        document.addEventListener('deviceready', this.onDeviceReady.bind(this), false);
    },

    // deviceready Event Handler
    //
    // Bind any cordova events here. Common events are:
    // 'pause', 'resume', etc.
    onDeviceReady: function () {
        const Http = new XMLHttpRequest();

        document.getElementById("signup-button").addEventListener("click", onSignUpClickHandler);

        function onSignUpClickHandler() {
            const username = document.getElementById("username").value
            const password = document.getElementById("password").value
            const email = document.getElementById("email").value

            console.log('hi')

            const signUpData = {
                username: username,
                password: password,
                email: email
            }

            Http.open("POST", 'http://127.0.0.1:5000/login');
            Http.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

            Http.send(JSON.stringify(signUpData));

            Http.onreadystatechange = (e) => {
                if (Http.readyState == 4 && Http.status == 200) {
                    alert("Signup Successful!")
                    window.localStorage.setItem(username, password)
                    location.replace('login.html')
                } else if (Http.readyState == 4 && Http.status == 401) {
                    alert("Signup Unsuccessful")
                    // location.replace('loginfail.html')
                    // alert("Wrong ID or Password! Please check again!")

                }
            }
        }
    }
};

app.initialize();