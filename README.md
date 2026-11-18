# Original blog subdomain

Static redirect site for `blog.diegopetrucci.it`, forwarding old article paths to `https://www.diegopetrucci.it/blog/`.

Generated from the public build in `diegopetrucci/blog`. Contains only published routes, public assets, and RSS feeds. Never copy WordPress exports or credentials here.

GitHub Pages serves these as HTML redirects (meta refresh with JavaScript preserving query strings and fragments), not HTTP 301 responses. Public media and feeds remain directly accessible for old embeds and subscriptions. A 404 fallback preserves unknown paths.

The custom domain and DNS are configured only during the coordinated domain cutover.

The Pages workflow refreshes both feeds from the live personal blog on each deployment and daily. The main blog's deployment workflow also enables and dispatches this workflow automatically after a successful publish, then waits for completion. Its `source_sha` input identifies the blog deployment in the run title. This recovers from GitHub disabling schedules after long periods without repository activity.

For manual recovery:

```sh
gh workflow enable pages.yml --repo diegopetrucci/personal-blog-redirects
gh workflow run pages.yml --repo diegopetrucci/personal-blog-redirects
```

Wait for the main blog deployment first. `python3 scripts/build.py` validates the fetched XML and builds only public site files; a failed fetch prevents deployment so the existing site stays available.
