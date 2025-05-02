const express = require('express');
const path = require('path');
const sqlite3 = require('sqlite3').verbose();
const crypto = require('crypto');
function sha256Hash(password) {
    return crypto.createHash('sha256')
                 .update(password)
                 .digest('hex');
  }
const app = express();
const PORT = 3000;

// Serve static files from the root directory
app.use(express.static(path.join(__dirname)));

// Body parser middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
// Add these specific routes before the catch-all route
app.get('/signup', (req, res) => {
    res.sendFile(path.join(__dirname, 'signup.html'));
  });
  
  app.get('/login', (req, res) => {
    res.sendFile(path.join(__dirname, 'login.html'));
  });
  
  // Keep your existing catch-all route for other cases
  app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
  });

// Simulated database
let db = new sqlite3.Database(':memory:');
db.serialize(() => {
    db.run("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password_hash TEXT)");
    db.run("INSERT INTO users (username, password_hash) VALUES ('admin', '4c906e03849d387468115678c9484f1d9f9234c26a8441b3c9b10d742e3deb36')");
    db.run("INSERT INTO users (username, password_hash) VALUES ('user1', '05d49692b755f99c4504b510418efeeeebfd466892540f27acf9a31a326d6504')");
});

const FLAG = "SecurinetsENIT{bl1ndSQLi_1n_Us3rn4m3_Ch3ck}";

// API Endpoints
app.post('/api/signup', (req, res) => {
    const { username, password } = req.body;
    //filters!
    // Function to validate the input
    function validateInput(input) {
    if (typeof input !== 'string') return false;
    
    const lowerInput = input.toLowerCase();
    
    // Check for invalid patterns
    const hasWhitespace = /\s/.test(input);
    const hasSleep = lowerInput.includes('sleep');
    const hasHyphen = input.includes('-') ;
    
    // Return true only if all checks pass
    return !hasWhitespace && !hasSleep && !hasHyphen;
    }

    // Validate username and password
    if (!validateInput(username)) {
    return res.status(400).json({ error: 'Username contains invalid characters or patterns' });
    }

    if (!validateInput(password)) {
    return res.status(400).json({ error: 'Password contains invalid characters or patterns' });
    }

    const query = `SELECT * FROM users WHERE username='${username}'`;
    
    db.get(query, (err, row) => {
        if (err) {
            return res.status(500).json({ error: 'Database error' });
        }
        
        if (row) {
            return res.status(400).json({ error: 'Username already exists' });
        } else {
            const password_hash = sha256Hash(password);
            db.run(
                'INSERT INTO users (username, password_hash) VALUES (?, ?)',
                [username, password_hash],
                function(err) {
                    if (err) {
                        return res.status(500).json({ error: 'Failed to create user' });
                    }
                    res.json({ message: 'User created successfully' });
                }
            );
        }
    });
});

app.post('/api/login', (req, res) => {
    const { username, password } = req.body;
    password_hash=sha256Hash(password);
    db.get(
        'SELECT * FROM users WHERE username = ? AND password_hash = ?',
        [username, password_hash],
        (err, row) => {
            if (err) {
                return res.status(500).json({ error: 'Database error' });
            }
            
            if (row) {
                if (row.username === 'admin') {
                    res.json({ message: `Welcome admin! Flag: ${FLAG}` });
                } else {
                    res.json({ message: `Welcome ${row.username}!` });
                }
            } else {
                res.status(401).json({ error: 'Invalid credentials' });
            }
        }
    );
});

app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});