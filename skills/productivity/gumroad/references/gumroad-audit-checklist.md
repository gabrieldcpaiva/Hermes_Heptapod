# Gumroad Product Audit Checklist

Use when a user asks for a "Gumroad audit" or when troubleshooting zero-sales products that have been live for 24+ hours.

## Step 1: Confirm login and access

- [ ] Can you access the Gumroad dashboard? (If bot-blocked, user logs in manually)
- [ ] Can you visit public product pages? (Always possible — no login needed for read-only audit)

## Step 2: Products table — overview

Navigate to Gumroad Dashboard → Products. Check all rows for:
- **Name** — readable? Not truncated?
- **Sales** — any non-zero? (0 sales = distribution problem, not product problem)
- **Revenue** — matches price × sales?
- **Price** — correct for each product?
- **Status** — all "Published"?

## Step 3: Public product pages — one by one

For each product, visit the public URL (e.g. `gpframes.gumroad.com/l/seo-domination-kit`). Check:

### Description formatting (MOST COMMON ISSUE)
- [ ] **Rich text?** Headings, paragraphs, bullet lists — clean and readable
- [ ] **Code block?** Text inside a gray `<code>` box with a "Copy" button — looks unfinished
- [ ] **Mix?** Some rich text, some code — fix the code sections

**How to tell:** If the description has a "Copy" button next to it on the public page, it's in a code block. Bad.

**How to fix:** Edit the product in Gumroad. Delete the code-block content. For manual fixes, paste the description as plain text and reformat with the toolbar. For browser automation, use the ProseMirror JS technique documented in the main SKILL.md under "The code-block description pitfall."

### Description content
- [ ] One-line summary at top — what is this?
- [ ] Specific numbers (231 prompts, 12 categories, etc.)
- [ ] What's inside — bullet list of sections/modules
- [ ] How it works — "paste into ChatGPT/Claude"
- [ ] What you get — file format (CSV, PDF, ZIP, webapp)
- [ ] No hype words, no fake urgency, no fake testimonials

### Price and CTA
- [ ] Price visible and correct
- [ ] "I want this!" button visible
- [ ] No hidden fees or confusing pricing tiers

### Cover image
- [ ] Present on the page
- [ ] Decent quality (not pixelated, not a screenshot of the editor)

### Tags (check in editor)
- [ ] All available tag slots used
- [ ] Relevant search terms — think about what a buyer would search for
- [ ] Mix of broad (ai prompts, marketing) and specific (keyword research, email sequences)

