import sys
from pathlib import Path
from unittest.mock import patch

# Make the repository root importable when pytest executes from tests/.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# app.py imports pywebview for the desktop shell. The password evaluator itself
# does not need a GUI, so provide a lightweight stub for headless CI.
sys.modules.setdefault("webview", type(sys)("webview"))

import app


def evaluate(password: str):
    with patch.object(app, "check_in_wordlists", return_value=[]):
        return app.evaluate_password(password)


def test_short_password_is_very_weak():
    result = evaluate("Ab1!")
    assert result["rating"] == 1
    assert result["strength"] == "Very Weak"
    assert result["details"]["Length"] == 4


def test_medium_password_without_symbol_is_moderate():
    result = evaluate("longpasswordABC123")
    assert result["rating"] == 5
    assert result["strength"] == "Moderate"


def test_strong_password_rule():
    result = evaluate("StrongPassword123!xyz")
    assert result["rating"] == 8
    assert result["strength"] == "Strong"


def test_very_strong_password_rule():
    result = evaluate("VeryStrongPassword123!!!XYZ")
    assert result["rating"] == 10
    assert result["strength"] == "Very Strong"


def test_breached_password_overrides_complexity():
    with patch.object(app, "check_in_wordlists", return_value=["rockyou.txt"]):
        result = app.evaluate_password("VeryStrongPassword123!!!XYZ")
    assert result["rating"] == 1
    assert "wordlists" in result["remark"].lower()
