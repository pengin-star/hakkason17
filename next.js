// Pythonにデータを送信
fetch('/receive_tags/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: inputField.value })
})
.then(response => response.json())
.then(data => {
alert(`Pythonからの応答: ${data.reply}`);
})
.catch(error => {
    console.error('Error:', error);
});