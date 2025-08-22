# Creating Hidden Pages in al-folio Template

This repository demonstrates how to create pages that don't appear in the navigation menu but can be accessed via direct links or hyperlinks.

## How It Works

### Method 1: Use `nav: false` in Front Matter

```yaml
---
layout: page
title: Your Page Title
permalink: /your-url/
nav: false
---
```

### Method 2: Omit `nav` Property (defaults to false)

```yaml
---
layout: page
title: Your Page Title
permalink: /your-url/
# No nav property = nav: false by default
---
```

## Examples in This Repository

### 1. **Hidden Page** (`/hidden-page/`)
- Basic example with `nav: false`
- Accessible via 🔍 icon link in footer
- File: `_pages/hidden-page.md`

### 2. **Internal Documentation** (`/internal-docs/`)
- Comprehensive documentation page
- Linked from Research section
- File: `_pages/internal-docs.md`

### 3. **Project Details** (`/projects/cpcd/data-collection/`)
- Detailed methodology for CPCD project
- Linked from main CPCD project page
- File: `_pages/cpcd-data-collection.md`

## Navigation Structure

### Pages WITH Navigation (nav: true)
- **About** (/) - Main page
- **Projects** (/projects/) - `nav: true, nav_order: 2`
- **Publications** (/publications/) - `nav: true, nav_order: 4`

### Pages WITHOUT Navigation (nav: false or omitted)
- **Hidden Page** (/hidden-page/)
- **Internal Docs** (/internal-docs/)
- **News** (/news/) - Already had no nav
- **CPCD Details** (/projects/cpcd/data-collection/)
- **404 Error** (/404.html)

## Use Cases

1. **Work-in-progress content** - Hide until ready
2. **Internal documentation** - For team members only
3. **Special landing pages** - Accessed via direct links
4. **Archive content** - Keep accessible but not prominent
5. **Detailed project information** - Linked from main project pages

## Technical Notes

- Pages are still built and deployed by Jekyll
- Pages are indexed by search engines (SEO-friendly)
- Direct URLs work normally
- Can be linked from any other page or external site

## Adding Links to Hidden Pages

### From Markdown
```markdown
[Link text](/hidden-page/)
```

### With Jekyll Variables
```liquid
[Link text]({{ '/hidden-page/' | relative_url }})
```

### From HTML
```html
<a href="{{ '/hidden-page/' | relative_url }}">Link text</a>
```

---

*This approach keeps the main navigation clean while maintaining flexible access to all content.*