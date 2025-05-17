function renderNavbarButtons() {
  const token = localStorage.getItem('access_token');
  const navbarButtons = document.getElementById('navbar-buttons');
  navbarButtons.innerHTML = '';

  if (token) {
    const myBookingsBtn = document.createElement('button');
    myBookingsBtn.textContent = 'My Bookings';
    myBookingsBtn.onclick = () => window.location.href = 'my_bookings.html';
    navbarButtons.appendChild(myBookingsBtn);

    const logoutBtn = document.createElement('button');
    logoutBtn.textContent = 'Logout';
    logoutBtn.onclick = async () => {
      try {
        await fetch('http://localhost:8000/api/api/token/logout/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ refresh: localStorage.getItem('refresh_token') })
        });
      } catch (e) {
      }
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      window.location.href = 'login.html';
    };
    navbarButtons.appendChild(logoutBtn);
  } else {
    const loginBtn = document.createElement('button');
    loginBtn.textContent = 'Login';
    loginBtn.onclick = () => window.location.href = 'login.html';

    const registerBtn = document.createElement('button');
    registerBtn.textContent = 'Register';
    registerBtn.onclick = () => window.location.href = 'register.html';

    navbarButtons.appendChild(loginBtn);
    navbarButtons.appendChild(registerBtn);
  }
}

async function loadEvents() {
  try {
    const res = await fetch("http://localhost:8000/api/events/");
    if (!res.ok) throw new Error(`HTTP error! status: ${res.status}`);

    const events = await res.json();
    const container = document.getElementById("events-list");
    container.innerHTML = "";

    events.forEach(event => {
      const card = document.createElement("div");
      card.className = "event-card";

      card.innerHTML = `
        <img src="${event.image || 'https://via.placeholder.com/400x200?text=No+Image'}" alt="${event.name}">
        <div class="event-content">
          <h3>${event.name}</h3>
          <p>${event.description.slice(0, 100)}...</p>
        </div>
        <div class="buttons">
          <button onclick="window.location.href = 'event_detail.html?id=${event.id}'">View Details</button>
        </div>
      `;

      container.appendChild(card);
    });
  } catch (error) {
    console.error("Error loading events:", error);
    document.getElementById("events-list").innerHTML = "<p>Failed to load events.</p>";
  }
}

renderNavbarButtons();
loadEvents();

const params = new URLSearchParams(window.location.search);
const eventId = params.get('id');

fetch(`http://localhost:8000/api/events/${eventId}/`)
  .then(res => res.json())
  .then(event => {
  });
