document.addEventListener('DOMContentLoaded', () => {
    const chatWindow = document.getElementById('chat-window');
    const userInput = document.getElementById('user-message');
    const sendButton = document.getElementById('send-button');

    function addMessageToChat(message, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender === 'user' ? 'user-message' : 'ai-message');
        
        const p = document.createElement('p');
        p.textContent = message;
        messageDiv.appendChild(p);
        
        chatWindow.appendChild(messageDiv);
        chatWindow.scrollTop = chatWindow.scrollHeight; // Auto-scroll to bottom
    }
    
    function addErrorMessageToChat(message) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', 'ai-message', 'error-message'); // Style as AI but with error indication
        
        const p = document.createElement('p');
        p.textContent = message;
        messageDiv.appendChild(p);
        
        chatWindow.appendChild(messageDiv);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }


    async function sendMessage() {
        const messageText = userInput.value.trim();
        if (!messageText) return;

        addMessageToChat(messageText, 'user');
        userInput.value = ''; // Clear input

        // Add a thinking indicator
        const thinkingDiv = document.createElement('div');
        thinkingDiv.classList.add('message', 'ai-message');
        thinkingDiv.innerHTML = '<p><em>Thinking...</em></p>';
        chatWindow.appendChild(thinkingDiv);
        chatWindow.scrollTop = chatWindow.scrollHeight;

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: messageText }),
            });

            chatWindow.removeChild(thinkingDiv); // Remove thinking indicator

            if (!response.ok) {
                const errorData = await response.json().catch(() => ({reply: "An unknown error occurred processing the server response."}));
                throw new Error(errorData.reply || `Server error: ${response.status}`);
            }

            const data = await response.json();
            addMessageToChat(data.reply, 'ai');

        } catch (error) {
            console.error('Error sending message:', error);
            if(thinkingDiv.parentNode === chatWindow) chatWindow.removeChild(thinkingDiv); // Ensure removal if error
            addErrorMessageToChat(`Sorry, an error occurred: ${error.message}`);
        }
    }

    sendButton.addEventListener('click', sendMessage);
    userInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });
});