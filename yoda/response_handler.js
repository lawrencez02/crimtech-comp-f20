// Declaring variables that you may want to use.
let names = ['cute', 'regular'];
let moods = ['dark', 'force', 'std'];

let dark_quotes = ["Once you start down the dark path, forever will it dominate your destiny, consume you it will.",
"In a dark place we find ourselves, and a little more knowledge lights our way.",
"Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering.",
"Always two there are, no more, no less. A master and an apprentice.",
"In the end, cowards are those who follow the dark side."];
let force_quotes = ["Luminous beings are we, not this crude matter.",
"A Jedi uses the Force for knowledge and defense, never for attack.",
"Clear your mind must be, if you are to find the villains behind this plot.",
"The force. Life creates it, makes it grow. Its energy surrounds us and binds us.",
"My ally is the Force, and a powerful ally it is."];
let std_quotes = ["Patience you must have, my young padawan.",
"When nine hundred years old you reach, look as good you will not.",
"No! Try not! Do or do not, there is no try.",
"Judge me by my size, do you?",
"Difficult to see. Always in motion is the future."
];

function respond() {
   
    var picture = document.getElementById("user_image");
    var usertext = document.getElementById("input_text");
    var displayedtext = document.getElementById("current_text");
    console.log(usertext.value);

    if (usertext.value.includes("cute") || usertext.value.includes("baby"))
    {
        if (usertext.value.includes("force") && usertext.value.includes("dark"))
        {
            picture.setAttribute("src", "img/cute-dark.jpg");
        }
        else if (usertext.value.includes("force"))
        {
            picture.setAttribute("src", "img/cute-force.jpg");
        }
        else
        {
            picture.setAttribute("src", "img/cute-std.jpg");
        }
    }
    else
    {
        if (usertext.value.includes("force") && usertext.value.includes("dark"))
        {
            picture.setAttribute("src", "img/regular-dark.jpg");
        }
        else if (usertext.value.includes("force"))
        {
            picture.setAttribute("src", "img/regular-force.jpg");
        }
        else
        {
            picture.setAttribute("src", "img/regular-std.jpg");
        }
    }

    usertext.value = "";
    var random1 = Math.floor(Math.random() * 3) + 1;
    var random2 = Math.floor(Math.random() * 5);
    var random3 = Math.floor(Math.random() * 5) + 5;
    var hmm = "m";

    if (random1 == 1)
    {
        displayedtext.innerHTML = dark_quotes[random2] + " Yes, h" + hmm.repeat(random3) + ".";;
    }
    else if (random1 == 2)
    {
        displayedtext.innerHTML = force_quotes[random2] + " Yes, h" + hmm.repeat(random3) + ".";;
    }
    else
    {
        displayedtext.innerHTML = std_quotes[random2] + " Yes, h" + hmm.repeat(random3) + ".";
    }
}