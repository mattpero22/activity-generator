document.getElementById('send-btn').addEventListener('click', async () => {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === '') return;

    addMessage('You', userInput);

    const response = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userInput }),
    });

    const data = await response.json();
    addMessage('Bot', data.response);
    document.getElementById('user-input').value = '';
});

function addMessage(sender, message) {
    const messagesDiv = document.getElementById('messages');
    const newMessage = document.createElement('div');
    newMessage.className = 'message';
    newMessage.innerHTML = `<strong>${sender}:</strong> ${message}`;
    messagesDiv.appendChild(newMessage);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}
