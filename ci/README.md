# CI/CD

## Pipeline goals
- Build and test backend, frontend, and ML services.
- Produce versioned container images.
- Promote releases through environments with approvals.

## Example workflow stages
1. Lint and unit tests.
2. Build and containerize.
3. Security scans (SAST + image scanning).
4. Deploy to staging.
5. Automated smoke tests.
6. Promote to production via GitOps.
