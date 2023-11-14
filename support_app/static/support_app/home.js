const msgerForm = get(".msger-inputarea");
const msgerInput = get(".msger-input");
const msgerChat = get(".msger-chat");
const msgrSendButton = get(".msger-send-btn")
const agentConsole = get(".console")

const PERSON_IMGS = [
    "/static/support_app/person_female.svg",
    "/static/support_app/person_male.svg"
]

const selector = Math.round(Math.random());
const PERSON_IMG = PERSON_IMGS[selector];
const BOT_IMG = "/static/support_app/chatbot.gif";
const BOT_NAME = "AI Support";
const PERSON_NAME = "Shopper";

// Set current time
document.getElementById("bot-welcome-time").innerText = formatDate(new Date())

// Add left pen show menu
Array.from(document.getElementsByClassName("showbtn")).map((btn) => {
    btn.addEventListener("click", () => {
        document.getElementById("sidemenu").classList.toggle("show")
    })
})

// Add user profile dropdown
document.getElementById("profile_dropdown").addEventListener("click",()=>{
    document.getElementsByClassName("profilre_dropdown")[0].classList.toggle("toggle_profile_dropdown")
})

// Create a WebSocket in JavaScript.
const webSocket = new WebSocket('ws://127.0.0.1:8000/ws/trace/');
// Add web socket handler
webSocket.onmessage = function (event) {
    var data = JSON.parse(event.data);
    switch(data.type) {
    case "Trace":
        console.log(data.message)
        switch(data.message.type) {
        case "Thought":
            text = data.message.thought;
            text += "<br><b>Action:</b> " + data.message.action;
            text += "<br><b>Action Input:</b> " + data.message.actionInput;
            appendConsoleMessage(data.message.type, data.message.type, text);
            break;
        case "Tool":
            text = data.message.message;
            appendConsoleMessage(data.message.type, data.message.type, text);
            break;
        case "Answer":
            text = data.message.thought;
            text += "<br><b>Answer:</b> " + data.message.answer;
            appendConsoleMessage(data.message.type, 'Thought', text);
            break;
        }
        break;
    case "Answer":
        botResponse(data.message);
        break;
    case "Stats":
        text = data.message;
        appendConsoleMessage(data.type, data.type, JSON.stringify(text,null,2));
        break;
    }
}

// Add query submit listener
msgerForm.addEventListener("submit", event => {
    event.preventDefault();

    const msgText = msgerInput.value;
    if (!msgText) return;

    appendMessage(PERSON_NAME, PERSON_IMG, "right", msgText);
    msgerInput.value = "";

    // disable further query
    msgrSendButton.disabled = true
    // start thinking
    botThinking();
    // send query to server
    sendQuery(PERSON_NAME, msgText);
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

function botResponse(text) {
    const delay = text.split(" ").length * 100;
    setTimeout(() => {
        document.getElementById("bot-thinking").outerHTML = ""
        appendMessage(BOT_NAME, BOT_IMG, "left", text);
        msgrSendButton.disabled = false
    }, delay);
}

function appendConsoleMessage(type, trait, text) {

    const msgHTML = `
    <p class="${type.toLowerCase()}">
        <b>${trait}:</b> ${text}
    </p>
    `;

    agentConsole.insertAdjacentHTML("beforeend", msgHTML);
    agentConsole.scrollTop += 500;
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

function sendQuery(user, queryText) {
    webSocket.send(JSON.stringify({
        'user_id': user,
        'user_query': queryText,
    }));
}
