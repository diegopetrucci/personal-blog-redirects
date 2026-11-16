# Original blog subdomain

Static redirect site for `blog.diegopetrucci.it`, forwarding old article paths to `https://www.diegopetrucci.it/blog/`.

Generated from the public build in `diegopetrucci/blog`. Contains only published routes, public assets, and RSS feeds. Never copy WordPress exports or credentials here.

GitHub Pages serves these as HTML redirects (meta refresh with JavaScript preserving query strings and fragments), not HTTP 301 responses. Public media and feeds remain directly accessible for old embeds and subscriptions. A 404 fallback preserves unknown paths.

The custom domain and DNS are configured only during the coordinated domain cutover.
