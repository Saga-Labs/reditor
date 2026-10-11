# reditor.cloud

Alternatives to iPhone apps (when one shuts down, gets expensive or does not fit), served by GitHub Pages. Run by Saga Labs.

- Edit or add a page in `pages/*.py` (add the module to `PAGE_MODULES` in `build.py`), then `python3 build.py` and commit the generated HTML.
- After publishing: `python3 build.py --indexnow`.
- Rules: our app first with "Our app" label and a disclosure; our links carry pt+ct, competitors get a plain App Store link; every price, version and rating copied from the App Store on the `checked` date. Recheck monthly and only change `updated` when the data was actually rechecked.
- Analytics: Umami at analytics.kilmaru.com (`umami.js`; empty WEBSITE_ID means off). App Store campaign links use `ct=rd-<slug>`.
- Common know-how: `Saga-Labs/ios-playbook` → PLAYBOOK.md.
