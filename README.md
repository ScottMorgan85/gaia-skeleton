# GAIA Skeleton Demo

This is a **public-safe skeleton** of GAIA (Generative AI Investment Analytics).
- Uses **synthetic demo data** under data/demo/
- Uses **placeholder prompts** under prompts/
- Real prompt engineering should live in prompts_private/ (gitignored)
- No secrets, no visitor logs, no real client data

## Run locally
pip install -r requirements.txt
streamlit run app.py

## Notes
- Add your private prompts in prompts_private/ with the same filenames as prompts/.
- Replace demo CSVs with your own in data/ for richer views.
