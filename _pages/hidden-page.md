---
layout: page
title: Hidden Page
permalink: /hidden-page/
description: This is a hidden page that doesn't appear in navigation but can be accessed via direct link.
nav: false
---

# Welcome to the Hidden Page! 🔍

This page demonstrates how to create a page that:
- **Does not appear** in the website navigation menu
- **Can be accessed** via direct URL or hyperlink
- **Is fully functional** like any other page

## How it works

In the al-folio template, navigation is controlled by the front matter of each page:

```yaml
---
layout: page
title: Hidden Page
permalink: /hidden-page/
nav: false  # This prevents the page from appearing in navigation
---
```

## Key Points

1. **`nav: false`** - This tells Jekyll not to include this page in the navigation menu
2. **`permalink: /hidden-page/`** - This creates a direct URL for the page
3. The page is still built and deployed, just not listed in the menu

## Usage Examples

This approach is useful for:
- **Internal documentation** that you don't want in main navigation
- **Landing pages** for specific campaigns or projects  
- **Easter eggs** or special content for those who know the URL
- **Work-in-progress** pages you're not ready to make public
- **Archive pages** that should be accessible but not prominent

## Navigation Back

You can [return to the main page]({{ '/' | relative_url }}) or use your browser's back button.

---

*This hidden page was created as an example of how to make pages accessible via hyperlink without cluttering the navigation menu.*