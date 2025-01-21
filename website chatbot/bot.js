document.getElementById("send-button").addEventListener("click", sendMessage);
document.getElementById("chat-input").addEventListener("keypress", function (e) {
    if (e.key === "Enter") sendMessage();
});

const messagesContainer = document.getElementById("chat-messages");

function sendMessage() {
    const inputField = document.getElementById("chat-input");
    const userMessage = inputField.value.trim();

    if (userMessage === "") return;

    // Display the user's message
    addMessage(userMessage, "user");

    // Process the bot's response
    setTimeout(() => {
        const botMessage = generateBotResponse(userMessage);
        addMessage(botMessage, "bot");
    }, 500);

    inputField.value = "";
    inputField.focus();
}

function addMessage(message, sender) {
    const messageElement = document.createElement("div");
    messageElement.className = sender === "bot" ? "message bot-message" : "message user-message";
    messageElement.textContent = message;
    messagesContainer.appendChild(messageElement);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function generateBotResponse(userMessage) {
    // Simple bot logic (You can replace this with AI integration)
    if (userMessage.toLowerCase().includes("hello")) {
        return "Hi there! How can I help you today?";
    } else if (userMessage.toLowerCase().includes("help")) {
        return "Sure! Please tell me what you need help with.";
    } else if (userMessage.toLowerCase().includes("who is vishwa")) {
        return " Vishwa GW is the creator of me and this web site, He is a self thought AI and robotics researcher."
    } else if (userMessage.toLowerCase().includes("what do you do")) {
        return "I can answers your basic questions";
    } else {
        return "I'm not sure I understand. Could you clarify?";
    }
}
