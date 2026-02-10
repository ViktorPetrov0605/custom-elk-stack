# Security Notice

## Credentials

**IMPORTANT:** Before using this repository, you MUST change all default passwords.

### Required Changes

1. **Edit `.env` file:**
```bash
ELASTIC_PASSWORD=your-strong-password-here
KIBANA_PASSWORD=your-strong-password-here
```

2. **Replace placeholder in documentation:**
The documentation uses `$ELASTIC_PASSWORD` as a placeholder. When running commands, either:
- Set an environment variable: `export ELASTIC_PASSWORD=yourpass`
- Or replace directly in commands

### Files That Contain Credential Placeholders

- `README.md` - Uses `elastic:$ELASTIC_PASSWORD` in examples
- `DEPLOYMENT.md` - Uses `elastic:<YOUR_PASSWORD>` in examples
- `monitoring/*.md` - Uses placeholders in curl commands
- `.env` - **NOT tracked by git** (in .gitignore)

### Never Commit

- Actual passwords
- `.env` file contents (already in .gitignore)
- Private keys
- Certificate files (use generate-certs.sh instead)

### Securing Your Deployment

1. **Change passwords immediately** after first deployment
2. **Use strong passwords** (20+ characters, mixed case, symbols)
3. **Rotate certificates** every 90 days
4. **Restrict network access** to Elasticsearch ports (9200/9201)
5. **Enable firewall rules** for flow collection ports (2050, 6343)

---
*Security audit completed: 2026-02-10*
