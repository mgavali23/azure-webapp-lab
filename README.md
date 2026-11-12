# Azure App Service Lab (Python)

A small Python Flask application for learning Azure App Service, GitHub and continuous deployment.

## Application endpoints

- `/` — landing page.
- `/health` — JSON health check.

## Files

- `app.py` — Flask application.
- `requirements.txt` — Python dependencies.
- `startup.sh` — Gunicorn startup command for Linux App Service.
- `.github/workflows/deploy.yml` — GitHub Actions build and deployment workflow.

## Configure Azure App Service

In the Azure Portal, open your Linux Web App and verify that its Python runtime version matches the workflow's Python version (currently Python 3.12).

Under **Settings → Environment variables → App settings**, add:

| Name | Value |
|---|---|
| `SCM_DO_BUILD_DURING_DEPLOYMENT` | `true` |
| `APP_ENV` | `learning` |

Under **Configuration → General settings**, set the startup command to:

```bash
gunicorn --bind=0.0.0.0:8000 --timeout 600 app:app
```

The startup command is also provided in `startup.sh`; setting it in the Portal makes the lab configuration explicit.

## Configure GitHub Actions

The workflow deploys automatically on every push to `main`, or manually using **Actions → Build and deploy Python app to Azure App Service → Run workflow**.

In the GitHub repository, open **Settings → Secrets and variables → Actions** and configure:

1. Add a repository **variable** named `AZURE_WEBAPP_NAME` with the exact Azure Web App resource name.
2. Add a repository **secret** named `AZUREAPPSERVICE_PUBLISHPROFILE` containing the complete publish-profile XML downloaded from the Azure Portal (**Web App → Overview → Get publish profile**).

Do not commit the publish profile, passwords, or other credentials to the repository.

For this beginner lab, the workflow uses a publish profile. For production, prefer Microsoft Entra workload identity federation (OIDC) rather than long-lived publish-profile credentials.

## Verify deployment

After a successful GitHub Actions run, open:

- `https://<your-web-app-name>.azurewebsites.net/`
- `https://<your-web-app-name>.azurewebsites.net/health`

If deployment fails, inspect the failed step in the GitHub Actions run and the App Service **Log stream** in Azure Portal.