### File attachments (check in editor → Content tab)
- [ ] Files actually attached (buyer can't download nothing)
- [ ] Correct file format (ZIP with CSV + PDF + webapp, not raw CSV alone)
- [ ] File names are clean (not auto-generated gibberish)

## Step 4: Payment / payout settings

- [ ] Stripe connected? (Check Settings → Payments)
- [ ] For Brazilian sellers: CPF (individual) or CNPJ (company)? CPF unless registered as company
- [ ] ID verification complete? (Gumroad/Stripe may require scanned ID)
- [ ] If Stripe blocked: PayPal as fallback? (Gumroad supports PayPal payouts)

**Common blocker:** Stripe requires ID verification for Brazilian accounts. If the user can't complete this (e.g. no scanner, no ID handy), the payout won't process even if sales happen. Mark this as a blocking issue.

## Step 5: Checkout flow (do a dry run)

Visit a product page → click "I want this!" → go through to payment screen (don't pay, just check the flow):
- [ ] Checkout page loads correctly (not broken)
- [ ] Price shown matches product page
- [ ] Payment options visible (card, PayPal, etc.)
- [ ] No confusing fees or shipping (it's digital — should be clean)
- [ ] "Buy" button works

## Step 6: Overall storefront

Visit the main store URL:
- [ ] Storefront loads cleanly
- [ ] All products visible (none accidentally hidden/archived)
- [ ] Store header/description is professional, matches brand voice
- [ ] Profile picture set
- [ ] Subscribe/Call-to-action present

## Step 7: Store infrastructure audit — beyond the product page

Products being published does NOT mean the store is ready to sell. Gumroad has several backend sections that must be configured for a functioning sales machine. Check each one.

### 7a — Checkout settings

Navigate to Dashboard → Checkout. Three tabs:

**Discounts tab:**
- [ ] Any active discount codes? Are they intentional or stale?
- [ ] Stale codes (e.g. 100% off for an old product) still active? If yes, disable them — they look unprofessional on the store and can be abused.
- [ ] Any launch promo codes ready to distribute? (Create before starting outreach.)

**Checkout form tab:**
- [ ] Custom fields configured? (e.g. collecting name, use case, coupon code)
- [ ] Discount code field visible? (Recommended: "Only if a discount is available" — don't show it empty.)
- [ ] Product recommendations enabled during checkout? (Cross-sell other products.)
- [ ] Tipping enabled? (Optional — can increase average order value.)
- [ ] Form looks clean in the preview pane — no broken fields or missing labels.

**Upsells tab:**
- [ ] Any upsells configured? (Post-purchase offers — "add this for $5 more.")
- [ ] If empty: upsells are a quick win. Even one "complete the bundle" upsell can lift revenue per buyer.

### 7b — Emails

Navigate to Dashboard → Emails. Check tabs:

**Published tab:**
- [ ] Any email campaigns sent? (Zero = no subscriber communication ever.)
- [ ] If empty: create at minimum a launch announcement campaign ready to send when subscribers exist.

**Subscribers tab:**
- [ ] Any subscribers? (Zero = no audience to email. Collection mechanism needed.)
- [ ] If zero: check if the email capture form on your storefront is visible and working.

### 7c — Workflows

Navigate to Dashboard → Workflows.

- [ ] Abandoned cart workflow present? (Gumroad creates one by default — check it's published.)
- [ ] Post-purchase workflows? (Welcome email, "how to use your purchase," cross-sell offers.)
- [ ] If only the default abandoned cart exists: this is the bare minimum. Add at least one post-purchase workflow for customer retention.

**Missing workflows to create (priority order):**
1. **Post-purchase thank-you** — delivered immediately after purchase: confirmation, download link, quick-start guide
2. **Post-purchase cross-sell** — 24-48 hours later: "since you bought X, you might also want Y"
3. **Review request** — 5-7 days later: ask for a rating/review
4. **Bundle completion offer** — if they bought an individual pack, offer the full collection at a discount

### 7d — Affiliates

Navigate to Dashboard → Affiliates.

- [ ] Affiliate program enabled? (Lets others promote your products for a commission.)
- [ ] If disabled: consider enabling with a 20-30% commission. Free marketing — you only pay on sales.
- [ ] If enabled: any affiliates signed up? (Zero = program exists but nobody knows about it.)

### 7e — Sales

Navigate to Dashboard → Sales.

- [ ] Any sales at all? (Zero across all products = distribution problem, not product problem.)
- [ ] First sale date? (If products have been live 24+ hours with no sales, active outreach is needed immediately — see outreach section.)
- [ ] Any refunds or chargebacks? (If yes, investigate product or delivery issues.)

### 7f — Analytics

Navigate to Dashboard → Analytics.

- [ ] Any page views? (Zero = no traffic being driven to store. Products don't sell themselves.)
- [ ] Traffic sources visible? (Organic search, direct link, social, affiliate — where is the little traffic you have coming from?)

## Step 8: Compile and present findings

Present findings in a clear table, grouped into four categories:

| Category | Status | Action needed |
|----------|--------|--------------|
| **Product pages** | ✅ / ❌ / ⚠️ | List specific fixes |
| **Payment/payouts** | ✅ / ❌ / ⚠️ | Verification or setup steps |
| **Store infrastructure** | ✅ / ❌ / ⚠️ | What's missing (checkout, emails, workflows, affiliates) |
| **Traffic/distribution** | ✅ / ❌ / ⚠️ | Outreach plan needed |

**Critical finding rule:** If any item in store infrastructure (checkout, emails, workflows) is completely empty or misconfigured, flag it as a critical gap. Products can be perfect, but without workflows and emails, there's no engine to convert visitors into buyers or retain them after purchase.

## Known issues from Gabriel's store (gpframes.gumroad.com)

As of 2026-05-26 (TUI session):
- Products: 7 prompt packs at $7–$29 — all live, all 0 sales
- ✅ Product pages: descriptions fixed (code blocks replaced with clean formatting on all 4 affected products), files attached, prices correct
- ✅ Payments: Stripe connected, weekly payouts, $100 min threshold
- ❌ **Checkout:** One stale 100% off code for a deleted product still active. No upsells configured. No launch discount codes.
- ❌ **Emails:** Completely empty. Zero email campaigns ever. Zero subscribers.
- ❌ **Workflows:** Only the default abandoned cart workflow (1 email: "You left something in your cart" at 24h). No post-purchase workflows.
- ❌ **Affiliates:** Not configured.
- ❌ **Traffic:** Zero visits to product pages. Distribution is the bottleneck.
- ✅ **Description formatting:** All 7 products now have clean rich-text descriptions. The 4 products that had code-block issues (Full Arsenal, Content Empire, YouTube Growth, E-commerce) were fixed via ProseMirror JS injection.
- Stripe: Needs ID verification (CPF for individual Brazilian seller) — blocking issue for payouts.
- **Key lesson:** Products published is step 1. Store infrastructure (emails, workflows, checkout optimization) is step 2. Both must be complete before launch outreach begins.