# PassMimi

PassMimi is a Flask-based password strength analyzer that checks password complexity and looks up common/leaked passwords using RockYou and SecLists datasets. It gives an intuitive score (0–10), visual feedback, and suggestions to improve passwords.

## Structure
- `app.py` — main Flask app (entry point)
- `static/` — css/js/logo
- `templates/` — html templates (if used)
- `rockyou.txt` — (optional, large; recommended: keep offline and use bloom)
- `wordlists/SecLists/` — SecLists folder (recommended: keep offline and use bloom)

## Deployment (Render)
1. Create `requirements.txt` and `Procfile` (present in repo).
2. Push to GitHub.
3. Create a Render Web Service, connect to this repo, and set:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 3`
4. (Optional) Add env vars in Render dashboard for S3 or BLOOM_URL if using external bloom.

## Wordlists and large files
**Important:** Do not commit multi-GB wordlists to this repository. Instead:
- Build an offline Bloom filter (`passmimi.bloom`) and store that in S3 or a cloud link, or
- Upload a trimmed/deduplicated subset if you must keep something inside repo.

## Contact
Email: fai_ebook@proton.me
