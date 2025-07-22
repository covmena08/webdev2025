 //console.log("Js Loaded");
 function generatePassword(length) {
                const allChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+";
                let password = "";
                for (let i = 0; i < length; i++) {
                    const randomIndex = Math.floor(Math.random() * allChars.length);
                    password += allChars[randomIndex]; //Concatinates the random character to the password
                }
                return password;
            }
            document.addEventListener("DOMContentLoaded", function () {
            const generateBtn = document.getElementById("generate");
            const copyBtn = document.getElementById("copy");
            const passwordInput = document.getElementById("passwordInput");

            generateBtn.addEventListener("click", function () {
                const password = generatePassword(12);
                passwordInput.value = password;
            });

            copyBtn.addEventListener("click", function () {
                navigator.clipboard.writeText(passwordInput.value)
                    .then(() => alert("Password copied!"))
                    .catch(err => alert("Failed to copy: " + err));
            });
        });




