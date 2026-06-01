# Image Generation Configuration Verification

When suggesting image generation for revenue-generating activities, always verify the configured image generation service before proceeding.

## Why This Matters
Gabriel has stated he has OpenAI API loaded but uses it for images mostly. However, the Hermes agent's default image generation tool uses FAL, not OpenAI/DALL-E. Failing to verify configuration leads to failed image generation attempts and wasted time.

## Verification Steps
1. **Check Environment Variables**: Verify if OPENAI_API_KEY is set in the environment
2. **Check Hermes Configuration**: Run `hermes tools` to see which image generation provider is configured
3. **Test with Minimal Prompt**: Before committing to an image-based revenue idea, test with a simple prompt to confirm service availability
4. **Have Fallback Ready**: If primary service is unavailable, be prepared to suggest non-image-based alternatives or configure the preferred service

## Common Configuration Issues
- **FAL_KEY Missing**: The FAL image generation service requires FAL_KEY environment variable
- **No Credits**: Even with FAL_KEY set, usable paid credits may be depleted
- **Provider Misconfiguration**: The agent may be configured to use a different provider than expected
- **OpenAI vs FAL Confusion**: Gabriel may have OpenAI configured but agent defaults to FAL

## Quick Check Commands
```bash
# Check if OpenAI API key is available in environment
echo $OPENAI_API_KEY

# Check Hermes tool configuration (requires interactive terminal)
# hermes tools  → Look under "Image Generation" section

# Test image generation with minimal prompt (use sparingly to avoid credit waste)
# Only do this after verifying configuration
```

## When Gabriel Mentions OpenAPI for Images
If Gabriel states he uses OpenAI API for images:
1. Verify OPENAI_API_KEY is set in the environment
2. Check if Hermes is configured to use OpenAI/DALL-E for image generation
3. If not configured, either:
   - Suggest configuring Hermes to use OpenAI (via `hermes tools` → Image Generation)
   - Pivot to non-image-based revenue ideas using existing assets
   - Verify FAL configuration if OpenAI is not preferred/available

## Revenue Generation Impact
Failed image generation attempts waste precious time when pursuing urgent revenue goals (like Julien's medical needs). Always verify before promising image-based deliverables.