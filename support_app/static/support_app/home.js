const msgerForm = get(".msger-inputarea");
const msgerInput = get(".msger-input");
const msgerChat = get(".msger-chat");
const msgrSendButton = get(".msger-send-btn")

const BOT_MSGS = [
    "Hi, how are you?",
    "Ohh... I can't understand what you trying to say. Sorry!",
    "I like to play games... But I don't know how to play!",
    "Sorry if my answers are not relevant. :))",
    "I feel sleepy! :("
];

const PERSON_IMGS = [
    "/static/support_app/person_female.svg",
    "/static/support_app/person_male.svg"
]

const selector = Math.round(Math.random());
const PERSON_IMG = PERSON_IMGS[selector];
const BOT_IMG = "/static/support_app/chatbot.gif";
const BOT_NAME = "AI Support";
const PERSON_NAME = "Shopper";

document.getElementById("bot-welcome-time").innerText = formatDate(new Date())

msgerForm.addEventListener("submit", event => {
    event.preventDefault();

    const msgText = msgerInput.value;
    if (!msgText) return;

    appendMessage(PERSON_NAME, PERSON_IMG, "right", msgText);
    msgerInput.value = "";
    msgrSendButton.disabled = true

    botThinking();
    sleep(5000).then(() => {
        document.getElementById("bot-thinking").outerHTML = ""
        botResponse();
        msgrSendButton.disabled = false
    });
});

function sleep (time) {
    return new Promise((resolve) => setTimeout(resolve, time));
}

function appendMessage(name, img, side, text) {
    //   Simple solution for small apps
    const msgHTML = `
    <div class="msg ${side}-msg">
        <div class="msg-img" style="background-image: url(${img})"></div>

        <div class="msg-bubble">
        <div class="msg-info">
            <div class="msg-info-name">${name}</div>
            <div class="msg-info-time">${formatDate(new Date())}</div>
        </div>

        <div class="msg-text">${text}</div>
        </div>
    </div>
    `;

    msgerChat.insertAdjacentHTML("beforeend", msgHTML);
    msgerChat.scrollTop += 500;
}

function botThinking() {
    const msgHTML = `
        <div class="msg left-msg" id="bot-thinking">
            <div class="msg-img" style="background-image: url(${BOT_IMG})"></div>

            <div class="msg-bubble">
                <div class="msg-info">
                    <div class="msg-info-name">${BOT_NAME}</div>
                    <div class="msg-info-time">${formatDate(new Date())}</div>
                </div>
                <div class="typing">
                    <div class="dot"></div>
                    <div class="dot"></div>
                    <div class="dot"></div>
                </div> 
            </div>
        </div>
        `; 
    msgerChat.insertAdjacentHTML("beforeend", msgHTML);
    msgerChat.scrollTop += 500;
}

function botResponse() {
    const r = random(0, BOT_MSGS.length - 1);
    const msgText = BOT_MSGS[r];
    const delay = msgText.split(" ").length * 100;

    setTimeout(() => {
        appendMessage(BOT_NAME, BOT_IMG, "left", msgText);
    }, delay);
}

// Utils
function get(selector, root = document) {
    return root.querySelector(selector);
}

function formatDate(date) {
    const h = "0" + date.getHours();
    const m = "0" + date.getMinutes();

    return `${h.slice(-2)}:${m.slice(-2)}`;
}

function random(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}

Array.from(document.getElementsByClassName("showbtn")).map((btn) => {
    btn.addEventListener("click", () => {
        document.getElementById("sidemenu").classList.toggle("show")
    })
})

document.getElementById("profile_dropdown").addEventListener("click",()=>{
    document.getElementsByClassName("profilre_dropdown")[0].classList.toggle("toggle_profile_dropdown")
})

/*document.querySelector('#submit').onclick = function (e) {
    const user_id = document.querySelector('#id_user_id').value;
    const user_query = document.querySelector('#id_user_query').value;
    webSocket.send(JSON.stringify({
        'user_id': user_id,
        'user_query': user_query,
    }));
    document.querySelector('#id_user_query').value = '';
};*/

//Create a WebSocket in JavaScript.
const webSocket = new WebSocket('ws://127.0.0.1:8000/ws/trace/');

webSocket.onmessage = function (e) {
    var data = JSON.parse(event.data);
    switch(data.type) {
    case "Trace":
        console.log(data.message)
        switch(data.message.type) {
        case "Thought":
            document.querySelector('#trace_console').innerText += data.message.thought;
            document.querySelector('#trace_console').innerText += data.message.action;
            document.querySelector('#trace_console').innerText += data.message.actionInput;
            break;
        case "Tool":
            document.querySelector('#trace_console').innerText += data.message.message;
            break;
        case "Answer":
            document.querySelector('#trace_console').innerText += data.message.thought;
            document.querySelector('#trace_console').innerText += data.message.answer;
            break;
        }
        break;
    case "Answer":
        document.querySelector('#expert_answer').innerText = data.message;
        break;
    }
}