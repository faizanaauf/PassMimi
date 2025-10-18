from flask import Flask, render_template_string, request, jsonify
import os, re, time

app = Flask(__name__)

# ========================== CONFIGURATION ==========================
LOGO_PATH = "logo.png" # It's good practice to put static files in a 'static' folder
WORDLIST_PATHS = ["wordlists/wordlists/rockyou.txt", "wordlists/wordlists/SecLists", "wordlists/wordlists/Weakpass.txt"]
THEME_COLOR = "#00f7ff"
PRIMARY_DARK = "#00c4cc"
SECONDARY_COLOR = "#8a2be2"
BACKGROUND_COLOR = "#0a0f1c"
SURFACE_COLOR = "#121a2e"
SURFACE_LIGHT = "#1a243c"
TEXT_COLOR = "#e0ffff"
TEXT_SECONDARY = "#a0b3c6"
DANGER_COLOR = "#ff4757"
WARNING_COLOR = "#ffa502"
SUCCESS_COLOR = "#23ac5c"
INFO_COLOR = "#1e90ff"

# ========================== WORDLIST CHECK ==========================
def check_in_wordlists(password):
    found_lists = []
    for path in WORDLIST_PATHS:
        if not os.path.exists(path):
            continue
        if os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    full_path = os.path.join(root, file)
                    try:
                        with open(full_path, "r", encoding="latin-1", errors="ignore") as f:
                            # Use a more efficient check
                            if f'{password}\n' in f.read():
                                if "SecLists" not in found_lists:
                                    found_lists.append("SecList") # Simplified for speed
                                return found_lists
                    except Exception:
                        continue
        else:
            try:
                with open(path, "r", encoding="latin-1", errors="ignore") as f:
                      if f'{password}\n' in f.read():
                          found_lists.append(os.path.basename(path))
                          return found_lists
            except Exception:
                continue
    return found_lists

