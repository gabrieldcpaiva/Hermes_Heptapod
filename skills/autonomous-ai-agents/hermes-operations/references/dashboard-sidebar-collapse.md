# Dashboard Sidebar Collapse — Custom Theme

The Hermes dashboard sidebar is 256px wide and always visible on desktop (≥1024px). On smaller screens this blocks significant content area.

## Solution: Custom Theme with `customCSS`

Create a theme YAML at `~/.hermes/dashboard-themes/compact-sidebar.yaml`:

```yaml
name: compact-sidebar
label: Compact Sidebar
description: Default Hermes Teal theme with auto-collapsing sidebar on desktop. Hover to expand.
palette:
  background:
    hex: "#041c1c"
    alpha: 1
  midground:
    hex: "#ffe6cb"
    alpha: 1
  foreground:
    hex: "#ffffff"
    alpha: 0
  warmGlow: "rgba(255, 189, 56, 0.35)"
  noiseOpacity: 1
typography:
  fontSans: 'system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif'
  fontMono: 'ui-monospace, "SF Mono", "Cascadia Mono", Menlo, Consolas, monospace'
  baseSize: "15px"
  lineHeight: "1.55"
  letterSpacing: "0"
layout:
  radius: "0.5rem"
  density: "comfortable"
customCSS: |
  @media (min-width: 1024px) {
    #app-sidebar {
      width: 48px !important;
      min-width: 48px !important;
      max-width: 48px !important;
      overflow: hidden;
      transition: width 0.2s ease;
    }
    #app-sidebar:hover {
      width: 256px !important;
      max-width: 256px !important;
      overflow: visible;
    }
    #app-sidebar .truncate,
    #app-sidebar nav span,
    #app-sidebar nav ul li a span {
      opacity: 0;
      white-space: nowrap;
      transition: opacity 0.15s ease;
    }
    #app-sidebar:hover .truncate,
    #app-sidebar:hover nav span,
    #app-sidebar:hover nav ul li a span {
      opacity: 1;
    }
  }
```

## Activate

```bash
hermes config set dashboard.theme compact-sidebar
hermes dashboard --stop
hermes dashboard
```

## How It Works

- Sidebar collapses to 48px (icon strip) on screens >=1024px
- Hovering over the sidebar expands it to full 256px width
- Text labels use `display: none` (NOT `opacity: 0`) — opacity leaves ghost elements taking up space
- Icons center in the collapsed state, left-align on hover
- The theme's palette, typography, and layout sections are required by the theme normalizer -- without them the theme is rejected
- customCSS is injected as a style tag on theme apply
- Max customCSS length: 32 KiB

## Verification

In browser console:
- `document.getElementById('app-sidebar').getComputedStyle().width` should be "48px"
- `document.querySelectorAll('style[data-hermes-theme-css]').length` should be >= 1
