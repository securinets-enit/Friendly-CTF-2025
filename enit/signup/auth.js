// Simulated database operations through API calls
const API_BASE_URL = '';

async function makeRequest(endpoint, data) {
    const response = await fetch(`/api/${endpoint}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    });
    return await response.json();
}

document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            const username = document.getElementById('loginUsername').value;
            const password = document.getElementById('loginPassword').value;
            
            try {
                const result = await makeRequest('login', { username, password });
                if (result.error) {
                    showMessage('loginMessage', result.error, 'error');
                } else {
                    showMessage('loginMessage', result.message, 'success');
                }
            } catch (err) {
                showMessage('loginMessage', 'Login failed', 'error');
                console.error(err);
            }
        });
    }

    const signupForm = document.getElementById('signupForm');
    if (signupForm) {
        signupForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            const username = document.getElementById('signupUsername').value;
            const password = document.getElementById('signupPassword').value;
            
            try {
                const result = await makeRequest('signup', { username, password });
                if (result.error) {
                    showMessage('signupMessage', result.error, 'error');
                } else {
                    showMessage('signupMessage', result.message, 'success');
                }
            } catch (err) {
                showMessage('signupMessage', 'Signup failed', 'error');
                console.error(err);
            }
        });
    }
});