# ========================== EVALUATION LOGIC ==========================
def evaluate_password(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    upper_count = sum(1 for c in password if c.isupper())
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    digit_count = sum(1 for c in password if c.isdigit())
    symbols = re.findall(r"[!@#$%^&*(),.?\":{}|<>]", password)
    symbol_count = len(symbols)

    # Rule 7: Check wordlists first - if found, rating is 1
    found_lists = check_in_wordlists(password)
    if found_lists:
        return {
            "rating": 1,
            "strength": "Very Weak",
            "circle_color": DANGER_COLOR,
            "remark": f"⚠️ Found in wordlists ({', '.join(found_lists)})",
            "details": {
                "Uppercase": has_upper, 
                "Lowercase": has_lower, 
                "Digits": has_digit, 
                "Symbols": symbol_count,
                "Length": length
            },
            "suggestion": "Password found in known data breaches; change immediately.",
        }

    # Rule 1: Under 6 characters
    if length < 6:
        return {
            "rating": 1, 
            "strength": "Very Weak", 
            "circle_color": DANGER_COLOR,
            "remark": "Password is too short", 
            "details": {
                "Uppercase": has_upper, 
                "Lowercase": has_lower, 
                "Digits": has_digit, 
                "Symbols": symbol_count,
                "Length": length
            },
            "suggestion": "Increase password length to at least 6 characters."
        }
    
    # Rule 2: 6 to 10 characters
    elif 6 <= length <= 10:
        return {
            "rating": 2, 
            "strength": "Weak", 
            "circle_color": "#ff6633",
            "remark": "Password is too short", 
            "details": {
                "Uppercase": has_upper, 
                "Lowercase": has_lower, 
                "Digits": has_digit, 
                "Symbols": symbol_count,
                "Length": length
            },
            "suggestion": "Increase password length to at least 12 characters and add complexity."
        }
    
    # Rule 3: 10 to 25 without symbols and uppercase
    elif 10 < length <= 25 and (not has_upper or symbol_count == 0):
        return {
            "rating": 5, 
            "strength": "Moderate", 
            "circle_color": WARNING_COLOR,
            "remark": "Password lacks complexity", 
            "details": {
                "Uppercase": has_upper, 
                "Lowercase": has_lower, 
                "Digits": has_digit, 
                "Symbols": symbol_count,
                "Length": length
            },
            "suggestion": "Add uppercase letters and special symbols to increase strength."
        }
    
    # Rule 4: 18 to 25 with symbol and uppercase (and at least 3 numbers)
    elif 18 <= length <= 25 and has_upper and symbol_count >= 1 and digit_count >= 3:
        return {
            "rating": 8, 
            "strength": "Strong", 
            "circle_color": SUCCESS_COLOR,
            "remark": "Strong password with good complexity", 
            "details": {
                "Uppercase": has_upper, 
                "Lowercase": has_lower, 
                "Digits": has_digit, 
                "Symbols": symbol_count,
                "Length": length
            },
            "suggestion": "Excellent password! Consider making it longer for even better security."
        }
    
    # Rule 5: 22 to 30+ with symbols (at least 3) and uppercase (at least 2) and numbers (at least 3)
    elif length >= 22 and symbol_count >= 3 and upper_count >= 2 and digit_count >= 3:
        return {
            "rating": 10, 
            "strength": "Very Strong", 
            "circle_color": THEME_COLOR,
            "remark": "Excellent password security!", 
            "details": {
                "Uppercase": has_upper, 
                "Lowercase": has_lower, 
                "Digits": has_digit, 
                "Symbols": symbol_count,
                "Length": length
            },
            "suggestion": "Perfect! This password meets all security criteria."
        }
    
    # Default case for passwords that don't match specific rules
    else:
        return {
            "rating": 4, 
            "strength": "Average", 
            "circle_color": "#ffff00",
            "remark": "Password could be stronger", 
            "details": {
                "Uppercase": has_upper, 
                "Lowercase": has_lower, 
                "Digits": has_digit, 
                "Symbols": symbol_count,
                "Length": length
            },
            "suggestion": "Add more character variety (uppercase, numbers, symbols) and increase length."
        }

# ========================== ROUTES ==========================
@app.route("/")
def index():
    logo_available = os.path.exists(LOGO_PATH)
    return render_template_string(TEMPLATE, 
                                  logo_available=logo_available, 
                                  logo_path=LOGO_PATH,
                                  theme_color=THEME_COLOR,
                                  primary_dark=PRIMARY_DARK,
                                  secondary_color=SECONDARY_COLOR,
                                  background_color=BACKGROUND_COLOR,
                                  surface_color=SURFACE_COLOR,
                                  surface_light=SURFACE_LIGHT,
                                  text_color=TEXT_COLOR,
                                  text_secondary=TEXT_SECONDARY,
                                  danger_color=DANGER_COLOR,
                                  warning_color=WARNING_COLOR,
                                  success_color=SUCCESS_COLOR,
                                  info_color=INFO_COLOR)

@app.route("/check", methods=["POST"])
def check_password():
    password = request.form.get("password", "")
    time.sleep(1.5)  # Simulate processing time
    result = evaluate_password(password)
    return jsonify(result)

# ========================== MODERN HTML TEMPLATE ==========================
TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PassMimi | Advanced Password Analyzer</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: {{ theme_color }};
            --primary-dark: {{ primary_dark }};
            --secondary: {{ secondary_color }};
            --background: {{ background_color }};
            --surface: {{ surface_color }};
            --surface-light: {{ surface_light }};
            --text: {{ text_color }};
            --text-secondary: {{ text_secondary }};
            --danger: {{ danger_color }};
            --warning: {{ warning_color }};
            --success: {{ success_color }};
            --info: {{ info_color }};
        }
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', system-ui, sans-serif; }
        body {
            background: var(--background);
            color: var(--text);
            min-height: 100vh;
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 10% 20%, rgba(0, 247, 255, 0.05) 0%, transparent 20%),
                radial-gradient(circle at 90% 80%, rgba(138, 43, 226, 0.05) 0%, transparent 20%);
        }

        .main-container {
            display: flex;
            justify-content: center; 
            align-items: center;
            min-height: 100vh;
            transition: all 0.5s ease; 
            padding: 2rem;
            position: relative;
        }

        .main-container.with-result {
            justify-content: space-between; 
            max-width: 1200px;
            margin: 0 auto;
        }

        .center-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            transition: all 0.5s ease;
            width: 100%;
            max-width: 500px; /* Set max-width here for initial state */
        }
        .main-container.with-result .center-container {
            align-items: flex-start;
            text-align: left;
            width: 45%; /* It takes the left 45% of the screen */
            max-width: 500px; /* Maintain max-width */
        }
        .header { display: flex; flex-direction: column; align-items: center; margin-bottom: 2rem; gap: 1rem; }
        .main-container.with-result .header { align-items: flex-start; }
        .logo-container { width: 120px; height: 120px; border-radius: 20px; display: flex; align-items: center; justify-content: center; background: var(--surface); box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3); border: 1px solid rgba(255, 255, 255, 0.05); padding: 10px; }
        .logo-img { max-width: 100%; max-height: 100%; border-radius: 15px; }
        .brand { font-size: 2.5rem; font-weight: 700; background: linear-gradient(90deg, var(--primary), var(--secondary)); -webkit-background-clip: text; background-clip: text; color: transparent; text-align: center; }
        .main-container.with-result .brand { font-size: 2rem; text-align: left; }
        .tagline { color: var(--text-secondary); margin-top: 0.5rem; font-size: 1.1rem; text-align: center; }
        .main-container.with-result .tagline { text-align: left; }
        .input-section { background: var(--surface); border-radius: 20px; padding: 2.5rem; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3); border: 1px solid rgba(255, 255, 255, 0.05); position: relative; overflow: hidden; width: 100%; transition: all 0.5s ease; }
        .input-section::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, var(--primary), var(--secondary)); }
        .input-title { font-size: 1.5rem; margin-bottom: 1.5rem; color: var(--text); text-align: center; }
        .password-input-container { position: relative; margin-bottom: 1.5rem; }
        .password-input { width: 100%; padding: 1.2rem 1rem; background: var(--surface-light); border: 2px solid rgba(255, 255, 255, 0.1); border-radius: 12px; color: var(--text); font-size: 1.1rem; transition: all 0.3s ease; }
        .password-input:focus { outline: none; border-color: var(--primary); box-shadow: 0 0 0 3px rgba(0, 247, 255, 0.2); }
        .toggle-password { position: absolute; right: 15px; top: 50%; transform: translateY(-50%); background: none; border: none; color: var(--text-secondary); cursor: pointer; font-size: 1.2rem; transition: color 0.3s; }
        .toggle-password:hover { color: var(--primary); }
        .analyze-btn { width: 100%; padding: 1.2rem; background: linear-gradient(90deg, var(--primary), var(--secondary)); border: none; border-radius: 12px; color: var(--background); font-size: 1.1rem; font-weight: 600; cursor: pointer; transition: all 0.3s ease; display: flex; align-items: center; justify-content: center; gap: 0.5rem; }
        .analyze-btn:hover { transform: translateY(-2px); box-shadow: 0 7px 15px rgba(0, 247, 255, 0.4); }
        .analyze-btn:active { transform: translateY(0); }
        .loading-container { display: none; flex-direction: column; align-items: center; justify-content: center; margin-top: 1.5rem; }
        .spinner { width: 60px; height: 60px; border: 4px solid rgba(0, 247, 255, 0.2); border-left: 4px solid var(--primary); border-radius: 50%; animation: spin 1s linear infinite; margin-bottom: 1rem; }
        .loading-text { color: var(--text-secondary); font-size: 1rem; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        .pulse { animation: pulse 1.5s ease-in-out infinite alternate; }
        @keyframes pulse { 0% { transform: scale(1); } 100% { transform: scale(1.05); } }
        
        .result-section {
            background: var(--surface); border-radius: 20px; padding: 2.5rem; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3); border: 1px solid rgba(255, 255, 255, 0.05);
            opacity: 0;
            transform: translateX(50px);
            transition: all 0.5s ease;
            position: relative; overflow: hidden; width: 45%; max-width: 500px;
        }
        .result-section::before { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, var(--primary), var(--secondary)); }
        
        .result-section.active {
            opacity: 1;
            transform: translateX(0);
        }

        .result-title { font-size: 1.5rem; margin-bottom: 1.5rem; color: var(--text); }
        .strength-display { display: flex; align-items: center; justify-content: space-between; margin-bottom: 2rem; }
        .strength-circle { width: 120px; height: 120px; border-radius: 50%; display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative; box-shadow: 0 0 20px rgba(0, 0, 0, 0.3); transition: all 0.5s ease; }
        .strength-rating { font-size: 2rem; font-weight: 700; }
        .strength-text { font-size: 0.9rem; margin-top: 0.3rem; }
        .strength-label { font-size: 1.2rem; font-weight: 600; }
        .details-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-bottom: 1.5rem; }
        .detail-item { background: var(--surface-light); padding: 1rem; border-radius: 10px; display: flex; align-items: center; gap: 0.8rem; }
        .detail-icon { width: 36px; height: 36px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 1rem; }
        .detail-info { flex: 1; }
        .detail-label { font-size: 0.9rem; color: var(--text-secondary); }
        .detail-value { font-size: 1.1rem; font-weight: 600; margin-top: 0.2rem; }
        .remark { background: var(--surface-light); padding: 1.2rem; border-radius: 12px; margin-bottom: 1.5rem; border-left: 4px solid var(--primary); }
        .suggestion { background: var(--surface-light); padding: 1.2rem; border-radius: 12px; margin-bottom: 1.5rem; border-left: 4px solid var(--info); }
        .suggestion-title { font-weight: 600; margin-bottom: 0.5rem; color: var(--info); }
        .footer { margin-top: 2rem; text-align: center; color: var(--text-secondary); font-size: 0.9rem; }

        /* --- START: RESPONSIVE DESIGN STYLES --- */
        @media (max-width: 900px) {
            .main-container {
                /* On mobile, use less horizontal padding */
                padding: 1rem;
            }

            .main-container.with-result {
                /* Stack the input and result cards vertically */
                flex-direction: column;
                gap: 2rem;
                justify-content: flex-start;
                align-items: center;
                /* Allow page to scroll if content is long */
                min-height: unset; 
            }

            .main-container.with-result .center-container,
            .result-section {
                /* Make both cards take the full width of the screen */
                width: 100%;
            }

            /* The result card animates from the bottom on mobile instead of the side */
            .result-section {
                transform: translateY(30px);
            }
            .result-section.active {
                transform: translateY(0);
            }

            /* Re-center the header text when cards are stacked */
            .main-container.with-result .header {
                align-items: center;
            }
            .main-container.with-result .brand,
            .main-container.with-result .tagline {
                text-align: center;
            }
        }
        
        @media (max-width: 480px) {
            .input-section, .result-section {
                /* Reduce padding on very small screens for more space */
                padding: 1.5rem;
            }

            .details-grid {
                /* Stack the detail items in a single column instead of a 2x2 grid */
                grid-template-columns: 1fr;
            }

            .brand {
                font-size: 2rem; /* Slightly smaller title for small screens */
            }

            .tagline {
                font-size: 1rem;
            }
        }
        /* --- END: RESPONSIVE DESIGN STYLES --- */
    </style>
