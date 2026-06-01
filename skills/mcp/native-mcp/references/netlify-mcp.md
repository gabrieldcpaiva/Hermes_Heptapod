# Netlify MCP Server Reference

## Overview
The Netlify MCP Server enables code agents to use the Netlify API and CLI to create projects, build, deploy, and manage Netlify resources via natural language prompts.

## Installation
```bash
npm install -g @netlify/mcp
```

## Configuration
Add to `~/.hermes/config.yaml`:
```yaml
mcp_servers:
  netlify:
    command: "npx"
    args: ["-y", "@netlify/mcp"]
    env:
      NETLIFY_AUTH_TOKEN: "your_personal_access_token"
    timeout: 60
```

## Available Tools
Once connected, the following tools become available:
- `mcp_netlify_list_sites` - List all sites in your account
- `mcp_netlify_get_site` - Get details for a specific site
- `mcp_netlify_create_site` - Create a new site
- `mcp_netlify_deploy_site` - Deploy a site
- `mcp_netlify_site_builds` - Get build history for a site
- `mcp_netlify_site_deploys` - Get deploy history for a site
- `mcp_netlify_site_environment_variables` - Manage environment variables
- `mcp_netlify_site_custom_domains` - Manage custom domains
- `mcp_netlify_site_edge_handlers` - Manage edge handlers
- `mcp_netlify_site_functions` - Manage serverless functions
- `mcp_netlify_site_redirects` - Manage redirects
- `mcp_netlify_site_headers` - Manage headers
- `mcp_netlify_site_plugins` - Manage plugins
- `mcp_netlify_site_snippet_injection` - Manage snippet injection
- `mcp_netlify_site_traffic_split` - Manage traffic splits
- `mcp_netlify_site_viewer_context` - Manage viewer context

## Authentication
Create a personal access token at:
https://app.netlify.com/user/applications#personal-access-token

The token should have access to the sites you want to manage.

## Troubleshooting
- **401 Unauthorized**: Check your NETLIFY_AUTH_TOKEN is valid and has sufficient permissions
- **Package not found**: Ensure `@netlify/mcp` is installed via npm
- **Timeout issues**: Increase the timeout value in config if dealing with large sites
- **Site not found**: Verify you have access to the site ID/name you're referencing

## Examples
List all sites:
```
mcp_netlify_list_sites
```

Deploy a site:
```
mcp_netlify_deploy_site --site-id YOUR_SITE_ID --dir ./dist
```

Create a new site from a GitHub repo:
```
mcp_netlify_create_site --github-repo username/repo --branch main
```