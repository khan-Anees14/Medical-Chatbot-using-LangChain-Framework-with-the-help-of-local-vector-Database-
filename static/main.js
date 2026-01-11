function sendMessage() {
  const input = document.getElementById("user-input");
  const text = input.value.trim();
  if (!text) return;

  const messages = document.getElementById("messages");

  // User message
  messages.innerHTML += `
    <div class="user-message message">
      <div class="message-div">
        <div class="message-profile-pic">
          <img src="https://abs.twimg.com/sticky/default_profile_images/default_profile_400x400.png" height="30" width="30"/>
        </div>
        <div class="message-content"><p>${text}</p></div>
      </div>
    </div>
  `;

  input.value = "";

  // Call backend
  fetch("/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ message: text })
  })
  .then(res => res.json())
  .then(data => {
    messages.innerHTML += `
      <div class="gpt-message message">
        <div class="message-div">
          <div class="message-profile-pic">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/ChatGPT_logo.svg/900px-ChatGPT_logo.svg.png" height="30" width="30"/>
          </div>
          <div class="message-content">
            <p>${data.reply}</p>
            <p class="disclaimer">⚠️ Educational use only.</p>
          </div>
        </div>
      </div>
    `;
    messages.scrollTop = messages.scrollHeight;
  });
}

function handleEnter(e) {
  if (e.key === "Enter") sendMessage();
}

function newChat() {
  document.getElementById("messages").innerHTML = "";
}

function clearChats() {
  document.getElementById("messages").innerHTML = "";
}


// <script>
function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");

    // Save preference
    if (document.body.classList.contains("dark-mode")) {
        localStorage.setItem("theme", "dark");
    } else {
        localStorage.setItem("theme", "light");
    }
}

// Load saved theme
window.onload = function () {
    if (localStorage.getItem("theme") === "dark") {
        document.body.classList.add("dark-mode");
    }
};
// </script>