</head>
<body>
    <div class="main-container" id="mainContainer">
        <div class="center-container">
            <div class="header">
                {% if logo_available %}
                <div class="logo-container pulse">
                    <img src="{{ url_for('static', filename='logo.png') }}" class="logo-img" alt="PassMimi Logo">
                </div>
                {% endif %}
                <div>
                    <h1 class="brand">PassMimi</h1>
                    <p class="tagline">Advanced Password Strength Analysis</p>
                </div>
            </div>
            
            <div class="input-section">
                <h2 class="input-title">Check Your Password Strength</h2>
                
                <div class="password-input-container">
                    <input type="password" class="password-input" id="password" placeholder="Enter your password">
                    <button class="toggle-password" id="togglePassword">
                        <i class="fas fa-eye"></i>
                    </button>
                </div>
                
                <button class="analyze-btn" id="analyzeBtn">
                    <i class="fas fa-search"></i> Analyze Password
                </button>
                
                <div class="loading-container" id="loadingContainer">
                    <div class="spinner"></div>
                    <div class="loading-text">Analyzing password security...</div>
                </div>
            </div>
        </div>
        
        <div class="result-section" id="resultSection">
            <h2 class="result-title">Password Analysis</h2>
            
            <div class="strength-display">
                <div class="strength-circle" id="strengthCircle">
                    <span class="strength-rating" id="strengthRating">0</span>
                    <span class="strength-text" id="strengthText">/10</span>
                </div>
                <div>
                    <h3 class="strength-label" id="strengthLabel">Enter Password</h3>
                    <p id="strengthDescription">Password analysis will appear here</p>
                </div>
            </div>
            
            <div class="details-grid">
                <div class="detail-item">
                    <div class="detail-icon" style="background: rgba(255, 71, 87, 0.2); color: var(--danger);"><i class="fas fa-font"></i></div>
                    <div class="detail-info">
                        <div class="detail-label">Uppercase</div>
                        <div class="detail-value" id="uppercaseValue">No</div>
                    </div>
                </div>
                
                <div class="detail-item">
                    <div class="detail-icon" style="background: rgba(255, 165, 2, 0.2); color: var(--warning);"><i class="fas fa-font"></i></div>
                    <div class="detail-info">
                        <div class="detail-label">Lowercase</div>
                        <div class="detail-value" id="lowercaseValue">No</div>
                    </div>
                </div>
                
                <div class="detail-item">
                    <div class="detail-icon" style="background: rgba(30, 144, 255, 0.2); color: var(--info);"><i class="fas fa-hashtag"></i></div>
                    <div class="detail-info">
                        <div class="detail-label">Digits</div>
                        <div class="detail-value" id="digitsValue">0</div>
                    </div>
                </div>
                
                <div class="detail-item">
                    <div class="detail-icon" style="background: rgba(46, 213, 115, 0.2); color: var(--success);"><i class="fas fa-asterisk"></i></div>
                    <div class="detail-info">
                        <div class="detail-label">Symbols</div>
                        <div class="detail-value" id="symbolsValue">0</div>
                    </div>
                </div>
            </div>
            
            <div class="remark" id="remark">
                <i class="fas fa-info-circle"></i> Enter a password to analyze its strength
            </div>
            
            <div class="suggestion">
                <div class="suggestion-title">
                    <i class="fas fa-lightbulb"></i> Suggestion
                </div>
                <div id="suggestionText">Our analyzer will provide personalized suggestions to improve your password security.</div>
            </div>
            
            <div class="footer">
                <p>Wordlists used: rockyou.txt, SecLists, Weakpass</p>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const passwordInput = document.getElementById('password');
            const togglePassword = document.getElementById('togglePassword');
            const analyzeBtn = document.getElementById('analyzeBtn');
            const loadingContainer = document.getElementById('loadingContainer');
            const resultSection = document.getElementById('resultSection');
            const mainContainer = document.getElementById('mainContainer');
            const strengthCircle = document.getElementById('strengthCircle');
            const strengthRating = document.getElementById('strengthRating');
            const strengthText = document.getElementById('strengthText');
            const strengthLabel = document.getElementById('strengthLabel');
            const strengthDescription = document.getElementById('strengthDescription');
            const uppercaseValue = document.getElementById('uppercaseValue');
            const lowercaseValue = document.getElementById('lowercaseValue');
            const digitsValue = document.getElementById('digitsValue');
            const symbolsValue = document.getElementById('symbolsValue');
            const remark = document.getElementById('remark');
            const suggestionText = document.getElementById('suggestionText');
            
            // Toggle password visibility
            togglePassword.addEventListener('click', function() {
                const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
                passwordInput.setAttribute('type', type);
                togglePassword.innerHTML = type === 'password' ? '<i class="fas fa-eye"></i>' : '<i class="fas fa-eye-slash"></i>';
            });
            
            // Analyze password
            analyzeBtn.addEventListener('click', function() {
                const password = passwordInput.value;
                
                if (!password) {
                    remark.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Please enter a password to analyze';
                    return;
                }
                
                // Disable the analyze button and show loading
                analyzeBtn.disabled = true;
                analyzeBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing...';
                loadingContainer.style.display = 'flex';
                
                // Send request to server
                fetch("/check", {
                    method: "POST", 
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: new URLSearchParams({password: password})
                })
                .then(r => r.json())
                .then(d => {
                    // Hide loading and re-enable button
                    loadingContainer.style.display = 'none';
                    analyzeBtn.disabled = false;
                    analyzeBtn.innerHTML = '<i class="fas fa-search"></i> Analyze Password';
                    
                    /* --- THIS IS THE JAVASCRIPT THAT TRIGGERS THE ANIMATION --- */
                    mainContainer.classList.add('with-result');
                    resultSection.classList.add('active');
                    /* --- END OF ANIMATION TRIGGER --- */

                    // Update detail values
                    uppercaseValue.textContent = d.details.Uppercase ? 'Yes' : 'No';
                    uppercaseValue.style.color = d.details.Uppercase ? 'var(--success)' : 'var(--danger)';
                    
                    lowercaseValue.textContent = d.details.Lowercase ? 'Yes' : 'No';
                    lowercaseValue.style.color = d.details.Lowercase ? 'var(--success)' : 'var(--danger)';
                    
                    digitsValue.textContent = d.details.Digits ? 'Yes' : 'No';
                    digitsValue.style.color = d.details.Digits ? 'var(--success)' : 'var(--danger)';
                    
                    symbolsValue.textContent = d.details.Symbols;
                    symbolsValue.style.color = d.details.Symbols > 0 ? 'var(--success)' : 'var(--danger)';
                    
                    // Update strength display
                    strengthRating.textContent = d.rating;
                    strengthText.textContent = "/10";
                    strengthLabel.textContent = d.strength;
                    strengthDescription.textContent = d.remark;
                    strengthCircle.style.background = `conic-gradient(${d.circle_color} 0%, ${d.circle_color} ${d.rating * 10}%, var(--surface-light) ${d.rating * 10}%, var(--surface-light) 100%)`;
                    strengthCircle.classList.add('pulse');
                    
                    // Update remark and suggestion
                    remark.innerHTML = `<i class="fas fa-info-circle"></i> ${d.remark}`;
                    suggestionText.textContent = d.suggestion;
                    
                    // Remove pulse animation after 3 seconds
                    setTimeout(() => {
                        strengthCircle.classList.remove('pulse');
                    }, 3000);
                })
                .catch(error => {
                    // Hide loading and re-enable button on error
                    loadingContainer.style.display = 'none';
                    analyzeBtn.disabled = false;
                    analyzeBtn.innerHTML = '<i class="fas fa-search"></i> Analyze Password';
                    remark.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Error analyzing password';
                    console.error('Error:', error);
                });
            });
            
            // Reset UI if user clears the input
            passwordInput.addEventListener('input', function() {
                if (passwordInput.value.length === 0) {
                    // Remove classes to revert to the initial centered layout
                    mainContainer.classList.remove('with-result');
                    resultSection.classList.remove('active');
                }
            });
        });
    </script>
</body>
</html>
'''

if __name__ == "__main__":
    # Ensure the 'static' directory exists for the logo
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True, port=5000)

