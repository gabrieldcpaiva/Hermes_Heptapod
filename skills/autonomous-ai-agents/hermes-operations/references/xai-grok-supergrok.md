# xAI / Grok — SuperGrok Integration in Hermes

## Context

Gabriel has a **SuperGrok subscription** (xAI's paid tier) but had never used the API. SuperGrok subscribers get API credits included — the API access is part of what you're already paying for, not an additional cost.

## Setting Up

1. **Generate an API key** at [console.x.ai](https://console.x.ai) (log in with the same account as SuperGrok)
2. **Add to Hermes env:**
   ```bash
   echo 'XAI_API_KEY=your-key-here' >> ~/.hermes/.env
   ```
3. **Select a model:**
   ```bash
   hermes config set model.default grok-4.20-reasoning
   # or use the interactive picker (needs real terminal):
   hermes model
   ```
4. **Verify:**
   ```bash
   hermes doctor
   ```

## Available Models (as of May 2026)

| Model | Purpose |
|-------|---------|
| `grok-4.20-reasoning` | Latest reasoning model (used for x_search in config) |
| `grok-3` | Standard chat model |
| `grok-3-mini` | Faster, lighter variant |

Model names may update — check xAI docs for current availability.

## What's Already Configured

In Gabriel's `~/.hermes/config.yaml`:
- `x_search` tool uses `grok-4.20-reasoning` as its backend model
- xAI TTS provider settings (voice, language, sample rate) are pre-configured
- xAI is enabled in model-providers plugin list

Missing piece: `XAI_API_KEY` was never set in `.env`, so all xAI features are dormant despite being configured.

## Economics

- SuperGrok ≈ $30/month (or $300/year)
- API credits are included with subscription
- Using Grok through Hermes costs nothing extra
- Gabriel was paying for SuperGrok but not using the API — free capacity

## Nickname Convention

In Hermes config, xAI models use `grok-` prefix (e.g. `grok-4.20-reasoning`, not `xai/...` or `x-ai/...`).

## Rate Limits

SuperGrok subscribers get higher rate limits than free tier. The recent Nous Discord announcement about "SuperGrok user limits reset" suggests rate caps were refreshed/expanded. If the user mentions hitting rate limits, this is worth checking.