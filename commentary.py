from utils_prompt import load_prompt

SYSTEM_PROMPT   = load_prompt("commentary_system")
USER_PROMPT_TPL = load_prompt("commentary_user")

def generate_commentary(client: str, strategy: str, model_name: str, context: dict) -> str:
    user_prompt = USER_PROMPT_TPL.format(
        client=client,
        strategy=strategy,
        model_name=model_name,
        top_holdings=", ".join(context.get("top_holdings", [])),
        period_return=context.get("period_return",""),
        benchmark_return=context.get("benchmark_return",""),
    )
    return f"**[Demo Commentary]**\n\n{user_prompt}\n\n_System prompt is kept private in production (prompts_private/)._"
