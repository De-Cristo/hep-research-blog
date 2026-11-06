# HEP weekly reading

Public summaries and reading guides for high-energy physics papers.

The first edition covers 4 November 2026. It contains thirteen paper summaries, their main caveats, and links to the original papers.

## Read online

[Read the first edition on GitHub](weekly/2026-11-04.md).

The Quarto website is prepared for https://de-cristo.github.io/hep-research-blog/. GitHub Pages must be enabled using the settings below.

## Build

Install [Quarto](https://quarto.org/docs/get-started/) from its official distribution, then run:

```sh
quarto render
```

The explicit render list includes only `index.qmd`. Code execution is disabled. The self-contained HTML output is `docs/index.html`. Keep `docs/.nojekyll` when replacing the output.

For GitHub Pages, select **Deploy from a branch**, **master**, and **/docs** in Settings → Pages. Render and review changes before committing the source and output together. There is no automatic publishing workflow.

The layout follows the [HEP web report guide](https://github.com/De-Cristo/hep-skills/tree/main/.agents/skills/hep-web-report): grouped sections, concise reading guides, responsive navigation, light and dark themes, and print styling.
